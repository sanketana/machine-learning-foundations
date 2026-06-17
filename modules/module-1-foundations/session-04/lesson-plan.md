# Session 4 — First Model, Full Workflow

Module 1 · Session 4 of 24 · 60 minutes

## 1. Lesson Theme

The payoff of Module 1. Sessions 1–3 built the pieces — vocabulary, cleaning, encoding, and the scikit-learn API. Today the student assembles them into one end-to-end run, *driving it themselves*, and earns the milestone: **"I trained a model today."** It is also the session where the course's spine gets its name: the workflow mantra **data → model → evaluation → insight**.

- **What came before:** Session 3 (encoding, scaling intuition, the `fit`/`predict`/`score` API, train/test split) — with the coach driving. The student has run every move once, under guidance.
- **What comes next:** Module 2 opens the black box — how linear regression actually draws its line, the cost function, reading coefficients. Today we use the model; next module we understand it.
- **Active threads:** the **workflow mantra is introduced and named here** — the central thread event of Module 1; the whole session is structured as walking its four steps in order. *Memorizing vs learning* is reinforced (train/test split returns as a habit). *"Numbers, not vibes"* is previewed again through `.score()` (binding from Session 8). *Insight* is the genuinely new move — Session 3 stopped at evaluation; turning numbers into a plain-English takeaway is what makes today a *full* workflow.

## 2. Key Activity

The student runs the complete loop themselves on a clean dataset — data, model, evaluation, and then the new step, **insight**: they predict a made-up student's score, nudge one habit (say, +5 study hours), and watch the prediction move. **The insight step is the one to protect:** it is what separates "I ran some code" from "I learned something about students," and it is the moment the student should be able to name the four-step mantra because they just walked it.

## 3. Tools & Materials

- **Libraries:** pandas, scikit-learn (`train_test_split`, `LinearRegression` — still a black box). No new library surface beyond Session 3.
- **Notebooks:** `modules/module-1-foundations/session-04/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — **introduced here**, 420 students, fully clean (no missing values, no text columns). This is the anchor dataset the student revisits through Modules 2, 3, and 5. Today's task: predict `test_score` from the five habit features. `student_id` is dropped (an identifier — the Session 1 `title` trap), and `passed` is ignored (it is Module 3's target).
- **Visual aid:** the workflow mantra, written once and kept on screen all session — every phase of the lesson is one of its four words:

  ```
  data  →  model  →  evaluation  →  insight
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Recite the workflow mantra — **data → model → evaluation → insight** — and name which step they are on at any point in a notebook.
2. Carry a clean dataset through the full pipeline themselves: load and define `X`/`y`, split, `fit`, and `score` — with only light prompting.
3. Explain why a clean dataset skips the cleaning and encoding of Sessions 2–3, and what made this dataset clean.
4. Produce one **insight**: use the model to predict a scenario, change a single feature, read how the prediction moves, and state a plain-English takeaway — without claiming the model "understands" anything.

## 5. Class Activities

A high-level map of how to unfold the hour. This is the student's first solo-ish run — let them type the moves; resist driving. Protect the insight step at the end.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 3's laptop homework; confirm everyone got the `fit`/`predict`/`score` trio working and read both scores. | Spaced retrieval; make sure the API is solid before the student goes solo. |
| Name the workflow | Put `data → model → evaluation → insight` on screen. "You've already done the first three with me — today you do all four, and you drive." | Give the course's spine its name, attached to things the student has already felt. |
| Meet the anchor dataset | Introduce `student_habits.csv`; flag that this same cohort returns for regression (Module 2), classification (Module 3), and clustering (Module 5). | Frame the anchor as a recurring lens, not a one-off; build investment in it. |
| Guided coding — Data | classwork Step 1: load, look, note it's already clean (contrast with S2–3), define `X` (habits) and `y` (`test_score`), dropping `student_id`. | Step 1 of the mantra, student-led. Reinforces "clean means we skip cleaning." |
| Guided coding — Model | classwork Step 2: train/test split, then `fit` the black box on the training set. | Step 2; reuse Session 3 muscle memory, now hands-on. |
| Guided coding — Evaluation | classwork Step 3: `.score()` on train and test; the two scores are close → it learned, didn't memorize. | Step 3; reinforce the memorizing-vs-learning check. |
| Guided coding — Insight | classwork Step 4: predict a scenario student, nudge one habit (+5 study hours, or −2 screen time), read the change, write one plain takeaway. | Step 4 — the new move. Turns numbers into meaning; the human's job. |
| Student-driven stretch | The student invents their own "what if" (e.g. "what if attendance fell to 60%?") and interprets the result in a sentence. | Ownership; previews Module 2's "which ingredient matters most" intuitively. |
| Wrap | Recap the named mantra and the "I trained a model" win. Preview Module 2: "next, we open the box — how does it draw that line?" | Close Module 1; bridge to regression. |

## 6. Differentiation Notes

**If the student is flying:**

- In the insight step, ask them to find a habit change that *barely* moves the prediction and one that moves it a lot, and to form a hypothesis about why — but do **not** show or explain `model.coef_` (that is Session 7). Keep it experimental, not algebraic.
- Let them try predicting their *own* habits and discuss whether they'd trust the number (and why a model trained on 420 strangers might be wrong about them).
- Ask what "insight" would even mean if the test score were random noise — seeding the idea that a model is only as meaningful as the pattern in the data.

**If the student is struggling:**

- Cut: the stretch "what if." Get them to the end of one clean full loop and one insight sentence — that is the win.
- Slow down on: defining `X` and `y` and the split. If Session 3 felt shaky, do the first two steps together before handing over.
- **Non-negotiable, never cut:** completing all four steps once, and saying the mantra aloud at the wrap. If the student leaves able to name `data → model → evaluation → insight` and say "I trained a model," the session worked.
- The insight step can be softened to a single prediction and one nudge, with the coach supplying the takeaway sentence for the student to confirm.

## 7. Student Templates / Starter Materials

The least scaffolded classwork of Module 1 — by design, this is the student's run.

- **Pre-filled:** imports, the dataset path, all concept and mantra markdown, and a working version of every code cell (so it runs untouched), but with more of the key lines left as ✏️ gaps than in Session 3.
- **Student writes:** the `X`/`y` definitions, the split call, the `fit`/`score` calls, the scenario nudge, and every ✏️ reflection. Working copies are provided so nothing blocks the run, but the intent is that the student types these.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. By now `X`/`y`, features/label, and the three moves should be familiar — let the student lead and only step in when they stall.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top-to-bottom (no errors); confirm `student_habits.csv` loads; have the Session 1 "memorizing vs learning" lookup table ready to recall once more for the train-vs-test moment.
- **Known gotchas:**
  1. **Dropping the right columns.** `student_id` must leave `X` (it's an identifier with no predictive meaning — the `title` trap from Session 1), and `passed` must leave `X` too (it's derived from `test_score`, so leaving it in would let the model "cheat" by reading a near-copy of the answer). Watch for both.
  2. **The two scores can land in either order.** With a random split, the test score is sometimes *higher* than the training score by a hair. The teaching point is that they are **close**, not that train is always higher. A *large* train-over-test gap is the warning sign (Session 16); a small gap either way means the model generalised.
  3. **"Insight" is not coefficient reading.** Keep the insight step experimental (nudge a feature, watch the prediction). Coefficient interpretation is Session 7; reaching for it now will confuse more than it clarifies.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`, populated in Phase 4):
  1. *"A high score means the model understands students."* It found a numeric pattern between habits and scores. No understanding, no causation claimed — nudging a feature shows association the model learned, not a law of nature.
  2. *"Insight = whatever the model predicts."* Insight is the human's interpretation of what the model's behaviour suggests, stated plainly and with appropriate doubt.
  3. *"We're done with cleaning forever."* This dataset was handed to us clean; most aren't. Module 2's homework returns to messy data on purpose.
- **Language note:** use all four mantra words explicitly and often today — say "we're on the *evaluation* step now" — so the names bind to the actions.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 30–45 minutes.
- **The exercise:** a **cumulative Module-1 capstone** on `datasets/secondary/housing.csv` — the *still-messy* dataset from Sessions 2–3 — taken through the entire workflow alone: (1) **data:** load, handle the missing values (S2), one-hot encode `neighborhood_type` (S3); (2) **model:** define `X`/`y` (predict `price_lakhs`), split, and `fit` the black box; (3) **evaluation:** report training and test `.score()`; (4) **insight:** predict a scenario home, nudge one feature (e.g. move it to `city_center`, or add 500 sqft), and write one plain-English takeaway about what drives price. One dataset, every Module 1 skill, student-driven.
- **Success criterion (concrete artifact):** all four steps completed; the encoded data has no text columns and no missing values; a test `.score()` (R²) is reported; and a written insight of at least two sentences names a feature and the direction it pushes price. (Named-metric success criteria begin in Session 8; until then, criteria are concrete artifacts.)
- **What it sets up:** this is the bridge out of Module 1. It rehearses the complete workflow on messy data without scaffolding, which is exactly what the **Module 1 checkpoint** (`assessments/module-checkpoints/checkpoint-module-1.ipynb`) assesses — and it leaves the student asking the question Module 2 answers: "the model drew a line through all this… how, and which features mattered most?"

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code, commented *for the teacher*, walking the same four mantra steps, with the expected ballpark test R² for housing and notes on acceptable alternatives (median vs mean fill, `drop_first` in encoding, different `random_state`, and a range of reasonable insight takeaways). All code runs top-to-bottom with no errors.
