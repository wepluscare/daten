# Gleiche Ausbildung, anderer Tarif: Pflegehelfer/innen SRK in der Spitex

Grafik `grafik/bezahlt.svg` (Markenversion) und `grafik/bezahlt-schlicht.svg` (Dokumentversion, Titel «Pflegehelfer/innen SRK in der Spitex nach Trägerschaft, 2011 bis 2024»), je auch als PNG 2400 × 1350.

**Aussage.** Die erwerbswirtschaftliche Spitex beschäftigt 2024 erstmals gleich viele Pflegehelferinnen und Pflegehelfer SRK wie der ganze gemeinnützige und öffentliche Sektor, 6'751 gegenüber 6'715, mit einem Drittel des Spitex-Personals. Dieselbe Ausbildung wird im Kanton Zürich 2026 unterschiedlich finanziert: 146.62 Franken Normkosten je Stunde Grundpflege bei der beauftragten Spitex, 68.36 Franken, wenn die Pflegehelferin als angestellte Angehörige arbeitet.

## Quellen

| Quelle | Inhalt | Datei |
|---|---|---|
| BFS, Statistik der Hilfe und Pflege zu Hause, Würfel `px-x-1404040000_103` | Beschäftigte nach Ausbildung/Hauptfunktion und Leistungserbringertyp, Schweiz, 2011–2024, Personen und Vollzeitäquivalente | `bfs_spitex_personal_ausbildung_schweiz.csv`, Abfrage und Antwort in `raw/` |
| Bundesrat, Bericht vom 15.10.2025 (BAG/BASS-Umfrage bei 75 Spitex-Organisationen) | gemeldete angestellte pflegende Angehörige 2022–2024, Vollzeitäquivalente | `angestellte_angehoerige_2011-2024.csv` (Spalten `umfrage_*`) |
| Kreisschreiben «Normdefizite 2026» der Gesundheitsdirektion Zürich (28.08.2025), Beilage 2 | Normkosten, KVG-Beitrag und Normdefizit je Stunde Grundpflege nach Leistungserbringer und Person | Tarifkasten in der Grafik |

Kategorien des BFS-Würfels (Dimension «Ausbildung/Hauptfunktion»), verwendet: Code 154 «Pflege-/Betreuungskurse (z. B. Pflegehelfer/in SRK)»; zum Vergleich Code 155 «Keine spezifische Ausbildung für die geleistete Arbeit» und `PERS_KeinSPX` (Kurse, Praktika und keine spezifische Ausbildung zusammen). Leistungserbringertypen: «Gemeinnützige und öffentlich-rechtliche Unternehmen», «Erwerbswirtschaftliche Unternehmen», «Selbstständige Pflegefachpersonen».

## Ergebnis

Personen mit Pflege- oder Betreuungskurs (Code 154), Schweiz:

| Jahr | gemeinnützig und öffentlich | erwerbswirtschaftlich | Anteil am Personal gemeinn. | Anteil erwerbsw. |
|---|---|---|---|---|
| 2011 | 6'568 | 1'837 | 20 % | 32 % |
| 2014 | 6'726 | 2'947 | 19 % | 36 % |
| 2017 | 6'844 | 3'557 | 18 % | 30 % |
| 2020 | 6'590 | 4'697 | 16 % | 31 % |
| 2022 | 6'972 | 4'981 | 16 % | 29 % |
| 2023 | 6'774 | 4'787 | 16 % | 26 % |
| 2024 | 6'715 | 6'751 | 15 % | 30 % |

- Erwerbswirtschaftliche Spitex 2024: 22'864 von 68'707 Beschäftigten (33 Prozent), aber 50 Prozent der Pflegehelfer/innen SRK.
- Pensen: 0,32 Vollzeitäquivalente je Person bei den Erwerbswirtschaftlichen, 0,44 bei den Gemeinnützigen (2024).
- Zusammen mit «keine spezifische Ausbildung» und Praktika: 31 Prozent des Personals bei den Gemeinnützigen, 51 Prozent bei den Erwerbswirtschaftlichen.
- Gemeldete angestellte Angehörige (BAG-Umfrage, Untergrenze): 333 (2022), 909 (2023), 3'023 (2024).

## Der Tarifvergleich (Kanton Zürich 2026)

| Leistungserbringer, Person | Normkosten | KVG-Beitrag | Normdefizit (Kanton) |
|---|---|---|---|
| Beauftragte Spitex, Fachpersonal (auch Pflegehelfer/in SRK) | 146.62 | 52.60 | 94.00 |
| Angestellte Angehörige, bei beauftragter oder nicht beauftragter Spitex | 68.36 | 52.60 | 15.75 |

Die Vernehmlassungsvorlage zur Totalrevision der Zürcher Pflegeverordnung (10.07.2026) würde vom Personalaufwand für pflegende Angehörige nur 32 Franken je Stunde anrechnen.

## Lesehinweise

- Die BFS-Kategorie zählt Ausbildung, nicht Tätigkeit. «Nur Grundpflege» lässt sich nicht isolieren; die Hauptfunktion (Pflege und Hilfe, Leitung, Administration) ist im Würfel eine getrennte Aufschlüsselung und nicht mit der Ausbildung kreuzbar.
- Die Kategorie sagt nichts über Verwandtschaft. Bei den Gemeinnützigen sind es reguläre Pflegehelferinnen SRK, bei den Erwerbswirtschaftlichen überwiegend, aber nicht nur angestellte Angehörige. Die BAG-Umfrage ist die einzige direkte Zählung.
- Die Ungleichbehandlung liegt an der Person, nicht an der Trägerschaft: auch eine Angehörige bei der beauftragten Spitex wird mit 68.36 Franken finanziert. Der Trägerschaftsvergleich zeigt, wo Pflegehelferinnen mit Verwandtschaft arbeiten.
- Der Tarifvergleich gilt für Zürich 2026. Andere Kantone kennen andere Ansätze, das Prinzip ist dasselbe.
- Pflegehelfer/in SRK ist ein Kurszertifikat; Assistenz Gesundheit und Soziales EBA und Pflegeassistenz SRK sind eine eigene Kategorie mit Berufsabschluss.

Der Würfel enthält eine Kantonsdimension; dieselbe Auswertung ist je Kanton möglich.

Quellenangabe: BFS – Statistik der Hilfe und Pflege zu Hause; Bundesrat 15.10.2025; Gesundheitsdirektion Kanton Zürich, Kreisschreiben Normdefizite 2026. Auswertung We+ / We Technology, CC BY 4.0.
