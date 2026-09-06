#!/usr/bin/env python3
"""Baut die Datengrundlage «Hilfe und Pflege zu Hause in der EL, nach Kanton».

Quellen:
  BSV, Statistik der EL zur AHV und IV 2025 (Mai 2026), Detailtabelle T5.2
      «Vergütete Krankheits- und Behinderungskosten der EL nach Kostenart», Blatt 2025.
      Lokal: statistics/el statistik/su-d-13.04.01-bsv-el-5.2.xlsx
  BFS PXWeb px-x-0102010000_102, Ständige Wohnbevölkerung nach Kanton, 31.12.2025.

Ausgabe:
  raw/bsv_t5.2_2025_kantone.csv        die entnommenen Zeilen, unverändert
  raw/px-x-0102010000_102.query.json   exakte BFS-Abfrage
  raw/px-x-0102010000_102.response.json unveränderte BFS-Antwort
  el_pflege_zu_hause_kantone.csv       Kanton, KB-Kosten total, Anteil, Betrag, Bevölkerung, Fr./Einwohner

Aufruf: python3 fetch_el_pflege.py   (nur Standardbibliothek)

WICHTIG — Zürich fehlt: Die Tabelle T5.2 weist Zürich nicht aus. Der Datensatz
umfasst deshalb 25 Kantone. Das ist keine Lücke unserer Aufbereitung, sondern
der Quelle; jede Darstellung muss es sichtbar machen.
"""
import csv, json, pathlib, urllib.request, zipfile
from xml.etree import ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
HERE = pathlib.Path(__file__).parent
RAW = HERE / 'raw'; RAW.mkdir(exist_ok=True)
XLSX = HERE / '../../../../../../statistics/el statistik/su-d-13.04.01-bsv-el-5.2.xlsx'

# BSV schreibt die Kantone deutsch und ohne Kürzel; BFS liefert sie teils zweisprachig.
BFS_NAME = {
    'Bern': 'Bern / Berne', 'Freiburg': 'Fribourg / Freiburg',
    'Graubünden': 'Graubünden / Grigioni / Grischun', 'Wallis': 'Valais / Wallis',
    'Tessin': 'Ticino', 'Waadt': 'Vaud', 'Genf': 'Genève', 'Neuenburg': 'Neuchâtel',
    'St.Gallen': 'St. Gallen', 'Appenzell A.Rh.': 'Appenzell Ausserrhoden',
    'Appenzell I.Rh.': 'Appenzell Innerrhoden',
}
KUERZEL = {
    'Zürich': 'ZH', 'Bern': 'BE', 'Luzern': 'LU', 'Uri': 'UR', 'Schwyz': 'SZ',
    'Obwalden': 'OW', 'Nidwalden': 'NW', 'Glarus': 'GL', 'Zug': 'ZG', 'Freiburg': 'FR',
    'Solothurn': 'SO', 'Basel-Stadt': 'BS', 'Basel-Landschaft': 'BL', 'Schaffhausen': 'SH',
    'Appenzell A.Rh.': 'AR', 'Appenzell I.Rh.': 'AI', 'St.Gallen': 'SG', 'Graubünden': 'GR',
    'Aargau': 'AG', 'Thurgau': 'TG', 'Tessin': 'TI', 'Waadt': 'VD', 'Wallis': 'VS',
    'Neuenburg': 'NE', 'Genf': 'GE', 'Jura': 'JU',
}


def sheet_rows(path, idx=0):
    z = zipfile.ZipFile(path)
    sheet = list(ET.fromstring(z.read('xl/workbook.xml')).iter(NS + 'sheet'))[idx]
    rels = {r.get('Id'): r.get('Target')
            for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    shared = [''.join(t.text or '' for t in si.iter(NS + 't'))
              for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(NS + 'si')]
    ws = ET.fromstring(z.read('xl/' + rels[sheet.get(RID)].lstrip('/')))
    for row in ws.iter(NS + 'row'):
        out = {}
        for c in row.iter(NS + 'c'):
            col = ''.join(ch for ch in c.get('r') if ch.isalpha())
            v = c.find(NS + 'v')
            if v is not None:
                out[col] = shared[int(v.text)] if c.get('t') == 's' else v.text
        yield out


# ── 1 · BSV T5.2, Blatt 2025 ────────────────────────────────────────────
# Spalte B = Krankheits-/Behinderungskosten total in Mio. Fr.
# Spalte F = Anteil «Haushaltshilfe und Pflege zu Hause» in Prozent
bsv, total_row = {}, None
for r in sheet_rows(XLSX):
    name = (r.get('A') or '').strip()
    if name and r.get('C') == '100' and r.get('B') and r.get('F'):
        rec = (float(r['B']), float(r['F']))
        if name == 'Total':
            total_row = rec
        else:
            bsv[name] = rec

with open(RAW / 'bsv_t5.2_2025_kantone.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kanton', 'kb_kosten_total_mio_chf', 'anteil_haushaltshilfe_pflege_zu_hause_pct'])
    w.writerow(['Total (CH ohne ZH)', f'{total_row[0]:.6f}', f'{total_row[1]:.2f}'])
    for k, (tot, pct) in bsv.items():
        w.writerow([k, f'{tot:.6f}', f'{pct:.2f}'])

# ── 2 · BFS-Bevölkerung 2025 ────────────────────────────────────────────
API = 'https://www.pxweb.bfs.admin.ch/api/v1/de/{c}/{c}.px'
CUBE = 'px-x-0102010000_102'
meta = json.load(urllib.request.urlopen(API.format(c=CUBE), timeout=90))
V = {v['code']: v for v in meta['variables']}


def code(var, text):
    return V[var]['values'][V[var]['valueTexts'].index(text)]


query = {'query': [
    {'code': 'Jahr', 'selection': {'filter': 'item', 'values': [code('Jahr', '2025')]}},
    {'code': 'Kanton', 'selection': {'filter': 'all', 'values': ['*']}},
    {'code': 'Bevölkerungstyp', 'selection': {'filter': 'item',
     'values': [code('Bevölkerungstyp', 'Ständige Wohnbevölkerung')]}},
    {'code': 'Geschlecht', 'selection': {'filter': 'item',
     'values': [code('Geschlecht', 'Geschlecht - Total')]}},
    {'code': 'Zivilstand', 'selection': {'filter': 'item',
     'values': [code('Zivilstand', 'Zivilstand - Total')]}},
    {'code': 'Alter', 'selection': {'filter': 'item', 'values': [code('Alter', 'Alter - Total')]}},
], 'response': {'format': 'json-stat2'}}
(RAW / f'{CUBE}.query.json').write_text(json.dumps(query, ensure_ascii=False, indent=1))
req = urllib.request.Request(API.format(c=CUBE), data=json.dumps(query).encode(),
                             headers={'Content-Type': 'application/json'})
res = json.load(urllib.request.urlopen(req, timeout=180))
(RAW / f'{CUBE}.response.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
pop = dict(zip(res['dimension']['Kanton']['category']['label'].values(), res['value']))

# ── 3 · Zusammenführen ──────────────────────────────────────────────────
rows = []
for k, (kb_total, pct) in bsv.items():
    einwohner = pop.get(BFS_NAME.get(k, k))
    if einwohner is None:
        raise SystemExit(f'Bevölkerung fehlt für {k!r} — Namensabgleich prüfen')
    betrag_mio = kb_total * pct / 100
    rows.append({
        'kanton': k,
        'kuerzel': KUERZEL[k],
        'kb_kosten_total_mio_chf': round(kb_total, 6),
        'anteil_pflege_zu_hause_pct': round(pct, 2),
        'pflege_zu_hause_mio_chf': round(betrag_mio, 6),
        'bevoelkerung_2025': einwohner,
        'franken_je_einwohner': round(betrag_mio * 1e6 / einwohner, 2),
    })
rows.sort(key=lambda r: -r['franken_je_einwohner'])
with open(HERE / 'el_pflege_zu_hause_kantone.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

print(f'{len(rows)} Kantone geschrieben (Zürich fehlt in T5.2).')
print(f'CH-Anteil laut Quelle: {total_row[1]:.2f} % von {total_row[0]:.2f} Mio Fr.')
