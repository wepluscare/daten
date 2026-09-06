#!/usr/bin/env python3
"""Holt die BFS-Rohdaten für die Grafik «Die Schere» und schreibt sie als CSV.

Quellen (BFS PXWeb-API, https://www.pxweb.bfs.admin.ch/api/v1/de/<cube>/<cube>.px):
  px-x-0102010000_101  STATPOP: Ständige Wohnbevölkerung nach Alter, Schweiz, 31.12., 2010–2025 (Ist)
  px-x-0104020000_101  Szenarien 2025–2055, Referenzszenario AR-00-2025, Bestand am 1. Januar
  px-x-0104020000_102  dito, 'hohes' Szenario BR-00-2025
  px-x-0104020000_103  dito, 'tiefes' Szenario CR-00-2025

Ausgabe:
  raw/<cube>.query.json      exakte Abfrage (zum Nachvollziehen / erneut Absenden)
  raw/<cube>.response.json   unveränderte Antwort des BFS
  bfs_bevoelkerung_nach_alter.csv   Langformat: quelle, jahr, alter, personen
  schere_aggregate.csv              je Quelle/Jahr: 45–69, 65+, 80+, Quote, Indizes (2024 = 100)

Aufruf: python3 fetch_bfs.py   (nur Standardbibliothek)
"""
import csv, json, urllib.request, datetime, pathlib

API = 'https://www.pxweb.bfs.admin.ch/api/v1/de/{c}/{c}.px'
HERE = pathlib.Path(__file__).parent
RAW = HERE / 'raw'; RAW.mkdir(exist_ok=True)

SOURCES = [
    ('statpop',  'px-x-0102010000_101', 'Ist (STATPOP, 31.12.)'),
    ('referenz', 'px-x-0104020000_101', 'Szenario Referenz AR-00-2025 (1.1.)'),
    ('hoch',     'px-x-0104020000_102', "Szenario 'hoch' BR-00-2025 (1.1.)"),
    ('tief',     'px-x-0104020000_103', "Szenario 'tief' CR-00-2025 (1.1.)"),
]

def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'} if data else {})
    return json.load(urllib.request.urlopen(req, timeout=180))

def code(V, var, text):
    v = V[var]; return v['values'][v['valueTexts'].index(text)]

def age_of(text):
    return int(text.split()[0].replace('+', ''))  # '100 Jahre und mehr' → 100

rows, agg = [], []
for label, cube, desc in SOURCES:
    meta = get(API.format(c=cube))
    V = {v['code']: v for v in meta['variables']}
    ages = [c for c, t in zip(V['Alter']['values'], V['Alter']['valueTexts']) if t != 'Alter - Total']
    if label == 'statpop':
        region_var = next(v['code'] for v in meta['variables'] if v['code'].startswith('Kanton'))
        q = [
            {"code": "Jahr", "selection": {"filter": "all", "values": ["*"]}},
            {"code": region_var, "selection": {"filter": "item", "values": [code(V, region_var, 'Schweiz')]}},
            {"code": "Bevölkerungstyp", "selection": {"filter": "item", "values": [code(V, 'Bevölkerungstyp', 'Ständige Wohnbevölkerung')]}},
            {"code": "Staatsangehörigkeit (Kategorie)", "selection": {"filter": "item", "values": [code(V, 'Staatsangehörigkeit (Kategorie)', 'Staatsangehörigkeit (Kategorie) - Total')]}},
            {"code": "Geschlecht", "selection": {"filter": "item", "values": [code(V, 'Geschlecht', 'Geschlecht - Total')]}},
            {"code": "Alter", "selection": {"filter": "item", "values": ages}},
        ]
    else:
        q = [
            {"code": "Kanton", "selection": {"filter": "item", "values": [code(V, 'Kanton', 'Schweiz')]}},
            {"code": "Staatsangehörigkeit (Kategorie)", "selection": {"filter": "item", "values": [code(V, 'Staatsangehörigkeit (Kategorie)', 'Staatsangehörigkeit - Total')]}},
            {"code": "Geschlecht", "selection": {"filter": "item", "values": [code(V, 'Geschlecht', 'Geschlecht - Total')]}},
            {"code": "Alter", "selection": {"filter": "item", "values": ages}},
            {"code": "Jahr", "selection": {"filter": "all", "values": ["*"]}},
            {"code": "Beobachtungseinheit", "selection": {"filter": "item", "values": [code(V, 'Beobachtungseinheit', 'Bevölkerungsstand am 1. Januar')]}},
        ]
    query = {"query": q, "response": {"format": "json"}}
    (RAW / f'{cube}.query.json').write_text(json.dumps(query, ensure_ascii=False, indent=1))
    resp = get(API.format(c=cube), json.dumps(query).encode())
    (RAW / f'{cube}.response.json').write_text(json.dumps(resp, ensure_ascii=False))
    cols = [c['code'] for c in resp['columns'] if c['type'] in ('d', 't')]  # 't' = Zeitachse (STATPOP: Jahr)
    # STATPOP liefert die Spalten unter ihren Texten, die Szenarien unter den Codes
    ai = next(i for i, c in enumerate(cols) if c.startswith('Alter'))
    ji = next(i for i, c in enumerate(cols) if c.startswith('Jahr'))
    agetext = dict(zip(V['Alter']['values'], V['Alter']['valueTexts']))
    yeartext = dict(zip(V['Jahr']['values'], V['Jahr']['valueTexts']))
    series = {}
    for r in resp['data']:
        raw = r['values'][0]
        if raw in ('...', '.', '', '"..."'): continue
        a, y, v = age_of(agetext[r['key'][ai]]), int(yeartext[r['key'][ji]]), float(raw)
        series.setdefault(y, {})[a] = v
        rows.append((label, y, a, int(v)))
    for y in sorted(series):
        s = series[y]
        p, o, o80, tot = (sum(v for a, v in s.items() if 45 <= a <= 69), sum(v for a, v in s.items() if a >= 65),
                          sum(v for a, v in s.items() if a >= 80), sum(s.values()))
        agg.append({'quelle': label, 'beschreibung': desc, 'cube': cube, 'jahr': y, 'pot_betreuende_45_69': int(p),
                    'bev_65plus': int(o), 'bev_80plus': int(o80), 'bev_total': int(tot), 'quote_45_69_pro_65plus': round(p / o, 4)})
    print(f'{label:9s} {cube}: {len(series)} Jahre ({min(series)}–{max(series)}), {len(rows)} Zeilen kumuliert')

# Indizes: Szenarien auf 2024 = 100 (Szenario-Basis), Ist auf 2024 = 100 (STATPOP 31.12.2024)
base = {a['quelle']: a for a in agg if a['jahr'] == 2024}
for a in agg:
    b = base[a['quelle']]
    for k in ('quote_45_69_pro_65plus', 'bev_65plus', 'bev_80plus'):
        a[f'index_{k}_2024_100'] = round(100 * a[k] / b[k], 1)

with open(HERE / 'bfs_bevoelkerung_nach_alter.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['quelle', 'jahr', 'alter', 'personen']); w.writerows(rows)
with open(HERE / 'schere_aggregate.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(agg[0].keys())); w.writeheader(); w.writerows(agg)
(HERE / 'raw' / 'FETCHED.txt').write_text(f'abgerufen {datetime.datetime.now().isoformat(timespec="minutes")} via {API}\n')
print('geschrieben:', 'bfs_bevoelkerung_nach_alter.csv', 'schere_aggregate.csv', 'raw/*.json')
