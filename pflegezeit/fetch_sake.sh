#!/bin/sh
# BFS SAKE-Modul «Unbezahlte Arbeit» (Paket 2025-0579, publiziert 04.06.2025) — Rohdaten
# Quelle: BFS SDMX-API stats.swiss. Die vollen CSVs (ca. 160 MB) werden NICHT versioniert;
# dieses Skript zieht sie neu. Die kleinen Auszüge daneben (sake_*.csv) sind versioniert.
set -e
for df in DF_SAKE_MOD_UA_1_ACTIVITY DF_SAKE_MOD_UA_1_GENERAL DF_SAKE_MOD_UA_2; do
  curl -s -A "Mozilla/5.0" -H "Accept: text/csv" \
    "https://disseminate.stats.swiss/rest/data/CH1.SAKE_MOD_UA,$df,1.0.0/all?format=csvfilewithlabels" \
    -o "sdmx_$df.csvfilewithlabels.csv"
  echo "$df: $(wc -l < sdmx_$df.csvfilewithlabels.csv) Zeilen"
done
# Excel «Zeitvolumen für unbezahlte Arbeit» (T 03.06.03.01, Mio Stunden/Jahr, 1997–2024)
curl -s -A "Mozilla/5.0" "https://dam-api.bfs.admin.ch/hub/api/dam/assets/34768200/master" -o 34768200-je-d-03.06.03.01.xlsx
