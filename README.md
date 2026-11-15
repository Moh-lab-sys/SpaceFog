# Space Fog

NASA Space Apps 2026 · Team Space Fog (Astronauts Cognition)

Space Fog is a crew console that predicts when an astronaut is at risk of cognitive decline, checks them with three short cognitive tests, and proposes moving their high-load task to a rested, qualified crewmate for the Commander to approve.

The app's predictions come from models trained in the notebook on NASA and PhysioNet data.

## What is in this folder

| Path | What it is |
|---|---|
| `app/space-fog.html` | The app. One self-contained file: open it in a browser. The trained models are embedded in it. |
| `notebook/SpaceFog.ipynb` | The notebook, already run from top to bottom, with all outputs and charts. |
| `models/space_fog_models.json` | The trained models as plain numbers, exported by the notebook (Part 12). This is what the app reads. |
| `models/space_fog_phys_model.joblib` | The strain Random Forest as a scikit-learn object (Part 5). |
| `tools/link_app.py` | Puts a newly exported `space_fog_models.json` into the app. |
| `data/` | Snapshots of the data used for training, taken 15 Nov 2026 (see below). |
| `report/Space_Fog_Report.pdf` | The project report, with citations. |
| `docs/` | The team's reference document and the six source documents it combines. |

## How the notebook and the app are linked

```
NASA EDA (RR-1 cabin telemetry) ──► Part 9   cabin MLP ───────────┐
NASA RadLab (DOSTEL-1 dose) ──────► Part 11  radiation MLP ───────┼─► Part 12 ─► space_fog_models.json ─► link_app.py ─► space-fog.html
PhysioNet (ECG, PPG, airway) ─────► Part 5   strain Random Forest ┘
```

| In the app | Model | Trained on |
|---|---|---|
| Risk prediction every 5 minutes: forecast of CO₂, temperature and humidity 6 h ahead, compared with NASA limits | MLP, 45 inputs → 32 → 3 (Part 9) | NASA OSDR Environmental Data Application, mission RR-1 |
| Radiation tile: dose forecast for the next 24 h along the orbit | MLP, 4 inputs → 32 → 1 (Part 11) | NASA OSDR RadLab, DOSIS-3D DOSTEL-1 |
| Physiological strain in the Space Fog risk score | Random Forest, 200 trees (Part 5) | PhysioNet respiratory and heart-rate dataset |

The app repeats the models' arithmetic in JavaScript. Part 12 of the notebook checks that this reproduces scikit-learn's predictions.

The app's "live" cabin and radiation sensors replay the held-out test periods (data the models never trained on). The wearable signals are simulated.

## Re-train and update the app

1. Open `notebook/SpaceFog.ipynb` in Google Colab (it uses `/content`) and run all cells. It downloads everything it needs: about 1.2 GB from PhysioNet, and the NASA data from the OSDR APIs.
2. Download `space_fog_models.json` from `/content`.
3. Run:

```bash
python tools/link_app.py space_fog_models.json app/space-fog.html
```

## Data snapshots in `data/`

| File | Source | Rows |
|---|---|---|
| `eda_rr1_telemetry.json` | `https://visualization.osdr.nasa.gov/eda/api/missions/RR-1/telemetry_data/` | 12,087 readings, every 5 min, 20 Sep – 1 Nov 2014 |
| `eda_rr1_radiation.json` | `https://visualization.osdr.nasa.gov/eda/api/missions/RR-1/radiation_data/` | 39 daily doses |
| `radlab_dostel1_2014-06_to_2014-12.csv.gz` | `https://visualization.osdr.nasa.gov/radlab/api/` (`instrument=DosTel1`) | 192,373 readings, about every 100 s, Jun – Dec 2014 |
| `physionet_labeled_window_features.csv` | Features the notebook extracts from the PhysioNet dataset (Parts 3–4) | 939 fifteen-second windows, 20 subjects |

The raw PhysioNet recordings are not included (1.2 GB): Guy et al. 2024, https://doi.org/10.13026/e4dt-f689.

## Results in one table

| Model | Test result | Simple baseline |
|---|---|---|
| Cabin MLP, 6 h ahead | CO₂ MAE 254 ppm · temperature 0.19 °C · humidity 2.4 % | Persistence: 251 ppm · 0.23 °C · 2.3 % |
| Radiation MLP, next 24 h dose | MAE 0.0064 mGy | Persistence: 0.0108 mGy |
| Strain forest, forced expiration vs rest | ROC-AUC 0.82 on unseen subjects | Rule alone: 0.81 |

The cabin MLP is about as good as assuming "no change in 6 hours": it only clearly wins on temperature. The report discusses this and the other limits.
