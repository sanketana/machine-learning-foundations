# What Is Machine Learning?

*Session 1 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The recipe and the taste

Think about how you'd teach someone to make your favourite dish.

The obvious way is to hand them a recipe: 200g of this, fry for four minutes, add salt at the end. That is **traditional programming**. A human figures out the rules, writes them down precisely, and the computer follows them exactly. The computer contributes nothing but obedience.

Now imagine a different approach: you don't hand over a recipe at all. Instead, you let your friend taste two hundred versions of the dish — some delicious, some terrible — and you tell them which is which. After enough examples, they start working out the recipe themselves: "the good ones always had more garlic… the bad ones were overcooked." Nobody told them the rules. They *extracted* the rules from examples.

That is **machine learning**. The whole field fits in one flip:

```
Traditional programming:   rules + data     →  answers
Machine learning:          data + answers   →  rules
```

The rules a computer extracts this way are called a **model**. When Netflix recommends a show, no programmer wrote an if-statement about you. A model learned, from millions of past viewing choices, which patterns predict "this person will watch this."

## The words we'll use every single session

Machine learning data usually arrives as a table. Here's a tiny one — six students, and whether they passed a test:

| study_hours | attendance_% | passed |
|---|---|---|
| 12 | 95 | yes |
| 3 | 60 | no |
| 9 | 88 | yes |
| 2 | 75 | no |
| 11 | 91 | yes |
| 5 | 70 | no |

- Each **row** is one example — one student.
- The columns the model is allowed to look at are the **features** — here, `study_hours` and `attendance_%`.
- The column we want to predict is the **label** — here, `passed`.
- The whole table is the **dataset**.

A useful habit: describe any ML task as **"predict ___ from ___."** Here: predict *passed* from *study hours and attendance*. If you can't fill in those two blanks, you don't have an ML task yet — you have a vague wish.

Now look at the table again, like a model would. Notice anything? Every student who studied 9 or more hours passed; everyone below 5 failed. You just did, by eye, what a model does with numbers: found a pattern in the features that predicts the label. A model is not magic — it's pattern-finding, made systematic and done at a scale no human could manage.

## Two kinds of learning

When the dataset includes the answer column — like `passed` above — and the model learns to predict it, that's **supervised learning**. It's "supervised" because the answers supervise the learning, like a teacher marking practice tests.

Sometimes there is no answer column at all. An online store has data about its shoppers — visits, spending, browsing time — but no column saying what "type" of shopper each one is. Asking a model to find natural groups hiding in such data is **unsupervised learning**. We'll spend most of this course on supervised learning and return to unsupervised near the end.

Quick test you can apply to any example: *is there an answer column?* Yes → supervised. No, just find structure → unsupervised.

## ⚠️ Common confusion: a perfect score proves nothing

Here's a trap almost everyone falls into at first.

Suppose a "model" simply memorizes the table above — all six rows, like flashcards. Quiz it on those six students and it scores 100%. Perfect, right?

Now show it a seventh student. It has no idea. Not a bad guess — *no* guess. It never found the pattern connecting study hours to passing; it just stored answers. A student who memorizes the answer key to last year's exam looks brilliant until the questions change.

**Memorizing is not learning.** Learning means finding the pattern, so you can handle examples you've never seen. Keep this phrase in your pocket — it returns in Session 16 as the most important idea in the whole course, and by then you'll be able to measure the difference, not just describe it.

## Where this goes

Over the next three sessions you'll work with real data (messier than today's tidy tables), meet the library that builds models for us, and — by Session 4 — train your first real model, end to end. Everything will keep coming back to the words on this page.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. Your phone keyboard suggests the next word as you type. In "predict ___ from ___" form, what is it doing — and is that supervised or unsupervised?
2. In the students table above, why is `passed` not a feature?
3. A friend's model scores 100% on the data it was built from. What single question would you ask before being impressed?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Predict *the next word* from *the words typed so far*. Supervised — every sentence ever typed provides "answer" examples of which word actually came next.
2. Because it's the thing being predicted — the label. A model that gets to look at `passed` while predicting `passed` isn't predicting anything.
3. "How does it do on examples it has *never seen*?" A perfect score on familiar data is exactly what memorizing looks like.

</details>
