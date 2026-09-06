# Datenpaket Angehörigenbetreuung Schweiz

Daten, Rechenschritte und Grafiken hinter den Infografiken von We+ zur Angehörigenbetreuung in der Schweiz. Für Medienschaffende, Datenjournalistinnen und Datenjournalisten, Forschung und Verwaltung. Jede Zahl lässt sich bis zur amtlichen Quelle zurückverfolgen; wo wir selbst gerechnet haben, steht die Formel daneben.

*Data package on family caregiving in Switzerland: source data (Swiss Federal Statistical Office, Obsan), documented calculations and the charts published by We+. German only; the CSV files are self-explanatory.*

Herausgeberin: **We Technology**, Trägerin der App We+ (weplus.care). Kontakt für Rückfragen, Hintergrundgespräche und Bestellungen weiterer Auswertungen: **media@weplus.care**.

## Themen

| Ordner | Grafik | Kernaussage | Quellen |
|---|---|---|---|
| [`schere-2040/`](schere-2040/) | Die Schere: mehr Hochbetagte, weniger Betreuende | Bis 2040 nimmt die Zahl der Menschen ab 80 um 52 Prozent zu, die Zahl der möglichen Betreuenden je Person ab 65 sinkt um 18 Prozent (Obsan-Quote), je Person ab 80 um 28 Prozent (eigene Erweiterung). | BFS STATPOP, BFS-Bevölkerungsszenarien 2025, Obsan-Bulletin 03/2026 |
| [`bedarf-2040/`](bedarf-2040/) | Bedarf 2040: bis zu 900'000 Menschen ab 65 mit Pflege oder Hilfe | Bei heutigen Anteilen wächst der Bedarf in jeder Versorgungsform; bezahlt ist ein Strich (3'023 angestellte Angehörige 2024). | Obsan 09/2025 T 10.1, BFS SGB 2022, Bundesrat 15.10.2025 |
| [`pflegehelfer-srk/`](pflegehelfer-srk/) | Gleiche Ausbildung, anderer Tarif: Pflegehelfer/innen SRK in der Spitex | Die erwerbswirtschaftliche Spitex beschäftigt 2024 gleich viele Pflegehelfer/innen SRK wie der ganze gemeinnützige Sektor (6'751 zu 6'715), mit einem Drittel des Personals; dieselbe Ausbildung als angestellte Angehörige wird in Zürich mit 68.36 statt 146.62 Franken je Stunde finanziert. | BFS Spitex-Statistik, Bundesrat 15.10.2025, Kreisschreiben Normdefizite 2026 ZH |
| [`versorgung-heute/`](versorgung-heute/) | Wer versorgt Menschen ab 65 | 518'000 Menschen ab 65 mit Pflege oder Hilfe, bei zwei Dritteln sind Angehörige beteiligt. | Obsan 09/2025, BFS SGB 2022, BFS-Bevölkerung 2024 |
| [`pflegezeit/`](pflegezeit/) | Pflegezeit 2024 | 126 Millionen Stunden unbezahlte Pflege von Erwachsenen pro Jahr, gegenüber rund 1 Million bezahlten Stunden. | BFS SAKE, Modul Unbezahlte Arbeit 2024 |

Jeder Ordner enthält eine `README.md` mit Quellen, Abfragen, Formeln, Ergebnistabellen und Lesehinweisen, die Rohdaten (CSV, wo möglich die unveränderte Antwort der BFS-Schnittstelle unter `raw/`) sowie die Grafiken in `grafik/` als SVG und PNG, je in der Markenversion und in einer schlichten Dokumentversion (`-schlicht`).

## Lesehinweise

- **Quelle oder Rechnung?** Jede README trennt, was die Quelle sagt und was We+ daraus gerechnet hat. Beispiel: Obsan nennt für 2040 «mindestens minus 19 Prozent» mögliche Betreuende und 80'000 bis 96'000 Betreuungsverhältnisse weniger. Die Spannweite «90'000 bis 337'000 betreuende Angehörige weniger» ist unsere Anwendung von Obsans Rechenschritt auf verschiedene Zählweisen, nicht eine Zahl von Obsan.
- **Spannweiten zitieren.** Wo wir Unter- und Obergrenze ausweisen, gehört beides in den Text.
- **Serienbrüche.** Die SAKE-Reihen haben Brüche 2007/2010, 2013/2016 und 2020/2024 (Details in `pflegezeit/README.md`). Zeitvergleiche über einen Bruch hinweg sind nur bedingt möglich.
- **Stichtage.** STATPOP zählt am 31. Dezember, die Szenarien am 1. Januar; Niveaus unterscheiden sich deshalb leicht, Verläufe nicht.

## Nutzung und Lizenz

- **Auswertungen, Tabellen und Grafiken von We+:** [Creative Commons Namensnennung 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.de). Namensnennung: «We+ / We Technology, nach BFS und Obsan» mit Link auf dieses Repository.
- **Rohdaten des Bundesamts für Statistik (BFS) und des Obsan:** gemäss den Nutzungsbedingungen der Quelle, Quellenangabe ist Pflicht («BFS – STATPOP», «BFS – Szenarien zur Bevölkerungsentwicklung 2025–2055», «BFS – SAKE», «BFS – SGB 2022», «Obsan 09/2025»). Die BFS-Daten stehen auf opendata.swiss unter «OPEN BY ASK»: freie Nutzung mit Quellenangabe, für kommerzielle Weiterverwendung der Rohdaten ist das BFS anzufragen.
- Zitiervorschlag: We+ / We Technology (2026): Datenpaket Angehörigenbetreuung Schweiz, Grafik-Satz 2, https://github.com/wepluscare/daten, nach BFS und Obsan.

## Versionen

Jeder Grafik-Satz ist ein Tag (`grafiksatz-2`, …), Änderungen stehen in [`CHANGELOG.md`](CHANGELOG.md). Die Grafiken selbst sind auf weplus.care/medien (Newsroom, Rubrik Infografiken) und weplus.care/public-affairs zu sehen.

## Was nicht hier liegt

Unsere Auswertung des öffentlichen Diskurses (parlamentarische Vorstösse, Medienartikel, Tonalität, Akteursgruppen) geben wir auf Anfrage weiter, mit Methodennote. Ebenso die Originale unserer Eingaben in Vernehmlassungen und Briefings an Parlamente. Anfragen an media@weplus.care.
