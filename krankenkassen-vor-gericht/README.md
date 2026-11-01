# Krankenversicherer gegen pflegende Angehörige vor Gericht: Daten und Methodik

Stand 1. November 2026 (Erstfassung 5. Oktober 2026, Nachträge siehe unten). Erstellt von We Technology für den Angehörigenverband in Gründung. Rückfragen: media@weplus.care.

Dieses Paket enthält alle öffentlich zugänglichen Gerichtsentscheide, die wir zur Frage gefunden haben, ob und wie Krankenversicherer die Vergütung von Grundpflege durch angestellte Angehörige kürzen. Jede Angabe lässt sich am beigelegten Urteilstext nachprüfen.

## Das Wichtigste

- 66 Entscheide gelesen, 54 davon betreffen einen Streit mit einem Krankenversicherer (46 Verfahren: sechs Entscheide sind Urteile des Bundesgerichts zu ebenfalls erfassten Vorinstanzen, zwei sind Zwischenentscheide im selben Verfahren wie ein erfasster Sachentscheid).
- In 32 Verfahren begründete die Kasse die Kürzung oder Ablehnung mit einer Pflicht der Familie. Gezählt wird je Verfahren der Endentscheid des erfassten Gerichts.
- Ausgang dieser 32: 21 Rückweisungen an die Kasse, 4 Niederlagen der Kasse, 3 teilweise Erfolge, 4 Siege. In 2 der 4 Siege stützte das Gericht die Kürzung auf die Pflicht; in den übrigen 30 schützte kein Gericht die Kürzung aus diesem Grund.
- 21 der 32 Entscheide stammen aus dem Jahr 2026.
- Wartezeit von der ersten Kürzung bis zum Urteil: Median 14,5 Monate (42 Verfahren mit beiden Daten), Spanne 4,7 bis 59,6 Monate; bei den Pflicht-Fällen 14,8 Monate (31 Verfahren).

## Dateien

| Datei | Inhalt |
|---|---|
| `urteile.csv` / `urteile.json` | eine Zeile je Entscheid; JSON enthält zusätzlich Zweitkodierung, Begründungen und Bereinigungen |
| `gesundheit.json` | je Verfahren: Diagnosen, Einschränkungen, gestrichene Pflegehandlungen, Daten für die Wartezeit |
| `quellen.csv` | Gericht, Aktenzeichen, Datum, Link zur Datenbank und zum Gericht, Prüfsumme des Urteilstexts |
| `entscheide/` | die 66 Urteilstexte, wie sie am Abrufdatum vorlagen |
| `pruefe_zitate.py` | prüft Prüfsummen und alle Zitate gegen die Urteilstexte |
| `kennzahlen.py` | rechnet alle Zahlen unter «Das Wichtigste» aus den Tabellen nach |
| `zitatpruefung.csv` | Ergebnis des letzten Laufs |

Nachprüfen: `python3 pruefe_zitate.py` (nur Standardbibliothek). Letzter Lauf (1. November 2026): 131 von 131 Zitaten gefunden, kein Prüfsummenfehler.

## Was erfasst ist

**Einschlägig** ist ein Entscheid, wenn es um Pflegeleistungen nach Krankenversicherungsgesetz geht, die Angehörige erbringen (in der Regel angestellt bei einer Spitex-Organisation), und ein Krankenversicherer Partei ist. Nicht gezählt, aber im Datensatz mit Begründung aufgeführt: Fälle der Invaliden-, Unfall- oder Ergänzungsleistungen, Fälle mit gewöhnlicher Spitex ohne angestellte Angehörige, Tarif- und Bewilligungsverfahren zwischen Organisationen und Kantonen.

**Zeitraum:** Entscheide vom 31. August 2017 bis 14. September 2026, Suche zuletzt am 1. November 2026.

## Wie gesucht wurde

Quelle ist die Entscheiddatenbank opencaselaw.ch (über eine Million Entscheide von Bund und Kantonen). Drei Wege:

1. Vier Stichwortsuchen (Beistandspflicht, Schadenminderungspflicht, Angehörigenpflege, Schiedsgericht, je mit Grundpflege/Spitex/Krankenversicherer), 1002 Kandidaten.
2. Zitationssuche: alle Entscheide, die einen der Leitentscheide (BGE 145 V 161, 150 V 273, 151 V 1 und weitere) oder einen bereits erfassten Fall zitieren, 409 Entscheide.
3. Breite Suche nach acht Begriffen seit 2017 (Grundpflege, Angehörigenpflege, Kinderspitex, Pflegebedarfsermittlung, Bedarfsmeldeformular, interRAI und zwei Kombinationen), 4297 Entscheide.

Insgesamt wurden rund 4600 Volltexte geladen und mit einem Filter in drei Sprachen geprüft (Bezug zur Krankenpflege-Leistungsverordnung, Grundpflege, Krankenversicherer als Partei, Hinweis auf angestellte Angehörige). Wege 2 und 3 brachten gegenüber Weg 1 drei zusätzliche Fälle.

**Nachtrag 1. November 2026.** Dieselben Wege erneut ab Januar 2025 (rund 2700 Kandidaten im Volltext, gleicher Filter; der Filter findet 41 der 46 bisher einschlägigen Entscheide wieder, die fünf übrigen sind Prozessentscheide oder sehr kurze Texte). Zusätzlich alle Zürcher Geschäftsnummern KV.2024 bis KV.2026 direkt auf der Seite des Sozialversicherungsgerichts. Neu erfasst: ZH KV.2025.00123 (11.8.2026), ZG S 2024 31 (14.7.2026), BGer 9C_710/2025 (29.6.2026, Tarifverfahren ohne Kasse) und das Urteil ZH KV.2026.00005 vom 21.4.2026. Zu dieser Nummer lag bisher nur der Beschluss vom 6.2.2026 vor; die Gerichtsseite zeigt unter derselben Adresse inzwischen nur noch das Urteil. Der Beschluss bleibt im Datensatz (`instanz` = `zwischenentscheid_im_selben_verfahren`) und zählt für die Pflicht-Kennzahlen nicht mehr. Das Urteil stammt von der Gerichtsseite, weil die Datenbank unter dieser Nummer nur den Beschluss führt. Die drei anderen Entscheide waren am 5. Oktober noch nicht in der Datenbank oder nicht auffindbar. Ein vermeintlicher Neufund, GR «SV1 2025 49», ist derselbe Urteilstext wie das bereits erfasste GR «SV2 2025 4» (die Referenz im Urteil lautet SV1 25 49); die Datenbank führt ihn doppelt. Er ist nicht doppelt gezählt; Duplikate werden seither am Textvergleich geprüft, nicht nur am Aktenzeichen.

**Zweiter Nachtrag 1. November 2026: unabhängige Nachrecherche.** Ein zweites System suchte ohne Kenntnis unserer Liste (Bundesgericht, kantonale Portale, Zitationswege, drei Sprachen) und glich erst danach ab (der Bericht der Nachrecherche ist auf Anfrage erhältlich). Es fand fünf weitere einschlägige Entscheide: BGer 9C_279/2025 (17.3.2026), GL VG.2023.00091 (21.2.2024), GL VG.2024.00037 (16.1.2025), GL VG.2024.00115 (2.6.2025) und TG VV.2023.148/E (8.1.2025). Drei davon (VG.2024.00037, VG.2024.00115, VV.2023.148/E) sind nicht in der Entscheiddatenbank opencaselaw.ch (Suche nach Aktenzeichen und Entscheiddatum am 1.11.2026; am selben Tag geführte Glarner und Thurgauer Entscheide betreffen andere Verfahren) und wurden auf dem Glarner Gerichtsportal nicht gefunden; das Thurgauer Portal ist nicht durchsuchbar. Zugänglich sind sie auf der Website der Anwaltskanzlei, welche die Versicherten vertritt (pflegerechtsanwalt.ch). **Die Kanzlei wählt selbst aus, was sie veröffentlicht**; diese drei Fälle sind im Feld `bemerkung` gekennzeichnet. Ohne sie wären es 30 Pflicht-Verfahren, in 28 davon keine geschützte Kürzung aus Pflichtgrund. Zwei dieser Texte sind Scans und wurden per Texterkennung (OCR) gelesen; die Zitate folgen dem OCR-Text. In der Thurgauer Fassung war ein Name nicht anonymisiert; er ist im gespeicherten Text geschwärzt. Ein Luzerner Fall (5V 23 176, Concordia) bleibt draussen, weil der Text keine Anstellung von Angehörigen belegt. Die Nachrecherche fand umgekehrt nur 28 unserer 60 bisherigen Entscheide wieder; Vollständigkeit lässt sich mit den zugänglichen Suchsystemen nicht belegen, die Zahlen bleiben eine Untergrenze. Korrigiert wurden ausserdem drei Entscheiddaten (BE 200 2025 503, BE 200 2025 744, NW SV 26 4: in der Tabelle stand das Datum der Datenbank) und zwei fehlende zweite Aktenzeichen (9C_535/2024, 9C_722/2025).

**Dritter Nachtrag 1. November 2026: Volltextsuche auf entscheidsuche.ch.** Fünf Suchen in drei Sprachen ab 2017 (144 Treffer, 92 nicht im Paket) wurden im Volltext gefiltert und geprüft. Neu ist ein Entscheid: TI 36.2025.60 vom 2.2.2026, der Sachentscheid im Tessiner Verfahren, zu dem bisher nur der Entscheid über die Rechtsverzögerung (36.2025.17) erfasst war. Wie beim Zürcher Beschluss zählt nun der Sachentscheid; 36.2025.17 ist als Zwischenentscheid markiert. Die übrigen Treffer betreffen IV, Unfallversicherung, Assistenzbeitrag, Bewilligungen oder sind bereits erfasst (teils unter anderem Aktenzeichen). Die drei Kanzlei-Urteile sind auch auf entscheidsuche.ch nicht vorhanden; zwei davon werden dort in einem erfassten Glarner Urteil (VG.2025.00067) zitiert.

## Wie kodiert wurde

Jeder Entscheid wurde zweimal unabhängig am Volltext kodiert; die zweite Kodierung kannte die erste nicht. Beide Durchgänge wurden von einem Sprachmodell (Claude) ausgeführt, nach schriftlichen Regeln (siehe [`kodierschema.md`](kodierschema.md) und [`kodierschema_gesundheit.md`](kodierschema_gesundheit.md) sowie den Zusatz für die Zweitkodierung). Abweichungen wurden am Urteilstext entschieden; Erstwert, bereinigter Wert und Grund stehen je Entscheid im Feld `bereinigung`.

| Feld | gleich kodiert |
|---|---|
| einschlägig | 65 von 66 |
| Kasse beruft sich auf Pflicht der Familie | 55 von 56 |
| Haltung des Gerichts zur Pflicht | 53 von 56 |
| Ausgang für die Kasse | 56 von 56 |

### Die drei Kernfelder

- **`pflicht_argument_der_kk` = ja** nur, wenn die Kasse selbst (Verfügung, Einspracheentscheid, Rechtsschrift, Schreiben) eine Pflicht der Familie als Grund anführt: Beistands-, Schadenminderungs-, Fürsorge-, Unterhalts- oder Verwandtenunterstützungspflicht, «Ohnehin-Aufwand», «sozial üblich». Bringt nur das Gericht die Pflicht ein, steht `nein` und beim Gericht `gericht_bringt_pflicht_selbst_ein` (zwei Fälle).
- **`gericht_zur_pflicht`:** `folgt_kk` = Gericht schützt die Kürzung aus diesem Grund; `folgt_teilweise` = Gericht bejaht die Pflicht im Grundsatz, schützt die konkrete Kürzung aber nicht oder nur zum Teil; `lehnt_ab` = Pflicht rechtfertigt im Fall keine Kürzung; `offen_gelassen`; `nur_obiter_standardformel`; `nicht_behandelt`.
- **`ausgang_fuer_kk`** nach dem Dispositiv.

## Grenzen

- **Nur publizierte Urteile.** Einspracheentscheide, Vergleiche, zurückgezogene Beschwerden und nicht publizierte Urteile fehlen. Die Zahlen sind eine Untergrenze. Schiedsgerichtsurteile werden selten publiziert.
- **Rückweisung ist kein Sieg der Versicherten.** Die Kasse entscheidet neu; das Ergebnis ist nicht öffentlich. Die Mehrheit der Gerichte (19 von 32) bejaht die Pflicht im Grundsatz. Das Zürcher Sozialversicherungsgericht hält in KV.2025.00123 (E. 4.7) fest, für die Schadenminderungspflicht in der Grundpflege brauche es keine eigene gesetzliche Grundlage.
- **Beide Kodierungen stammen vom selben Modell.** Die Übereinstimmung zeigt, dass die Regeln eindeutig sind, ersetzt aber keine menschliche Kontrolle. Eine juristische Gegenlesung einer Zufallsstichprobe steht aus.
- **`folgt_teilweise` gegenüber `lehnt_ab`** ist die unsicherste Abgrenzung; die Begründung steht je Entscheid in `zweitkodierung_begruendung` und `bemerkung`.
- **Romandie und Tessin** sind dünn vertreten (ein Walliser und zwei Tessiner Fälle). Ob das die Praxis spiegelt oder die Publikation, lässt sich nicht sagen.
- **Anonymisierung.** In acht Entscheiden ist die Kasse nicht genannt.
- **Gruppenzuordnung.** `kk_gruppe` fasst Mutuel, Philos und Avenir zusammen. «Groupe Mutuel» steht im Rubrum von sechs Urteilen; 20 von 21 nennen denselben Rechtsdienst in Martigny. Für die Gesellschaften mit «Mutuel» im Namen ist die Zuordnung unsere.
- **Gesundheitsangaben** stammen oft aus der Beschwerde oder dem Pflegeplan der Spitex, nicht aus Feststellungen des Gerichts (Feld `unsicherheiten`).
- **Datum.** Bei einzelnen Entscheiden weicht das Datum der Datenbank vom Datum im Urteilstext ab; massgebend ist `datum_urteil_laut_text` in `gesundheit.json`.
- **Näherungen.** Angaben wie «in mehr als einem Dutzend Verfahren wurden die Zahlungen gestoppt» beruhen auf Stichwortsuche in den Kodierungen.
- **Urteilstexte** stammen aus der Datenbank, nicht direkt vom Gericht; der Link zum Gericht steht in `quellen.csv`. Die Texte enthalten Seitenzahlen und Trennstriche aus der PDF-Umwandlung; Zitate markieren Seitenumbrüche mit […].

## Personen

Die Urteile sind von den Gerichten anonymisiert. Namen von Anwältinnen und Anwälten haben wir nicht erfasst; sie stehen in den Urteilstexten, wie die Gerichte sie publiziert haben. Die Kombination von Kanton, Jahrgang und Diagnose kann eine Familie am Wohnort erkennbar machen; wer daraus berichtet, sollte das berücksichtigen.


## Nutzung und Lizenz

- **Tabellen, Kodierung, Methodik und Skripte von We Technology:** [Creative Commons Namensnennung 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.de). Namensnennung: «We Technology, Datenpaket Krankenkassen gegen pflegende Angehörige vor Gericht» mit Link auf diesen Ordner.
- **Urteilstexte in `entscheide/`:** Entscheide von Behörden und Gerichten sind nach Art. 5 Abs. 1 Bst. c des Urheberrechtsgesetzes nicht geschützt. Die Texte stammen aus der Entscheiddatenbank opencaselaw.ch, von entscheidsuche.ch, von den Gerichtsportalen oder, bei drei Entscheiden, von der Website der Rechtsvertretung der Versicherten (Fundstelle je Entscheid in `quellen.csv`). Zwei davon sind Scans und per Texterkennung gelesen; in einem war ein Name nicht anonymisiert und ist geschwärzt.
- **Zitiervorschlag:** We Technology (2026): Krankenkassen gegen pflegende Angehörige vor Gericht. Daten und Methodik, Stand 1. November 2026, https://github.com/wepluscare/daten/tree/main/krankenkassen-vor-gericht.
