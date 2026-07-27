# Session 15 — Growing and Reading Trees

Module 4 · Session 15 of 24 · 60 minutes

## 1. Lesson Theme

Yesterday we built a tree's **root split** by hand and let sklearn confirm it. Today we do two things with that tree: we **grow it** — turn the `max_depth` knob and watch new questions appear — and we **read what it learned back to us**. The headline idea is **feature importance**: after fitting, the tree can tell you *which habit it leaned on most*. On our students it comes back loud and clear — **study hours** carries about **0.88** of the importance, while screen time is essentially **0.00**. The tree didn't just predict; it *ranked what mattered*, and it did so in numbers we can inspect and challenge.

This is interpretability deepening from "I can read the rules" to "I can see what the model thinks is important." That's a genuinely useful thing to hand a non-technical stakeholder: not a black-box score, but a sentence like *"the model's decision is driven almost entirely by weekly study hours; attendance and screen time barely move it."* A counsellor can act on that. A parent can argue with it. That's the power — and, as we'll flag, the responsibility: an importance ranking can also encode bias, so reading it critically matters.

We also meet the `max_depth` **knob** properly. Depth 1 is a single question; depth 2 adds a follow-up; depth 3 adds another layer. As we grow, **training accuracy creeps up** (0.881 → 0.912 → 0.922) while **test accuracy barely moves** (0.865 → 0.865 → 0.881). We name that gap today but don't yet dramatise it — that is deliberately **Session 16's** job. Today the knob is a tool for *reading* trees at a sensible depth; tomorrow it becomes the instrument of the overfitting deep-dive.

- **What came before:** Session 14 (the root split by hand; a tree is readable if-then rules; the one misclassified student as a hint). Today grows that tree and reads its priorities.
- **What comes next:** Session 16 — the **overfitting deep-dive** — cranks `max_depth` to the extreme and watches test accuracy *fall*. Today's gentle train-vs-test gap is the on-ramp.
- **Active threads:** **Interpretability** — *deepened*: from readable rules to a numeric ranking of what the model uses. **"Numbers, not vibes"** — importance is a measured quantity, not a guess about what "should" matter. **Overfitting** — the train-vs-test gap is named and parked one session before its deep-dive. **Ethics** — a first, light touch: an importance ranking can surface (or hide) a feature you'd be uncomfortable relying on; reading it is a responsibility.

## 2. Key Activity

**Grow the knob, then ask the tree what mattered.** Fit trees at `max_depth` 1, 2, 3 and print train and test accuracy for each — watch training accuracy climb while test accuracy stalls. Then take the depth-3 tree, print `feature_importances_`, and rank the five habits. Discover that **study hours ≈ 0.88** dominates and **screen time ≈ 0.00** is ignored. Draw the tree with `plot_tree` and confirm by eye: study hours is at the top and reappears; screen time never gets asked. The protected takeaway: **"a fitted tree reports feature importance — a numeric ranking of which inputs it actually used — turning the model into a readable statement about what drives the prediction; and growing the tree deeper raises training accuracy faster than test accuracy, a gap we'll confront next session."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`DecisionTreeClassifier`, `feature_importances_`, `plot_tree`, `export_text`, `train_test_split`).
- **Notebooks:** `modules/module-4-trees/session-15/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — same students, same five habit features, same `passed` label (still excluding `test_score`). Continuity lets us compare directly against yesterday's root split.
- **Visual aid — the importance bar chart, on the board:**

  ```
   feature importance (depth-3 tree), tallest = most used:

   study_hours       ██████████████████████████████████  0.88
   practice_sessions ██                                   0.06
   sleep_hours       █                                    0.04
   attendance        █                                    0.02
   screen_time                                            0.00   <- never even asked
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Use `max_depth` as a **knob**: fit trees at increasing depth and describe how each added level adds follow-up questions.
2. Read **feature importance** off a fitted tree (`feature_importances_`), rank the inputs, and state in plain language which feature the model relies on and which it ignores.
3. Confirm the importance ranking against the tree diagram (`plot_tree`) — the most important feature sits at the top and recurs; ignored features never appear.
4. Observe that growing depth raises **training** accuracy faster than **test** accuracy, and name that widening gap (without yet explaining it — that's Session 16).
5. Explain **why an importance ranking is useful and must be read critically** — it tells a stakeholder what drives a decision, and it can also reveal reliance on a feature you'd be uneasy about.

## 5. Class Activities

A high-level map of the hour. Protect **reading feature importance and tying it to the tree diagram** — that is the lesson. Keep the train-vs-test gap *named but not dramatised*; S16 owns the drama.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through S14's by-hand attendance split and the surprise that the tree rooted on *study hours* (~10 min). | Spaced retrieval; motivate "which feature does the tree actually use?" |
| Turn the knob | classwork Step 1–2: fit `max_depth` 1, 2, 3; tabulate train & test accuracy; see training climb, test stall. | Introduce depth as a knob; name the gap. |
| Ask what mattered | classwork Step 3: print `feature_importances_` for the depth-3 tree; rank the five habits; bar-chart them. | The headline skill: the tree ranks its own inputs. |
| Cross-check the picture | classwork Step 4: `plot_tree`; verify study hours sits on top and screen time is absent. | Importance number ↔ tree picture, made consistent. |
| Say it to a human | classwork Step 5 (✏️): write one sentence a counsellor could use — what drives the prediction, what barely matters. | Interpretability as communication. |
| Read it critically | classwork Step 6 (✏️): name one feature you'd be *uncomfortable* letting a model rely on for a high-stakes decision, and why. | Light ethics touch; sets up S18 and the capstone. |
| Wrap | A tree reports what it used; deeper trees fit training better but not always test. Bridge to S16: push the knob to the extreme. | Close; hand off the gap to the deep-dive. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them compute importance at depth 2 vs depth 5 and notice it **shifts** (at depth 2 study hours is ~0.96; deeper, minor features pick up small shares). Ask: why does a shallower tree concentrate importance more?
- Ask them to predict, *before* running it, whether adding an obviously useless random column would show ~0 importance — then add an `np.random` noise feature and confirm the tree mostly ignores it (great S16 foreshadowing about noise).
- Pose: "importance says the model *used* study hours most. Does that prove studying *causes* passing?" Seed the correlation-vs-causation caution (returns in the capstone).

**If the student is struggling:**

- Cut: the depth-sweep table and critical-reading extension. Keep: fit one depth-3 tree, print importances, name the biggest and the smallest.
- Slow down on: matching the **number** to the **picture** — point at study hours on top of `plot_tree` and at its 0.88 bar; point at screen time's empty bar and its absence from the diagram.
- **Non-negotiable, never cut:** the student leaves able to (a) read `feature_importances_` and name which feature the tree relies on most, and (b) say why that ranking is something you could show a non-technical stakeholder.
- The bar chart and `plot_tree` are provided; the skill is *interpreting* them, not producing them.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown, the depth-sweep loop, the importance bar-chart cell, and `plot_tree` — the notebook runs untouched.
- **Student writes:** the plain-language "what drives the prediction" sentence, and the ✏️ reflection on a feature they'd be uncomfortable relying on.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. Both written cells are required — a blank reflection is incomplete, like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Key numbers on `student_habits.csv` (habit features, `random_state=0`, split `random_state=42` stratified): **depth 1** train 0.881 / test 0.865; **depth 2** 0.881 / 0.865; **depth 3** 0.912 / 0.865; **depth 4** 0.922 / 0.881. **Depth-3 feature importance:** study_hours **0.876**, practice_sessions 0.062, sleep_hours 0.037, attendance 0.025, screen_time **0.000**. (At depth 2, study_hours is ~0.96 — importance concentrates in shallow trees.)
- **Known gotchas:**
  1. **Importance depends on depth (and seed).** It's not a fixed property of the data — it's what *this* tree used. Report the depth alongside the ranking. Don't call it "the importance of study hours" full stop; call it "how much this tree used study hours."
  2. **Zero importance ≠ useless feature.** Screen time scoring 0.00 means *this tree never needed it*, often because a correlated feature (study hours) already did the job — not that screen time is unrelated to passing. Say so; it prevents a real misconception.
  3. **Don't dramatise the train-vs-test gap yet.** Name it ("training is pulling ahead"), then explicitly say "we confront this next session." S16 needs the reveal fresh.
  4. **Importance ≠ causation.** High importance means the model *leans on* the feature, not that the feature *causes* the outcome. Keep the language careful.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"Feature importance is a fact about the world."* It's a fact about *this fitted model* — change depth or seed and it shifts.
  2. *"A feature with 0 importance is irrelevant."* It may just be redundant with a feature the tree already used.
  3. *"Deeper is smarter."* Deeper fits *training* better; test barely improved and will soon get *worse* (S16).
  4. *"The most important feature causes the label."* Importance is about use, not cause.
- **Language note:** say **"what did the tree lean on?"** and always attach a **depth** to an importance ranking. Frame importance as *something you could show a stakeholder* — that's the interpretability payoff. Introduce the ethics touch gently: "would you be comfortable if this top feature were, say, someone's postcode?"

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** on `student_habits.csv`, (1) fit trees at `max_depth` 1, 2, 3, 4 and make a small **train-vs-test accuracy table**; describe in one sentence what happens to each column as depth grows; (2) for the depth-3 tree, print `feature_importances_`, rank all five habits, and **bar-chart** them; (3) identify the feature the tree relies on **most** and one it **ignores**, and explain in 1–2 sentences why an ignored feature isn't necessarily unrelated to passing; (4) **write a 3–4 sentence note to a school counsellor** stating what drives the model's prediction and what barely matters, in plain language, and naming one feature you would be *uncomfortable* letting such a model rely on (and why).
- **Success criterion (concrete artifact + interpretation + ethics):** the depth-sweep table with a correct description of the trend; a ranked importance chart; a correct statement of most-used vs ignored plus the redundancy caveat; and a plain-language stakeholder note that names an uncomfortable-to-use feature. A note that only lists numbers, or omits the ethics reflection, does not pass.
- **What it sets up:** the depth-sweep table is the **exact data Session 16 explodes** — students arrive having already seen training pull ahead, ready to watch test accuracy *fall* when depth is pushed further. The importance ranking feeds the model-comparison judgement in S18.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: idiomatic code commented *for the teacher*, with the depth-1→4 train/test table (train rising 0.881→0.922, test roughly flat 0.865→0.881), the depth-3 importance ranking (study_hours ~0.88 dominant, screen_time ~0.00), a bar chart, the most-used/ignored identification with the redundancy caveat spelled out (screen time is likely redundant with study hours, not irrelevant), and a sample counsellor note that states the driver in plain language and names an uncomfortable feature (e.g. a demographic proxy) with a reason. Acceptable-variation notes cover any reasonable uncomfortable-feature choice and slightly different importance values by seed. The solution explicitly flags that the widening train-vs-test gap is *next session's topic* and should not be "explained away" here. All code runs top to bottom with no errors.
