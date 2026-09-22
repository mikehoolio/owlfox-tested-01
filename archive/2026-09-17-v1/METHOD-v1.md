# EP002 — Test Method (pre-registration)

**Locked 17.9.2026, before final results are computed.** Any change after this date is logged in §7 with the reason, and the on-screen method changes with it.

**Honesty note:** the data researcher's preliminary look (`research/ep002-fourth-turning-2026-09-17/C-data-for-the-test.md` §10) was computed *before* this lock, using provisional Crisis windows. We have therefore seen the rough direction of Tests 2 and 3. To keep that from steering the rules, every choice below is the simplest defensible default (no thresholds tuned to the preview), and the video discloses that the method was fixed after a first look at the data.

Grades: **HOLDS** · **PARTLY** · **DOESN'T HOLD**, using the criteria written for each test below.

---

## 0. Which version of the theory we test

- **Primary text:** Strauss & Howe, *The Fourth Turning* (1997). It is the book the reference video discusses, and it was published before the period whose predictions we check.
- **Turning dates:** the authors' own 1997 table. Where the 1997 book gives no date (e.g. when the current Crisis started), the gap is recorded, and Howe's later dating (*The Fourth Turning Is Here*, 2023) is used and **labelled as a revision** on screen.
- **Crisis windows** = the authors' Crisis turnings, first to last year inclusive. The current Crisis ends 2026 (today) for counting purposes.
- **Geography:** United States (Anglo-American saeculum), as the authors frame it.
- If a date cannot be verified from the authors' text (research file A), it is marked `unverified` and that row is left out of the grade; the omission is shown.

## 1. Test 1 · The Calendar

**Question:** Do Crises really come about every 80 years, on the authors' own dates?

**Method**
1. Take the start year of every Crisis turning in the authors' Anglo-American table.
2. Compute every start-to-start interval, and each saeculum's length.
3. Report the list of intervals, the mean, the minimum and the maximum.

**Grade**
- **HOLDS:** every interval within 80 ± 10 years.
- **PARTLY:** mean within 80 ± 10, but at least one interval outside that band.
- **DOESN'T HOLD:** mean outside 80 ± 10.

**The ±10 band** is chosen because the authors describe the cycle as "the length of a long human life", not an exact number. The exact wording is checked in research file A, and the band is kept either way.

## 2. Test 2 · The Mood

**Question:** Does measured public mood move the way the theory says: trust highest in the High, lower in the Awakening, lower again in the Unraveling, lowest in the Crisis?

**Data** (licences checked in research file C)
- **Primary:** Pew Research Center, "Public Trust in Government: 1958–2025", all readings, as published.
- **Secondary:** GSS "most people can be trusted" (TRUST), 1972–2024, **weighted** using the official GSS weights before publication. Unweighted preview values are not used on screen.
- Gallup is **not** used unless written permission is obtained.

**Method**
1. Assign each reading to a turning by its survey year, using the §0 dates.
2. Compute the mean per turning.
3. Check two things:
   - **(a) Order:** do the turning means fall in the predicted order?
   - **(b) Beyond a straight line:** fit one straight linear trend across all readings. Do the turning means still differ from what that line alone predicts? Concretely, is the mean residual in the High positive and in the Crisis negative?

**Grade**
- **HOLDS:** (a) and (b) both satisfied, in both series.
- **PARTLY:** (a) satisfied but (b) not, or only one series satisfies both.
- **DOESN'T HOLD:** (a) not satisfied.

**Stated on screen regardless of grade**
- The series cover less than one cycle, so they cannot show *repetition*.
- Survey-mode changes affect the Crisis years: Pew moved to online panels in 2020; GSS moved to web/multimode from 2021 (the 1972–2024 cumulative file has no TRUST reading for 2020–2021, and 2022–2024 are multimode).

## 3. Test 3 · The Misses

**Question:** If Crises are special, do independently dated national crises cluster inside Crisis windows more than chance would predict?

**Chronologies**, chosen because they were compiled by others without reference to Strauss & Howe
- **A. Recessions:** NBER Business Cycle Dating Committee contractions, 1854–2020, **all of them** (no length threshold); plus Davis (2006, working-paper table) annual recessions for 1796–1853.
- **B. Banking crises:** Reinhart & Rogoff (2008), Appendix Table A5, US rows, by start year.

**Wars are not used as a test chronology.** The authors drew the Crisis windows around the Revolution, Civil War and WWII, so counting wars would be circular. Wars are shown separately as context, with that caveat said out loud.

**Method**
1. An event is a **hit** if its start year falls inside a Crisis window.
2. **Expected hits by chance** = number of events × share of years (in that chronology's span) covered by Crisis windows.
3. **Ratio** = observed ÷ expected.

**Grade**
- **HOLDS:** ratio ≥ 1.5 in both chronologies.
- **PARTLY:** ratio ≥ 1.5 in one chronology.
- **DOESN'T HOLD:** ratio < 1.5 in both.

**The 1.5 cutoff** means "clearly more than chance". It was set without reference to the preview numbers. With so few events, no significance test is claimed; the video says "about as often as chance" or "noticeably more often", not "statistically significant".

## 4. Test 4 · The Prediction

**Question:** What did the 1997 book predict about the years after its publication, and what happened?

**Method**
1. From research file A, list only predictions stated in the 1997 book with a time reference, quoted (under 15 words each). Page numbers are not required (the editor's decision, 17.9.2026).
2. Leave out predictions too vague to check, and **show how many were left out**. Vagueness is itself part of the result.
3. For each checkable prediction, record what happened, using a neutral dated source.
4. Score each prediction **hit / partial / miss / not yet due**.

**Grade**
- **HOLDS:** majority hits among due predictions.
- **PARTLY:** hits plus partials make a majority.
- **DOESN'T HOLD:** otherwise.

Later statements by Howe (2023) are shown as revisions, never scored as 1997 predictions.

## 5. Context segments (not graded)

- **A rival with data:** Turchin's 2010 *Nature* forecast, quoted exactly ("the next decade is likely to be a period of growing instability in the United States and western Europe"). Both his own 2020 evaluation and the independent 2023 test (Georgescu) are shown.
- **Where you fit:** the authors' generation birth-year ranges and archetypes, plus the critique of generational labels (Pew 2023; Cohen et al. 2021; Duffy 2021). No current politicians or public figures are placed into archetypes.

## 6. Reproducibility

- The calculations live in `production/002-fourth-turning-tested/analysis/`: a script, input CSVs with source URLs, and an output table.
- The video description links the sources.
- Every on-screen number carries its source and year.

## 7. Change log

| Date | Change | Reason |
|---|---|---|
| 17.9.2026 | Method locked | — |
| 17.9.2026 | **Clarification (Test 2), before computing:** a survey in a boundary year (e.g. Oct 1964) belongs to the turning that *starts* that year. The alternative is reported as sensitivity. | Method said "by survey year", but the authors' dates share boundary years. |
| 17.9.2026 | **Clarification (Test 3):** the span for "share of years" is each source's own coverage (recessions 1796–2026; RR2008 A5 1800–2008). Laeven & Valencia's 2007 US crisis is added only as a sensitivity run, not to the primary count. | Method named A5 only; A5 predates 2008, so the span ends there. |
| 17.9.2026 | **Clarification (Test 4), before scoring:** tolerance for "around year X" (hit ±2, partial ±3–5); the counted event is the one the authors themselves later named. | Method gave no tolerance; this avoids choosing events ourselves. |
| 17.9.2026 | **Design flaw found (Test 2), after computing Pew:** GSS starts in 1972, so it has no High-turning readings and can never satisfy criterion (b). HOLDS is therefore unreachable; the effective best grade is PARTLY. The criterion is **not** changed; the flaw is disclosed. | Discovered when checking GSS coverage against §0 dates. |
| 17.9.2026 | **Knife-edge results disclosed:** Test 1 mean 91.0 vs 90 cutoff; Test 3 banking ratio 1.49 vs 1.5. Grades stay as the locked rules give them; the script must say the results are borderline. | Changing a cutoff after seeing a borderline result would be exactly the bias the episode is about. |
| 17.9.2026 | GSS weighted with **WTSSPS** (not WTSSNRPS); "depends" kept in the denominator. | NORC codebook (release 3a): WTSSPS is the recommended weight for analysis across 1972–2024; WTSSNRPS exists only from 2004. |
| 17.9.2026 | Page numbers dropped from the Test 4 quote requirement. | the editor's decision; quotes stay verified against the 1997 text via Open Library search-inside. |
