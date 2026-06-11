# Session 1 — What Is Machine Learning?

Module 1 · Session 1 of 24 · 60 minutes

## 1. Lesson Theme

The course opener: a computer can do things nobody programmed it to do, because it found the rules in data. This session draws the single most important distinction of the course — *rules written by humans* vs *rules learned from examples* — and equips the student with the vocabulary (features, label, dataset, supervised, unsupervised) that every later session assumes.

- **What came before:** nothing — this is first contact. The student arrives with intermediate Python and basic pandas (verified by the prerequisite check).
- **What comes next:** Session 2 gets hands dirty with a real, imperfect dataset (missing values, cleaning). Today's data is tiny and perfect on purpose.
- **Active threads:** *Overfitting* is **seeded** here — the phrase "memorizing vs learning" must land today, attached to a felt experience (the lookup-table model), so Session 16 can pay it off. The *workflow mantra* is only glimpsed in the wrap (named properly in Session 4). Ethics stays dormant.

## 2. Key Activity

The student builds a "model" that is a pure lookup table: it answers perfectly for every song it has seen and is useless for any song it hasn't. **This is the memorizing-vs-learning moment** — the one thing they should still remember in Session 16. Everything else in the session supports it.

## 3. Tools & Materials

- **Libraries:** Python stdlib, pandas (light). **No scikit-learn today** — it enters in Session 3.
- **Notebooks:** `modules/module-1-foundations/session-01/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder — point the student to it at the wrap.
- **Datasets:** none from `datasets/` — all data today is tiny and inline (a 6-song table, a lookup dictionary). This is deliberate: real files with real problems start in Session 2.
- **Visual aid:** the two-box diagram, drawn live (whiteboard or shared screen):

  ```
  Traditional programming:   rules + data     →  answers
  Machine learning:          data  + answers  →  rules (a "model")
  ```

## 4. Learning Outcomes & Thinking Skills

By the end of the session the student can:

1. State the difference between traditional programming and machine learning in their own words, with an example that is not Netflix.
2. Point at a small tabular dataset and correctly name its rows, features, and label — and frame a task as "predict ___ from ___."
3. Classify a described task as supervised or unsupervised and justify the choice in one sentence.
4. Explain why the lookup-table model's perfect score proves nothing, using the phrase "memorizing, not learning."

**Thinking skills exercised:**

- **Mental Modeling** — the two-box diagram is the course's first mental model; the student should be able to redraw it from memory.
- **Critical Evaluation** — interrogating the hand-written rule system ("find a hit song that breaks these rules") and the lookup-table's fake perfection.
- **Intentional Direction** (light) — the "predict ___ from ___" framing is the seed of asking precise questions of data, which the capstone will demand.

## 5. Timestamped Class Activities

> No homework review today — Session 1 is the only session that skips it.

| Time | Activity |
|---|---|
| 0:00–0:08 | **Welcome & course tour.** How the 24 sessions work: twice weekly, homework between sessions, every session from next time opens with homework review. Set the promise: "by Session 4 you will have trained a real model." Quick prerequisite pulse-check: ask them to read a 3-line pandas snippet aloud. |
| 0:08–0:18 | **Concept: the flip.** Open with the Netflix/YouTube question: "Nobody at Netflix wrote an if-statement about *you*. So how does it know?" Draw the two-box diagram live. Land the definition: ML finds the rules from data + answers; the found rules are called a **model**. |
| 0:18–0:30 | **Guided coding 1 (classwork Part 1):** the hand-written `is_hit_song` rule function. Student adds one rule of their own, then the coach supplies counterexamples until a rule breaks. Discussion: how many rules would real Spotify need? Brittleness is the point. |
| 0:30–0:40 | **Vocabulary on a real table (classwork Part 2):** the 6-song DataFrame. Student labels features and label, answers the `title` trap question (it identifies, it doesn't inform). Practice the "predict ___ from ___" framing aloud, twice, with different labels on the same table. |
| 0:40–0:50 | **Guided coding 2 (classwork Part 3): the lookup-table model.** Perfect on every seen song, useless on every new one. Let the student *feel* the fake 100% before naming it: "memorizing, not learning." Say explicitly: "keep this phrase — it comes back in Session 16 as the most important idea in the course." |
| 0:50–0:55 | **Supervised vs unsupervised (classwork Part 4):** sort the five scenarios. **Stretch (student-driven):** invent one supervised and one unsupervised task from their own life, naming the features and (if any) the label. |
| 0:55–1:00 | **Wrap.** Recap the three vocabulary wins (features/label, supervised/unsupervised, memorizing vs learning). Glimpse the path: "every project we do follows data → model → evaluation → insight — we'll name it properly in Session 4." Preview homework and point to the explainer. |

## 6. Differentiation Notes

**If the student is flying:**

- Hand them the adversary role: "design a song that fools `is_hit_song_v2`" — then ask what that implies about rule systems at Spotify scale.
- Introduce the words *training data* and *unseen data* informally during Part 3 (they're formally defined in Session 3) and ask: "how would you check whether a friend memorized or learned?" Let them invent the train/test split idea themselves — don't name it, just smile and say "hold that thought for Session 3."
- In the stretch, require their invented tasks to name concrete, *measurable* features (not "how good the song is" — how would you measure that?).

**If the student is struggling:**

- Cut: the `is_hit_song_v2` rule-writing (use the provided version and just discuss it) and reduce the Part 4 sort to scenarios A, B, and E.
- Slow down on: the two-box diagram. Redraw it with a second example (keyboard next-word suggestion). Most confusion at this age is here, not in the code.
- **Non-negotiable, never cut:** the features/label vocabulary on the songs table, and the lookup-table moment with the phrase "memorizing, not learning." If only two things survive the hour, it's these.
- The supervised/unsupervised distinction can be softened to "data with an answer column vs data without" and revisited in Session 19 — don't burn minutes polishing it today.

## 7. Student Templates / Starter Materials

This is the most scaffolded notebook of the course — first session, everything pre-filled except deliberate gaps:

- **Pre-filled:** all imports, the complete `is_hit_song` function, the songs DataFrame, the full lookup-table demo, all concept markdown.
- **Student writes:** one extra rule in `is_hit_song_v2` (a working copy is provided, so the notebook runs even untouched); answers in every ✏️ markdown cell; the scenario sort; the reflection.
- **Convention to establish today:** ✏️ marks cells the student owns. Every cell runs top-to-bottom even if the student writes nothing — gaps are additive, not blocking.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top-to-bottom (it must show no errors); confirm the student's environment per `student-resources/setup-guide.md`; have two counterexample hit songs ready for Part 1 (a 7-minute hit, a hit from an unknown artist — pick current ones, the examples in the notebook are deliberately generic).
- **Known gotchas:** none technical — no dataset files, no sklearn. The risk in this session is *pacing*: the course-tour and Netflix discussion can eat 25 minutes. The lookup-table moment (0:40) is the heart; protect it.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`, populated in Phase 4):
  1. *"ML = robots / ChatGPT / general intelligence."* Correct gently: today's ML is narrow — one task, learned from one dataset.
  2. *"The computer understands the songs."* It doesn't — it finds number patterns. No understanding is implied anywhere.
  3. *"More rules would fix the rule system."* The point isn't that rules are too few; it's that humans can't anticipate everything and rules don't update themselves.
  4. *"100% right = it works."* The seed misconception — let the lookup table embody it rather than arguing abstractly. This exact confusion is re-harvested in Session 16.
- **Language note:** say "label" consistently, not "target/output/y" — synonyms arrive later (Session 3) once "label" is solid.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 30–45 minutes.
- **The exercise:** five parts ramping in difficulty — (1) identify label/features/paradigm in three described scenarios; (2) name features vs label on a preloaded app-usage table, twice, with two different prediction questions on the same table; (3) write their own 2–3-rule prediction function and find where it breaks; (4) demonstrate the memorizing model's failure on unseen data and reflect in writing; (5) open-ended: describe one ML system from their own life in data/features/label terms.
- **Success criterion (concrete artifact):** all five exercises attempted; Exercise 2's two framings correctly labeled; the Exercise 3 function runs on all test cases; the Exercise 4 reflection is at least three sentences using "memorizing" and "learning" correctly. (Named-metric criteria begin in Session 8 — until then, criteria are concrete artifacts.)
- **What it sets up:** Exercise 2's same-table-two-questions move previews the anchor-dataset strategy (one dataset, many lenses). The homework's tiny, perfect tables set up Session 2's opening line: "real data is never like this."
