# Method, limitations and correction log

**Tested 01 — History Repeats Every 80 Years. We Tested It.** · owlfox.studio
Current version: v3, 20 September 2026. The original 17 September method is kept unchanged in [archive/2026-09-17-v1/METHOD-v1.md](archive/2026-09-17-v1/METHOD-v1.md). Current results: [RESULTS.md](RESULTS.md). Calculations: [analysis/run_tests.py](analysis/run_tests.py).

This is an openly logged revision made **after the results had been seen**. It is not a pre-registered study.

## 0. What these checks can and cannot say

The episode runs four limited, exploratory checks. The author had seen part of the data before the original rules were written. This work is not described as pre-registered, independent confirmation, or a decisive test of the whole theory.

The original numeric thresholds are unchanged. The revision changes source selection, the handling of missing data, and what each conclusion is about. **INCONCLUSIVE** is added as an editorial evidence label for this episode: the existing calculation cannot settle the broad question being asked. It is not a new numeric pass mark. For each check we keep three things apart: the descriptive result, the grade under our own original rule, and the conclusion about the theory.

| Check | What is measured | Limit of the conclusion |
|---|---|---|
| 1: strict 80 years | Intervals between the book's crisis start years, with the 1997 projection marked separately | Our own 70–90-year band does not refute the book's broader 80–100-year claim. |
| 2: trust | Observed levels of two different survey questions during each turning | No verified four-step prediction, and no repeat of the same cycle in the data. |
| 3: economic crises | Recession peak years and banking-episode starts, relative to the calendar | Not all disasters, not severity, not statistical significance, not forecast accuracy. |
| 4: predictions | Scorable timing matches among the dated claims we checked | A match with an event named after the fact, in one case, does not show reliable forecasting skill. |

Source labels: `DOCUMENTED` = verified from a source or a calculation; `CLAIMED` = a claim by the theory or its authors; `NOT SHOWN` = these checks do not show it. `missing` / JSON `null` is not zero and not a failed observation.

## 1. Chronology and the strict schedule

The chronology comes from the dates in the 1997 book, in `analysis/turnings_1997.csv`. The 2005 and 2026 dates are projections made in 1997. The analysis cut-off for the present is 20 September 2026, not a final observation of the whole of 2026.

The crisis starts 1459, 1569, 1675, 1773, 1860 and 1929 give five historical intervals. The 2005 projection is added as a sixth, clearly marked comparison. The original grading is kept: all intervals within 80 ± 10 → HOLDS; otherwise mean within 80 ± 10 → PARTLY; otherwise DOESN'T HOLD. What it grades is **our own strict 80-year check**. The band is not derived from the book as a statistical acceptance region.

The historical intervals and the calculation including the projection are reported separately. The book's 80–100-year range refers to the whole long cycle; the interval between crisis starts and a full saeculum are not the same measure. Full-saeculum lengths are reported as background. Howe's later 2008 start is a sensitivity run and does not replace the original prediction.

## 2. Trust: description and testability

The Pew series uses individual poll readings 1958–2025. The turning average weights every reading equally, so years with more polls weigh more. It is not an average published by Pew, and not a year-balanced series. The GSS series (1972–2024) uses yearly percentages weighted with WTSSPS; "depends" answers stay in the denominator. Pew asks about trust in the federal government; the GSS asks whether most people can be trusted. They are not independent replications of the same measure.

In the main run a boundary year belongs to the turning that starts that year; the alternative (boundary year belongs to the ending turning) is reported as sensitivity. The mean and residual of a missing turning are `null`. The four-turning order is `NOT TESTABLE` if any turning is missing. Observed components are still reported separately.

The original criteria are kept as diagnostics:

- (a) the order of the four means is High > Awakening > Unraveling > Crisis;
- (b) against one straight OLS line fitted to the whole series, the mean residual is > 0 in the High and < 0 in the Crisis.

Comparisons use full precision, not rounded display values. The straight line is a descriptive comparison, not evidence of a better model or of the absence of a cycle. The GSS has no High readings; its observed Crisis residual is positive, so the negative-residual component is separately false. The two gaps are not explained by one cause.

**Conclusion about the theory: INCONCLUSIVE.** A requirement of falling steps is not a prediction we could verify from the primary passages we checked; the 1997 text also describes trust being rebuilt during a Crisis. Pew passes our diagnostic conditions; the GSS cannot run the full four-turning test. Both series cover less than 80 years. A comparison of turning averages like this can neither confirm nor refute a repeating cycle.

## 3. Economic crises against the calendar

The Crisis windows come from the same 1997 chronology. Both the first and last year are included, as in the original Test 3 rule; this differs from the boundary rule in the trust check, and the results show it. The projected 2005–2026 window does not mean that crisis has been confirmed.

**Recessions:** Davis's annual peaks before 1854 plus NBER's later monthly peaks, grouped by the calendar year of the peak. 44 events. In our data `peak_year` is the year of the business-cycle peak, not necessarily the year of the first month of recession. The on-screen label is `RECESSION PEAK YEARS`. The early industrial-production index and the modern NBER method differ, and the sources say so.

The main comparison, 1796–2026, is kept so the old calculation stays traceable. 2026 is incomplete and dates are set after the fact, so a full-years sensitivity (1796–2025) is also reported. No future year-end is treated as observed. Clustering of recession years does not measure duration or severity.

**Banks:** the old series of 15 episodes counted from description rows in Reinhart & Rogoff (2008) Appendix Table A5 is withdrawn from the grade. A3's 12 starts, A5's 15 descriptions and Table 4's 13 crises do not form one list that the source confirms. 1914 is not dropped arbitrarily. The original CSV and calculation are kept, labelled `WITHDRAWN LEGACY`.

The new descriptive series is derived from the Harvard Behavioral Finance & Financial Stability (BFFS) global crisis file dated 23 September 2016, `Sheet1 / CC3=USA / Banking Crisis`. Coverage is 1800–2014: every year has a 0 or 1. The `n/a` values for 2015–2016 are not zero and are left out of the denominator. Our episode rule: every unbroken run of consecutive 1-years is one episode, starting in its first year. `Systemic Crisis` is a different column and is not mixed in. The 16 derived episodes are in `analysis/banking_crises_us_harvard_bffs_2016.csv`, with the source file hash and row numbers.

**Calculation for both series:** events are limited to the same observation window as the calendar years. Expected = number of events × share of years inside Crisis windows. Ratio = observed hits ÷ expected. This is an expected value under an equal-years assumption, not a simulation, a p-value or a model of how historical events happen. The old **≥ 1.5** cut-off is kept as a diagnostic, computed from unrounded values.

Recessions fall below the cut-off; the Harvard banking series exceeds it. Applying the original combining rule alone would now give **PARTLY**, and that result is reported in RESULTS.md and results.json. The video shows the positive banking result and the broader conclusion separately. **The broad conclusion is INCONCLUSIVE:** source chronologies, event definitions and coverage all move the result, and a single clustering ratio does not show a cycle mechanism. That evidence label does not cancel the positive descriptive banking result. Comparisons over 1800–2008 and 1800–2014, the A3 alternative, boundary-year sensitivity and year-by-year data are in [analysis/banking-sensitivity.json](analysis/banking-sensitivity.json).

## 4. Scoring dated predictions

We check the four timing claims found in our research. We do not claim this is a complete list of the book's predictions. Overlapping 2005 catalyst sentences are counted once. Example scenarios are not treated as predictions that were claimed to come true.

The original rules are kept: claims too vague to check are left unscored; the event used is the one the author later named himself; "around X" gets a HIT within ±2 years and a PARTIAL within ±3–5 years. A clearly late or unfulfilled **checkable** claim can get a MISS. The absence of a vaguely defined event is not inferred from the calendar alone.

Among scorable claims: majority HIT → HOLDS; otherwise majority HIT + PARTIAL → PARTLY; otherwise DOESN'T HOLD. The current single PARTIAL gives PARTLY. No minimum sample is invented after the fact, but **1 scorable timing claim** is stated right next to the grade. It is not a success rate for the whole book and not a validation of forecasting skill.

The 2020 climax and the 2026 resolution are both conditional on a crisis that began on schedule. They are not automatically shifted three years later. The 2026 HIT window stays open until the end of 2028; a PARTIAL could extend to 2031 if the event and the condition can be settled. The "great gate" before 2025 is unscored: a clear date does not make the event criterion unambiguous. Howe's later changes are recorded as revisions, not as proof that the original failed. Scoring and sources: [PREDICTIONS.md](PREDICTIONS.md).

## 5. Context, not extra grades

Turchin measures political violence, not the same whole-society structure as Strauss and Howe. The 2020 Turchin–Korotayev paper uses data through 2018. Georgescu (2023) tests key mechanisms; it is not presented as a refutation of all of Turchin's forecasts.

The generation cards are the authors' classification. Pew's 2023 position is more selective use of generational labels and separating age, period and generation effects, not an end to all generational research. An earlier claim that no academic tests had ever been done was removed.

## 6. Reproducibility

Run `python3 analysis/run_tests.py` (Python 3, standard library only). It writes `analysis/results.json`: the current results, SHA-256 hashes of every input file, and the exact original `legacy_v2` results. Test 4 is a source-based scoring and is not computed by the script.

Every on-screen number carries a source and a period; derived numbers are also labelled `OUR CALCULATION`. The line between original data and our transformation is visible.

## 7. Decision log, 20 September 2026

| Change | Before | Now | Reason |
|---|---|---|---|
| Status of the study | Described as rules fixed before results / "pre-registered" | Exploratory, with the early look and corrections shown | The original log's own admission. |
| Test 1 | FAIL looked like a rejection of the whole book | Same strict FAIL, with the different claims separated; historical and projection-including calculations reported separately | 91 is inside the book's broad range. |
| Test 2 | PARTLY; GSS's missing High counted as false | INCONCLUSIVE; missing components are null, the observed positive Crisis residual reported separately | The link between the measure and the prediction, and the time coverage. |
| Test 3 | A5's 15 rows; 1.49 → FAIL | Old selection withdrawn; Harvard's 16 episodes; 1.58 passes the same cut-off; broad conclusion INCONCLUSIVE | Corrected source coding and traceable yearly data. |
| Test 4 | Great gate MISS; 1 partial / 1 miss → FAIL | Great gate unscored; 1 partial / 0 miss → PARTLY, n = 1 | Consistent use of the original vagueness rule. |
| Rounding | Some comparisons after display rounding | Full precision for decisions, rounding for display | Stops rounding from moving a result across a cut-off. |

The revision raises some earlier negative grades or leaves them open. We do not hide that effect. The original document's log is kept unchanged in the archive.
