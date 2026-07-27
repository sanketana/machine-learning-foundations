# Decision Trees: A Model You Can Read Aloud

*Session 14 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## A model that can explain itself

All through Module 3 we built classifiers that *worked* but couldn't really *talk*. Ask a KNN model "why did you predict this student fails?" and the honest answer is "because the five students nearest to them in the data mostly failed" — true, but not something you can write on a form. Ask logistic regression and you get a weighted sum of numbers. Useful, but not an explanation a worried parent or a loan applicant would accept.

Today's model is different. A **decision tree** makes its decision by asking a short series of yes/no questions, and you can read the whole thing aloud:

> *If study hours are under 8 → predict **fail**.
> Otherwise, if attendance is under 80 → predict **fail**; else predict **pass**.*

That's it. That's the entire model. No hidden sum, no invisible neighbours — just questions a human can follow, agree with, or argue against. This property has a name we'll come back to all module: **interpretability**. A tree is a model you can read.

## How a tree learns: one good question at a time

Here's the beautiful part — the tree isn't handed those questions. It *finds* them, and the way it finds them is something you can do by hand.

Start with a mixed pile of students — some passed, some failed. The tree asks: **of all the yes/no questions I could ask, which single one best splits this mixed pile into two cleaner piles?** "Cleaner" means *more one-colour* — a pile that's all-fail or all-pass is what we're after.

Take a dozen students and try the question **"is study_hours < 8?"**:

- **Yes** (studied under 8 hrs): 5 students — **0 passed, 5 failed.** Completely one-colour.
- **No** (studied 8+ hrs): 7 students — **6 passed, 1 failed.** Almost one-colour.

That's a great question! It took a totally mixed pile (6 pass / 6 fail) and sorted it into one pure "fail" group and one mostly-"pass" group. Now try a worse cut, **"is study_hours < 12?"**:

- **Yes:** 9 students — 3 passed, 6 failed. Still mixed.
- **No:** 3 students — 3 passed, 0 failed. Pure, but tiny.

Worse — the big group is still a muddle. By trying a few thresholds and **just counting**, you discover that **study < 8** separates these students best. That counting *is* the algorithm. When you later run `DecisionTreeClassifier`, it scans every feature and every threshold, counts exactly like you did, and picks the winner. On the full class dataset it lands on **study hours ≤ 7.65** — essentially the same line you drew by hand.

## Purity, and a number for it

We keep saying "cleaner" and "more one-colour." The proper word is **purity**, and there's a simple number for its opposite, **impurity** (the one sklearn uses is called **Gini**):

- A group that's **all one class** (all pass, or all fail) → impurity **0**. Perfectly pure.
- A group that's **50/50** → impurity **0.5**. As mixed as it gets.

You don't need the formula. You need the picture: the tree's whole strategy is *pick the split that drops impurity the most* — that turns one muddy pile into two of the cleanest piles available. Our 12-student pile starts at impurity 0.5 (6/6); after the study<8 split the two children together sit at about 0.14. That drop is why the tree chooses it.

## Reading the finished tree

Once it's grown a level or two, you read a tree by **tracing a path from top to bottom**, turning each branch into a clause:

```
study_hours <= 7.65 ?
├── yes → predict FAIL
└── no  → attendance <= 80 ?
          ├── yes → predict FAIL
          └── no  → predict PASS
```

Path by path, in plain English: *"Studied little? Fail. Studied enough but barely showed up? Still fail. Studied enough and attended? Pass."* Every prediction the model will ever make is one of these sentences. That's what makes a tree special — the explanation and the model are the same object.

## The one student it gets wrong — and a hint of trouble

Look back at our great split. The "study ≥ 8" side had **6 passed and 1 failed.** That one failer studied plenty and still didn't pass — maybe they were ill, maybe the label's just noisy. Our clean, shallow tree gets that student **wrong**, and that's fine. A good model is *mostly* right, not *perfectly* right.

But notice the temptation: we *could* add more questions to carve that one student out and get everyone right. Hold that thought. Chasing a tree that gets *every* training student correct is exactly how a model starts **memorising** the data instead of learning the pattern — and in two sessions (the Session 16 deep-dive) we'll watch that backfire spectacularly. For now, just notice: the shallow, readable tree that makes one honest mistake is a *feature*, not a bug.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. In one sentence each, what makes a decision tree more *interpretable* than a KNN model?
2. You split 10 students by "attendance < 70": the "yes" group is 1 pass / 4 fail, the "no" group is 4 pass / 1 fail. Is this a good split? Which group is purer?
3. A classmate proudly grows a tree that gets **all** their training students correct, including every odd exception. Why might you be *worried* rather than impressed?

---

<details>
<summary>Answers (open after attempting)</summary>

1. A tree's decision is a short chain of yes/no questions you can **read aloud as if-then rules** ("if study < 8 then fail"); KNN's decision is "the nearby points mostly looked like this," which you can't write as a rule or show to the person affected.
2. It's a **decent** split — both groups lean strongly one way (4:1 and 1:4), far purer than the mixed starting pile. Neither is perfectly pure; the "no" group (4 pass / 1 fail) and the "yes" group (1 pass / 4 fail) are equally impure here (both 1-out-of-5 wrong).
3. Getting *every* training point right — including weird one-off exceptions — is a sign the tree has started **memorising** the training data rather than learning the general pattern. It may do worse on new students. That's overfitting, and Session 16 makes it visible.

</details>
