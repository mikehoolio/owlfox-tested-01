# EP002 — Test results v1

Computed 17.9.2026 with `analysis/run_tests.py` (Tests 1–3) and `TEST-4-PREDICTIONS.md` (Test 4), following the locked method in TEST-METHOD.md. Raw output: `analysis/results.json`.

## Scoreboard

| Test | Grade | One-line finding | Borderline? |
|---|---|---|---|
| 1 · The Calendar | **DOESN'T HOLD** | On the authors' own dates, Crises started 110, 106, 98, 87, 69 and 76 years apart; mean 91.0. | **Yes**: mean is 1 year past the ±10 band. |
| 2 · The Mood | **PARTLY** | Trust falls in the predicted order in both series. In the GSS it is a straight line: once the steady decline is removed, the turnings differ by less than 1 point. | Pew's High = a single 1958 survey; GSS has no High. |
| 3 · The Misses | **DOESN'T HOLD** | Recessions start inside Crisis windows at 0.8× chance; banking crises at 1.49× chance. | **Yes**: banking is 0.01 below the 1.5 cutoff. |
| 4 · The Prediction | **DOESN'T HOLD** | Of two checkable dated 1997 predictions: one partial (spark ~2005 → authors chose 2008), one miss ("great gate" before 2025, deadline later moved by Howe). | Only 2 scorable cases. |

## Details

### Test 1 · The Calendar
- **Crisis starts (1997 book):** 1459, 1569, 1675, 1773, 1860, 1929, 2005.
- **Intervals:** 110, 106, 98, 87, 69, 76. Min 69, max 110; 2 of 6 are within 80 ± 10.
- **With Howe's later 2008 start:** last interval 79, mean 91.5. Grade unchanged.
- **Context (not graded):**
  - The reference video's three US Crises plus now give 87, 69, 76 (mean 77.3). The famous "80 years" comes from these, and only the recent stretch is near 80.
  - The authors themselves wrote "roughly eighty to one hundred years".
  - Complete saecula lasted 107, 110, 90, 71 and 81 years (mean 91.8). The theory's own range is closer to its record than the viral "every 80 years".
- **Fair on-screen reading:** "Not every 80 years. The gaps have shrunk from about 110 to about 70, and the popular 80-year figure comes from the most recent stretch."

### Test 2 · The Mood

**Pew, trust in the federal government, 163 readings 1958–2025**

| Turning (1997 dates) | Readings | Mean trust | Above/below straight-line trend |
|---|---:|---:|---:|
| High 1946–64 | 1 | 73.0 % | +18.6 |
| Awakening 1964–84 | 19 | 40.6 % | −4.2 |
| Unraveling 1984–2005 | 91 | 35.3 % | +1.4 |
| Crisis 2005–26 | 52 | 22.7 % | −1.3 |

- **Trend:** −5.7 points per decade. (a) order ✔, (b) High above the line and Crisis below ✔. The boundary sensitivity run gives the same result.
- After the trend is removed, the Unraveling sits *above* the line and the Awakening *below* it, which is not a stepwise decline by turning.
- The High rests on one survey.

**GSS, "most people can be trusted", 30 survey years 1972–2024, weighted with WTSSPS** (NORC's recommended weight for 1972–2024)

| Turning | Survey years | Mean | Above/below straight-line trend |
|---|---:|---:|---:|
| High | 0 | – | – |
| Awakening 1972–83 | 7 | 41.8 % | −0.9 |
| Unraveling 1984–2004 | 14 | 37.5 % | +0.2 |
| Crisis 2005–24 | 9 | 30.5 % | +0.4 |

- **Trend:** −3.3 points per decade.
- **Order within the turnings GSS covers:** ✔ (41.8 > 37.5 > 30.5).
- **Formal (a) and (b):** not satisfied, because there is no High. This is the design flaw logged in the method.
- **Key finding:** every turning sits within 1 point of a straight line. The turnings add nothing beyond a steady decline.
- **Gaps and caveats:** no 2020–2021 readings in the file; mode changed to multimode/web in 2022; "depends" answers are kept in the denominator.

**Grade: PARTLY.** Pew satisfies both criteria and the GSS does not.

**Fair on-screen reading:** "Trust really did fall in the order the theory predicts. But in the longest careful survey it falls in a straight line, with no seasons. And we only have one cycle of data."

### Test 3 · The Misses
- **Recessions** (Davis 1796–1853 + NBER 1857–2020, all 44):
  - 7 start inside Crisis windows: 1860, 1865, 1929, 1937, 1945, 2007, 2020.
  - Crisis windows cover 19.9 % of 1796–2026, so chance predicts 8.8. **Ratio 0.80.**
  - Big recessions outside the windows: 1815, 1836–39, 1873–79, 1882–85, 1893.
- **Banking crises** (Reinhart & Rogoff 2008, Table A5, 15 events 1814–1984):
  - 3 inside: 1861, 1864, 1929.
  - Windows cover 13.4 % of 1800–2008, so chance predicts 2.0. **Ratio 1.49.**
- **Sensitivity:** adding the 2007 crisis from Laeven & Valencia (span to 2017) gives 4 of 16 inside, ratio 1.47. Grade unchanged.
- **Not tested (circular):** wars. The Revolution, Civil War and WWII define the windows. WWI (1917–18) falls outside.
- **Fair on-screen reading:**
  - Recessions: "no more often than chance".
  - Banking crises: "a little more often than chance, but not clearly more; too few cases to say".

### Test 4 · The Prediction
See `TEST-4-PREDICTIONS.md`.

## Before the script: what must still happen

1. ~~GSS weighted run~~ done 17.9.2026 (the editor approved the download). Aggregated yearly values are in `analysis/gss_trust_1972_2024_weighted.csv`; the microdata stays outside the project, in the session scratchpad.
2. Page numbers: **not required** (the editor's decision 17.9.2026). Quotes are cited as *The Fourth Turning* (1997) without page numbers.
3. **Editorial check of the verdict's tone.** Three of four tests fail, two of them on knife-edge margins. The honest verdict is "the calendar and the predictions don't hold; the mood story partly does; the cycle isn't more than chance". It is not "debunked". The video should also credit what the theory gets right: the direction of trust, and the authors' own admission of anomalies.
