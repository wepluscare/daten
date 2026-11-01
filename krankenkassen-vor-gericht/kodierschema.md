# Kodierauftrag: Krankenkassen gegen pflegende Angehörige (KVG-Grundpflege)

## Wozu
We Technology (Angehörigen-App We+) will belegen, wie oft und mit welchem Erfolg Schweizer Krankenversicherer vor Gericht die Vergütung von Grundpflege durch pflegende Angehörige (meist bei einer Spitex angestellt, Art. 7 Abs. 2 lit. c KLV) kürzen oder verweigern, und wie oft sie sich dabei auf eine familiäre Pflicht berufen (eheliche Beistandspflicht Art. 159 Abs. 3 ZGB, Schadenminderungspflicht der Angehörigen, elterliche Fürsorge-/Unterhaltspflicht, «Ohnehin-Aufwand», «sozial übliches Mass»). Die Zahlen gehen an Parlament und Medien. Jede Angabe muss am Urteilstext stimmen. Lieber «unklar» als geraten.

## Material
Jede Datei unter `txt/` ist ein Gerichtsentscheid im Volltext, mit Kopfzeilen (decision_id, court, docket, date, citation, url). Die Entscheide sind lang (bis 170'000 Zeichen). Lies Rubrum, Sachverhalt und Dispositiv ganz; für die Erwägungen suche gezielt (grep nach Beistandspflicht, Schadenminderung, Schadensminderung, Fürsorgepflicht, Unterhaltspflicht, Ohnehin, zumutbar, üblich, devoir d'assistance, dommage, obbligo) und lies die betreffenden Erwägungen vollständig, inklusive ihres Endes. Ein Treffer in einer Standardformel (Wiedergabe von BGE 145 V 161) ist nicht dasselbe wie eine tragende Begründung im konkreten Fall: unterscheide das.

## Ausgabe
Schreibe eine JSON-Datei (Pfad steht in deinem Auftrag) mit einer Liste, ein Objekt je Entscheid, genau diese Felder:

- `nr`: Nummer aus dem Dateinamen (int)
- `docket`: Aktenzeichen wie in der Kopfzeile
- `einschlaegig`: `ja` / `nein`. `ja` nur, wenn es um Pflegeleistungen nach KVG/KLV geht, die Angehörige erbringen oder erbringen wollen (angestellt bei Spitex oder selbständig), oder um deren Tarif/Zulassung. Reine IV-, UV-, EL-Fälle = `nein` (dann genügen `nr`, `docket`, `einschlaegig`, `bemerkung`).
- `verfahrenstyp`: eines von `leistungsstreit_versicherte_gegen_kk` (versicherte Person bzw. Angehörige gegen Kasse über Umfang/Bestand der Leistung), `schiedsgericht_spitex_gegen_kk` (Leistungserbringer und Versicherer, Art. 89 KVG, egal wer klagt), `tarif_restfinanzierung_gegen_kanton_gemeinde`, `zulassung_bewilligung`, `anderes`
- `krankenversicherer`: Name der Kasse laut Rubrum, sonst `anonymisiert` oder `keiner`
- `spitex_organisation`: Name laut Urteil, `anonymisiert`, oder `keine`
- `rechtsmittel_von`: wer das Verfahren vor DIESEM Gericht angestrengt hat: `versicherte_person`, `spitex`, `krankenversicherer`, `kanton_gemeinde`, `anderes`
- `beziehung`: wer pflegt wen: `ehegatte`, `konkubinat`, `elternteil_pflegt_minderjaehriges_kind`, `elternteil_pflegt_erwachsenes_kind`, `kind_pflegt_elternteil`, `andere_verwandte`, `mehrere`, `unklar`, `nicht_anwendbar`
- `streitgegenstand`: 1 bis 2 Sätze, konkret (was verlangt, was die Kasse zugestand; Minuten/Stunden/Franken, wenn genannt)
- `kk_hat_gekuerzt_oder_verweigert`: `verweigert_ganz`, `gekuerzt`, `rueckforderung`, `nein`, `nicht_anwendbar`
- `pflicht_argument_der_kk`: `ja` / `nein` / `unklar`. Hat die KASSE (oder die Vorinstanz zu ihren Gunsten) im konkreten Fall mit Beistands-, Schadenminderungs-, Fürsorge-/Unterhaltspflicht oder «Ohnehin-Aufwand» argumentiert?
- `pflicht_art`: Liste aus `beistandspflicht_ehe`, `schadenminderungspflicht_angehoerige`, `elterliche_fuersorge_unterhalt`, `ohnehin_aufwand_altersvergleich`, `konkubinat_analog`, `anderes`
- `pflicht_zitat_kk`: wörtliches Zitat (höchstens 350 Zeichen) der Stelle, an der das Argument der Kasse wiedergegeben wird, plus `pflicht_fundstelle_kk` (z. B. «Sachverhalt B.», «E. 4.2»). Leer, wenn `nein`.
- `gericht_zur_pflicht`: `folgt_kk` (Kürzung wegen Pflicht geschützt), `folgt_teilweise`, `lehnt_ab` (Pflicht rechtfertigt die Kürzung im Fall nicht), `offen_gelassen`, `nur_obiter_standardformel`, `nicht_behandelt`
- `gericht_zitat`: wörtliches Zitat (höchstens 400 Zeichen) der tragenden Aussage des Gerichts zur Pflicht, plus `gericht_fundstelle` (Erwägungsnummer exakt wie im Text). Leer, wenn nicht behandelt.
- `weitere_argumente_kk`: Liste aus `wirtschaftlichkeit_pflegeheimvergleich`, `fehlende_qualifikation`, `betreuung_statt_pflege`, `ueberentschaedigung_he_ipz_iv`, `bedarfsermittlung_mangelhaft`, `keine_aerztliche_anordnung`, `psychiatrische_grundpflege`, `zustaendigkeit_verfahren`, `anderes: …`
- `dispositiv`: die entscheidenden Ziffern des Dispositivs, wörtlich gekürzt (höchstens 300 Zeichen)
- `ausgang_fuer_kk`: `kk_obsiegt` (Kürzung/Verweigerung hält ganz), `kk_obsiegt_teilweise`, `kk_unterliegt` (Kasse muss zahlen bzw. Kürzung aufgehoben und Leistung zugesprochen), `rueckweisung_zur_neuabklaerung` (Entscheid der Kasse oder der Vorinstanz aufgehoben, Sache zurück; im Feld `bemerkung` sagen, zu wessen Gunsten das eher wirkt), `prozessual_ohne_sachentscheid`, `kk_nicht_partei`
- `betraege`: genannte Streitwerte, Stundenansätze, Minuten pro Tag, kurz; sonst leer
- `rechtsvertretung_angehoerigenseite`: `anwaltlich_vertreten` / `nicht_vertreten` / `unklar` (KEINE Namen von Anwältinnen oder Anwälten erfassen)
- `bemerkung`: was sonst wichtig ist, besonders: Hinweise im Urteil auf Serien- oder Parallelverfahren derselben Kasse oder Spitex, Kritik des Gerichts am Verhalten der Kasse (z. B. Rechtsverzögerung, widersprüchliche Begründung, Androhung reformatio in peius), und alle Unsicherheiten deiner Kodierung.

## Regeln
- Zitate müssen zeichengenau aus dem Text stammen (Auslassungen mit […]). Keine Paraphrase im Zitatfeld.
- Erwägungsnummern nur angeben, wenn sie im Text so stehen.
- Bei französischen oder italienischen Entscheiden die Zitate im Original belassen.
- Wenn zwei Aktenzeichen im selben Urteil vereinigt sind, ein Objekt, beide Nummern in `docket`.
- Deine Schlussantwort an mich: nur der Pfad der JSON-Datei und in höchstens zehn Zeilen, was dir beim Kodieren aufgefallen ist (Muster, Zweifelsfälle). Keine Wiederholung der Tabelle.
