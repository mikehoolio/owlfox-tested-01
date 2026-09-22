#!/usr/bin/env python3
"""EP002 "History Repeats Every 80 Years. We Tested It." — Tests 1–3.

Implements ../TEST-METHOD.md, including the 20.9.2026 post-results revision.
The original calculations are retained explicitly under legacy_v2.
Inputs are the CSVs in this folder; every row carries its source.
Writes results.json and prints a report. No network access is required.
Test 4 (predictions) is scored by hand in ../TEST-4-PREDICTIONS.md.

    python3 run_tests.py
"""
import csv
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).parent
TODAY = 2026


def read(name):
    with open(HERE / name, newline="") as f:
        return list(csv.DictReader(f))


turnings = read("turnings_1997.csv")
for t in turnings:
    t["start"], t["end"] = int(t["start"]), int(t["end"])
crises = [t for t in turnings if t["turning"].startswith("4")]
results = {}

# ---------------------------------------------------------------- Test 1
starts = [c["start"] for c in crises]
intervals = [b - a for a, b in zip(starts, starts[1:])]
mean = sum(intervals) / len(intervals)
in_band = [abs(i - 80) <= 10 for i in intervals]
if all(in_band):
    grade1 = "HOLDS"
elif abs(mean - 80) <= 10:
    grade1 = "PARTLY"
else:
    grade1 = "DOESN'T HOLD"
saecula = {}
for t in turnings:
    s = saecula.setdefault(t["saeculum"], [t["start"], t["end"]])
    s[0], s[1] = min(s[0], t["start"]), max(s[1], t["end"])
complete = {k: v[1] - v[0] for k, v in saecula.items() if k not in ("Late Medieval", "Millennial")}
# Sensitivity: Howe's later start 2008 for the current Crisis
alt = starts[:-1] + [2008]
alt_int = [b - a for a, b in zip(alt, alt[1:])]
# Context: the three US crises the reference video names, plus now
us = [1773, 1860, 1929, 2005]
us_int = [b - a for a, b in zip(us, us[1:])]
results["test1"] = {
    "crisis_starts": starts,
    "intervals": intervals,
    "mean": round(mean, 1),
    "min": min(intervals),
    "max": max(intervals),
    "within_80_pm_10": sum(in_band),
    "grade": grade1,
    "sensitivity_2008_start": {"intervals": alt_int, "mean": round(sum(alt_int) / len(alt_int), 1)},
    "context_us_only_intervals": us_int,
    "context_us_only_mean": round(sum(us_int) / len(us_int), 1),
    "complete_saecula_lengths": complete,
    "complete_saecula_mean": round(sum(complete.values()) / len(complete), 1),
    "authors_stated_range": "roughly eighty to one hundred years (1997)",
}

# ---------------------------------------------------------------- Test 2
pew = read("pew_trust_1958_2025.csv")
modern = [t for t in turnings if t["saeculum"] == "Millennial"]
order = ["1 High", "2 Awakening", "3 Unraveling", "4 Crisis"]


def turning_of(year, boundary):
    """boundary='start': a boundary year belongs to the turning starting that year
    (primary, clarification logged 17.9.2026). boundary='end': to the one ending."""
    for t in modern:
        last = t is modern[-1]
        if boundary == "start" and (t["start"] <= year < t["end"] or (last and year <= t["end"])):
            return t["turning"]
        if boundary == "end" and (t["start"] < year <= t["end"] or (t is modern[0] and year == t["start"])):
            return t["turning"]
    return None


def linfit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def mood(boundary, series="pew", legacy=True):
    if series == "pew":
        pts = [(int(r["year"]) + (int(r["month"]) - 0.5) / 12, int(r["year"]), float(r["individual_poll_pct"])) for r in pew]
    else:
        pts = [(int(r["year"]) + 0.5, int(r["year"]), float(r["most_people_can_be_trusted_pct_weighted_wtssps"]))
               for r in read("gss_trust_1972_2024_weighted.csv")]
    a, b = linfit([p[0] for p in pts], [p[2] for p in pts])
    groups = {k: [] for k in order}
    for x, yr, v in pts:
        k = turning_of(yr, boundary)
        if k:
            groups[k].append((v, v - (a + b * x)))
    out = {}
    for k in order:
        g = groups[k]
        out[k] = {
            "n": len(g),
            "mean_pct": round(sum(v for v, _ in g) / len(g), 1) if g else None,
            "mean_residual_vs_line": round(sum(r for _, r in g) / len(g), 1) if g else None,
        }
        if not legacy:
            out[k]["mean_pct_full_precision"] = sum(v for v, _ in g) / len(g) if g else None
            out[k]["mean_residual_vs_line_full_precision"] = sum(r for _, r in g) / len(g) if g else None
    if not legacy:
        missing = [k for k in order if not groups[k]]
        means = [out[k]["mean_pct_full_precision"] for k in order if groups[k]]
        high_res = out["1 High"]["mean_residual_vs_line_full_precision"]
        crisis_res = out["4 Crisis"]["mean_residual_vs_line_full_precision"]
        high_positive = high_res > 0 if high_res is not None else None
        crisis_negative = crisis_res < 0 if crisis_res is not None else None
        return {
            "by_turning": out,
            "a_order_ok": None if missing else all(x > y for x, y in zip(means, means[1:])),
            "b_beyond_line_ok": None if high_res is None or crisis_res is None else high_positive and crisis_negative,
            "a_order_status": "NOT TESTABLE" if missing else "TESTABLE",
            "b_beyond_line_status": "NOT TESTABLE" if high_res is None or crisis_res is None else "TESTABLE",
            "missing_turnings": missing,
            "observed_components": {
                "high_residual_positive": high_positive,
                "crisis_residual_negative": crisis_negative,
                "order_across_observed_turnings": all(x > y for x, y in zip(means, means[1:])) if len(means) > 1 else None,
            },
            "trend_pct_points_per_decade": round(b * 10, 2),
            "trend_pct_points_per_decade_full_precision": b * 10,
            "linear_fit": {"intercept": a, "slope_per_year": b},
        }
    means = [out[k]["mean_pct"] for k in order if out[k]["mean_pct"] is not None]
    ordered = all(x > y for x, y in zip(means, means[1:])) and len(means) == len(order)
    high_res = out["1 High"]["mean_residual_vs_line"]
    beyond_line = high_res is not None and high_res > 0 and out["4 Crisis"]["mean_residual_vs_line"] < 0
    return {"by_turning": out, "a_order_ok": ordered, "b_beyond_line_ok": beyond_line,
            "trend_pct_points_per_decade": round(b * 10, 2)}


primary = mood("start")
sens = mood("end")
gss = mood("start", "gss")
gss_sens = mood("end", "gss")


def verdict(m):
    return "both (a) and (b)" if m["a_order_ok"] and m["b_beyond_line_ok"] else "(a) only" if m["a_order_ok"] else "neither"


v_pew, v_gss = verdict(primary), verdict(gss)
if v_pew == v_gss == "both (a) and (b)":
    grade2 = "HOLDS"
elif "both (a) and (b)" in (v_pew, v_gss) or v_pew == "(a) only" or v_gss == "(a) only":
    grade2 = "PARTLY"
else:
    grade2 = "DOESN'T HOLD"
# Sub-check (method §2 (a) restricted to the turnings GSS actually covers)
g = gss["by_turning"]
gss_order_where_covered = g["2 Awakening"]["mean_pct"] > g["3 Unraveling"]["mean_pct"] > g["4 Crisis"]["mean_pct"]
results["test2"] = {
    "pew_primary_boundary_start": primary,
    "pew_sensitivity_boundary_end": sens,
    "gss_weighted_primary_boundary_start": gss,
    "gss_weighted_sensitivity_boundary_end": gss_sens,
    "pew_result": v_pew,
    "gss_result": v_gss,
    "gss_order_ok_across_turnings_it_covers": gss_order_where_covered,
    "grade": grade2,
}

# ---------------------------------------------------------------- Test 3
windows = [(c["start"], c["end"]) for c in crises if c["saeculum"] != "Late Medieval"]
windows = [(s, min(e, TODAY)) for s, e in windows]


def inside(year):
    return any(s <= year <= e for s, e in windows)


def share(span_start, span_end):
    years = range(span_start, span_end + 1)
    return sum(1 for y in years if inside(y)) / len(years)


def hitcount(years, span):
    hits = [y for y in years if inside(y)]
    sh = share(*span)
    exp = len(years) * sh
    return {"events": len(years), "hits": len(hits), "hit_years": hits, "span": span,
            "share_of_years_in_crisis": round(sh, 3), "expected_by_chance": round(exp, 2),
            "ratio": round(len(hits) / exp, 2) if exp else None}


rec_years = [int(r["peak_year"]) for r in read("recessions_davis_1796_1853.csv")] + \
            [int(r["peak_year"]) for r in read("recessions_nber_1857_2020.csv")]
bank = read("banking_crises_us.csv")
bank_a5 = [int(r["start_year"]) for r in bank if r["in_rr2008_table_a5"] == "yes"]
bank_all = [int(r["start_year"]) for r in bank]

rec = hitcount(rec_years, (1796, TODAY))
bnk = hitcount(bank_a5, (1800, 2008))
bnk_sens = hitcount(bank_all, (1800, 2017))
passes = [rec["ratio"] >= 1.5, bnk["ratio"] >= 1.5]
grade3 = "HOLDS" if all(passes) else "PARTLY" if any(passes) else "DOESN'T HOLD"
passes_s = [rec["ratio"] >= 1.5, bnk_sens["ratio"] >= 1.5]
grade3_s = "HOLDS" if all(passes_s) else "PARTLY" if any(passes_s) else "DOESN'T HOLD"
results["test3"] = {
    "crisis_windows": windows,
    "recessions_davis_nber": rec,
    "banking_rr2008_a5": bnk,
    "grade": grade3,
    "sensitivity_banking_with_2007_laeven_valencia": bnk_sens,
    "sensitivity_grade": grade3_s,
}

# ------------------------------------------------------ Revision v3, 20.9.2026
# Everything above reproduces v2, including its rounded comparisons and the
# missing-data bug. Preserve it for audit only, then compute corrected outputs.
legacy_v2 = copy.deepcopy(results)
results = {"revision": {
    "version": 3,
    "date": "2026-09-20",
    "status": "post-results revision",
    "reason": "Correct source selection, missing-data handling and claim scope after editorial audit; thresholds unchanged.",
    "original_thresholds_unchanged": True,
    "research_note": "research/tested-01-editorial-corrections-2026-09-20/banking.md",
    "legacy_status": "Audit only: v2 grades are superseded; bank A5 selection withdrawn.",
    "input_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in [
        "turnings_1997.csv", "pew_trust_1958_2025.csv", "gss_trust_1972_2024_weighted.csv",
        "recessions_davis_1796_1853.csv", "recessions_nber_1857_2020.csv",
        "banking_crises_us.csv", "banking_crises_us_harvard_bffs_2016.csv",
    ]},
}}

historical_starts = [c["start"] for c in crises if c["saeculum"] != "Millennial"]
historical_intervals = [b - a for a, b in zip(historical_starts, historical_starts[1:])]
results["test1"] = {
    **legacy_v2["test1"],
    "grade_scope": "Our strict 80 +/- 10 year claim, not the entire book or its broader 80-100 year range.",
    "mean_full_precision": mean,
    "includes_projected_endpoint": 2005,
    "historical_only": {
        "starts": historical_starts, "intervals": historical_intervals,
        "gap_count": len(historical_intervals),
        "mean": round(sum(historical_intervals) / len(historical_intervals), 1),
        "mean_full_precision": sum(historical_intervals) / len(historical_intervals),
    },
    "including_1997_projection": {"gap_count": len(intervals), "mean": round(mean, 1), "mean_full_precision": mean},
    "book_range_80_100": {
        "mean_with_projection_inside": 80 <= mean <= 100,
        "historical_mean_inside": 80 <= sum(historical_intervals) / len(historical_intervals) <= 100,
        "individual_gaps_inside": sum(80 <= i <= 100 for i in intervals),
        "status": "CONTEXT ONLY: distinct claim, not graded by our strict 80 +/- 10 rule.",
    },
    "sensitivity_2008_start": {**legacy_v2["test1"]["sensitivity_2008_start"],
                               "mean_full_precision": sum(alt_int) / len(alt_int)},
    "context_us_only_mean_full_precision": sum(us_int) / len(us_int),
    "complete_saecula_mean_full_precision": sum(complete.values()) / len(complete),
}

primary, sens = mood("start", legacy=False), mood("end", legacy=False)
gss, gss_sens = mood("start", "gss", legacy=False), mood("end", "gss", legacy=False)

def scoped_mood_result(m):
    if m["a_order_ok"] is None or m["b_beyond_line_ok"] is None:
        return "NOT TESTABLE"
    return verdict(m)

results["test2"] = {
    "pew_primary_boundary_start": primary,
    "pew_sensitivity_boundary_end": sens,
    "gss_weighted_primary_boundary_start": gss,
    "gss_weighted_sensitivity_boundary_end": gss_sens,
    "pew_result": scoped_mood_result(primary),
    "gss_result": scoped_mood_result(gss),
    "gss_order_ok_across_turnings_it_covers": gss["observed_components"]["order_across_observed_turnings"],
    "grade": "INCONCLUSIVE",
    "grade_scope": "These trust observations cannot establish a repeating four-season cycle.",
    "legacy_grade": legacy_v2["test2"]["grade"],
    "theory_operationalization_verified": False,
    "operationalization_status": "Our descriptive check; exact monotonic-step prediction not verified in the primary theory source.",
    "limitations": ["Pew has one High observation; GSS has none.",
                    "Missing High is null/NOT TESTABLE, not a failed observation.",
                    "GSS observed Crisis residual is positive: its negative-residual subcondition is separately false.",
                    "A linear fit is descriptive; it does not establish absence of cycles or predictive accuracy."],
}

def hitcount_full(years, span):
    selected = [y for y in years if span[0] <= y <= span[1]]
    hits = [y for y in selected if inside(y)]
    total_years = span[1] - span[0] + 1
    winter_years = sum(inside(y) for y in range(span[0], span[1] + 1))
    sh = winter_years / total_years
    exp = len(selected) * sh
    ratio = len(hits) / exp if exp else None
    return {"events": len(selected), "event_years": selected, "hits": len(hits), "hit_years": hits,
            "span": list(span), "calendar_years": total_years, "winter_years": winter_years,
            "share_of_years_in_crisis": round(sh, 3), "share_of_years_in_crisis_full_precision": sh,
            "expected_by_chance": round(exp, 2), "expected_by_chance_full_precision": exp,
            "baseline": "Expected count under uniform placement across observed calendar years, not a simulated score.",
            "ratio": round(ratio, 2) if ratio is not None else None, "ratio_full_precision": ratio,
            "threshold": 1.5, "threshold_pass": ratio >= 1.5 if ratio is not None else None}

harvard = read("banking_crises_us_harvard_bffs_2016.csv")
coverage = {(int(r["coverage_start"]), int(r["coverage_end"])) for r in harvard}
if len(coverage) != 1:
    raise ValueError("Harvard banking rows must share one observed coverage interval")
bank_span = next(iter(coverage))
harvard_years = [int(r["start_year"]) for r in harvard]
if len(set(harvard_years)) != len(harvard_years) or any(not bank_span[0] <= y <= bank_span[1] for y in harvard_years):
    raise ValueError("Harvard episode starts must be unique and inside observed coverage")
rec_v3 = hitcount_full(rec_years, (1796, TODAY))
bank_v3 = hitcount_full(harvard_years, bank_span)
results["test3"] = {
    "crisis_windows": windows,
    "window_boundary": "Both endpoints included, preserving original Test3 rule; separate right-open sensitivity is in the research note.",
    "recessions_davis_nber": {**rec_v3,
        "event_unit": "Peak calendar year, not first recession month or crisis duration.",
        "narrow_grade": "HOLDS" if rec_v3["threshold_pass"] else "DOESN'T HOLD",
        "scope": "No concentration above our unchanged 1.5 threshold for this selected chronology and simple baseline.",
        "coverage_note": "2026 is an incomplete year as of revision date; dates are retrospective. See complete-year sensitivity."},
    "banking_harvard_bffs2016_episodes": {**bank_v3,
        "status": "PRIMARY DESCRIPTIVE BANKING COUNT; broader claim remains inconclusive",
        "event_unit": "First year of each maximal consecutive run of Banking Crisis=1 in the published annual US indicator.",
        "missing_years_excluded": [2015, 2016],
        "source": {k: harvard[0][k] for k in ["source_url", "source_sha256", "source_sheet", "episode_rule", "retrieved"]},
        "source_csv": "banking_crises_us_harvard_bffs_2016.csv",
        "grade": "INCONCLUSIVE",
        "interpretation": "Clears the numerical bar; chronology sensitivity and limited evidence do not establish a repeating mechanism."},
    "primary_banking_key": "banking_harvard_bffs2016_episodes",
    "banking_rr2008_a5": {**hitcount_full(bank_a5, (1800, 2008)),
        "status": "WITHDRAWN LEGACY: A5 descriptive rows are not a validated complete episode chronology."},
    "grade": "INCONCLUSIVE",
    "grade_scope": "Broad financial-crisis concentration claim; neither all disasters nor validated forecast skill.",
    "legacy_grade": legacy_v2["test3"]["grade"],
    "numeric_threshold_combination_only": "HOLDS" if rec_v3["threshold_pass"] and bank_v3["threshold_pass"] else "PARTLY" if rec_v3["threshold_pass"] or bank_v3["threshold_pass"] else "DOESN'T HOLD",
    "sensitivity_recessions_complete_years": hitcount_full(rec_years, (1796, 2025)),
    "sensitivity_same_1800_2008_span": {
        "recessions": hitcount_full(rec_years, (1800, 2008)),
        "banking_harvard": hitcount_full(harvard_years, (1800, 2008)),
    },
    "sensitivity_same_1800_2014_span": {
        "recessions": hitcount_full(rec_years, bank_span),
        "banking_harvard": hitcount_full(harvard_years, bank_span),
    },
    "sensitivity_banking_with_2007_laeven_valencia": {**hitcount_full(bank_all, (1800, 2017)),
        "status": "WITHDRAWN LEGACY SENSITIVITY: mixes sources and changes horizon together; not a validated series."},
    "sensitivity_grade": "INCONCLUSIVE",
    "legacy_sensitivity_grade": legacy_v2["test3"]["sensitivity_grade"],
}

results["scope_matrix"] = [
    {"test": 1, "status": "DOCUMENTED", "measured": "Authors' historical Crisis start gaps plus one explicitly projected endpoint.",
     "claim_tested": "Our strict 80 +/- 10 year schedule", "not_established": "A verdict on the whole book or its broader 80-100 year range.",
     "sources": ["turnings_1997.csv", "https://penguinrandomhousehighereducation.com/book/?isbn=9780767900461"]},
    {"test": 2, "status": "NOT SHOWN", "measured": "Trust-level averages and linear-trend residuals across available periods.",
     "claim_tested": "Our descriptive trust alignment check", "not_established": "Verified exact stair-step theory prediction or a repeated four-season cycle.",
     "sources": ["pew_trust_1958_2025.csv", "gss_trust_1972_2024_weighted.csv", "https://www.pewresearch.org/politics/2025/12/04/public-trust-in-government-1958-2025/", "https://gss.norc.org/"]},
    {"test": 3, "status": "DOCUMENTED", "measured": "Recession peak years and separately defined banking episode starts compared with calendar exposure.",
     "claim_tested": "Concentration under a simple uniform-year benchmark", "not_established": "All disasters, statistical significance, a cyclic mechanism or out-of-sample predictive skill.",
     "sources": ["https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions", "https://www.nber.org/system/files/working_papers/w11157/w11157.pdf", harvard[0]["source_url"], "https://rogoff.scholars.harvard.edu/resource/2008-version"]},
]
results["legacy_v2"] = legacy_v2

(HERE / "results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
print(json.dumps(results, indent=2, ensure_ascii=False))
