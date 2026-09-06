# Wer versorgt Menschen ab 65: bei zwei Dritteln die Angehörigen

Grafik `grafik/versorgung-heute.svg` (Donut), auch als PNG und in der schlichten Dokumentversion. Aktuellstes Jahr, keine Projektion.

**Aussage.** 518'000 Menschen ab 65 erhalten Pflege oder Hilfe (Schweiz 2023/24, Personen ohne Doppelzählung). Bei 334'000 davon, zwei Dritteln, sind Angehörige beteiligt; 196'000 werden nur von Angehörigen versorgt. Bei einer Spitex angestellt sind davon 3'023 (BAG-Umfrage 2024) bis 11'469 (BFS-Näherung).

| Segment | Personen | Herleitung |
|---|---|---|
| Nur Angehörige | 195'584 | Menschen ab 65 mit Hilfe von Angehörigen aus gesundheitlichen Gründen (SGB-Anteile × Bevölkerung 2024) abzüglich der Überschneidung mit Spitex |
| Spitex-Pflege und Angehörige | 138'706 | 59 Prozent der Spitex-Klientinnen und -Klienten ab 65 (BFS-Medienmitteilung 12.11.2024, SGB 2022) |
| Nur Spitex-Pflege | 96'389 | 41 Prozent der Spitex-Klientinnen und -Klienten ab 65 (Obsan 2023) |
| Pflegeheim, Langzeit | 85'568 | Obsan 09/2025, T 10.1 (2023) |
| Kurzzeitaufenthalt | 2'341 | Obsan 09/2025, T 10.1 (2023) |
| **Total** | **518'588** | Angehörige beteiligt: 334'290 (64 Prozent) |

Alle Altersgruppen zum Vergleich: Spitex 5,3 Prozent der Bevölkerung (476'000 Personen, Spitex-Statistik 2024); Hilfe von Angehörigen 13 Prozent (BFS, SGB 2022).

## Dateien

| Datei | Inhalt |
|---|---|
| `obsan_09_2025_T10-1_bedarf_schweiz.csv` | Obsan-Bedarfstabelle (Heim, Spitex ab 65, Kurzzeit), 2023 und Szenarien |
| `sgb2022_informelle-hilfe_spitex_nach_alter_geschlecht.csv` | SGB 2022: Anteile Hilfe von Angehörigen und Spitex nach Alter und Geschlecht |
| `informelle_hilfe_projektion_sgb2022.csv` | SGB-Anteile × Bevölkerung: Menschen mit Angehörigen-Hilfe und mit Spitex, 2024 und Szenarien |

Rechenschritte und Rohabfragen: siehe `../bedarf-2040/README.md`.

## Lesehinweise

- Die Angehörigen-Hilfe aus der SGB ist eine Untergrenze (Selbstangabe im Haushalt; stark eingeschränkte Personen sind untervertreten). Obsan nennt als Obergrenze 459'000 betreute Menschen ab 65 (EFG 2023).
- Die Überschneidung Spitex/Angehörige (59 Prozent) stammt aus der SGB 2022 und wird auf die Obsan-Klientenzahl übertragen.

Quellenangabe: Obsan 09/2025; BFS – SGB 2022; BFS – STATPOP 2024. Auswertung We+ / We Technology, CC BY 4.0.
