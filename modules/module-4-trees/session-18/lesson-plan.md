# Session 18 — Random Forest II

Module 4 · Session 18 of 24 · 60 minutes

## 1. Lesson Theme

We close the module — and cross the halfway point of the course — by doing the thing every previous session has been quietly training the student for: **putting several models on the same problem, with the same yardstick, and choosing one.** Three contenders on the fraud data: a single **decision tree** (readable, from S14–16), a **random forest** (robust, from S17), and **logistic regression** (the linear model from Module 3). One split, one metrics table, precision and recall for each. This is "numbers, not vibes" at its fullest expression so far — a decision made by *measuring*, not by which model sounds most impressive.

And the measurement delivers a genuine surprise, which is the whole point of the session. The fanciest model **does not win.** On this fraud data the humble **logistic regression is best on every metric** — accuracy 0.984, precision 0.923, recall 0.667 — beating the forest (0.978 / 0.786 / 0.611) and the single tree (0.973 / 0.688 / 0.611). Two sessions building forests, and a linear model from Module 3 quietly takes the trophy. That is not an anticlimax; it is the lesson. **You do not get to assume the complex model is better — you have to check.** There is no universal "best" algorithm; the right model depends on the problem, and the only way to know is to run the comparison.

Then we add the second axis that a metrics table alone can't hold: **interpretability.** A single tree reads aloud as if-then rules; logistic regression gives a signed weight per feature (here, *distance from home* is the strongest fraud signal); a forest is a black box that only offers importances. On this problem the interpretable model *also* happens to be the most accurate — a happy alignment — but that won't always be true, and choosing a model means weighing accuracy **and** explainability **and** who is owed an explanation. This is where the module's ethics thread lands: **who is owed an explanation of a model's decision, and does our choice honour that?** The student leaves able to defend a model choice as a real judgement, made with numbers *and* values — exactly the reasoning the capstone will demand.

- **What came before:** the whole module (trees S14–16, forests S17) and Module 3's logistic regression and precision/recall (S10–13). Today they all meet on one table.
- **What comes next:** Module 5 (Unsupervised Learning, S19+) leaves labelled prediction behind for clustering — where "overfitting" returns as over-segmentation (S21). The model-comparison discipline built today is exactly what the **capstone (S22–24)** runs for real.
- **Active threads:** **"Numbers, not vibes"** — *fullest expression*: three models, one table, a decision. **Interpretability vs accuracy** — *made concrete and resolved*: the trade-off named in S14–15, now weighed in an actual choice. **Overfitting** — its antidote (the forest) takes its place in the line-up, and "did we overfit?" is a column to check. **Ethics** — who is owed an explanation. **Workflow mantra** — the complete loop (data → model → evaluation → insight) run **three times** and compared.

## 2. Key Activity

**Run the loop three times, then choose — and be surprised.** Fit a decision tree, a random forest, and a logistic regression on the identical fraud split. Assemble one table: accuracy, precision, recall for each. Discover that **logistic regression wins outright** — the fanciest model loses. Then add the interpretability axis: read the tree's rules, logistic's signed weights, and note the forest's opacity. Finally, the student writes a **model recommendation** for a named stakeholder that cites the numbers, weighs interpretability, and justifies the choice — acknowledging that a *different* problem could flip the answer. The protected takeaway: **"choosing a model is a judgement made by measuring several on the same data with the same metrics — not by assuming the most complex one is best; and the decision weighs accuracy together with interpretability and who is owed an explanation, so the 'best' model is the one that fits the problem and its stakeholders, proven with numbers."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`DecisionTreeClassifier`, `RandomForestClassifier`, `LogisticRegression`, `StandardScaler`, `make_pipeline`, `confusion_matrix`/`ConfusionMatrixDisplay`, `precision_score`, `recall_score`, `accuracy_score`, `train_test_split`).
- **Notebooks:** `modules/module-4-trees/session-18/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/fraud_transactions.csv` — the same imbalanced fraud problem used in S17 and Module 3, so all three models are judged on a problem with real stakes and a yardstick the class owns.
- **Visual aid — the decision table, on the board:**

  ```
   model                 accuracy  precision  recall   interpretability
   ------------------------------------------------------------------------
   decision tree           0.973     0.688    0.611    HIGH  (read as rules)
   random forest (100)     0.978     0.786    0.611    LOW   (black box, votes)
   logistic regression     0.984     0.923    0.667    MED   (signed weight/feature)
                              ^         ^        ^
                          the SIMPLE model wins every metric  -> you had to MEASURE
        interpretability is a SECOND axis the table can't hold — weigh both.
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Run the **same workflow loop** (fit → predict → evaluate) for three different model families on one split, and assemble a single comparison table of accuracy, precision, and recall.
2. Interpret the table to conclude that **the most complex model is not automatically the best**, and that model choice must be *measured*, not assumed.
3. Add **interpretability** as a second axis — read a tree's rules, logistic's signed weights, and name a forest's opacity — and articulate the accuracy-vs-explainability trade-off.
4. Write a **defensible model recommendation** for a named stakeholder that cites specific numbers, weighs interpretability, and names who is owed an explanation.
5. Explain that the "best" model is **problem-dependent** — a different dataset (e.g. with strong non-linear interactions) could favour the forest — so the comparison must be re-run per problem.

## 5. Class Activities

A high-level map of the hour. Protect **the three-model table and the recommendation write-up** — the comparison is the skill, and the recommendation is the assessed synthesis. The "simple model won" surprise is the emotional core; let it land.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Recap S17: forest beat a single tree on precision. Predict aloud: will a forest beat *everything*, including logistic? (Bank the guess.) | Set up the surprise; spaced retrieval. |
| Run the loop ×3 | classwork Step 1–2: fit tree, forest, logistic on one split; predict each. | The workflow mantra, three times, one problem. |
| Build the table | classwork Step 3: assemble accuracy/precision/recall for all three. | One yardstick, side by side. |
| The surprise | classwork Step 4: reveal logistic wins every metric; compare to the earlier guess. | "You had to measure" — the session's core. |
| Add interpretability | classwork Step 5: read the tree's rules, logistic's signed weights, note the forest's opacity. | The second axis a metrics table can't show. |
| Recommend | classwork Step 6 (✏️): write a model recommendation for a named stakeholder, citing numbers, interpretability, and who's owed an explanation. | The assessed synthesis; ethics lands. |
| Wrap | Best = fits the problem and stakeholders, proven with numbers; re-run per problem. Close the module; bridge to unsupervised learning. | Close Module 4 and the course's first half. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them construct (or reason about) a problem where the **forest would win** — e.g. add an interaction feature or a clearly non-linear boundary — and confirm logistic's linear boundary can't capture it. This proves "best is problem-dependent" rather than asserting it.
- Ask them to tune the **decision threshold** (from S13) on the *logistic* model to hit a stated recall target, and note that model choice and threshold choice are two separate dials — you tune both.
- Pose: logistic won on accuracy **and** is fairly interpretable here. When would you *still* prefer the single tree's rules over logistic's weights, even at a small accuracy cost? (When the explanation must be a literal rule a customer can follow.)

**If the student is struggling:**

- Cut: constructing a forest-wins case and threshold tuning. Keep: the three-row table and the one-sentence conclusion "the simplest model won — we only know because we measured."
- Slow down on: reading the table *across* — for each metric, which model is highest? Then the punchline: it's the same model (logistic) every time, and it's not the fanciest.
- **Non-negotiable, never cut:** the student leaves able to (a) compare models on one metrics table and name the winner, and (b) say the best model is chosen by *measuring*, not by assuming complexity wins — and that interpretability is a second thing to weigh.
- All fitting/plotting is provided; the skill is *reading the comparison* and *defending a choice*.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown, the three model fits, the comparison-table builder, the interpretability read-outs (rules, weights), and the board table — the notebook runs untouched.
- **Student writes:** the ✏️ model recommendation for a named stakeholder (the module's assessed synthesis).
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The recommendation is a required written cell — a blank one is an incomplete submission, exactly like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). **The comparison table on `fraud_transactions.csv`** (features amount, hour_of_day, is_online, distance_from_home_km, transactions_last_24h; split `random_state=42` stratified; test n=450, 18 frauds): **Decision tree** (`random_state=0`) acc 0.973 / precision 0.688 / recall 0.611; **Random forest** (100, `random_state=0`) 0.978 / 0.786 / 0.611; **Logistic regression** (StandardScaler + `max_iter=1000`) **0.984 / 0.923 / 0.667** — best on all three. **Logistic signed weights** (scaled): distance_from_home_km **+3.17** (biggest fraud signal), transactions_last_24h +0.97, is_online +0.90, amount +0.83, hour_of_day −0.21. Logistic **must** be scaled (it's in a pipeline); tree and forest don't need scaling.
- **Known gotchas:**
  1. **Scale logistic, not the trees.** Distance-based/linear models need `StandardScaler`; trees are scale-invariant. Use a `make_pipeline(StandardScaler(), LogisticRegression())` so the scaling only touches logistic. If a student scales the tree too, it's harmless but unnecessary — explain why.
  2. **The surprise is the point — don't "fix" it.** A teacher tempted to tune the forest until it wins is missing the lesson. The honest result (simple model wins on this linear-ish signal) is *more* valuable than a rigged forest victory. Say so.
  3. **"Best is problem-dependent" must be stated, or students overgeneralise.** The takeaway is *not* "logistic is always best" — it's "measure, because it depends." Have a one-line example ready: a problem with strong feature interactions would favour the forest.
  4. **Recall is the same for tree and forest (0.611); logistic edges it (0.667).** Don't let students report recall as the forest's win — the forest's edge over the tree was *precision* (S17); logistic beats *both* on everything here.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"The most sophisticated model is the best."* Directly refuted today — the linear model wins. Complexity is a hypothesis to test, not a guarantee.
  2. *"Once you know forests beat trees, you're done."* You compare *against the field*, including simple models, every time.
  3. *"Accuracy alone picks the model."* Interpretability, and who's owed an explanation, are part of the choice.
  4. *"There's one best algorithm."* No free lunch — the winner depends on the data; re-run the comparison per problem.
- **Language note:** ask **"which model wins — and how do you know?"** and insist the answer is *the table*, not a hunch. Name the surprise: **"we spent two sessions on forests and the simple model won — that's why we measure."** Close the ethics thread explicitly: **"who is owed an explanation of this decision, and does our choice honour that?"** Frame the hour as **the workflow loop run three times.**

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions in `homework-solutions.ipynb`).
- **Expected time:** 30–40 minutes (the module's capstone homework — a written recommendation).
- **The exercise:** on `fraud_transactions.csv`, (1) fit all three models (tree, forest, logistic) on one split and build a **comparison table** of accuracy, precision, recall; (2) state **which model wins and how you know**, and note explicitly that the most complex model did *not* win; (3) read out the **interpretability** of each — one tree rule, logistic's top signed weight, and why the forest is opaque; (4) **write a 6–7 sentence model recommendation** to a bank's fraud team: name your chosen model, justify it with **specific numbers** from the table, weigh **interpretability** (who is owed an explanation of a declined transaction?), and acknowledge that a **different problem** could change the answer.
- **Success criterion (concrete artifact + measured decision + ethics):** a three-model comparison table; a correct winner with the "complexity didn't win" observation; the interpretability read-out for each model; and a recommendation that cites specific metrics, weighs explainability with a named stakeholder, and concedes problem-dependence. A recommendation with no numbers, or that ignores interpretability/stakeholders, does not pass — this is the module's flagship deliverable.
- **What it sets up:** this is a dress rehearsal for the **capstone's model-selection and Project Ethics Check (S22)** and Demo Day's "why this model, and what it gets wrong and about whom" (S24). The habit — compare on one yardstick, weigh interpretability, name who's owed an explanation — is the course's central competency, now performed end to end.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: idiomatic code commented *for the teacher*, with the three-model comparison table (tree 0.973/0.688/0.611, forest 0.978/0.786/0.611, logistic **0.984/0.923/0.667**), an explicit statement that **logistic wins every metric and the most complex model did not**, the interpretability read-out (a tree rule read aloud, logistic's top weight — distance_from_home ≈ +3.2 — and the forest's opacity), and a 6–7 sentence recommendation to a fraud team that cites specific numbers, argues the explainability angle (a declined customer is owed a reason, which logistic's weights and a tree's rules can give but a forest cannot), and concedes that a problem with strong non-linear interactions could favour the forest. Acceptable-variation notes: a student may reasonably recommend the **single tree** for its readable rules *if* they acknowledge the accuracy cost and justify it by the explanation requirement — model choice is a defensible judgement, graded on the reasoning, not a single "correct" pick, provided the numbers and the interpretability trade-off are both engaged. It closes the module and the course's first half: choosing a model is judgement, made with numbers and values. All code runs top to bottom with no errors.
