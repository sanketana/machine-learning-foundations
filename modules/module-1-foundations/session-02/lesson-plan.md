# Session 2 — Working with Real Data I

Module 1 · Session 2 of 24 · 60 minutes

## 1. Lesson Theme

The first contact with real, imperfect data. Session 1's data was tiny and perfect on purpose; this session pays off its closing promise — "real data is never like this" — by opening an actual 600-row CSV and discovering that some values are simply *missing*. The session teaches the first move of every real project: load the data, look at it, find what's broken, and decide — with a reason — what to do about it.

- **What came before:** Session 1 (ML vs traditional programming; features, label, dataset; "memorizing vs learning"). The student can name the parts of a tabular dataset but has not yet touched a real file.
- **What comes next:** Session 3 finishes data prep — encoding the text column `neighborhood_type` into numbers, why scaling matters, train/test split — and introduces scikit-learn. Today deliberately *stops* at missing values and leaves the categorical column untouched.
- **Active threads:** *Ethics* opens quietly here as **"garbage in = garbage out"** — the data-responsibility thread, felt through a careless fill rather than lectured. The *workflow mantra* is glimpsed in the wrap as the *data* step (named properly in Session 4). *Overfitting* stays dormant. This is also the **first session that opens with homework review** — the mandatory spaced-retrieval rhythm begins now.

## 2. Key Activity

The student opens `housing.csv`, turns the vague feeling "some data is missing" into exact numbers (`.isna().sum()`), then fills the holes two ways — once honestly (median) and once carelessly (fill age with 0) — and *watches the summary statistics distort*. **The careless-fill moment is the one to protect:** it makes "garbage in = garbage out" a thing they saw happen, not a slogan.

## 3. Tools & Materials

- **Libraries:** pandas (the workhorse today), numpy (light, only where pandas surfaces `NaN`). **No scikit-learn yet** — it enters in Session 3.
- **Notebooks:** `modules/module-1-foundations/session-02/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder — point the student to it at the wrap.
- **Datasets:** `datasets/secondary/housing.csv` — 600 listings, prices in lakhs. It carries **24 missing `age_years` values and 15 missing `distance_to_center_km` values** by design (one row is missing both, so `dropna()` removes 38 rows). The categorical `neighborhood_type` column is present but **parked for Session 3** — do not encode it today.
- **Visual aid:** the drop-vs-fill trade-off, drawn live:

  ```
  Drop the rows  →  clean, but 38 listings (and all they knew) are gone
  Fill the holes →  every row kept, but you invented 39 values — choose them honestly
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Load a CSV with pandas and take a structured first look (`.head()`, `.shape`, `.info()`, `.describe()`) — and read the non-null counts to spot trouble.
2. Detect missing values precisely, reporting them as both a count and a percentage per column.
3. Handle missing values two ways — `dropna()` and `fillna()` with the median — and state, in their own words, the cost of each.
4. Decide drop vs fill for a given dataset and justify the choice with a concrete reason.
5. Explain "garbage in = garbage out" using the careless-fill demonstration: a dishonest stand-in becomes a fact the model will believe.

## 5. Class Activities

A high-level map of how to unfold the hour. Adapt pacing to the student; protect the careless-fill moment and the homework-review habit.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 1's homework together. Anchor on Exercise 2 (one table, two questions) and any scenario the student found hard to frame as "predict ___ from ___." | The mandatory spaced-retrieval open. Re-activates last session's vocabulary before new work lands on it. |
| Concept: real data has holes | Set the scene — "last time the data was perfect because I made it perfect." Draw the drop-vs-fill trade-off. Frame today's question: before any model, who finds and fixes what's broken? | Motivates the session and frames cleaning as essential, not menial. |
| Guided coding — load & look | classwork Parts 1–2: load `housing.csv`, then `.head()`, `.shape`, `.info()`, `.describe()`. Read the non-null counts aloud together and notice two columns fall short of 600. | Builds the universal first move; the student *discovers* the missing data rather than being told. |
| Guided coding — detect & handle | classwork Parts 3–4: turn "some are missing" into exact counts and percentages, locate the rows, then drop vs fill with the median. Compare row counts after each. | The core skill. Makes the trade-off concrete: dropping costs 38 listings; filling keeps them but invents values. |
| Guided coding — garbage in, garbage out | classwork Part 5: fill `age_years` with 0 and watch the mean/median move. Name it: a dishonest fill is not "no information," it's wrong information. | The protected moment — the ethics seed lands as something seen, not stated. |
| Student-driven stretch | Ask the student to decide, for *this* dataset, whether they'd drop or fill — and defend it. Stronger students: is filling `distance_to_center_km` with 0 worse than filling `age_years` with 0, and why? | Turns the skill into a judgment they own; previews the homework's written justification. |
| Wrap | Recap: load → look → detect → decide. Locate today on the path: this was the *data* step of data → model → evaluation → insight (named in Session 4). Preview homework; point to `explainer.md`. | Consolidation and the thread checkpoint; sets up Session 3. |

## 6. Differentiation Notes

**If the student is flying:**

- After the median fill, ask them to fill by a smarter group: "would the median age of *city-center* homes be a better stand-in for a missing city-center home than the overall median?" Let them try a `groupby` fill — but don't require it; it's a Session-3-and-beyond idea offered early.
- In the stretch, push on *distance 0*: a home zero km from the center is a strong, false claim — worse than an "average age" guess. Draw out *why some careless fills are more dangerous than others*.
- Mention, without formalizing, that "which rows are missing" can itself be a pattern (are cheaper listings missing age more often?). Plant the idea; don't chase it today.

**If the student is struggling:**

- Cut: the percentage computation (a raw count is enough) and the `groupby` idea entirely. Keep the workflow to `.isna().sum()` → `dropna()` → `fillna(median)`.
- Slow down on: reading `.info()`. The non-null count is the single most useful output today; make sure they can point to the two short columns unaided.
- **Non-negotiable, never cut:** the careless-fill demonstration in Part 5 and the phrase "garbage in = garbage out." If only one idea survives the hour, it's that a dishonest fill quietly corrupts everything downstream.
- The drop-vs-fill choice can be softened to "small dataset → fill; lots of data and few holes → dropping is fine" without deeper nuance.

## 7. Student Templates / Starter Materials

Less scaffolded than Session 1, more than later sessions — the student now writes real pandas, not just prose.

- **Pre-filled:** all imports, the `read_csv` path to `housing.csv`, all concept markdown, and a working version of every code cell (so the notebook runs top-to-bottom untouched).
- **Student writes:** the median-fill lines (a working copy is provided, gaps are additive), every ✏️ markdown answer, and the stretch decision.
- **Convention reminder:** ✏️ still marks the student's cells; gaps never block the run. State once at the top that the path `../../../datasets/secondary/housing.csv` is relative to the notebook's folder — a common first stumble.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top-to-bottom (it must show no errors); confirm the relative path to `housing.csv` resolves in the student's environment (the notebook must be opened from its own folder, not the repo root); skim the student's Session 1 homework so the review is specific, not generic.
- **Known gotchas:**
  1. **The dataset path.** If the student opened Jupyter at the repo root, `../../../datasets/...` will fail. Fix the working directory, don't rewrite the path on the fly.
  2. **`NaN` is a float.** A column with any missing value shows up as `float64` even if every present value is a whole number (`age_years`). Mention it so the dtype doesn't confuse them.
  3. **`fillna` returns a copy.** Re-assign (`homes["col"] = homes["col"].fillna(...)`) or the fill silently does nothing. This is the single most common bug today.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`, populated in Phase 4):
  1. *"A missing value is just a zero."* The Part 5 demonstration exists to kill this — 0 is a specific, usually false claim, not "unknown."
  2. *"Filling is cheating / dropping is always safer."* Both are legitimate; the right choice depends on how much data you have and how much each row is worth.
  3. *"Mean and median are interchangeable."* They're close on this dataset, but median resists extreme values — the habit to build before messier data arrives.
  4. *"Cleaning is the boring bit before the real work."* Reframe: prep decides whether anything built later can be trusted. Garbage in, garbage out.
- **Language note:** say "missing value" consistently; `NaN` is the thing pandas prints, "null"/"NA" are synonyms to introduce only if the student meets them.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 30–45 minutes.
- **The exercise:** five parts on a fresh, small inline dataset (second-hand phone listings) with its own deliberate holes, ramping in difficulty — (1) load and take a structured first look; (2) detect missing values as both a count and a percentage, and name the worst-affected column; (3) handle them two ways — a dropped version and a median-filled version — and verify the filled version has zero missing values; (4) decide drop vs fill *for this tiny dataset* and justify it in writing; (5) open-ended: reproduce a "garbage in = garbage out" mistake by filling battery health with a dishonest 100% and explain who it misleads and how.
- **Success criterion (concrete artifact):** all five parts attempted; Exercise 2 reports missing values correctly as both count and percentage; Exercise 3's filled dataset returns `0` from `.isna().sum()` on every column; Exercise 4's justification is at least three sentences and names a concrete reason tied to the dataset's size; Exercise 5 explains the harm of the dishonest fill in terms of a real person (a buyer). (Named-metric success criteria begin in Session 8; until then, criteria are concrete artifacts.)
- **What it sets up:** the homework's dataset still has a text column left untouched, mirroring how today we parked `neighborhood_type`. That dangling categorical column is the exact hook for Session 3: "we cleaned the numbers — but a model can't read words yet."

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic pandas, commented *for the teacher*, with notes on acceptable alternative answers (e.g., mean-vs-median fills, and why dropping is defensible only when data is plentiful). All code runs top-to-bottom against the inline dataset with no errors.
