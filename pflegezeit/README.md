# Pflegezeit: unbezahlte Pflege von Erwachsenen in der Schweiz

Grafik `grafik/pflegezeit-2024.svg`, auch als PNG und in der schlichten Dokumentversion.

**Aussage.** 2024 leisteten Menschen in der Schweiz rund 126 Millionen Stunden unbezahlte Pflege von Erwachsenen im eigenen und in anderen Haushalten (BFS SAKE, Modul Unbezahlte Arbeit). Bezahlt sind davon rund 1 Million Stunden Grundpflege durch bei einer Spitex angestellte Angehörige (BAG-Umfrage 2024, Bericht des Bundesrats vom 15.10.2025).

## Quelle

BFS, Schweizerische Arbeitskräfteerhebung (SAKE), Modul «Unbezahlte Arbeit» 2024 (Paket 2025-0579 vom 4. Juni 2025), SDMX-Reihen `CH1.SAKE_MOD_U*`. Abfrage in `fetch_sake.sh`.

| Datei | Inhalt |
|---|---|
| `sake_beteiligung_total_1997-2024.csv` | Beteiligung an informeller Freiwilligenarbeit in Prozent der Bevölkerung ab 15, nach Tätigkeit (`code`), 1997–2024 |
| `sake_stunden_pro_woche_total_1997-2024.csv` | Stunden pro Woche je Tätigkeit, Bezugsbevölkerung ab 15 |
| `zeitvolumen_unbezahlte_arbeit_1997-2024.csv` | Jahresvolumen in Millionen Stunden je Kategorie, total, Frauen, Männer |

Codes in `sake_beteiligung_total_1997-2024.csv` (Auswahl): `PFLEGE` Pflege von Erwachsenen, `PFLEGE_VERW` davon Verwandte, `ANDERES_VERW` andere Hilfeleistungen für Verwandte, `KIBE_*` Kinderbetreuung, `INFFA_VERW` informelle Freiwilligenarbeit für Verwandte total, `_T` Total.

## Serienbrüche (aus der BFS-Notiz zur Tabelle T 03.06.03.01)

- 2007 → 2010: Umstellung auf kontinuierliche Erhebung und neue Gewichtung.
- 2013 → 2016: informelle Freiwilligenarbeit neu je unterstützte Person erfragt; Zeitvergleiche «nur bedingt möglich». Die Beteiligung bei «andere Hilfe für Verwandte» springt von 2,8 auf 13,6 Prozent.
- 2020 → 2024: Mixed-Mode-Erhebung (Internet und Telefon) und Fragebogen nach Eurostat IESS; Bruch «für einen Teil der Ergebnisse».

Grafiken mit SAKE-Reihen markieren diese Brüche. Wer Zeitreihen zitiert, zitiert innerhalb eines Abschnitts.

## Lesehinweise

- Die 126 Millionen Stunden sind die Kategorie «Pflege von Erwachsenen» (eigener und anderer Haushalt), nicht die gesamte informelle Hilfe. Mit Kinderbetreuung und anderer Hilfe für Verwandte ist das Volumen ein Mehrfaches.
- Der Vergleich mit den rund 1 Million bezahlten Stunden ist unser Vergleich; die BAG-Umfrage erfasst nur teilnehmende Organisationen (Untergrenze).

Quellenangabe: BFS – SAKE, Modul Unbezahlte Arbeit 2024; Bundesrat 15.10.2025. Auswertung We+ / We Technology, CC BY 4.0.
