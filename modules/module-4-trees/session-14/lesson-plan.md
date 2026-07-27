# Session 14 — Decision Trees: Rules a Human Can Read

Module 4 · Session 14 of 24 · 60 minutes

## 1. Lesson Theme

Module 3 gave us models that *work* but that a person can't easily read: KNN's decision comes from invisible neighbours, logistic regression's from a weighted sum. Today we meet the first model whose reasoning you can **read aloud like a set of if-then rules**: the **decision tree**. Ask a tree why it predicted "fail" and it answers in plain language — *"because study hours were under 8, and attendance under 80."* That readability is the whole reason trees open this module, and it is the thread — **interpretability** — that the next four sessions build on.

The heart of today is that we build the tree **by hand, on paper, before sklearn touches the data.** A tree learns by asking: *of all the questions I could ask about a student, which single split best separates the passers from the failers?* We make that concrete by taking a dozen students the class already knows, trying a few **thresholds on study hours**, counting how "pure" each resulting group is, and picking the cleanest cut. Only *after* students have found the split with their own hands do we let `DecisionTreeClassifier` loose — and watch it choose **the very same split** (study hours ≈ 7.65). The algorithm stops being magic; it's the counting they just did, done faster.

We also meet, gently, the idea of **impurity** — a number for "how mixed is this group?" A group that's all-fail or all-pass is pure (impurity 0); a 50/50 group is as impure as it gets. The tree's entire strategy is: pick the split that makes the two child groups as pure as possible. Students don't need the Gini formula memorised; they need the *intuition* that a good question sorts a mixed pile into two cleaner piles.

- **What came before:** Module 3 built classifiers we judged on precision/recall (S12–13) but couldn't easily *explain*. Session 9's k=1 KNN scoring 100% on its own training data is the seed we'll cash in at S16.
- **What comes next:** Session 15 grows the tree deeper and reads **feature importance** off it (which habit mattered most). Session 16 is the **overfitting deep-dive** — where growing the tree too deep is shown to backfire. Today plants both: a shallow tree that's readable, and the first hint (one misclassified student) that a tree can be pushed to memorise.
- **Active threads:** **Interpretability** — *introduced here as the module's spine*: a tree is a model you can read. **"Numbers, not vibes"** — the split is chosen by counting purity, not by hunch. **Overfitting** — parked, but previewed: the one student our clean split gets wrong hints that chasing zero errors means memorising. **Workflow mantra** — data → model → evaluation → insight, now with a model you can narrate.

## 2. Key Activity

**Grow the root split by hand, then let sklearn confirm it.** On paper, take the 12-student sample. Sort them by study hours. Try three candidate cuts — study < 5, study < 8, study < 12 — and for each, split the students into two groups and **count pass/fail in each**. Fill in a small table of "how pure is each side." Discover that **study < 8** gives the cleanest split (left side: 5 students, all fail; right side: 7 students, 6 pass). Then run `DecisionTreeClassifier(max_depth=1)` on the full dataset and see it pick **study hours ≤ 7.65** as the root — essentially the same line the class drew by hand. The protected takeaway: **"a decision tree learns by repeatedly asking the one yes/no question that best separates the classes — and because it's just questions, you can read the finished model aloud as human rules."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`DecisionTreeClassifier`, `export_text`, `plot_tree`, `train_test_split`, `accuracy_score`).
- **Notebooks:** `modules/module-4-trees/session-14/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — the students the class has known since Module 1. We predict `passed` from **habit features** (study hours, attendance, sleep, screen time, practice) — deliberately **not** from `test_score`, which is essentially where the pass/fail label comes from (see Teacher Prep). Homework reuses the same data with a fresh by-hand split.
- **Visual aid — the root split, on the board all hour:**

  ```
                    12 students: 6 passed, 6 failed   (a totally mixed pile — impurity high)
                                   │
                    ask:  study_hours < 8 ?
                        ┌──────────┴───────────┐
                     YES (5 students)       NO (7 students)
                     0 passed / 5 failed    6 passed / 1 failed
                     PURE → predict FAIL    MOSTLY PASS → predict PASS
                                             └─ the 1 exception: studied a lot, still failed
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain a **decision tree** as a stack of yes/no questions, and read a fitted shallow tree aloud as **human-readable if-then rules**.
2. Perform the **root split by hand**: given a small dataset, try candidate thresholds on a feature, count pass/fail on each side, and pick the split that makes the two groups **purest**.
3. Explain **impurity** in plain words — a mixed group is impure, an all-one-class group is pure — and that a tree chooses the split that most reduces it.
4. Fit a `DecisionTreeClassifier` in sklearn, extract its rules with `export_text`/`plot_tree`, and confirm the root split matches the one found by hand.
5. Articulate **why interpretability matters** — that a model you can read aloud can be explained to, and challenged by, the person it affects — and spot the single misclassified student as an early hint that a perfect fit would mean memorising.

## 5. Class Activities

A high-level map of the hour. Protect the **by-hand root split** — it is the lesson. sklearn confirming the hand-drawn cut is the payoff; do not let the API come first.

| Phase | What happens | Purpose |
|---|---|---|
| Hook | Ask a KNN or logistic model from Module 3 "why did you predict fail?" — it can't really say. Pose today's question: can a model *explain itself*? | Motivate interpretability as a real, missing property. |
| Split by hand | classwork Step 1–2: load the 12-student sample; sort by study hours; try cuts at <5, <8, <12; count pass/fail each side; fill the purity table. | The core skill — a tree split is counting, done by a human first. |
| Name impurity | classwork Step 3: introduce "purity" for each group (all-one-class = pure); see that study<8 gives the purest pair; meet Gini as a number for it (intuition only). | Give the counting a name and a number, without formula-drilling. |
| Let sklearn confirm | classwork Step 4: fit `max_depth=1` on the **full** data; print the rule; see root = study ≤ 7.65 — the same cut. | The reveal: the algorithm is the counting they just did. |
| Read the tree aloud | classwork Step 5: grow to `max_depth=2`, `export_text` + `plot_tree`; each student reads one path as an if-then sentence. | Interpretability made literal: the model *is* rules. |
| Spot the exception | classwork Step 6 (✏️): find the student our clean split gets wrong; write one sentence on why a tree that got *everyone* right might be memorising. | Seed S16's overfitting deep-dive honestly. |
| Wrap | Trees are readable models; the split is chosen by purity, not vibes. Bridge to S15: grow it deeper and ask which habit mattered most. | Close; set up feature importance. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them compute the **weighted Gini** for the study<8 split by hand (parent 0.5 → weighted child 0.143) and confirm it against a second candidate feature's split — feeling that "best split = biggest impurity drop."
- Ask them to hand-build the **second level** under the "study ≥ 8" node: what single question best separates the lone failer from the six passers? Compare to sklearn's `max_depth=2` tree.
- Pose the interpretability stakes: *a bank must, by law, tell a customer why a loan was refused.* Which Module 3 model could it use, and which couldn't? Why does a tree win here even if it's slightly less accurate? (Seeds S18.)

**If the student is struggling:**

- Cut: Gini as a number and the second level. Keep only: try two thresholds on study hours, count pass/fail on each side, pick the cleaner one.
- Slow down on: the **counting**. Physically sort the paper cards by study hours; draw the line; put failers on the left pile, passers on the right; *see* which line makes the cleanest two piles.
- **Non-negotiable, never cut:** the student leaves able to (a) split a small dataset by hand and say which cut separates the classes best, and (b) read one path of a fitted tree aloud as an if-then rule. Interpretability — "a tree is a model you can read" — is the headline.
- `plot_tree` draws the diagram for them; the skill is *reading* it, not producing the picture.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, the 12-student sample as a small DataFrame, all markdown and the board diagram, the purity-counting helper, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the pass/fail counts for each candidate cut, the chosen best split, the read-aloud rule for one tree path, and the ✏️ sentence on the misclassified student and memorising.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The "why a perfect tree might be memorising" cell is a required written reflection — a blank one is incomplete, like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the by-hand numbers on the **12-student sample** (ids S169, S303, S221, S343, S352, S024, S347, S312, S172, S062, S257, S237): parent is 6 pass / 6 fail (Gini 0.5). **study < 8** → left 0 pass / 5 fail (pure), right 6 pass / 1 fail; weighted Gini **0.143** — the best of the candidates (study<5 → 0.250, study<12 → 0.333). On the **full** data, `DecisionTreeClassifier(max_depth=1, random_state=0)` roots at **study_hours_per_week ≤ 7.65** (train acc 0.881, test acc 0.865). The lone exception in the sample is **S172** (9.1 study hours, still failed).
- **Known gotchas:**
  1. **Exclude `test_score` as a feature.** It correlates 0.83 with `passed` — it's essentially the label in disguise (this is *leakage*; the full lesson is later). If a student adds it, the tree trivially roots on it and learns nothing about habits. Predict from the five habit features only, and say why.
  2. **`random_state` matters.** Ties between equally-good splits are broken pseudo-randomly; fix `random_state=0` so everyone's root matches the notes. The notebook sets it everywhere.
  3. **The by-hand threshold won't be exactly 7.65.** Students pick a round number (8); sklearn picks 7.65 by scanning midpoints between sorted values. "Nearly the same line" is the point — don't chase exactness by hand.
  4. **Gini is intuition today, not a target.** Teach "how mixed is this pile?" Do not drill the formula; S15 doesn't need it either. The number just confirms the counting.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"The tree tries every possible tree."* No — it greedily picks the single best split now, then repeats on each child. Local, one question at a time.
  2. *"A split has to be perfectly pure."* Rarely is. study<8's right side still has one failer; the tree accepts an imperfect but *best-available* split.
  3. *"More questions (deeper) is always better."* The seed for S16 — a student who wants to fix the one exception by adding rules is beginning to memorise. Name it, park it.
  4. *"Trees only work on numbers like study hours."* They handle thresholds on any numeric feature and categories too; today is numeric for clarity.
- **Language note:** say **"the tree asks a question"** and **"how pure is this pile?"** all hour. Insist students **read a path aloud** ("if study < 8 then predict fail") before trusting the model — that sentence *is* the interpretability skill. Attach "on these students" to every count.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** on a fresh 12-student sample from `student_habits.csv`, (1) **by hand**, try two threshold cuts on **attendance** (attendance < 75 and attendance < 85), count pass/fail on each side, and say which cut is purer; (2) fit a `max_depth=1` tree on the full data and report its root split and test accuracy; (3) fit a `max_depth=2` tree, print its rules with `export_text`, and **write two paths aloud** as if-then sentences; (4) **write 3–4 sentences** answering: which single habit does the tree split on first, and why would a school counsellor prefer this tree over a more accurate model they *couldn't* read?
- **Success criterion (concrete artifact + interpretation):** the two by-hand attendance counts with the purer cut named; the fitted root split and its accuracy; two tree paths written as plain-language rules; and a short interpretability argument naming a real stakeholder. Rules copied without being rewritten in plain language, or an argument with no named stakeholder, does not pass.
- **What it sets up:** doing a split by hand on a *different* feature cements that any feature can be the question, and sets up **S15's feature importance** (which habit the tree leans on most) and **S16's overfitting** (what happens when we stop stopping at depth 1–2).

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the by-hand attendance counts (both cuts, purity compared and the purer one named), the fitted `max_depth=1` root split on the habit features and its test accuracy (~0.865), a `max_depth=2` tree with two paths written aloud as if-then rules, and a 3–4 sentence interpretability argument. The solution notes that the tree roots on **study hours** even though the homework had students split on attendance by hand — a deliberate mismatch that previews S15's feature-importance lesson (the tree tells you which feature it actually found most useful). Acceptable-variation notes cover slightly different by-hand thresholds and any well-argued stakeholder (counsellor, parent, admissions officer). All code runs top to bottom with no errors.
