# Hilfe und Pflege zu Hause in der EL: sechs Kategorien, eine Zahl

Die Ergänzungsleistungen (EL) vergüten Kosten für Hilfe, Pflege und Betreuung
zu Hause (Art. 14 ELG). Die Kantone bezeichnen dabei mehrere klar getrennte
Kategorien — die Bundesstatistik fasst sie in **einer** Spalte zusammen.
Dieser Ordner enthält beides: die amtlichen Kategorien und die eine Zahl.

**Die Leerstelle ist der Gegenstand.** Wie viel von diesem Geld an
Familienangehörige geht, weist keine öffentliche Statistik aus.

## Was die Quelle sagt

Das BSV veröffentlicht in der EL-Statistik die vergüteten Krankheits- und
Behinderungskosten je Kanton, aufgeteilt nach Kostenart. Eine dieser Kostenarten
heisst **«Haushaltshilfe und Pflege zu Hause»**. 2025 entfielen darauf
**17,65 Prozent** der gesamten vergüteten Krankheits- und Behinderungskosten.

Die Kategorien, die ein Kanton darunter führt, zeigt das Beispiel der SVA
Aargau. Sie lauten dort wörtlich:

| Kategorie | Rahmen laut SVA Aargau |
|---|---|
| Hauswirtschaftliche Leistungen | höchstens 25 Fr./Stunde, 4’800 Fr./Jahr |
| Betreuung durch Organisationen | — |
| Pflege – Patientenbeteiligung Spitex | höchstens 15.35 Fr./Tag |
| Pflege und Betreuung durch direkt angestelltes Pflegepersonal | setzt eine Hilflosenentschädigung voraus |
| Pflege und Betreuung durch Familienangehörige | Hilflosenentschädigung und mindestens 10 % Erwerbsausfall |
| Begleitetes oder betreutes Wohnen | höchstens 25 Fr./Stunde, 4’800 Fr./Jahr |

Die SVA Aargau führt zusätzlich einen «Pauschalbetrag für ein selbstbestimmtes
Wohnen» (300 Fr./Monat). Er ist hier **nicht** aufgeführt, weil er eine
Aargauer Besonderheit ist und die Liste sonst als schweizweite Struktur
missverstanden würde.

**Die Ausgestaltung ist kantonal.** Andere Kantone gliedern und benennen
anders, setzen andere Höchstbeträge — oder vergüten eine Kategorie gar nicht.

## Was wir gerechnet haben

Aus dem Anteil und den vergüteten Krankheits- und Behinderungskosten des
Kantons ergibt sich der Betrag, aus dem Betrag und der Wohnbevölkerung der
Wert je Einwohnerin:

```
Betrag (Mio Fr.)  = KB-Kosten des Kantons (Mio Fr.) × Anteil (%) / 100
Fr. je Einwohner  = Betrag × 1'000'000 / ständige Wohnbevölkerung 31.12.2025
```

Das ist der einzige Rechenschritt. Beide Eingangsgrössen stammen unverändert
aus den Quellen; nichts ist geschätzt, fortgeschrieben oder modelliert.

**Warum je Einwohnerin und nicht nur der Anteil:** Der Anteil misst mit, wie
gross der Krankheits- und Behinderungskosten-Topf eines Kantons überhaupt ist.
Genf etwa liegt beim Anteil auf Rang 15, je Einwohnerin auf Rang 6. Beide
Ansichten stehen im CSV; wer Kantone vergleicht, sollte beide ansehen.

## Ergebnis

25 Kantone zusammen: **91,0 Mio Franken**, im Mittel **12,14 Fr. je Einwohnerin**.

Höchste Werte: Basel-Stadt 37.68 · Waadt 23.81 · Jura 19.11 Fr.
Tiefste Werte: Nidwalden 2.66 · Zug 2.49 · Appenzell Innerrhoden 1.18 Fr.

## Lesehinweise

- **Zürich fehlt.** Die Tabelle T5.2 weist Zürich nicht aus. Der Datensatz
  umfasst deshalb 25 Kantone, und die 91,0 Mio sind die Summe dieser 25 — nicht
  der Schweizer Gesamtwert. Auch der Mittelwert von 12,14 Fr. ist der Wert der
  25 Kantone, keine schweizerische Kennzahl.
- **Die Zahl misst nicht die Angehörigenvergütung.** Sie enthält Spitex-
  Patientenbeteiligung, Haushaltshilfe, Betreuung durch Organisationen,
  betreutes Wohnen und Angehörigenbetreuung zusammen. Ein Satz wie «Kanton X
  zahlt Y Franken für Angehörigenbetreuung» lässt sich aus diesen Daten **nicht**
  belegen.
- **Kein Rückschluss von tiefen Werten auf strenge Regeln.** Appenzell
  Innerrhoden hat den tiefsten Wert und, soweit wir sehen, keine besonderen
  Einschränkungen; Basel-Stadt den höchsten. Was die Unterschiede erklärt —
  Regeln, Praxis, Altersstruktur, Heimquote — sagt dieser Datensatz nicht.
- **Der Mittelwert ist keine Norm.** Die gestrichelte Linie in der Grafik ist
  die Summe der 25 Kantone geteilt durch ihre Bevölkerung, kein Sollwert.
  Rechtlich gibt es keine Vorgabe, wie hoch dieser Wert sein müsste.

## Dateien

| Datei | Inhalt |
|---|---|
| `el_pflege_zu_hause_kantone.csv` | Ergebnistabelle: Kanton, KB-Kosten, Anteil, Betrag, Bevölkerung, Fr./Einwohner |
| `fetch_el_pflege.py` | Aufbereitung, nur Standardbibliothek — erzeugt CSV und `raw/` neu |
| `raw/bsv_t5.2_2025_kantone.csv` | die aus T5.2 entnommenen Zeilen, unverändert |
| `raw/px-x-0102010000_102.query.json` | die exakte BFS-Abfrage |
| `raw/px-x-0102010000_102.response.json` | die unveränderte BFS-Antwort |
| `grafik/el-kategorien.*` | «Sechs Kategorien, eine Zahl» |
| `grafik/el-pflege-zu-hause.*` | Kantonsvergleich je Einwohnerin |

`-schlicht` bezeichnet die neutrale Dokumentfassung ohne Wortmarke.

## Quellen

- BSV, **Statistik der Ergänzungsleistungen zur AHV und IV 2025** (Mai 2026),
  Detailtabelle T5.2 «Vergütete Krankheits- und Behinderungskosten der EL nach
  Kostenart», Blatt 2025. https://www.bsv.admin.ch/de/statistik-el
- BFS, **STATPOP**, ständige Wohnbevölkerung nach Kanton, 31.12.2025, PXWeb-Würfel
  `px-x-0102010000_102`.
- SVA Aargau, **Ergänzungsleistungen — Krankheits- und Behinderungskosten**,
  Kategorien und Höchstbeträge wörtlich übernommen, Abruf 6. September 2026.
  https://www.sva-aargau.ch/dienstleistungen/unsere-sozialversicherungen/ergaenzungsleistungen/krankheits-und-1
- Rechtsgrundlage: Art. 14 des Bundesgesetzes über Ergänzungsleistungen zur
  AHV und IV (ELG, SR 831.30) und die kantonalen Verordnungen.

Lizenz: siehe [`../LICENSE.md`](../LICENSE.md). Auswertungen und Grafiken von
We+ unter CC BY 4.0, Namensnennung «We+ / We Technology, nach BSV und BFS».
