# KNN: You're Probably Like Your Neighbours

*Session 9 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## A different kind of question

For four sessions our model answered *"how much?"* — a test score, a house price. The answer was always a **number on a line**. Today the question changes to *"which one?"* — **did the student pass, yes or no?** The answer is a **category**, not a magnitude. That's **classification**, and it's a whole new half of machine learning.

Same students as Module 2, same habits — we just swap the label. Instead of predicting the exact score, we predict `passed`: 1 or 0. About **58%** of our cohort passed, so a lazy "everyone passes" guess would already be right 58% of the time. We want to beat that with something smarter.

## The simplest possible classifier

Here's how a person would guess whether a new student passes: *look at the students most like them, and see how those turned out.* If the five people closest to you in study hours and attendance all passed, you'd bet you pass too. That instinct **is** the algorithm. It's called **k-Nearest Neighbours** — KNN — and it has no equation:

> To classify a new point, find the **k** training examples closest to it, and let them **vote**. Majority wins.

That's it. There's nothing to "fit" — KNN just remembers all the training students, and when a new one arrives, it measures who's nearest and counts their votes. `k` is how many neighbours get a say.

## Distance needs a fair scale

"Closest" means distance, and distance is only fair if the features are on the same footing. Attendance runs from about 55 to 100 (a span of ~45); practice sessions run from 0 to 7. If we measure distance on the raw numbers, attendance's big range **drowns out** every other habit — two students would count as "near" based on attendance alone. So, exactly as in **Session 3**, we **scale** the features first, putting each on the same "one standard step" footing before measuring distance. (On our data this barely moves the accuracy — attendance happens to be a decent predictor — but scaling is the right default whenever a model works by distance. KNN always does.)

## The picture: a decision boundary

Because KNN is pure geometry, we can *see* it. Take just two habits — study hours and attendance — so every student is a dot on a 2-D plot. Now colour **every point on the map** by what KNN would predict there: blue where it says "pass," red where it says "fail." The border between the colours is the **decision boundary** — the line where the model changes its mind. Your students are dots sitting on top of this coloured map. This plot is the thing to remember from today: a classifier is a way of **carving up the space** into regions.

## The one knob: k

KNN has a single dial, **k**, and turning it reshapes the boundary:

- **k = 1** — each new point just copies its single nearest neighbour. The boundary becomes **jagged**, wrapping tightly around every individual point, with little islands of one colour stranded in a sea of the other. On the *training* data this scores a perfect **100%** — because every training point's nearest neighbour is itself. That sounds great and is actually a **warning light**.
- **k = 15** — each point polls a whole neighbourhood of 15 and takes the majority. The boundary **smooths out** into a sensible, gentle border. One weird outlier can't flip the vote anymore.

So k trades **memorising** for **generalising**. Small k clings to every point (including the noise); large k steps back and sees the general trend. Push k too far — all the way to "poll everyone" — and the model just predicts the majority class everywhere and the boundary disappears. The skill is picking a k in between.

## ⚠️ Common confusion: 100% accuracy is not a trophy

When k=1 scores 100% on the training data, it is *not* the best model — it has simply **memorised** the answers to questions it has already seen. The honest test is on data it never trained on. On our held-out students, k=1 scores noticeably *lower* than a bigger k. This is the same memorising-vs-learning trap from Session 1, showing up in a new place. (We're not fully unpacking it yet — that's the flagship lesson in **Session 16** — but train your eye now: *perfect on training, worse on test* is the signature.)

## Choosing k with numbers, not vibes

So how do you pick k? Not by which one looks nicest, and definitely not by training accuracy. You **try several values of k, score each on the held-out test set, and choose the one that does best there.** That's the "numbers, not vibes" rule (Session 8) applied to a real decision. For our two-habit model, test accuracy climbs from ~0.80 at k=1 up to around ~0.87 for a k in the low teens, then flattens. You'd ship one of those — a k big enough to be steady, not so big it goes blurry.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. In one sentence, how does KNN decide what class a new point belongs to?
2. A friend proudly reports their k=1 classifier gets **100% accuracy**. Why is that not the good news it sounds like, and what would you ask to see instead?
3. Why do we scale the features before running KNN, when we didn't have to for the predictions in linear regression?

---

<details>
<summary>Answers (open after attempting)</summary>

1. It finds the **k nearest training examples** (by distance) and takes a **majority vote** of their labels — the new point gets whichever class is most common among its neighbours.
2. k=1 scores 100% on the **training** data by construction — every point's nearest neighbour is itself, so it just recites answers it has already seen (memorising, not learning). Ask for the accuracy on a **held-out test set**; that's the honest number, and for k=1 it's usually noticeably lower.
3. KNN decides everything by **distance**, so a feature with a wide numeric range (like attendance, 55–100) would dominate "closeness" and drown out the others. Scaling puts every feature on the same footing so the distance is fair. Linear regression's predictions don't depend on distance, so it didn't need scaling (we only scaled there to *compare coefficients*).

</details>
