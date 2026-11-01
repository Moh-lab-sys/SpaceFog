# Space Fog — Project Reference

NASA Space Apps 2026 · Team Space Fog (Astronauts Cognition)

One reference for the Space Fog app: where the real NASA data lives, what it contains, what to measure on astronauts, how cognitively demanding each crew task is, and how it all feeds the app. Combined from six team docs (originals in [`sources/`](sources/)).

## Contents

1. [The app in one paragraph](#1-the-app-in-one-paragraph)
2. [Where NASA keeps the data](#2-where-nasa-keeps-the-data)
3. [Astronaut cognition data (Dev et al. 2024)](#3-astronaut-cognition-data-dev-et-al-2024)
4. [NASA Twins Study](#4-nasa-twins-study)
5. [Spacecraft environment data](#5-spacecraft-environment-data)
6. [What to measure on astronauts](#6-what-to-measure-on-astronauts)
7. [Crew tasks and cognitive load](#7-crew-tasks-and-cognitive-load)
8. [How it fits together in Space Fog](#8-how-it-fits-together-in-space-fog)
9. [Open questions](#9-open-questions)
10. [Sources](#10-sources)

---

## 1. The app in one paragraph

Cabin environment measurements (CO₂, temperature, humidity, radiation) and crew signals (sleep, heart rate) drive a periodic **cognitive-decline risk prediction**. When predicted risk is high, the astronaut takes a short cognitive test. Scores are z-scored against a real NASA astronaut baseline; **z ≤ −1.5 is abnormal**. If one astronaut is abnormal, their high-load tasks move to a crewmate with normal scores. If most of the crew is flagged, it is treated as a **group issue** caused by external factors.

---

## 2. Where NASA keeps the data

NASA splits its data by science division. Human astronaut data lives in the life-sciences branch, mostly behind a request process; spacecraft environment data is open. Rows marked ★ are the ones relevant to Space Fog.

| Category | Repository | What it holds | Access |
|---|---|---|---|
| ★ Human research (life sciences) | [NASA Life Sciences Portal (NLSP)](https://www.nasa.gov/?p=213360) | Gateway to all archived data from NASA Human Research Program (HRP) studies | Search open; data by request |
| ★ Human research → research data | [Life Sciences Data Archive (LSDA)](https://www.nasa.gov/?p=213360) | Human, plant and animal research data from 1961 (Mercury) to current ISS and flight-analog studies | By request (de-identified) |
| ★ Human research → standardized measures | Standard Measures repository (via NLSP) | Same core tests run on every ISS astronaut (includes the Cognition battery) | By request |
| ★ Space biology & physical sciences | [Open Science Data Repository (OSDR)](https://osdr.nasa.gov/bio/repo/data/missions/SpaceX%20Inspiration4) = GeneLab + Ames LSDA (ALSDA) + NASA Biological Institutional Scientific Collection | Omics and physiology from spaceflight experiments (mostly rodents, plants, microbes), Inspiration4 human omics, **ISS cabin and radiation telemetry (EDA, RadLab)** | Mostly open; raw human data controlled |
| Human research → clinical data | [Lifetime Surveillance of Astronaut Health (LSAH)](https://nlsp.nasa.gov/explore/lsdahome/datarequest) | Astronaut medical/clinical records | By request, strict privacy review |
| Commercial spaceflight (non-NASA) | TRISH Commercial Spaceflight Data Repository (TrialX) | Inspiration4 data incl. Dragon cabin readings | Controlled access |
| Earth science | Earthdata (DAACs) | Satellite and climate data | Open |
| Planetary science | Planetary Data System (PDS) | Mission data from planets, moons, small bodies | Open |
| Astrophysics | MAST, HEASARC, IRSA | Telescope archives (e.g., Hubble, JWST) | Open |
| Heliophysics | Space Physics Data Facility (SPDF) | Sun and space-weather data | Open |
| Reports | NASA Technical Reports Server (NTRS) | Technical papers and presentations | Open |

The Earth, planetary, astrophysics, heliophysics and reports rows are listed for orientation only; they are not relevant to Space Fog.

### The datasets Space Fog uses

| Dataset | NASA? | Repository class | Access | Role in Space Fog |
|---|---|---|---|---|
| ISS Standard Measures — Cognition (Dev et al. 2024) | Yes, NASA HRP | NLSP / LSDA, human research → Behavioral Health & Performance | Raw: by request; summary tables open in paper | **Main source:** baseline norms + abnormal cutoff |
| ISS cabin environment — EDA / RadLab | Yes, NASA OSDR | OSDR, environmental monitoring telemetry | **Open download** | **Only real dataset we can train on this weekend** |
| Inspiration4 — Cognition + Apple Watch + Dragon cabin (Jones et al. 2024) | No; SpaceX mission, NASA-funded via TRISH | TRISH repository; omics on OSDR | Controlled access | Secondary: links sleep, HRV and cabin CO₂ to cognition |
| NASA Twins Study (Garrett-Bakelman et al. 2019) | Yes | LSDA | By request | Case study only (1 astronaut + twin) |

Key difference: environment readings describe the spacecraft, not a person, so there is no privacy barrier. All astronaut-level data needs a request.

---

## 3. Astronaut cognition data (Dev et al. 2024)

The ISS cognition data is classed as **Life sciences → Human Research Program → NLSP → LSDA / Standard Measures → Behavioral Health & Performance**, deposited in LSDA under experiment ID `ea3997a6-1093-5e0f-8f54-47684d4f1e73` ([dataset page](https://nlsp.nasa.gov/view/lsdapub/lsda_experiment/ea3997a6-1093-5e0f-8f54-47684d4f1e73)). The paper publishes baseline and per-phase scores openly, so the tables below are usable without a data request.

**Paper:** [Dev SI, Khader AM, Begerowski SR, Anderson SR, Clément G, Bell ST. *Cognitive performance in ISS astronauts on 6-month low earth orbit missions.* Front. Physiol. 15:1451269 (2024)](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2024.1451269/full). Open access (CC BY).

| Question | Answer |
|---|---|
| Components | 10-test Cognition battery (speed + accuracy per test); self-reported sleep hours the night before; alertness rating 0–10. No wearable data. |
| Labelled? | By subject and mission phase only. No impairment labels; the paper defines a **low score as z ≤ −1.5** vs pre-flight baseline. |
| Size | 25 astronauts (age 33–61, 32% female) × 5 sessions ≈ 125 sessions, ~37 min each; 4 subtest results excluded for quality. |
| Published? | Yes, Nov 2024; Tables 1–4 give baseline, per-phase z-scores, low-score rates, sleep/alertness. |
| When | Pre-flight (~90 days before launch), early flight (~30 days in), late flight (~30 days before return), early post (~10 days), late post (~30 days). Mission years not stated. |
| Where | ~6-month ISS missions; tested on HP ZBook laptops. |
| Who | NASA Behavioral Health & Performance Laboratory, Johnson Space Center; funded by NASA HRP Standard Measures Cross-Cutting Project. |

### The 10 cognitive tests

The Cognition battery (Basner et al., 2015) has 10 short computerized tests modeled on classic neuropsychology tasks, with 15 alternate versions to limit practice effects. Speed = mean reaction time in ms; accuracy = proportion correct (0–1).

| Code | Test | What the astronaut does | What it measures | Scores |
|---|---|---|---|---|
| PVT | Psychomotor Vigilance Test | Presses a key as fast as possible when a counter appears at random moments (3 min) | Sustained attention; the most sleep-sensitive test | Speed (10 − 1/RT), accuracy (lapses > 355 ms, false starts) |
| DSST | Digit–Symbol Substitution Task | Matches symbols to digits using a legend, as fast as possible for 90 s | Processing speed, visual scanning | Speed, accuracy |
| F2B | Fractal 2-Back | Responds when the current fractal matches the one shown two steps back | Working memory | Speed, accuracy (hits + correct rejections) |
| VOLT | Visual Object Learning Test | Memorizes 3D shapes, then picks them out among new ones | Visual learning & memory | Speed, accuracy |
| AM | Abstract Matching | Matches an object to one of two pairs using a hidden rule | Abstraction, concept formation (executive function) | Speed, accuracy |
| MRT | Matrix Reasoning Test | Picks the missing piece that completes a pattern grid | Abstract reasoning | Speed, accuracy |
| LOT | Line Orientation Test | Rotates one line until it is parallel to another | Spatial orientation | Speed, accuracy (clicks off target) |
| ERT | Emotion Recognition Test | Labels faces as happy, sad, angry, fearful or no emotion | Emotion identification | Speed, accuracy |
| BART | Balloon Analogue Risk Test | Pumps a balloon for reward or cashes out before it pops | Risk-taking | Speed, risk score (0–1, higher = more risk) |
| MPT | Motor Praxis Task | Clicks shrinking squares as they appear | Sensorimotor speed | Speed only |

### Table 1 — Pre-flight baseline raw scores (normative reference)

Speed in ms (PVT speed = 10 − 1/RT); accuracy as proportion 0–1.

| Subtest | N | Mean | Median | SD | Min | Max |
|---|---|---|---|---|---|---|
| VOLT Speed | 25 | 1627.96 | 1506 | 617.83 | 712.20 | 3097.40 |
| VOLT Accuracy | 25 | .95 | .95 | .06 | .78 | 1.0 |
| F2B Speed | 24 | 552.94 | 530.80 | 60.95 | 469.40 | 670.0 |
| F2B Accuracy | 24 | .92 | .93 | .07 | .77 | 1.0 |
| AM Speed | 25 | 2353.32 | 2179.6 | 877.69 | 1028.0 | 4587.1 |
| AM Accuracy | 25 | .81 | .84 | .11 | .60 | 1.0 |
| LOT Speed | 24 | 4691.30 | 4455.30 | 1183.95 | 2874.20 | 7026.1 |
| LOT Accuracy | 24 | .78 | .81 | .08 | .58 | .97 |
| ERT Speed | 25 | 2645.30 | 2631.82 | 886.40 | 1439.60 | 4720.38 |
| ERT Accuracy | 25 | .72 | .72 | .11 | .47 | .92 |
| MRT Speed | 25 | 8546.15 | 8021.43 | 2340.55 | 5114.22 | 13,908.73 |
| MRT Accuracy | 25 | .79 | .83 | .14 | .49 | .99 |
| DSST Speed | 25 | 1209.38 | 1184.2 | 145.95 | 932.9 | 1485.1 |
| DSST Accuracy | 25 | .98 | .98 | .02 | .95 | 1 |
| BART Speed | 25 | 637.83 | 575.44 | 429.65 | 0 | 1702.88 |
| BART Risk | 25 | .72 | .74 | .11 | .43 | .93 |
| PVT Speed | 24 | 5.25 | 5.21 | .24 | 4.75 | 5.73 |
| PVT Accuracy | 24 | .97 | .97 | .04 | .81 | 1 |
| MPT Speed | 25 | 1061.18 | 1040.5 | 153.53 | 855.5 | 1434.3 |

### Table 2 — Z-scores by mission phase, mean (SD)

Z vs the group's pre-flight baseline; higher = better (faster or more accurate). BART Risk: higher = more risk-taking.

| Subtest | Pre-flight | Early flight | Late flight | Early post-flight | Late post-flight |
|---|---|---|---|---|---|
| Summary Speed | −.02 (.59) | −.33 (.54) | −.18 (.61) | −.13 (.64) | −.04 (.50) |
| Summary Accuracy | −.03 (.43) | −.07 (.41) | −.06 (.37) | −.20 (.44) | −.22 (.44) |
| VOLT Speed | −.02 (1.09) | −.10 (1.17) | .09 (.79) | .07 (.91) | .004 (.77) |
| VOLT Accuracy | −.04 (1.14) | −.13 (1.04) | −.21 (.85) | .03 (.86) | −.52 (1.10) |
| F2B Speed | −.01 (1.07) | −1.24 (1.64) | −1.06 (1.59) | −.82 (1.40) | −1.24 (1.41) |
| F2B Accuracy | −.02 (1.08) | .24 (.76) | .01 (.97) | −.15 (.95) | −.16 (.96) |
| AM Speed | −.02 (1.10) | .10 (.87) | .38 (.79) | .45 (.71) | .50 (.52) |
| AM Accuracy | −.01 (1.07) | −.42 (1.38) | −.09 (1.01) | −.38 (1.40) | −.55 (1.27) |
| LOT Speed | −.01 (1.07) | −.15 (1.06) | −.24 (.97) | −.11 (.95) | −.14 (.87) |
| LOT Accuracy | −.01 (1.13) | .29 (.90) | .14 (.87) | −.13 (1.00) | .06 (1.09) |
| ERT Speed | −.02 (1.10) | .03 (.88) | .12 (.92) | .40 (.74) | .39 (.69) |
| ERT Accuracy | −.01 (1.08) | −.23 (.70) | −.04 (1.15) | −.10 (1.13) | .31 (.99) |
| MRT Speed | −.01 (1.08) | −.33 (1.09) | −.19 (1.18) | .13 (1.20) | .41 (1.07) |
| MRT Accuracy | −.02 (1.09) | −.29 (.85) | −.45 (1.03) | −.40 (1.17) | −.38 (1.01) |
| DSST Speed | −.01 (1.08) | −.79 (1.54) | −.73 (1.48) | −.75 (1.72) | −.33 (1.39) |
| DSST Accuracy | −.01 (1.07) | .04 (1.17) | .22 (1.11) | −.20 (1.38) | −.30 (1.58) |
| BART Speed | −.01 (1.09) | −.11 (.95) | .01 (.90) | −.19 (.75) | .02 (.80) |
| BART Risk | −.02 (1.12) | −.20 (1.19) | −.88 (.95) | −.72 (1.02) | −.96 (1.05) |
| PVT Speed | −.003 (1.08) | −.53 (1.04) | −.23 (1.43) | −.39 (1.45) | −.40 (1.73) |
| PVT Accuracy | −.11 (1.48) | −.09 (.68) | −.06 (.61) | −.29 (1.06) | −.19 (1.03) |
| MPT Speed | −.02 (1.09) | −.16 (.99) | .02 (.87) | .12 (1.18) | .41 (.89) |

### Table 3 — Share of low scores (z ≤ −1.5) during flight and post-flight, %

| Subtest | Speed | Accuracy | Subtest total |
|---|---|---|---|
| BART | 7.1 | 19.2 (risk) | 13.3 |
| F2B | 28.3 | 9.1 | 18.7 |
| DSST | 19.4 | 14.3 | 16.7 |
| PVT | 20.2 | 7.1 | 13.6 |
| MRT | 11.1 | 13.1 | 12.1 |
| AM | 1.01 | 20.2 | 10.6 |
| VOLT | 5.1 | 13.1 | 9.1 |
| MPT | 8.1 | — | 8.1 |
| LOT | 7.1 | 7.1 | 7.1 |
| ERT | 5.1 | 8.1 | 6.6 |
| **Total** | **11.2** | **12.4** | **11.8** |

### Table 4 — Self-reported sleep and alertness, mean (SD) range

Sleep = hours slept the night before testing; alertness 0 (tired) to 10 (alert).

| Measure | Pre-flight | Early flight | Late flight | Early post-flight | Late post-flight |
|---|---|---|---|---|---|
| Sleep (h) | 6.53 (1.56) .75–8.5 | 6.42 (.94) 4–8 | 6.38 (1.21) 3–8 | 7.24 (1.23) 3.5–9 | 6.98 (.70) 6–8 |
| Alertness | 6.56 (2.02) 2–9 | 6.46 (1.89) 3–10 | 5.96 (2.46) 2–9 | 5.92 (2.25) 2–9 | 6.32 (2.10) 3–10 |

**Key reading:** early flight slowed processing speed (DSST), working memory (F2B) and sustained attention (PVT); risk-taking dropped after early flight. The paper found no clear link between self-reported sleep or alertness and test scores.

---

## 4. NASA Twins Study

Stored in **LSDA**, reached through the NLSP. Not downloadable: you submit a [data request](https://nlsp.nasa.gov/explore/lsdahome/datarequest), and NASA withholds even the accession codes for privacy, since the two subjects are publicly known ([Nature Comms 2024 data statement](https://www.nature.com/articles/s41467-024-48920-y)). Same class as the ISS cognition data: **Life sciences → HRP → NLSP → LSDA → Behavioral Health & Performance**. What you can use today is the results and figures in the published paper.

**Paper:** [Garrett-Bakelman FE et al. *The NASA Twins Study: A multidimensional analysis of a year-long human spaceflight.* Science 364, eaau8650 (2019)](https://www.science.org/doi/10.1126/science.aau8650).

| Item | Detail |
|---|---|
| Mission | Scott Kelly, 340 days on the ISS, March 2015 – March 2016 |
| Control | Twin brother Mark Kelly, on Earth |
| Funded by | NASA Human Research Program |
| Cognition team | Mathias Basner & Ruben Gur, University of Pennsylvania — one of 10 NASA-selected teams ([Penn Today](https://penntoday.upenn.edu/news/how-year-space-affects-brain)) |
| Cognition test | NASA's 10-test Cognition battery, 17 sessions for Scott (3 pre, 6 early flight, 5 late flight, 3 post) |

### Main findings

Scott's thinking held up in space but **got worse after landing and stayed worse for about 6 months**.

| Phase | What happened to Scott's cognition |
|---|---|
| Early flight (months 1–6) | Mostly stable or faster; accuracy dipped in visual memory and abstract reasoning (> 1 SD) |
| Late flight (months 7–12) | Slower emotion recognition (> 1 SD) and less accurate abstract reasoning (> 2 SD) vs early flight |
| After landing | Speed and accuracy dropped across most tests, lasting ~6 months |
| All phases | Took more risks than his twin on the balloon test (BART), most of all in flight |

- **Long missions can cause lasting decline**, and the worst may come after return to gravity.
- **The twin on Earth works as a control**: changes seen in Scott but not Mark point to spaceflight, not age or test practice.
- **It is one person**, so it is a warning sign, not proof; the 25-astronaut ISS study later found no such post-flight decline after ~6-month missions, suggesting mission length matters.

---

## 5. Spacecraft environment data

NASA publishes ISS cabin environment data — **CO₂, temperature, humidity and radiation** — openly through OSDR, with free download. Category: **Space Biology & Physical Sciences → OSDR → environmental monitoring telemetry** ([NTRS 2024](https://ntrs.nasa.gov/citations/20240001562)). Two tools serve it: the **Environmental Data Application (EDA)** for cabin telemetry and radiation, and **RadLab** for radiation from multiple agencies.

### Datasets at a glance

EDA is the best fit for Space Fog: one place, four variables, open CSV download.

| Question | EDA (Environmental Data App) | RadLab | Inspiration4 Dragon cabin |
|---|---|---|---|
| Components | ISS cabin temperature, relative humidity, CO₂ (+ matching ground-control values); daily radiation dose: GCR without SAA, SAA only, total, accumulated | Absorbed radiation dose rate per instrument, with spacecraft, ISS module, time, and orbit position (lat, long, altitude) | Cabin CO₂, O₂, pressure, temperature, humidity; sound levels from Apple Watch |
| Labelled? | By mission, ISS vs ground, and mission milestones (launch, return) | By instrument, spacecraft and module (ISS, LEO, beyond-LEO) | By mission phase; paired with crew data |
| Size | Covers the **Rodent Research (RR) mission** windows only, timestamped readings (date + HH:MM) | Many detectors from several agencies; long time series (years) | 3-day mission |
| Published? | Yes, open tool + [NTRS papers](https://ntrs.nasa.gov/citations/20240008072); summary tables (min, max, mean, SD, median) | Yes, open tool + Data API | Summarized in [Jones et al. 2024, Nature](https://www.nature.com/articles/s41586-024-07648-x) |
| When / where / who | ISS cabin sensors during RR missions; built by NASA OSDR team at Ames Research Center | ISS and other spacecraft; curated from NASA SRAG data with LBNL | Sept 2021, SpaceX Crew Dragon; TRISH / Penn |
| Primary source | [visualization.osdr.nasa.gov/eda](https://visualization.osdr.nasa.gov/eda) | [visualization.osdr.nasa.gov/radlab](https://visualization.osdr.nasa.gov/radlab/gui/data-overview/) | TRISH Commercial Spaceflight Data Repository (controlled) |
| Download | Excel, CSV, PDF from Data Tables tab | CSV, TSV, JSON, HTML + API | By request |

### What is measured

Reference ranges come from the Inspiration4 paper's ISS and Dragon comparison.

| Variable | Unit (check file header) | Resolution | ISS normal range | Dragon (Inspiration4) average |
|---|---|---|---|---|
| CO₂ | mmHg (partial pressure) | Timestamped readings | NASA 1-h limit < 3 mmHg | 0.8 mmHg (0.4–2.0) |
| Temperature | °C | Timestamped readings | 18–25 °C | 25.5 °C (21.8–27.9) |
| Relative humidity | % | Timestamped readings | 25–75% | 29.9% (27.3–52.3) |
| Radiation dose | Absorbed dose (e.g., mGy/day) | Daily (EDA); finer in RadLab | Varies with orbit; spikes in the South Atlantic Anomaly | Not reported |

GCR = galactic cosmic rays (steady background); SAA = South Atlantic Anomaly, a region where the ISS passes through extra radiation several times a day.

### From environment to cognitive risk

The evidence linking cabin conditions to cognition is **mixed**: sleep has the strongest link, CO₂ is debated, radiation is long-term. Weight the risk score accordingly.

| Factor | Risk rule for the app | Evidence strength | What the studies show |
|---|---|---|---|
| Sleep (from crew, not cabin) | High risk at ≤ 6 h | Strong | ISS astronauts sleeping ≤ 6 h showed significant attention (PVT) deficits ([Jones et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8919197)) |
| CO₂ | Flag above NASA's 3 mmHg 1-h limit; treat as moderate | Mixed | Spacecraft CO₂ runs ~10× Earth levels. In 22 astronaut-like subjects, Cognition scores dipped at 1,200 ppm but not at higher levels; NASA's medical office says recent studies show no cognitive loss at current spacecraft levels ([Scully et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584569); [NASA OCHMO-TB-004](https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-004-carbon-dioxide.pdf)) |
| CO₂ → body | Use as a stress signal | Preliminary | In Inspiration4, higher cabin CO₂ went with higher HRV in 3 of 4 crew ([Jones et al. 2024](https://www.nature.com/articles/s41586-024-07648-x)) |
| Radiation | Cumulative dose = long-term risk, not same-day | Mostly animal studies | Track accumulated dose; flag deep-space missions |
| Temperature / humidity | Outside 18–25 °C or 25–75% RH = minor risk | Weak | Comfort factor; affects sleep |

**Closest published model:** Penn researchers used ISS environmental data plus self-reported and PVT data from 24 astronauts to predict attention performance across 6-month missions (Tu et al. 2022, *Scientific Reports*; data controlled, [Penn lab page](https://www.med.upenn.edu/uep/astronaut.html)).

---

## 6. What to measure on astronauts

Six measurement groups, in priority order.

### 6.1 Reaction time and sustained attention — top priority

- **Measure:** median reaction time (ms); number of unusually slow responses (lapses); variability in reaction time; incorrect and premature responses.
- **Why:** an astronaut may be awake and physically healthy but respond too slowly to an alert, miss a critical signal, or lose focus during a repetitive task.
- **How:** a short Psychomotor Vigilance Test (PVT) using a screen and simple visual stimuli. NASA's ISS Reaction Self-Test is designed for repeated monitoring and takes less than five minutes.

### 6.2 Sleep duration, quality and fatigue

- **Measure:** total sleep over 24 h including naps; sleep efficiency (share of time in bed spent asleep); number of awakenings and time awake; time to fall asleep; self-reported fatigue and sleepiness; sleep timing vs the astronaut's normal schedule.
- **Why:** insufficient or disrupted sleep can reduce attention, impair emotional regulation, and increase errors during complex tasks.
- **How:** wrist actigraphy, wearable sleep estimates, sleep logs, and a brief fatigue questionnaire. NASA's Spaceflight Standard Measures program uses actigraphy and subjective sleep assessments.

### 6.3 Cognitive performance and decision-making

- **Measure:** accuracy and completion time; working memory; processing speed; spatial reasoning and problem-solving; decision errors and risk-taking.
- **Why:** space operations require processing information, solving problems, operating equipment and deciding under pressure. NASA research found processing speed, working memory and sustained attention can decline in flight even when overall cognition stays broadly stable.
- **How:** short computerized memory, visual recognition, spatial reasoning and decision-making tasks — the Cognition battery in [section 3](#the-10-cognitive-tests).

### 6.4 Cardiovascular and respiratory indicators

- **Measure:** heart rate and resting heart rate; heart-rate variability (HRV); respiratory rate; blood oxygen saturation (SpO₂); body temperature; heart-rate recovery after exertion.
- **Why:** context about physiological strain, recovery, illness, or possible medical and environmental problems.
- **How:** wearable sensors, pulse oximetry and temperature sensors, depending on available hardware.

### 6.5 Motor coordination, balance and physical capacity

- **Measure:** hand-eye coordination and precision; movement speed and errors; tremor or instability; balance and spatial orientation; muscle force and endurance; motion-sickness symptoms.
- **Why:** an astronaut could score well cognitively but struggle with precise equipment operation, robotic control, or movement during gravity transitions. NASA's human-performance standards name balance, eye-hand coordination, gaze control and spatial orientation as important to mission operations.
- **How:** task-specific coordination tests, wearable inertial measurement units (IMUs), movement tracking, and exercise performance logs.

### 6.6 Stress, mental workload and mood

- **Measure:** self-reported stress and fatigue; perceived mental effort; frustration and time pressure; mood and irritability; team cohesion and communication problems.
- **Why:** excessive workload causes rushing and errors, while too little stimulation leads to boredom and reduced attention.
- **How:** short daily questionnaires, NASA Task Load Index (NASA-TLX), and the Bedford workload scale.

---

## 7. Crew tasks and cognitive load

These scores tell the app which tasks to move first when an astronaut is flagged: the higher the load, the more it matters who does it.

### 7.1 Task categories

| Task category | Cognitive load (1–10) | Primary brain function used | Key external risk/factor |
|---|---|---|---|
| 1 — Extravehicular Activity (EVA) | **9.5** | High-level spatial awareness, stress control, motor execution | Vacuum, thermal extremes, spatial disorientation |
| 2 — Emergency & Systems Repair | **8.5** | Rapid fault-diagnosis, 3D spatial reasoning, critical decision-making | Time pressure, floating loose hardware, habitability threats |
| 3 — Scientific Payload Operations | **7.0** | Procedural precision, attention to detail, active monitoring | Complex protocols, microgravity fluid behavior |
| 4 — Mandatory Daily Exercise | **3.0** | Motor discipline, stress tolerance | Core heat accumulation, physical exertion, monotony |
| 5 — Routine Housekeeping | **2.5** | Basic focus, systematic execution | Dust/debris floating into air intakes |
| 6 — Hygiene, Meals & Sleep | **2.0** | Low cognitive engagement | Circadian disruption (16 sunrises/day), CO₂ buildup, fluid shift |

Scientific payload operations include conducting biological, chemical, physical and human-physiology experiments; operating gloveboxes; processing and logging research samples.

### 7.2 By crew role

Frequency: **D** = daily, **W** = weekly, **O** = occasionally.

#### Commander (CDR)

Load profile: **High to extreme peak demand (7.0–9.5)** · Domains: executive decision-making, crisis management, real-time risk assessment, cross-team delegation.

| Task | Load | Freq. | Key external factors |
|---|---|---|---|
| Off-nominal / emergency command *(depressurization, fire, system abort)* | 9.5 | O | High stress, immediate time-criticality, high noise/alarm environments, risk to human life |
| Manual spacecraft piloting & docking override | 9.0 | O | Microgravity inertia control, low-margin visual alignment, high consequences for structural impact |
| Ground-to-crew tactical operations & comm link | 7.5 | D | 20-minute voice loop saturation, high information density from Mission Control, telemetry discrepancies |
| Crew well-being, morale & task schedule allocation | 7.0 | D | Long-duration isolation stress, monitoring psychological fatigue in crewmates, resolving team friction |

#### Pilot (PLT)

Load profile: **Consistently high / technical (6.5–9.0)** · Domains: continuous spatial tracking, multivariable telemetry evaluation, system monitoring, procedural precision.

| Task | Load | Freq. | Key external factors |
|---|---|---|---|
| Trajectory, attitude thrusters & re-entry management | 9.0 | O | High visual-motor coordination, dynamic orbital mechanics calculations, tight timeline constraints |
| Spacecraft life support (ECLSS) & power systems management | 8.5 | D | Multi-system telemetry monitoring, tracking battery depletion/solar array pointing, subtle fault detection |
| Co-pilot docking & rendezvous navigation | 8.0 | O | Real-time laser/radar rangefinder data, managing fuel margins, spatial relative-velocity tracking |
| Routine flight telemetry & battery maintenance | 6.5 | D | Repetitive system checks; managing automation bias to avoid missing subtle electronic anomalies |

#### Mission Specialist 1 (MS1) — Operations & EVA lead

Load profile: **Bimodal: extreme physical/cognitive peaks to moderate (2.5–9.5)** · Domains: 3D spatial awareness, fine tactile-motor control under pressure, robotic manipulation.

| Task | Load | Freq. | Key external factors |
|---|---|---|---|
| EVA / spacewalk lead | 9.5 | O | Thermal extremes (−150 °C to +120 °C), suit pressurized-resistance fatigue, tether safety, fall risk |
| Space station robotic arm (Canadarm2) capture | 8.5 | O | Dual camera-angle depth perception limits, zero-gravity momentum of multi-ton cargo craft |
| In-flight hardware repairs & external payload install | 8.0 | W | Loose hardware floating, tight spaces, mental 3D rotation of mechanical schematics |
| Intravehicular (IV) spacewalk support (guiding EVA from inside) | 7.0 | O | Continuous step-by-step procedure monitoring, tracking two spacewalkers' oxygen, suit pressure and time |

#### Mission Specialist 2 (MS2) — Science & medical lead

Load profile: **High analytical precision to routine moderate (2.0–8.5)** · Domains: procedural precision, clinical diagnosis, data logging, scientific focus.

| Task | Load | Freq. | Key external factors |
|---|---|---|---|
| In-flight emergency medical management (CMO role) | 8.5 | O | Zero-gravity fluid behavior during treatment, isolated diagnosis without on-site physician support |
| Complex scientific research & glovebox experiments | 7.5 | D | High protocol complexity; unrepeatable samples where small errors invalidate months of research |
| Physiological monitoring & health metrics logging | 5.5 | W | Microgravity physiological shifts (fluid retention, vision changes), coordinating telemetry with ground doctors |
| Medical kit maintenance & sample freezing operations | 4.0 | O | Strict temperature-preservation windows for biological samples, cold-storage management |

#### Shared baseline tasks (all four roles)

| Task | Load | Freq. | Key external factors |
|---|---|---|---|
| Station/spacecraft emergency drills *(depress, fire)* | 8.5 | O | High stress, emergency breathing masks, strict spatial route memorization |
| Mandatory daily physical exercise (2.5 h/day) | 3.0 | D | Core heat buildup from poor sweat evaporation, physical fatigue, fighting microgravity bone loss |
| Housekeeping & air vent intake cleaning | 2.5 | W | No natural air convection, so floating hair/dust accumulates on intake fans |
| Meals, hygiene & sleep readiness | 2.0 | D | Circadian disruption (16 sunrises/sunsets every 24 h), localized CO₂ pooling around sleeping pods |

---

## 8. How it fits together in Space Fog

**A. Environment branch (real, open data)**

1. **Download** EDA Data Tables (CSV) for several Rodent Research missions: CO₂, temperature, humidity, daily radiation.
2. **Forecast** each variable hours to days ahead (ARIMA, Prophet or LSTM), trained on the ISS series; the ground-control series is a ready-made comparison.
3. **Score risk** per time window with the rules in [section 5](#from-environment-to-cognitive-risk), giving sleep the most weight and CO₂ a moderate one.
4. High predicted risk for the whole crew → **"group issue / external factors"** before anyone's test score drops.

**B. Cognitive test branch (NASA baseline)**

1. **Cognitive test box:** run the 3–4 tests that show the biggest in-flight change — **PVT, DSST, F2B** (free versions exist in jsPsych / PsyToolkit). Triggered when predicted risk is high.
2. **Software model:** z = (score − Table 1 mean) / Table 1 SD; speed z is multiplied by −1 so higher = better.
3. **Normal / abnormal:** any key test at **z ≤ −1.5** → abnormal (~11.8% of in-flight and post-flight scores hit this in real astronauts).

**C. Crew decision**

- **One astronaut flagged** → move their high-load tasks ([section 7](#7-crew-tasks-and-cognitive-load)) to a crewmate with normal scores.
- **Most of the crew flagged** → group issue; check cabin factors (Inspiration4 links cabin CO₂ to HRV, a candidate external factor).

---

## 9. Open questions

- Raw per-astronaut cognition data needs an LSDA request, which won't return before the hackathon ends — use **simulated data calibrated to Tables 1–2**.
- EDA covers only the Rodent Research mission windows, not continuous ISS operations.
- CO₂–cognition evidence is mixed; keep its weight moderate.
- Twins Study is n = 1; use it as a case study, not training data.

---

## 10. Sources

**Cognition and crew studies**
- [Dev et al. 2024, Front. Physiol. — Cognitive performance in ISS astronauts](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2024.1451269/full)
- [Garrett-Bakelman et al. 2019, Science — The NASA Twins Study](https://www.science.org/doi/10.1126/science.aau8650)
- [Jones et al. 2024, Nature — Inspiration4 crew](https://www.nature.com/articles/s41586-024-07648-x)
- [Jones et al. 2022, Sleep — ISS sleep and attention](https://pmc.ncbi.nlm.nih.gov/articles/PMC8919197)
- [Scully et al. 2019, npj Microgravity — CO₂ and cognition](https://pmc.ncbi.nlm.nih.gov/articles/PMC6584569)
- [Penn Today — How a year in space affects the brain](https://penntoday.upenn.edu/news/how-year-space-affects-brain)
- [Smithsonian — Twins Study overview](https://www.smithsonianmag.com/science-nature/nasas-twins-study-creates-portrait-human-body-after-year-space-180971945/)
- [Nature Comms 2024 — Twins data availability statement](https://www.nature.com/articles/s41467-024-48920-y)
- [Penn Unit for Experimental Psychiatry — Astronaut behavioral health](https://www.med.upenn.edu/uep/astronaut.html)

**NASA data portals**
- [NASA Life Sciences Portal (NLSP) and LSDA](https://www.nasa.gov/?p=213360)
- [NLSP data request page](https://nlsp.nasa.gov/explore/lsdahome/datarequest)
- [LSDA dataset for Dev et al.](https://nlsp.nasa.gov/view/lsdapub/lsda_experiment/ea3997a6-1093-5e0f-8f54-47684d4f1e73)
- [NASA OSDR — SpaceX Inspiration4 mission](https://osdr.nasa.gov/bio/repo/data/missions/SpaceX%20Inspiration4)
- [OSDR Environmental Data Application (EDA)](https://visualization.osdr.nasa.gov/eda)
- [OSDR tutorial — View and Download Environmental Data](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/environmental_data_application.html)
- [OSDR RadLab portal](https://visualization.osdr.nasa.gov/radlab/gui/data-overview/)
- [OSDR tutorial — RadLab Portal and Data API](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/radlab_portal.html)

**NASA technical reports**
- [NTRS — The Environmental Data Application for Analysis of Space Telemetry Data](https://ntrs.nasa.gov/citations/20240008072)
- [NTRS — NASA OSDR overview (HRP IWS 2024)](https://ntrs.nasa.gov/citations/20240001562)
- [NASA OCHMO-TB-004 — CO₂ technical brief](https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-004-carbon-dioxide.pdf)

**Team docs combined here** (in [`sources/`](sources/))
- NASA Astronaut Cognition Data — Reference Guide
- NASA Twins Study — Data Source & Findings
- NASA Spacecraft Environment Data — Reference
- Measurements to collect (Nizar)
- Tasks of astronauts (by crew role)
- Task categories, scores and external factors
