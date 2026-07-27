# Growing and Reading Trees: What Did the Model Lean On?

*Session 15 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## Two things you can do with a fitted tree

Last session we grew a tree's first split by hand and read a shallow tree aloud. Today, two moves: **grow** the tree with the `max_depth` knob, and **read back what it learned** — specifically, *which feature it leaned on most.* The second move is the star: it's called **feature importance**, and it turns a fitted model into a plain-language statement about what drives its decisions.

## The `max_depth` knob

`max_depth` controls how many layers of questions the tree may ask. Depth 1 is a single question (our root split). Depth 2 adds one follow-up under each branch. Depth 3 adds another layer. More depth means more, finer questions — the tree can carve the students into smaller and smaller groups.

Here's what happens to accuracy on our students as we turn the knob:

| max_depth | training accuracy | test accuracy |
|---|---|---|
| 1 | 0.881 | 0.865 |
| 2 | 0.881 | 0.865 |
| 3 | 0.912 | 0.865 |
| 4 | 0.922 | 0.881 |

Notice the two columns drifting apart. **Training** accuracy — how well the tree does on the students it learned from — creeps *up* with depth. **Test** accuracy — how well it does on students it's never seen — barely moves. That gap is a quiet early warning. We'll name it today and leave it there. **Next session it becomes the whole story**: push the knob far enough and test accuracy doesn't just stall, it *falls*. Hold that thought.

## Feature importance: the tree ranks its own inputs

After fitting, every tree exposes `feature_importances_` — one number per feature, all adding to 1, saying **how much the tree relied on that feature to separate the classes.** Bigger = leaned on more. For our depth-3 student tree:

```
study_hours       ██████████████████████████████████  0.88
practice_sessions ██                                   0.06
sleep_hours       █                                    0.04
attendance        █                                    0.02
screen_time                                            0.00   <- never even asked
```

The tree is shouting: **study hours is almost the whole story here.** Screen time it never even asked about. You can cross-check this against the tree diagram — study hours sits at the very top and reappears deeper down, while screen time appears nowhere. The number and the picture agree.

This is interpretability levelling up. Last session: *"I can read the rules."* This session: *"I can see what the model thinks matters, ranked, in numbers."* That's something you can hand to a school counsellor: *"the model's call is driven almost entirely by weekly study hours; attendance and screen time barely move it."* They can act on that sentence — and, just as importantly, they can *argue* with it.

## Three things people get wrong about importance

**"Importance is a fact about the world."** It isn't — it's a fact about *this fitted tree.* Change the depth or the random seed and the numbers shift (at depth 2, study hours is ~0.96; deeper, the minor features pick up small shares). Always say *which* tree you're reading. Importance is "how much this model used the feature," not "how important the feature truly is in life."

**"A feature with 0 importance is useless."** Screen time scored 0.00 — but that almost certainly does **not** mean screen time is unrelated to passing. More likely, study hours is so closely related to screen time (people who study more scroll less) that once the tree used study hours, screen time had nothing left to add. It's **redundant here**, not irrelevant. Drop study hours and screen time's importance would jump.

**"The most important feature causes the outcome."** Importance says the model *leans on* study hours, not that studying *causes* passing. It's still just correlation — a powerful, useful correlation, but not proof of cause. (We return to this in the capstone.)

## Reading importance responsibly

One more reason feature importance matters: it lets you *catch a model relying on something it shouldn't.* Imagine a loan model whose top feature turned out to be a customer's postcode — a stand-in for their neighbourhood, and often for race or income. Importance makes that visible in a single ranking, where a black-box model would hide it. So reading importance isn't only a convenience; it's part of the responsibility of shipping a model. What a model leans on is a choice you're accountable for — and importance is how you check.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. As you increase `max_depth`, which accuracy rises faster — training or test — and why is a widening gap between them worth watching?
2. A tree reports `attendance` importance = 0.00. Your classmate concludes "attendance has nothing to do with passing." What's the flaw?
3. Why is a feature-importance ranking something you could hand to a non-technical stakeholder, where a KNN model's reasoning isn't?

---

<details>
<summary>Answers (open after attempting)</summary>

1. **Training** accuracy rises faster — deeper trees can carve the training students into ever-finer groups and get more of them exactly right. Test accuracy lags because those fine carvings often fit quirks of the training set that don't generalise. A widening gap warns that the tree is starting to fit the training data *specifically* rather than the general pattern — the seed of overfitting (Session 16).
2. Zero importance means *this tree never needed attendance* — very likely because a correlated feature (study hours) already did the separating. Attendance can be strongly related to passing yet score 0.00 because it was **redundant**, not irrelevant. Remove the correlated feature and its importance would rise.
3. A tree's importance is a short, ranked, plain-language list — "study hours drives it, screen time doesn't" — that a stakeholder can understand, act on, and challenge. KNN's reasoning is "the nearby points looked like this," which has no per-feature story to hand over.

</details>
