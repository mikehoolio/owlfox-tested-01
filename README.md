# Tested 01 — History Repeats Every 80 Years. We Tested It.

Method, source data, calculations and corrections for the first episode of **Tested**, owlfox.studio's series where a big idea about how the world works meets the data.

- YouTube: [owlfox.studio](https://www.youtube.com/@owlfox.studio)
- Theory checked: William Strauss and Neil Howe, *The Fourth Turning* (1997)
- Every figure in the video with its source: [owlfox.studio/sources/tested-01](https://owlfox.studio/sources/tested-01)

## Scoreboard (v3, 20 September 2026)

| Check | Result |
|---|---|
| 1 · Strict 80-year schedule | **DOESN'T HOLD** for our strict 80 ± 10 check (mean interval 91 with the 2005 projection, 94 without). Inside the book's own 80–100-year range. |
| 2 · A repeating trust cycle | **INCONCLUSIVE**. Trust falls, but the data covers less than one cycle and cannot show repetition. |
| 3 · An economic-crisis cycle | **INCONCLUSIVE**. Recession peak years: 0.80× the equal-years expectation. Harvard banking episodes: 1.58×, above our 1.5 cut-off. |
| 4 · Dated predictions | **PARTLY**, from **1 scored timing claim** (a 2005 catalyst; the author later named 2008). |

These are exploratory checks. We had seen some of the data before writing the rules, and we corrected problems after seeing results. Every correction is logged. The evidence does not establish a reliable date for the next crisis, and it does not prove the whole theory wrong.

## Files

| File | What it is |
|---|---|
| [METHOD.md](METHOD.md) | Current method, limitations, the decision log of the 20 September revision and corrections to the video |
| [RESULTS.md](RESULTS.md) | Current results with all tables and sensitivity runs |
| [PREDICTIONS.md](PREDICTIONS.md) | Test 4 scoring sheet and sources |
| [analysis/](analysis/) | Input data (CSV), the calculation script and its output |
| [archive/2026-09-17-v1/](archive/2026-09-17-v1/) | The original 17 September method, results and scoring, unchanged except that a personal name was replaced with "the editor" |

## Reproduce

```bash
cd analysis
python3 run_tests.py
```

Python 3 with the standard library only. The script rewrites `analysis/results.json`: current results for Tests 1–3, SHA-256 hashes of every input file, and the original results under `legacy_v2`. Test 4 is scored by hand from sources, see PREDICTIONS.md. `banking-sensitivity.json` holds the year-by-year banking data and the extra sensitivity runs; it is research output, not the graded result.

Notes like "research A §3" or "research C §8b" in the CSV source columns point to the production's internal research notes, which are not published. Each row also names its public source.

## Data sources

- **Crisis chronology:** Strauss and Howe, *The Fourth Turning* (1997), checked through public Open Library search-inside passages; Neil Howe, *The Fourth Turning Is Here* (2023), for later revisions.
- **Trust in government:** Pew Research Center, *Public Trust in Government: 1958–2025*. Pew Research Center bears no responsibility for the analyses or interpretations of the data presented here.
- **Trust in other people:** General Social Survey 1972–2024 cumulative file, release 3a, NORC at the University of Chicago; variable TRUST, weight WTSSPS. Only yearly weighted percentages are included here, not microdata.
- **Recessions:** NBER Business Cycle Dating Committee; Joseph H. Davis, NBER Working Paper 11157, for 1796–1853.
- **Banking crises:** Harvard Business School Behavioral Finance & Financial Stability, global crisis data (file dated 23 September 2016), with our own episode grouping; Reinhart and Rogoff (2008), NBER Working Paper 14587, for the withdrawn legacy series.

The episode's full source list is in the YouTube description.

## Corrections

If you think a comparison is unfair or a number is wrong, open an issue and tell us which one and why. Corrections are logged in METHOD.md with the date and the reason.

## Licence

Our code, text and derived tables: CC BY 4.0. Third-party data stays under its providers' terms; cite the original sources above.
