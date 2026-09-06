# Bedarf 2040 und bezahlte Angehörigenbetreuung

Zwei Grafiken:

- `grafik/bedarf-balken.svg`: **Bedarf 2040: bis zu 900'000 Menschen ab 65 mit Pflege oder Hilfe.** Personen ohne Doppelzählung, 2023/24 gemessen, 2040 und 2050 bei heutigen Anteilen. Der Stapel liest sich von unten nach oben wie ein Lebenslauf: zu Hause nur mit Angehörigen (fest die Untergrenze, gestrichelt darüber die Obergrenze), mit Spitex (davon ein Strich bezahlt), nur Spitex, Übergang (Kurzzeitaufenthalt), Heim zuoberst.
- `grafik/bezahlt.svg`: **Gleiche Ausbildung, anderer Tarif: Pflegehelfer/innen SRK in der Spitex.** Personen mit Pflege- oder Betreuungskurs (z. B. Pflegehelfer/in SRK) nach Trägerschaft 2011–2024 (BFS, `bfs_spitex_personal_ausbildung_schweiz.csv`, Kategorie 154), darin die gemeldeten angestellten Angehörigen (BAG-Umfrage), dazu die Normkosten je Stunde Grundpflege im Kanton Zürich 2026 für dieselbe Ausbildung: 146.62 Franken bei der beauftragten Spitex, 68.36 als angestellte Angehörige.

Je auch als PNG und in der schlichten Dokumentversion (`-schlicht`).

## Quellen

| Quelle | Inhalt | Datei |
|---|---|---|
| Obsan 09/2025, Tabelle 10.1 | Bedarfsprognose Langzeitpflege Schweiz 2023 → 2040/2050: Bewohnerinnen und Bewohner Langzeit Pflegeheim, Klientinnen und Klienten Spitex-Pflege ab 65, Kurzzeitaufenthalte; Referenz- und weitere Szenarien | `obsan_09_2025_T10-1_bedarf_schweiz.csv` |
| BFS Spitex-Statistik (`px-x-1404040000_102`) | Spitex-Klientinnen und -Klienten ab 65 nach Leistungsangebot, 2011–2024 | `bfs_spitex_klienten_schweiz.csv`, `raw/` |
| BFS SOMED (`px-x-1404010100_301`) | Plätze und fakturierte Tage Langzeit, 2006–2024 | `bfs_somed_angebot_schweiz.csv`, `raw/` |
| BFS Spitex-Statistik (`px-x-1404040000_103`) | Beschäftigte nach Ausbildung und Rechtsform, 2011–2024 | `bfs_spitex_personal_ausbildung_schweiz.csv`, `raw/` |
| BFS SGB 2022, Seite «Informelle Hilfe» | Anteil mit Hilfe von Angehörigen aus gesundheitlichen Gründen und Spitex-Anteil nach Alter und Geschlecht; erhaltene und geleistete Hilfe nach Alter | `sgb2022_*.csv` |
| BFS-Medienmitteilung 12.11.2024 (SGB 2022) | 59 Prozent der Spitex-Unterstützten erhalten auch Hilfe von Angehörigen oder Bekannten | Konstante `OVERLAP` |
| Bundesrat, Bericht vom 15.10.2025 (Postulat) | BAG/BASS-Umfrage bei Spitex-Organisationen: angestellte pflegende Angehörige 2022–2024, Vollzeitäquivalente, rund 1 Million Stunden Grundpflege 2024 | `angestellte_angehoerige_2011-2024.csv` |

## Rechenschritte

**Angehörigen-Hilfe fortgeschrieben (eigene Rechnung).** Altersspezifische Anteile der SGB 2022 (Hilfe von Angehörigen aus gesundheitlichen Gründen, nach Geschlecht und Altersgruppe unter 65, 65–74, 75–84, 85+) multipliziert mit der Bevölkerung nach Alter und Geschlecht (STATPOP 2024, Referenzszenario 2040 und 2050). Status-quo-Logik wie Obsan für die formelle Pflege: die Anteile bleiben konstant, nur die Bevölkerung verändert sich. Ergebnis in `informelle_hilfe_projektion_sgb2022.csv`.

```
personen(jahr, gruppe) = Σ_{geschlecht, alter} bevölkerung(jahr, geschlecht, alter) × anteil_SGB2022(geschlecht, altersgruppe)
```

| | 2024 | 2040 | 2050 |
|---|---|---|---|
| Menschen ab 65 mit Hilfe von Angehörigen (Untergrenze, SGB) | 334'000 | 465'000 | 526'000 |
| Obergrenze (Obsan 03/2026, EFG: 459'000 im Jahr 2023, gleich fortgeschrieben) | 459'000 | 638'000 | 722'000 |
| Menschen ab 65 mit Spitex (Selbstangabe SGB) | 168'000 | 247'000 | 292'000 |

**Ohne Doppelzählung.** Von der Angehörigen-Hilfe wird der Teil abgezogen, der zugleich Spitex-Pflege erhält (59 Prozent der Spitex-Klientinnen und -Klienten, BFS 12.11.2024). Dieser Teil ist in der Grafik schraffiert.

**Bezahlt (nur 2024).** 3'023 bei einer Spitex angestellte pflegende Angehörige (BAG/BASS-Umfrage, 75 Organisationen, 614 Vollzeitäquivalente; Untergrenze, nur teilnehmende Organisationen). BFS-Näherung: 11'469 Beschäftigte ohne spezifische Pflegeausbildung oder nur mit Pflegekurs bei erwerbswirtschaftlichen Spitex-Organisationen (Würfel `px-x-1404040000_103`). Die Entwicklung nach 2024 ist politisch offen und wird nicht fortgeschrieben.

| Jahr | BFS-Näherung | BAG/BASS-Umfrage |
|---|---|---|
| 2020 | 6'717 | |
| 2021 | 7'329 | |
| 2022 | 7'843 | 333 (118 VZÄ) |
| 2023 | 7'818 | 909 (278 VZÄ) |
| 2024 | 11'469 | 3'023 (614 VZÄ) |

## Ergebnis der Grafik «Bedarf 2040» (Referenzszenario)

| | 2023/24 | 2040 | 2050 |
|---|---|---|---|
| Nur Angehörige (Untergrenze) | 196'000 | 269'000 | 305'000 |
| Spitex und Angehörige zugleich | 139'000 | 196'000 | 222'000 |
| Nur Spitex | 96'000 | 136'000 | 154'000 |
| Kurzzeitaufenthalt | 2'000 | 3'000 | 4'000 |
| Pflegeheim, Langzeit | 86'000 | 129'000 | 153'000 |
| **Total (Untergrenze)** | **519'000** | **734'000 (+41 %)** | **838'000 (+62 %)** |
| Total mit Obergrenze der Angehörigen-Hilfe | 643'000 | 907'000 | 1'034'000 |

## Pflegehelfer/innen SRK nach Trägerschaft (Grafik «Gleiche Ausbildung, anderer Tarif»)

| Jahr | gemeinnützig und öffentlich | erwerbswirtschaftlich | Anteil am Personal gemeinn. | Anteil erwerbsw. |
|---|---|---|---|---|
| 2011 | 6'568 | 1'837 | 20 % | 32 % |
| 2017 | 6'844 | 3'557 | 18 % | 30 % |
| 2020 | 6'590 | 4'697 | 16 % | 31 % |
| 2024 | 6'715 | 6'751 | 15 % | 30 % |

Quelle: BFS-Würfel `px-x-1404040000_103`, Dimension «Ausbildung/Hauptfunktion», Code 154 «Pflege-/Betreuungskurse (z. B. Pflegehelfer/in SRK)», Anzahl Personen, Schweiz. Erwerbswirtschaftliche Spitex 2024: 22'864 von 68'707 Beschäftigten (33 Prozent), aber 50 Prozent der Pflegehelfer/innen SRK. Grenzen: die Kategorie zählt Ausbildung, nicht Tätigkeit («nur Grundpflege» lässt sich nicht isolieren; die Hauptfunktion ist im Würfel eine getrennte Aufschlüsselung), und sie sagt nichts über Verwandtschaft; die BAG-Umfrage ist die einzige direkte Zählung angestellter Angehöriger. Der Tarifvergleich gilt für Zürich 2026; die Ungleichbehandlung liegt an der Person (verwandt), nicht an der Trägerschaft.

## Lesehinweise

- Obsan prognostiziert die formelle Pflege (Heim, Spitex, Kurzzeit). Die Angehörigen-Hilfe und die Zusammenführung ohne Doppelzählung sind We+.
- Unter- und Obergrenze gehören zusammen in den Text: «519'000 bis 643'000 Menschen ab 65 mit Pflege oder Hilfe (2023/24)».
- Der Strich «bezahlt» ist keine Prognose; die beiden Zählungen messen Verschiedenes (Umfrage bei Organisationen gegenüber Personalstatistik nach Ausbildung).

Quellenangabe: Obsan 09/2025; BFS – Spitex-Statistik; BFS – SOMED; BFS – SGB 2022; Bundesrat 15.10.2025. Auswertung We+ / We Technology, CC BY 4.0.
