#!/usr/bin/env python3
"""Prüft jedes Zitat der Tabelle gegen den gespeicherten Urteilstext.

Aufruf:  python3 pruefe_zitate.py
Liest:   urteile.json, quellen.csv, entscheide/*.txt (im selben Ordner)
Schreibt: zitatpruefung.csv und eine Zusammenfassung auf die Konsole.

Ein Zitat gilt als gefunden, wenn jedes Teilstück zwischen Auslassungen ([…], [...])
in der richtigen Reihenfolge im Urteilstext vorkommt. Verglichen wird ohne Leerraum,
ohne Trennstriche und ohne Unterschied der Anführungszeichen, weil die Volltexte aus
PDF stammen und Zeilenumbrüche mitten im Wort enthalten. Nur Standardbibliothek.
"""
import csv, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FELDER = ["pflicht_zitat_kk", "gericht_zitat", "dispositiv"]

def norm(s):
    s = s.replace("­", "")
    s = re.sub(r"[«»„“”\"‹›‘’']", "", s)
    s = re.sub(r"[\s\-–—]+", "", s)
    return s.lower()

def teile(z):
    return [t for t in (norm(x) for x in re.split(r"\[\s*(?:…|\.\.\.)\s*\]|…", z)) if len(t) >= 12]

def main():
    urteile = json.load(open(os.path.join(HERE, "urteile.json"), encoding="utf-8"))
    quellen = {r["nr"]: r for r in csv.DictReader(open(os.path.join(HERE, "quellen.csv"), encoding="utf-8"))}
    zeilen, ok, fehl, hashfehler = [], 0, 0, 0
    for u in urteile:
        q = quellen.get(str(u["nr"]))
        if not q:
            continue
        roh_b = open(os.path.join(HERE, q["datei"]), "rb").read()
        roh = roh_b.decode("utf-8")
        if hashlib.sha256(roh_b).hexdigest() != q["sha256"]:
            hashfehler += 1
        text = norm(roh)
        for f in FELDER:
            z = (u.get(f) or "").strip()
            if not z:
                continue
            pos, gefunden, stuecke = 0, True, teile(z)
            if not stuecke:
                continue
            for t in stuecke:
                i = text.find(t, pos)
                if i < 0:
                    i = text.find(t)          # Reihenfolge verletzt, aber vorhanden?
                    gefunden = False if i < 0 else gefunden
                    if i < 0:
                        break
                pos = i + len(t)
            zeilen.append({"nr": u["nr"], "aktenzeichen": u["aktenzeichen"], "feld": f,
                           "gefunden": "ja" if gefunden else "nein", "teilstuecke": len(stuecke),
                           "zitat_anfang": z[:80]})
            ok += gefunden; fehl += (not gefunden)
    with open(os.path.join(HERE, "zitatpruefung.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(zeilen[0])); w.writeheader(); w.writerows(zeilen)
    print(f"Zitate geprüft: {ok+fehl}, gefunden: {ok}, nicht gefunden: {fehl}, Prüfsummenfehler: {hashfehler}")
    for z in zeilen:
        if z["gefunden"] == "nein":
            print("  NICHT GEFUNDEN:", z["nr"], z["aktenzeichen"], z["feld"], "|", z["zitat_anfang"])
    sys.exit(1 if (fehl or hashfehler) else 0)

if __name__ == "__main__":
    main()
