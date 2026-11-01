# Zweiter Lesedurchgang: gesundheitliche Lage der Familien

## Wozu
We Technology (Angehörigen-App We+) hat Gerichtsentscheide erfasst, in denen Krankenkassen die Vergütung von Grundpflege durch Angehörige kürzen. Medienschaffende sollen in einer Tabelle sehen, um welche Menschen es geht: welche Krankheit, welche Einschränkungen, welche Pflegehandlungen gestrichen wurden, wie es der pflegenden Person geht. Jede Angabe muss im Urteil stehen. Nichts ergänzen, nichts aus Allgemeinwissen über eine Krankheit ableiten. Fehlt eine Angabe, schreibe `nicht_genannt`.

## Material
Dateien unter `txt/` sind Volltexte mit Kopfzeilen. Die Gesundheitsangaben stehen meist im Sachverhalt und in den Erwägungen zur Bedarfsermittlung (Stichworte: Diagnose, leidet, erkrankt, Geburtsgebrechen, Hilflosenentschädigung, Hilflosigkeit, interRAI, Bedarfsabklärung, Pflegebedarf, Transfer, Inkontinenz, Rollstuhl, Demenz, nachts; französisch/italienisch entsprechend). Lies Sachverhalt und diese Erwägungen vollständig.

## Ausgabe
JSON-Liste (Pfad im Auftrag), ein Objekt je Entscheid, genau diese Felder:

- `nr` (int aus Dateiname), `docket`
- `gepflegte_person_geschlecht`: `w` / `m` / `nicht_genannt`
- `gepflegte_person_jahrgang`: Jahrgang oder Altersangabe wie im Urteil, sonst `nicht_genannt`
- `altersgruppe`: `kind_unter_18`, `18_bis_64`, `65_bis_79`, `80_plus`, `unklar` (Stichtag: Beginn der strittigen Periode; nur wenn aus dem Urteil bestimmbar)
- `diagnosen`: Liste, jede Diagnose so knapp wie im Urteil genannt (Originalsprache)
- `diagnose_kategorie`: Liste aus `neurologisch` (MS, Parkinson, Para-/Tetraplegie, Schlaganfall u. ä.), `demenz`, `geburtsgebrechen_entwicklungsstoerung`, `psychisch`, `onkologisch`, `herz_niere_stoffwechsel`, `altersgebrechlichkeit_multimorbid`, `anderes`, `nicht_genannt`
- `einschraenkungen`: Liste konkreter Einschränkungen laut Urteil (z. B. «rollstuhlabhängig», «Urin- und Stuhlinkontinenz», «kann nicht selbständig essen»), höchstens acht, in den Worten des Urteils
- `pflegehandlungen_gesamt`: Liste der im Urteil genannten Grundpflegehandlungen (z. B. Körperpflege, An-/Auskleiden, Transfer, Lagerung, Toilettengang, Essen eingeben, Kompressionsstrümpfe)
- `gestrichene_handlungen`: Liste der Handlungen, die die Kasse gestrichen oder gekürzt hat, mit Minutenangabe wenn genannt (z. B. «Nägel schneiden, 20 Min./Monat»)
- `nachtpflege`: `ja` / `nein` / `nicht_genannt` (Pflegehandlungen nachts)
- `hilflosenentschaedigung`: `leicht` / `mittel` / `schwer` / `ja_grad_nicht_genannt` / `nein` / `nicht_genannt`
- `weitere_leistungen`: Liste (z. B. Intensivpflegezuschlag, Assistenzbeitrag, IV-Rente, Ergänzungsleistungen), sonst leer
- `pflegebeduerftig_seit`: Jahr oder Angabe wie im Urteil, sonst `nicht_genannt`
- `pflegende_person`: Objekt mit `jahrgang_oder_alter`, `ausbildung` (z. B. Pflegehelferkurs SRK, Pflegefachperson, keine), `erwerbssituation` (was das Urteil dazu sagt, z. B. Pensum bei der Spitex, andere Stelle, Studium, Rentenalter), `eigene_gesundheit_belastung` (was das Urteil dazu sagt); jeweils `nicht_genannt`, wenn nichts steht
- `weitere_helfende`: wer laut Urteil sonst noch pflegt oder hilft (öffentliche Spitex, andere Angehörige), sonst `nicht_genannt`
- `verweis_auf_alternative`: Hat Kasse oder Gericht auf Pflegeheim, externe Spitex oder Dritte verwiesen? Kurz, sonst `nein`
- `datum_erste_verfuegung_oder_kuerzung`: Datum der ersten Kürzungsmitteilung/Verfügung der Kasse (JJJJ-MM-TT), sonst `nicht_genannt`
- `datum_einspracheentscheid`: JJJJ-MM-TT, sonst `nicht_genannt`
- `datum_urteil_laut_text`: JJJJ-MM-TT wie im Urteilstext
- `verstorben_waehrend_verfahren`: `ja` / `nein` / `nicht_genannt`
- `zitat_lage`: EIN wörtliches Zitat (höchstens 350 Zeichen), das die gesundheitliche Lage oder den Pflegealltag am anschaulichsten beschreibt; `zitat_fundstelle` (Sachverhaltsziffer oder Erwägungsnummer exakt wie im Text)
- `unsicherheiten`: was du nicht sicher zuordnen konntest

## Regeln
- Zitate zeichengenau (Zeilenumbrüche und Silbentrennung der Extraktion darfst du auflösen), Auslassungen mit […]. Prüfe jedes Zitat maschinell gegen den Text.
- Keine Namen von Personen erfassen.
- Unterscheide, wessen Aussage etwas ist: Wenn nur die Beschwerde etwas behauptet und das Gericht es nicht feststellt, schreibe das in `unsicherheiten`.
- Schlussantwort an mich: nur der Pfad der JSON-Datei und höchstens acht Zeilen zu Auffälligkeiten und Lücken. Keine Wiederholung der Daten.
