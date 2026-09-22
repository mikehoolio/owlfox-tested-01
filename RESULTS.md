# Results

**Tested 01 — History Repeats Every 80 Years. We Tested It.** · owlfox.studio
Current version: v3, 20 September 2026, a content revision made after the results had been seen. Source of truth: [analysis/results.json](analysis/results.json), produced by [analysis/run_tests.py](analysis/run_tests.py). Method and reasons for the changes: [METHOD.md](METHOD.md). The original grades are kept in `legacy_v2` inside results.json and in [archive/2026-09-17-v1/](archive/2026-09-17-v1/).

## What the video can say

| Check | Current card | Finding and limit |
|---|---|---|
| Strict 80-year schedule | **DOESN'T HOLD — strict 80-year check** | Start-to-start intervals 69–110 years. The mean of 91 includes the 2005 projection. It is above our own 70–90 band; the book's broader claim is not refuted by it. |
| A repeating trust cycle | **INCONCLUSIVE** | Trust falls, but missing turnings, short coverage and an unverified step prediction cannot settle whether it repeats. |
| An economic-crisis cycle | **INCONCLUSIVE** | Recessions do not cluster beyond expectation in this calculation. The Harvard banking figure passes the old numeric cut-off; a broader cycle is not shown. |
| Dated predictions | **PARTLY · 1 scored timing claim** | One partial timing match, two unscored, one still open. Not a validation of reliable forecasting skill. |

**Conclusion:** these checks do not show a reliable date for the next crisis. That does not prove the whole theory wrong, nor that no historical model could ever predict anything.

## 1. The schedule

| Calculation | Intervals / lengths, years | Mean |
|---|---|---:|
| Six historical crisis starts → five intervals | 110, 106, 98, 87, 69 | **94.0** |
| The above + the 1997 projection of 2005 | 110, 106, 98, 87, 69, 76 | **91.0** |
| Sensitivity: last start at Howe's later 2008 | 110, 106, 98, 87, 69, 79 | 91.5 |
| Full saecula, a different measure | 107, 110, 90, 71, 81 | 91.8 |

Historical starts: 1459, 1569, 1675, 1773, 1860, 1929. 2005 is not an observed start in this data but the 1997 forecast. Both 94 and 91 fall inside the book's rough 80–100-year range. That does not make the individual intervals regular, and a mean inside the range does not by itself validate the theory.

Our original 80 ± 10 rule gives DOESN'T HOLD for the calculation that includes the projection. The grade applies **only to this strict claim of our own**. The 91 vs 90 cut-off in the video is not a test that rejects the whole theory.

## 2. Trust

The turning averages of individual Pew poll readings and of yearly weighted GSS percentages are our own calculations. In the main run a boundary year belongs to the turning that starts that year.

| Series / turning | Readings or survey years | Mean % | Difference from the whole-series straight line, points |
|---|---:|---:|---:|
| Pew High | 1 | 73.0 | +18.6 |
| Pew Awakening | 19 | 40.6 | −4.2 |
| Pew Unraveling | 91 | 35.3 | +1.4 |
| Pew Crisis | 52 | 22.7 | −1.3 |
| GSS High | 0 | missing | missing |
| GSS Awakening | 7 | 41.8 | −0.9 |
| GSS Unraveling | 14 | 37.5 | +0.2 |
| GSS Crisis | 9 | 30.5 | +0.4 |

Pew's 73% in 1958 is one poll reading, not one respondent and not the level of the whole turning. The September 2025 reading is 17%.

Pew meets our old order and residual conditions. For the GSS, the four-turning order and the combined High + Crisis comparison are `NOT TESTABLE` because the High is missing. The three observed means fall in order; the High residual sign is missing; **the observed Crisis residual of +0.3748 does not meet the negative-sign condition.** This observed shortfall is not erased because the High is missing.

The theory's required step curve has not been verified. Fitting a straight line does not test for the absence of a cycle, and Pew's 1958 point is not even close to that line. Pew asks about trust in government, the GSS about whether other people can be trusted. Neither series covers 80 years. The conclusion about the theory is therefore **INCONCLUSIVE**.

## 3. Economic crises against the calendar

Each series has its own observation window. Under the old rule both boundary years of each Crisis window count. Equal-years expectation = number of events × share of Crisis-window years. This is not a simulation or a significance test.

| Series | Coverage | Events | Hits in Crisis windows | Crisis years / all years | Expected | Ratio | Own ≥ 1.5 cut-off |
|---|---|---:|---:|---|---:|---:|---|
| Davis + NBER, business-cycle peak years | 1796–2026 | 44 | 7 | 46 / 231 | 8.7619 | 0.7989 | no |
| Same, full years only | 1796–2025 | 44 | 7 | 45 / 230 | 8.6087 | 0.8131 | no |
| Harvard BFFS, derived banking-episode starts | 1800–2014 | 16 | 4 | 34 / 215 | 2.5302 | 1.5809 | **yes** |
| Old A5 selection, **withdrawn from the grade** | 1800–2008 | 15 | 3 | 28 / 209 | 2.0096 | 1.4929 | legacy calculation, not a current grade |

Recession hit years: **1860, 1865, 1929, 1937, 1945, 2007, 2020**. Banking: **1861, 1864, 1929, 2007**.

2026 is a partial year, and NBER sets dates after the fact. The 8.76 kept from the old window is not a final full-year 2026 figure. The sensitivity ending in 2025 does not change the limited recession finding. `peak_year` is not always the year of the first recession month, and the early Davis series and modern NBER do not date turning points with an identical method.

The banking data is Harvard's 2016 file, not a 2026 update. Our own rule derives 16 episodes from unbroken runs of `Banking Crisis = 1` years. 2015–2016 are `n/a` and stay out of the denominator. 1914 is kept. The method is traceable, but it does not resolve how Reinhart & Rogoff's conflicting A3 / A5 / Table 4 lists match each other.

Applying the original numeric combining rule to the new sub-results gives **PARTLY**: recessions do not pass 1.5, banks do. This positive banking finding is said out loud and shown on screen. The **INCONCLUSIVE** label for the broader cycle claim means that calendar clustering alone does not show a cycle mechanism or skill at timing future crises. It does not mean the banking result is rejected.

### Sensitivity runs with the same denominators

| Alternative | Events / hits | Expected | Ratio |
|---|---|---:|---:|
| RR2008 A3, 1800–2007 | 12 / 2 | 1.5577 | 1.2840 |
| Harvard, same 1800–2007 window | 16 / 4 | 2.0769 | 1.9259 |
| Harvard, old 1800–2008 window | 16 / 4 | 2.1435 | 1.8661 |
| Harvard 1800–2014, end boundary to the next turning | 16 / 4 | 2.3814 | 1.6797 |

The old sensitivity run added 2007 and at the same time moved the end year to 2017, so it did not isolate the effect of one row; it is labelled withdrawn legacy. Missing years in the new Harvard series are not filled with zeros. Year-by-year data and the independent sensitivity calculations: [analysis/banking-sensitivity.json](analysis/banking-sensitivity.json).

## 4. Predictions

[Separate scoring and sources](PREDICTIONS.md): one partial timing match (2005 → 2008), the 2020 climax unscored, the 2026 resolution conditional and open, the "great gate" before 2025 too vague to score. Later shifts are revisions, not automatic misses.

Grade **PARTLY**, because the only scorable case is a partial. Required sample note: **1 scored timing claim**. The 2026 HIT window runs to the end of 2028, a possible late PARTIAL to 2031; whether the condition and the event can be assessed has to be settled separately.

## 5. What happened to the old result

The v2 scoreboard was DOESN'T HOLD / PARTLY / DOESN'T HOLD / DOESN'T HOLD. The current scoreboard is DOESN'T HOLD (strictly limited) / INCONCLUSIVE / INCONCLUSIVE / PARTLY (n = 1). The changes come from corrected reasoning and sources. They are not presented as new criteria decided in advance.
