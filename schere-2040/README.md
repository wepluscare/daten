# Die Schere: mehr Hochbetagte, weniger Betreuende

Grafik `grafik/schere.svg` (Markenversion) und `grafik/schere-schlicht.svg` (Dokumentversion), je auch als PNG 2400 × 1350.

**Aussage.** Bis 2040 wächst die Zahl der Menschen ab 65 um 34 Prozent und die der Menschen ab 80 um 52 Prozent (BFS-Referenzszenario). Die Zahl der möglichen Betreuenden je Person ab 65 sinkt gleichzeitig um 18 Prozent (Obsan: «mindestens minus 19 Prozent»), je Person ab 80 um 28 Prozent (eigene Erweiterung). Wir nennen diese Lücke zwischen Pflegebedarf und Betreuenden den Care-Gap.

## Was Obsan gerechnet hat

Obsan-Bulletin 03/2026 (Dutoit & Pellegrini, «Betreuende Angehörige»), S. 5–7, Begleitdokument T1–T3: www.obsan.admin.ch/de/publikationen/2026-bulletin-03-begleitdokument.

- **Potenzielle Betreuende** = Personen zwischen 45 und 69 Jahren («nahezu drei Millionen»).
- **Ältere Personen** = Personen ab 65 Jahren («1,77 Millionen»).
- **Quote** = potenzielle Betreuende ÷ ältere Personen = 1,715 (STATPOP, Ist).
- **Prognose:** gemäss dem mittleren Bevölkerungsszenario des BFS (2025) sinkt die Quote bis 2040 auf 1,4 (minus 19 Prozent); Basisszenario minus 17,6, hohes Szenario minus 19,6 Prozent.
- **Folgen laut Obsan:** 80'000 bis 96'000 weniger Betreuungsverhältnisse; 41'000 bis 87'000 weniger betreute Menschen ab 65.

## Dateien

| Datei | Inhalt |
|---|---|
| `fetch_bfs.py` | holt alle Reihen per BFS-PXWeb-API, nur Python-Standardbibliothek (`python3 fetch_bfs.py`) |
| `raw/<cube>.query.json` | die exakte Abfrage je Würfel |
| `raw/<cube>.response.json` | die unveränderte Antwort des BFS |
| `bfs_bevoelkerung_nach_alter.csv` | Langformat `quelle, jahr, alter, personen`: Ist 2010–2025 (STATPOP) und drei Szenarien 2024–2055, je Einzelalter |
| `bfs_bevoelkerung_nach_alter_geschlecht.csv` | dito nach Geschlecht (STATPOP 2024, Referenzszenario 2024–2055) |
| `schere_aggregate.csv` | je Quelle und Jahr: Personen 45–69, ab 65, ab 80, Total, Quote, Indizes (2024 = 100) |
| `informelle_hilfe_projektion_sgb2022.csv` | Fortschreibung der Angehörigen-Hilfe und Spitex-Nutzung bei heutigen Anteilen (siehe `../bedarf-2040/`) |

BFS-Würfel (https://www.pxweb.bfs.admin.ch/api/v1/de/`<cube>`/`<cube>`.px):

| Würfel | Inhalt | Auswahl |
|---|---|---|
| `px-x-0102010000_101` | STATPOP, ständige Wohnbevölkerung nach Alter, 31.12. | Schweiz · Total Nationalität · Total Geschlecht · Einzelalter · 2010–2025 |
| `px-x-0104020000_101` | Szenarien 2025–2055, Referenzszenario AR-00-2025, Bestand 1.1. | Schweiz · Einzelalter · 2024–2055 |
| `px-x-0104020000_102` | dito, hohes Szenario BR-00-2025 | dito |
| `px-x-0104020000_103` | dito, tiefes Szenario CR-00-2025 | dito |

## Formeln

```
quote(jahr)    = Σ personen(alter 45…69) ÷ Σ personen(alter ≥ 65)      (Obsan-Definition)
quote80(jahr)  = Σ personen(alter 45…69) ÷ Σ personen(alter ≥ 80)      (eigene Erweiterung)
index(jahr)    = 100 × wert(jahr) ÷ wert(2024)                          je Quelle, keine Glättung
```

Gemessen (STATPOP, 31.12.) bis 2024, Szenario (1.1.) ab 2024; beide Reihen sind je auf ihr eigenes Jahr 2024 = 100 gesetzt.

## Ergebnis

| | 45–69 | ab 65 | ab 80 | Quote 65 | Quote 80 |
|---|---|---|---|---|---|
| Ist 2024 (STATPOP 31.12.) | 2,969 Mio | 1,769 Mio | 523'000 | 1,68 | 5,67 |
| Szenario-Basis 2024 (1.1.) | 2,981 Mio | 1,837 Mio | 569'000 | 1,62 | 5,24 |
| Referenz 2040 | 3,246 Mio | 2,456 Mio | 867'000 | 1,32 | 3,74 |
| hoch 2040 | 3,349 Mio | 2,556 Mio | 944'000 | 1,31 | |
| tief 2040 | 3,143 Mio | 2,355 Mio | 792'000 | 1,33 | |

- Quote je Person ab 65, 2024 → 2040: Referenz minus 18,6 Prozent, hoch minus 19,2, tief minus 17,8. Obsan: minus 19 (mittel), minus 19,6 (hoch), minus 17,6 (Basis). Reihenfolge und Grössenordnung stimmen überein.
- Quote je Person ab 80, 2024 → 2040: minus 28 Prozent (Index 2010 = 121, 2040 = 71,5). Diese Zahl ist unsere Erweiterung und wird so zitiert.
- Niveau der Quote: Obsan 1,715 (Ist), hier 1,68 (Ist 2024) bzw. 1,62 (Szenario-Basis). Der Unterschied kommt vom Stichtag (31.12. gegenüber 1.1.) und davon, dass die Szenarien den Bestand ab 65 höher ansetzen. Für die Grafik zählt der Verlauf; wer das Niveau zitiert, zitiert Obsan.
- Die Quote sinkt schon seit 2010 (1,93 → 1,68).

## Das Inset «zwei Zählweisen» (eigene Rechnung)

Obsans Rechenschritt (Bulletin S. 7: bei einer Verringerung um 19 Prozent «würde auch die Zahl der Betreuungsverhältnisse um 19 Prozent sinken») angewendet auf die Bevölkerungsanteile aus dem Bulletin (T2/T3, Erhebungen EFG und IHP):

| Zählweise | Anteil | Personen heute | × 0,19 |
|---|---|---|---|
| eng: betreuen regelmässig (mindestens wöchentlich) eine Person ab 65 | 7 / 8 % | 476'000 / 529'000 | 90'000 / 101'000 |
| weit: betreuen Angehörige, alle Häufigkeiten und Alter | 21 / 26 % | 1'442'000 / 1'773'000 | 274'000 / 337'000 |

Obsan selbst wendet den Schritt nur auf die wöchentlichen Betreuungsverhältnisse an und kommt auf 80'000 bis 96'000. Die grössere Spannweite ist unsere Rechnung.

Warum die beiden Zählweisen nicht als Kurven gezeichnet sind: in der Projektion sind beide ein fester Anteil der Bevölkerung ab 15 (plus 12,6 Prozent bis 2040) und damit deckungsgleich; die gemessene SAKE-Reihe (`../pflegezeit/`) hat 2016 einen Methodenbruch.

## Was die Daten nicht hergeben

- Keine Aufteilung der Prognose in Betreuung und Pflege; die Zusammensetzung der Hilfe gibt es nur für heute (Bulletin S. 5).
- Keine Reihe der auf Hilfe angewiesenen Personen; Näherungen in `../bedarf-2040/`.

## Lesehinweise

- «Mindestens minus 19 Prozent» und «80'000 bis 96'000 Betreuungsverhältnisse weniger» sind Obsan. «Minus 28 Prozent je Person ab 80» und «90'000 bis 337'000 betreuende Angehörige weniger» sind We+, nach Obsans Rechenschritt.
- Die Quote zählt mögliche, nicht tatsächliche Betreuende.

Quellenangabe: BFS – STATPOP; BFS – Szenarien zur Bevölkerungsentwicklung 2025–2055; Obsan-Bulletin 03/2026. Auswertung We+ / We Technology, CC BY 4.0.
