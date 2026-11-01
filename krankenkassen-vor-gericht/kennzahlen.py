#!/usr/bin/env python3
"""Rechnet die Kennzahlen aus METHODIK.md aus urteile.json und gesundheit.json nach.

Aufruf:  python3 kennzahlen.py
Zählregeln: Kassen-Entscheide = einschlaegig «ja» und Kasse Partei. Pflicht-Kennzahlen je
Verfahren mit dem Endentscheid (ohne Zwischenbeschlüsse im selben Verfahren).
Wartezeit = erste Kürzung bis Urteil laut Text, in Monaten. Nur Standardbibliothek.
"""
import collections, datetime as dt, json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
u = json.load(open(os.path.join(HERE, "urteile.json"), encoding="utf-8"))
g = json.load(open(os.path.join(HERE, "gesundheit.json"), encoding="utf-8"))

kk = [x for x in u if x["einschlaegig"] == "ja" and x["ausgang_fuer_kk"] != "kk_nicht_partei"]
pf = [x for x in kk if x["pflicht_argument_der_kk"] == "ja" and x["instanz"] != "zwischenentscheid_im_selben_verfahren"]
print("Entscheide gelesen:", len(u))
print("Kassen-Entscheide:", len(kk), "in", len({x["verfahren_id"] for x in kk}), "Verfahren")
print("Pflicht-Argument der Kasse:", len(pf), "Verfahren")
print("  nicht aus Pflichtgrund geschützt:", sum(x["gericht_zur_pflicht"] != "folgt_kk" for x in pf))
print("  Haltung Gericht:", dict(collections.Counter(x["gericht_zur_pflicht"] for x in pf)))
print("  Ausgang:", dict(collections.Counter(x["ausgang_fuer_kk"] for x in pf)))
print("  Jahr:", dict(sorted(collections.Counter(x["entscheid_datum"][:4] for x in pf).items())))
mut = [x for x in pf if "Mutuel" in x["kk_gruppe"]]
print("  Groupe Mutuel:", len(mut), dict(collections.Counter(x["ausgang_fuer_kk"] for x in mut)))

def datum(s):
    try:
        return dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None

nr_vid = {str(x["nr"]): x["verfahren_id"] for x in u}
pf_vid = {x["verfahren_id"] for x in pf}
alle, pflicht = [], []
for k, v in g.items():
    a, b = datum(v.get("datum_erste_verfuegung_oder_kuerzung")), datum(v.get("datum_urteil_laut_text"))
    if a and b:
        m = (b - a).days / 30.4375
        alle.append(m)
        if nr_vid.get(k) in pf_vid:
            pflicht.append(m)
print("Wartezeit Median %.1f Monate (n = %d, Spanne %.1f bis %.1f); Pflicht-Fälle %.1f (n = %d)"
      % (statistics.median(alle), len(alle), min(alle), max(alle), statistics.median(pflicht), len(pflicht)))
