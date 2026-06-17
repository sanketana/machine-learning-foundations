# Sanketana School of Code — Machine Learning Foundations
## Curriculum Repository Handoff Document (for Claude Code)

**Document purpose:** This is the single source of truth for generating the complete curriculum repository for the ML Foundations course. Claude Code should read this document fully before generating any content, then build the repository following the folder hierarchy, lesson plan template, and generation guidance below.

**Status:** Curriculum outline reviewed and refined (June 2026). Repository generation not yet started.

---

## 1. Course Identity

| Field | Value |
|---|---|
| Course name | Machine Learning Foundations |
| School | Sanketana School of Code (never "Sanketana Academy") |
| Duration | 3 months |
| Format | 24 instructor-led 1:1 online sessions, 60 minutes each |
| Cadence | Twice weekly, with student practice (homework) between consecutive sessions |
| Audience | High school students, **Grade 8/9 and above** (age floor raised from the original "middle & high school" — see §2) |
| Language/stack | Python, pandas, matplotlib, **scikit-learn** (new to students), numpy (light) |
| Positioning | Concept-led, instructor-driven. Students learn how ML algorithms work, when to use them, and how to reason about results — not just how to run code. |

### Eligibility criteria (prerequisite check)
- Intermediate Python: functions, loops, conditionals, lists/dicts, basic OOP awareness
- pandas: loading CSVs, filtering, groupby, basic column operations
- matplotlib (or similar): basic plotting
- Light numpy familiarity is helpful but not required
- **scikit-learn is NOT a prerequisite** — its API is explicitly taught in Session 3

### Brand and pedagogical context
- Sanketana targets sophisticated parents; content must have genuine depth, never shallow or gimmicky.
- Core thesis: students learn how ML algorithms work, when to use them, and how to reason about results — genuine conceptual depth backing every visible project output, never just "how to run the code." (Note: this is a coding/ML course, not the AI Fluency course — do **not** import the AI Fluency "thinking skills" framing such as Mental Modeling, Critical Evaluation, Selective Judgment, or Ethical Reasoning. Lesson plans list concrete learning outcomes only.)
- "Coach not curriculum" identity: the roadmap is fixed, but pacing, examples, and projects adapt to the student. Every lesson plan must include differentiation notes (see template §6).
- Tone of all materials: warm, precise, intellectually respectful of the student. No baby-talk, no hype.

---

## 2. Changes from the Original Outline (Review Decisions)

These decisions were made during curriculum review and are **binding** for generation:

1. **Age floor raised to Grade 8/9+.** Logistic regression, cost functions, and evaluation metrics need algebra comfort. The age floor now matches the prerequisite bar. Math is taught intuition-first and visually (e.g., cost function as "a bowl we slide down"), with notation introduced only after intuition lands. No calculus anywhere in the course.
2. **Data preparation added as a named topic (Sessions 2–3).** Loading data, missing values, encoding categorical columns, feature scaling, train/test split mechanics, and the scikit-learn `fit`/`predict` API are taught explicitly, not absorbed by osmosis.
3. **Regression evaluation metrics added (Session 8).** MAE, RMSE, R² — so regression homework has a success criterion. The original outline only covered classification metrics.
4. **Overfitting relocated.** Vocabulary is *seeded* in Session 1 but the real lesson lives in the decision tree module (Session 16), where students experientially crank tree depth and watch test accuracy fall. Overfitting is a recurring thread: it must be referenced again in random forest, k-means (over-segmentation), and the capstone.
5. **KNN added (Session 9)** as the on-ramp to classification — zero math, fully geometric, builds a working classifier before any sigmoid appears, and makes decision boundaries trivially visualizable.
6. **Capstone block committed (Sessions 22–24).** Dataset selection, full end-to-end workflow, and a Demo Day-style presentation session. The ethics layer lives here and in threaded moments throughout (see §5).
7. **Anchor dataset strategy adopted.** One relatable dataset recurs across modules so students see the same data through regression, classification, and clustering lenses (see §6).

---

## 3. The 24-Session Arc

> Each session is 60 minutes. Every session ends with a homework exercise; every session (from Session 2 onward) opens with ~10 minutes of homework review. This rhythm is mandatory in every lesson plan.

### Module 1 — Foundations & Working with Real Data (Sessions 1–4)

| # | Session title | Core concepts |
|---|---|---|
| 1 | What Is Machine Learning? | ML vs traditional programming; supervised vs unsupervised; features, labels, datasets; *seed* overfitting vocabulary ("memorizing vs learning"). Use case: how Netflix/YouTube recommendations improve from past data. |
| 2 | Working with Real Data I | Loading datasets; exploring with pandas; missing values (detect, drop, fill); why garbage in = garbage out. |
| 3 | Working with Real Data II + Meet scikit-learn | Encoding categorical columns; feature scaling (intuition: "why salary in lakhs shouldn't drown out age"); the `fit`/`predict`/`score` API as an explicit teaching moment; train/test split — why we hide data from the model. |
| 4 | First Model, Full Workflow | Build the simplest possible end-to-end pipeline on a clean dataset. The win: "I trained a model today." Establish the workflow mantra: **data → model → evaluation → insight**. |

### Module 2 — Linear Models: Regression (Sessions 5–8)

| # | Session title | Core concepts |
|---|---|---|
| 5 | Linear Regression: The Idea | Predicting continuous values; the line of best fit, visually; features as "ingredients" of a prediction. Use case: house prices from size, location, rooms. |
| 6 | Error and the Cost Function | What "wrong" means numerically; cost function as a bowl we slide down (visual only, no calculus); model fit. |
| 7 | Multi-Feature Regression in Practice | From one feature to many; interpreting coefficients ("which ingredient matters most?"); building on the anchor dataset. |
| 8 | How Good Is My Model? Regression Metrics | MAE, RMSE, R²; what counts as "good" depends on the problem; comparing models with numbers, not vibes. |

### Module 3 — Classification (Sessions 9–13)

| # | Session title | Core concepts |
|---|---|---|
| 9 | KNN: Your First Classifier | "You're probably similar to your neighbors"; geometric intuition; choosing k; first decision boundary visualization. |
| 10 | Logistic Regression I | Why a straight line fails for yes/no questions; probability-based classification; the S-curve, intuition-first. Use case: spam vs not spam. |
| 11 | Logistic Regression II + Decision Boundaries | Thresholds; moving the threshold and watching predictions change; binary vs multi-class overview. |
| 12 | Evaluating Classifiers | Accuracy and its failure mode (the 99%-accurate fraud model that catches zero fraud); precision, recall; class imbalance. Use case: credit card fraud. |
| 13 | The Confusion Matrix | Reading the four quadrants; precision/recall trade-off as a real decision ("which mistake is worse?"); connecting metrics to consequences — **first major ethics thread moment**. |

### Module 4 — Tree-Based Models (Sessions 14–18)

| # | Session title | Core concepts |
|---|---|---|
| 14 | Decision Trees: Rules a Human Can Read | Rule-based learning; interpretability; building a tree by hand first, then with sklearn. Use case: will a student pass, based on attendance, practice time, test scores. |
| 15 | Growing and Reading Trees | Tree depth; feature importance; visualizing trees; why interpretability matters to real stakeholders. |
| 16 | **Overfitting: The Deep Dive** | The flagship experiential lesson: crank `max_depth`, watch training accuracy hit 100% while test accuracy falls; memorizing vs generalizing; connect back to Session 1's seed. |
| 17 | Random Forest I | Ensemble intuition: "ask 100 slightly different experts and take a vote"; why forests beat single trees. |
| 18 | Random Forest II | Robustness; comparing forest vs tree vs logistic on the same fraud-style problem; choosing a model is a judgment call. Use case: fraud detection via many trees. |

### Module 5 — Unsupervised Learning (Sessions 19–21)

| # | Session title | Core concepts |
|---|---|---|
| 19 | Learning Without Labels | The unsupervised mindset shift; pattern discovery; k-means intuition (centroids as "magnets"). Use case: grouping online shoppers into behavior segments with no predefined categories. |
| 20 | K-Means in Practice | Running k-means; visualizing clusters; interpreting what a cluster *means* (the human's job, not the algorithm's). |
| 21 | Choosing k + Limits of Clustering | The elbow method; over-segmentation as the unsupervised cousin of overfitting; when clustering misleads. |

### Module 6 — Capstone (Sessions 22–24)

| # | Session title | Core concepts |
|---|---|---|
| 22 | Capstone Kickoff: Choose and Frame | Student selects from 4–5 curated capstone datasets (or proposes their own); frames the question; plans the workflow; **Project Ethics Check** (see §5). |
| 23 | Capstone Studio | Full end-to-end execution with coach support: prep → model → evaluate → iterate. Instructor coaches, does not drive. |
| 24 | Demo Day | Student presents: the question, the workflow, the results, what the model gets wrong and about whom, and what they'd do next. Parents may attend. Course retrospective. |

---

## 4. Recurring Threads (must appear across sessions, not just once)

1. **The workflow mantra** — *data → model → evaluation → insight* — introduced Session 4, referenced in every module, structurally embodied in the capstone.
2. **Overfitting** — seeded S1, deep-dive S16, echoed S17–18 (forests as an antidote), S21 (over-segmentation), S24 (capstone reflection).
3. **"Numbers, not vibes"** — every model built after Session 8 must be evaluated with a named metric. Homework rubrics enforce this.
4. **Ethics & consequences** — see §5.
5. **Interpretability vs accuracy** — first raised with trees (S14–15), made concrete in the S18 model comparison.

---

## 5. Ethics Layer

Not a separate lecture — threaded into moments where it has teeth:

- **S12–13:** Which mistake is worse — flagging an honest customer or missing a fraudster? Who bears the cost of each error type?
- **S14–15:** Why a loan officer (or a parent!) might demand an interpretable model over a more accurate black box.
- **S19–21:** What happens when people get put in clusters they didn't choose.
- **S22 (Capstone Kickoff):** A lightweight **Project Ethics Check** — three questions the student must answer in writing before building: (1) Where did this data come from and who is in it? (2) What's the worst thing that happens if my model is wrong? (3) Who could be unfairly affected by my model's mistakes?
- **S24:** "What the model gets wrong and about whom" is a mandatory section of the Demo Day presentation.

---

## 6. Dataset Strategy

**Principles:**
- Early datasets (Sessions 1–8) must require **zero or minimal cleaning** so the algorithm is the star. Messy data appears only after Sessions 2–3 establish prep skills.
- Datasets must be relatable to a 13–17-year-old: student performance, music/Spotify-style data, housing, sports, app usage, simple e-commerce.
- Avoid datasets requiring domain knowledge a teen lacks (medical lab values, financial derivatives).

**Anchor dataset:** Create or curate one synthetic-but-realistic dataset (suggested: a **student habits & outcomes** dataset — study hours, attendance, sleep, screen time, practice frequency, test scores, pass/fail) that recurs:
- Module 2: regress test score (continuous)
- Module 3: classify pass/fail (binary)
- Module 5: cluster students into habit-based segments (unsupervised)

Seeing one dataset through three lenses is itself a core lesson. Claude Code should **generate this dataset as a CSV with a documented generation script** (so it's reproducible and tweakable), ~300–500 rows, with plausible correlations and a little noise.

**Per-module secondary datasets:** one fresh dataset per module for homework variety (housing for regression, spam-style or fraud-style for classification, shopper-segments for clustering). Prefer small (<2,000 rows), clean, CSV format, stored in-repo with a README documenting columns and provenance (generated vs sourced; if sourced, only from open/public-domain sources).

---

## 7. Repository Folder Hierarchy

Claude Code must generate the repository with this exact structure:

```
ml-foundations/
├── README.md                        # Course overview, how to navigate the repo, build status
├── HANDOFF.md                       # This document (copy it in verbatim)
├── curriculum-map.md                # The 24-session arc table + recurring threads (from §3–§4)
├── datasets/
│   ├── README.md                    # Column docs + provenance for every dataset
│   ├── anchor/
│   │   ├── student_habits.csv
│   │   └── generate_student_habits.py
│   └── secondary/
│       ├── housing.csv
│       ├── spam_features.csv
│       ├── fraud_transactions.csv
│       └── shoppers.csv
├── modules/
│   ├── module-1-foundations/
│   │   ├── module-overview.md       # Module goals, sessions list, datasets used, thread checkpoints
│   │   ├── session-01/
│   │   │   ├── lesson-plan.md       # 9-section template (§8)
│   │   │   ├── classwork.ipynb      # In-session guided notebook
│   │   │   ├── homework.ipynb       # Between-session practice notebook
│   │   │   ├── homework-solutions.ipynb
│   │   │   └── explainer.md         # Student-facing concept explainer (§9.3)
│   │   ├── session-02/
│   │   │   └── ... (same five files per session)
│   │   ├── session-03/
│   │   └── session-04/
│   ├── module-2-regression/         # sessions 05–08, same pattern
│   ├── module-3-classification/     # sessions 09–13
│   ├── module-4-trees/              # sessions 14–18
│   ├── module-5-unsupervised/       # sessions 19–21
│   └── module-6-capstone/           # sessions 22–24 (see capstone exceptions below)
├── assessments/
│   ├── README.md                    # Assessment philosophy + rubric conventions
│   ├── prerequisite-check.ipynb     # Pre-enrollment Python/pandas diagnostic
│   ├── module-checkpoints/
│   │   ├── checkpoint-module-1.ipynb    # Short applied check after each module (+ solutions file each)
│   │   ├── checkpoint-module-2.ipynb
│   │   ├── checkpoint-module-3.ipynb
│   │   ├── checkpoint-module-4.ipynb
│   │   └── checkpoint-module-5.ipynb
│   └── capstone/
│       ├── capstone-brief.md        # Student-facing project brief
│       ├── capstone-datasets.md     # 4–5 curated dataset options with framing prompts
│       ├── ethics-check.md          # The 3-question Project Ethics Check template
│       └── capstone-rubric.md       # Demo Day evaluation rubric
├── teacher-resources/
│   ├── teaching-philosophy.md       # Sanketana pedagogy distilled for this course (§1 brand context + §10)
│   ├── differentiation-guide.md     # Fast/struggling student strategies per module
│   ├── common-misconceptions.md     # Per-topic misconception bank with corrective moves
│   └── parent-communication/
│       ├── module-progress-templates.md   # WhatsApp-ready progress notes per module
│       └── course-completion-summary.md
└── student-resources/
    ├── setup-guide.md               # Environment setup (Python, Jupyter, libraries)
    ├── ml-vocabulary.md             # Running glossary, organized by module
    └── cheat-sheets/
        ├── sklearn-api.md
        ├── evaluation-metrics.md
        └── workflow-checklist.md    # The data→model→evaluation→insight checklist
```

**Capstone module exceptions:** sessions 22–24 replace `homework.ipynb` with `capstone-worklog.md` (a student work-tracking template), and session 24 has no classwork notebook — it has `demo-day-runsheet.md` instead.

---

## 8. Lesson Plan Template (9 Sections — Sanketana Standard)

Every `lesson-plan.md` follows this structure (adapted from the Sanketana AI Fluency Lab template for a coding-first course):

1. **Lesson Theme** — One-line session identity + where it sits in the arc (what came before, what comes next, which recurring threads are active).
2. **Key Activity** — The one hands-on thing the student will remember from this session.
3. **Tools & Materials** — Libraries, dataset(s), notebooks, any visual aids. Exact file references into the repo.
4. **Learning Outcomes** — 3–5 concrete, observable outcomes ("Student can explain why we split data before training"). Outcomes only — this is an ML course, not the AI Fluency course, so do **not** add a "thinking skills" subsection.
5. **Class Activities** — A **high-level summary table** with three columns: **Phase | What happens | Purpose**. Each row is one phase of the hour. **Not minute-by-minute timestamps** (too granular for a 1:1 instructor). Keep the mandatory rhythm as the ordered phases: homework review (from Session 2 onward) → concept block with live visual/demo → guided coding in classwork notebook → student-driven stretch → wrap connecting to the workflow mantra and previewing homework.
6. **Differentiation Notes** — "If the student is flying" (stretch path) and "If the student is struggling" (simplification path, what to cut, what is non-negotiable). This is the "coach not curriculum" section — it must be specific, not generic.
7. **Student Templates / Starter Materials** — What's pre-filled in the classwork notebook vs what the student writes; scaffolding level for this session.
8. **Teacher Prep Notes** — What to run/check before class; known failure points (library versions, dataset gotchas); the session's likely misconceptions (cross-reference `common-misconceptions.md`).
9. **Homework** — The exercise, expected time (30–45 min), success criterion (a named metric or concrete artifact — "numbers, not vibes"), and what the homework sets up for next session.

---

## 9. Content Generation Guidance for Claude Code

### 9.1 Build order
Generate in this sequence, completing each phase before the next:
1. **Phase 1 — Skeleton:** Full folder tree, all README/overview files, `curriculum-map.md`, dataset generation scripts + CSVs.
2. **Phase 2 — Module 1 complete** (all 4 sessions, all 5 files each) + prerequisite check. *Stop for human review after Phase 2* — this calibrates voice, difficulty, and scaffolding before scaling to 24 sessions.
3. **Phase 3 — Modules 2–5**, one module at a time, each with its checkpoint assessment.
4. **Phase 4 — Capstone module + teacher resources + student resources.**

### 9.2 Notebook conventions
- **Classwork notebooks:** scaffolded — markdown concept cells, pre-written setup/imports, code cells with `# TODO` gaps the student fills live with the coach. Each notebook ends with a "What we learned" reflection cell and the workflow mantra checkpoint.
- **Homework notebooks:** less scaffolding than classwork; a clear task statement, the dataset pre-loaded, 3–5 exercises ramping in difficulty, final exercise lightly open-ended. Every homework states its success criterion up front.
- **Solutions notebooks:** complete, idiomatic, *commented for the teacher* — including notes on acceptable alternative answers.
- All notebooks must run top-to-bottom with no errors against the in-repo datasets. Use only: python stdlib, numpy, pandas, matplotlib, scikit-learn. No seaborn, no plotly, no internet calls.

### 9.3 Explainers
Student-facing, ~600–900 words each, written for a sharp 14-year-old: one core analogy per concept, one worked visual or numeric example, a "common confusion" callout, and a 3-question self-check at the end. These are revision material between sessions — they must stand alone without the teacher.

### 9.4 Assessments
- **Prerequisite check:** ~30-min notebook covering Python control flow, functions, pandas filtering/groupby, one matplotlib plot. Scoring guide included; defines the enrollment bar.
- **Module checkpoints:** ~30-min applied notebooks (not quizzes) — a fresh small dataset, "do the thing" tasks mirroring module skills, with a teacher scoring rubric (concept understanding / execution / reasoning quality).
- **Capstone rubric:** weight reasoning and communication at least as heavily as model accuracy. A mediocre model excellently reasoned about beats a great model the student can't explain.

### 9.5 Voice & style rules
- Warm, precise, intellectually respectful. No exclamation-mark enthusiasm, no "Wow, ML is magic!" framing — ML is demystified, never mystified.
- Indian-context examples welcome (rupees/lakhs in salary examples, cricket data acceptable as a secondary dataset) but keep globally legible — student base spans US, Singapore, India, Australia, Dubai.
- Math: intuition → visual → notation, in that order, always. No calculus. Notation is optional enrichment, never load-bearing.
- Code style: readable over clever; meaningful variable names; comments explain *why*, not *what*.

### 9.6 Hard constraints (do not violate)
- School name is **Sanketana School of Code** everywhere.
- The 24-session arc in §3 is fixed — do not add, remove, or reorder sessions.
- The 9-section lesson plan template in §8 is fixed.
- Every session has homework; every session from S2 opens with homework review.
- Every post-S8 model must be evaluated with a named metric.
- The ethics moments in §5 are mandatory, placed exactly where specified.

---

## 10. Pedagogical Notes (carried over from curriculum review)

- **Why this order:** geometric/visual ideas before algebraic ones (KNN before logistic regression); experience before terminology (overfitting felt in S16, not defined in S1); evaluation immediately after each model family so students never build without judging.
- **The session rhythm matters more than any single session:** twice-weekly with homework between is where retention happens at this age. Homework review is not optional warm-up — it's spaced retrieval.
- **The anchor dataset is a pedagogical device, not a convenience:** when the student clusters the same students they earlier regressed and classified, the difference between the three learning paradigms becomes visceral.
- **Capstone is the product:** for Sanketana's positioning, Demo Day artifacts (a project a teen can explain end-to-end, including its failure modes) are what sophisticated parents pay for. Generate capstone materials with the same care as core sessions.

---

*End of handoff. Claude Code: begin with Phase 1 (§9.1) and pause for review after Phase 2.*
