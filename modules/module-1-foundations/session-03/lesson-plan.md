# Session 3 — Working with Real Data II + Meet scikit-learn

Module 1 · Session 3 of 24 · 60 minutes

## 1. Lesson Theme

The bridge session. It finishes the data-preparation skills started in Session 2 — turning a text column into numbers (encoding) and putting features on comparable scales — and then introduces **scikit-learn**, the library that builds every model for the rest of the course. The single most important idea today is not any one prep trick: it is the **train/test split**, and *why we hide data from the model*. That question is the direct payoff of Session 1's "memorizing vs learning" seed.

- **What came before:** Session 2 (load, look, detect and handle missing values; "garbage in = garbage out"). The student cleaned `housing.csv`'s missing values and left its text column `neighborhood_type` deliberately untouched.
- **What comes next:** Session 4 — the student drives a full pipeline end-to-end on the clean anchor dataset and earns the "I trained a model" win, where the workflow mantra gets its name. Today the *coach demonstrates* the moves; next session the *student drives* them.
- **Active threads:** *"Numbers, not vibes"* is **previewed** here through `.score()` (it becomes binding after Session 8 — today we read the number without dwelling on what counts as good). *Memorizing vs learning* (the Session 1 seed) is **paid forward**: the train/test split is introduced as the answer to "how do we check whether a model learned or just memorized?" The *workflow mantra* is still only glimpsed; it is named in Session 4.

## 2. Key Activity

The student watches a model score well on the data it trained on, then score on data it has never seen — and connects it back to the Session 1 lookup table that faked a perfect score by memorizing. **The train/test split is the moment to protect:** it turns "memorizing is not learning" from a phrase into a procedure the student will use in every session that follows.

## 3. Tools & Materials

- **Libraries:** pandas, numpy (light), and **scikit-learn for the first time** — `train_test_split`, `StandardScaler` (intuition demo only), and `LinearRegression` (used strictly as a black box). matplotlib not required today.
- **Notebooks:** `modules/module-1-foundations/session-03/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/housing.csv` — continued from Session 2. Today we pick up the parked categorical column `neighborhood_type` (`city_center` / `suburb` / `outskirts`) and predict `price_lakhs`. The missing-value handling from Session 2 is repeated as a quick recap at the top.
- **Visual aid:** the universal scikit-learn API, drawn live and kept on screen all session:

  ```
  model.fit(X, y)        →  learn the pattern from training data
  model.predict(X_new)   →  apply the pattern to new rows
  model.score(X, y)      →  how well did it do?   (one number)
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Encode a categorical column with one-hot encoding (`pd.get_dummies`) and explain why labelling categories `0`/`1`/`2` would invent a false order.
2. Explain, in their own words, why features on wildly different scales can be a problem, and apply a scaler to put them on comparable footing.
3. Use the scikit-learn `fit` / `predict` / `score` API on a model treated as a black box, knowing those three moves are the same for every model in the course.
4. Perform a train/test split and explain *why we hide test data* — connecting a high training score with a low test score back to "memorizing, not learning."

## 5. Class Activities

A high-level map of how to unfold the hour. This is the densest session in Module 1 — protect the train/test split at the end; if time is short, shrink the scaling demo, never the split.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 2's phone-listings homework. End on its untouched text column: "a model can't do arithmetic on the word *iPhone* — so what do we do with it?" | Spaced retrieval; hand directly into today's first topic. |
| Recap: re-clean the data | classwork Part 1: reload `housing.csv` and re-apply the Session 2 median fill in two lines. | Reinforces last session and gives a clean starting point without re-teaching it. |
| Guided coding — encoding | classwork Part 2: show `neighborhood_type`, name the `0`/`1`/`2` trap, then one-hot encode with `pd.get_dummies`. | The first prep skill; kills the "categories are ordered numbers" misconception. |
| Guided coding — scaling (intuition) | classwork Part 3: put `area_sqft` (thousands) next to `bedrooms` (1–5), apply a scaler, eyeball before/after. State plainly: critical for some later models (e.g. KNN), optional for today's — but always a core prep move. | Builds scale intuition without math; sets honest expectations about when it matters. |
| Concept + demo — the sklearn API | classwork Part 4: introduce `fit` / `predict` / `score` as the three universal moves. Fit a black-box `LinearRegression` to predict price. "Watch the moves, not the math — we open this model in Module 2." | The library payoff; the API shape they will reuse 20+ times. |
| Guided coding — train/test split | classwork Part 5: split the data, train on the training set, score on the held-out set. Compare the two scores and connect to Session 1's memorizing lookup table. | Pays off the overfitting seed; teaches *why we hide data*. |
| Student-driven stretch | Before running it, the student predicts whether the training score or the test score will be higher, and says why. | Turns the split rationale into a prediction the student owns. |
| Wrap | Recap the four moves (encode → scale → split → fit/predict/score). Preview Session 4: "next time *you* drive the whole thing, start to finish." Point to the explainer. | Consolidation; set up the Session 4 win. |

## 6. Differentiation Notes

**If the student is flying:**

- After the split, ask them to try a second `random_state` and notice the test score wobbles a little — plant the idea that one split is one sample, not gospel (formalised much later).
- Let them inspect `model.coef_` on the black-box model and guess which feature pushes price up most — but do **not** teach coefficient interpretation (that is Session 7). Curiosity only.
- In the scaling demo, ask why one-hot columns (already 0/1) barely change under scaling.

**If the student is struggling:**

- Cut: the scaling demo down to a single sentence and a look at `.describe()` — do not apply a scaler at all. Scaling is not load-bearing for today's model and can be revisited in Module 3.
- Slow down on: the `X` / `y` split. Many students stumble on "features go in `X`, the label goes in `y`" before any sklearn appears. Make `X` and `y` concrete by printing their shapes.
- **Non-negotiable, never cut:** the `fit`/`predict`/`score` trio and the train-vs-test score comparison. If only one thing survives, it is "a high score on data the model already saw proves nothing — check it on data it hasn't."
- Encoding can be reduced to "run `get_dummies`, look at the new columns" without dwelling on the trap, then revisit the trap verbally.

## 7. Student Templates / Starter Materials

Scaffolded but a clear step down from Session 2 — the student now meets a new library, so the API calls are pre-written to read, with small gaps to complete.

- **Pre-filled:** all imports, the `read_csv` + median-fill recap, the concept markdown, the API diagram, and a working version of every code cell (so the notebook runs top-to-bottom untouched).
- **Student writes:** the `get_dummies` call (a working copy is provided), the `X` / `y` definitions, and every ✏️ markdown answer including the stretch prediction.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. Note once that `X` is conventionally capital (a table of features) and `y` lower-case (one column of labels) — a convention, not a rule.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top-to-bottom (no errors); confirm scikit-learn is installed in the student's environment (`import sklearn` — see `student-resources/setup-guide.md`); have the Session 1 lookup-table example ready to recall by name for the train/test callback.
- **Known gotchas:**
  1. **scikit-learn not installed.** First session it is needed; check before class, not during.
  2. **`get_dummies` returns boolean columns** in recent pandas. The notebook passes `dtype=int` so the new columns read as 0/1 — mention it so the output isn't a surprise.
  3. **Feeding text to a model errors loudly.** If a student forgets to encode and passes `neighborhood_type` straight into `fit`, sklearn raises a `ValueError` about converting a string to float. That error is a *teaching moment*, not a disaster — it is exactly why we encode.
  4. **Scaling and leakage.** We deliberately keep scaling *out* of the model pipeline today to avoid the train/test leakage conversation (fit-the-scaler-on-train-only), which is beyond Module 1. Teach scaling as standalone intuition; do not fold it into the fitted model.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`, populated in Phase 4):
  1. *"Encoding categories as 0/1/2 is fine."* It invents an order and a spacing the data never had. One-hot avoids the lie.
  2. *"A high score means a good model."* The whole point of the split: a high *training* score can just be memorizing. Only the test score is evidence of learning.
  3. *"The model understands what it predicts."* It found a numeric pattern; today's `LinearRegression` is a black box whose insides wait for Module 2.
  4. *"`score` is accuracy."* For a regressor it is R² — name it, don't explain it yet. "Numbers, not vibes" becomes binding in Session 8.
- **Language note:** say "the label" and "features" (from Session 1) alongside the new `X` / `y`; let the synonyms travel together so the student maps the words to the symbols.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 30–45 minutes.
- **The exercise:** a fresh, self-contained dataset of laptop listings (generated in the notebook with a fixed seed, so it is reproducible and has a real price signal), with a categorical `brand` column. Five parts ramping in difficulty — (1) load and identify the one text column; (2) one-hot encode `brand` and confirm no text columns remain; (3) build `X` and `y`, do a train/test split, and run the black-box `fit`/`predict`/`score` trio; (4) predict the price of the first held-out laptop and compare it to the real price; (5) open-ended: explain in writing why we score on held-out data, connecting to "memorizing vs learning," plus one sentence on when scaling would matter.
- **Success criterion (concrete artifact):** all five parts attempted; Exercise 2's encoded table contains no text columns (`select_dtypes(include="object")` is empty); Exercise 3 reports both a training and a test score from `.score()`; Exercise 4 prints a predicted price next to the actual price; Exercise 5's reflection is at least three sentences and uses "memorizing" and "learning" correctly. (Named-metric success criteria begin in Session 8; until then, criteria are concrete artifacts.)
- **What it sets up:** the student has now performed every move of the workflow once, under guidance — encode, split, fit, predict, score. Session 4 removes the scaffolding: the student assembles these moves themselves on the clean anchor dataset, start to finish, and the workflow mantra (**data → model → evaluation → insight**) finally gets its name.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code, commented *for the teacher*, with notes on acceptable alternatives (e.g. `drop_first=True` in `get_dummies`, or a different `random_state`) and the expected ballpark test R² for the seeded dataset. All code runs top-to-bottom with no errors.
