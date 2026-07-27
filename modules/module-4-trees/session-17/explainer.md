# Random Forests: A Crowd of Trees That Vote

*Session 17 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The problem we're solving

Session 16 left us stuck. A single decision tree is readable and powerful — but grow it deep enough to capture a hard pattern and it **memorises the training data**, then does *worse* on new data than a shallow tree. Depth gives power; depth also overfits. Do we have to choose?

No. Today's idea gives us depth's power *and* resistance to overfitting, and it's almost embarrassingly intuitive: **don't rely on one tree — grow a hundred slightly different ones and let them vote.** That voting crowd is a **random forest.**

## Why a crowd beats an expert

Ask one brilliant expert a hard question and you're stuck with their particular blind spots. Ask a hundred experts who each studied a slightly different slice of the evidence, then go with the majority answer — and something lovely happens. Where each expert is *idiosyncratically* wrong (their own quirks), they disagree, and the majority washes those quirks out. Where they're right for real reasons, they agree, and the signal survives. The crowd's average is steadier than any single member.

This only works if the experts are actually **different.** A hundred identical trees would just repeat the same mistake a hundred times. So a random forest manufactures difference on purpose, with two doses of randomness:

1. **Random rows (bootstrap sampling).** Each tree is trained on a random sample of the transactions — drawn with replacement, so each tree sees a slightly different dataset.
2. **Random features per split.** At each split, a tree may only consider a random *subset* of the features. So one tree leans on `amount`, another is forced to find signal in `distance_from_home`.

Those two knobs make every tree genuinely its own expert. On our fraud data, seven such trees each score about 0.97–0.98 — individually fine — but they **disagree on 19 of 450 transactions.** That disagreement isn't a flaw; it's the raw material the vote works on.

## The payoff, measured honestly

Let's put a single tree and a 100-tree forest on the exact same fraud problem and judge them with the Module 3 yardstick — precision and recall (18 real frauds in the test set):

| model | frauds caught | false alarms | recall | precision |
|---|---|---|---|---|
| single decision tree | 11 of 18 | 5 | 0.61 | 0.688 |
| random forest (100) | 11 of 18 | **3** | 0.61 | **0.786** |

Read it carefully, because the honest story matters. The forest catches the **same** 11 frauds — recall is identical. What it improves is **precision**: it raises only **3** false alarms instead of 5. Two honest customers who'd have had their cards wrongly frozen by the single tree are spared, for the same fraud caught. The vote cancelled two of the single tree's private mistakes.

That's a *modest* win, and we're going to be honest about that. The forest didn't work a miracle; it made the model **steadier.** And it did so while resisting the overfitting that made a single deep tree brittle in Session 16 — because even though each tree in the forest is itself a deep, overfit, unreadable tree, their **disagreeing errors partly cancel in the vote.** The individual is brittle; the crowd is robust.

## How many experts?

More trees help — up to a point. Sweeping the number of trees on the fraud data: 1 tree scores 0.969, 5 trees 0.978, and by 25–100 trees it plateaus around 0.978. Adding trees mainly steadies the vote (reduces variance) and then gives diminishing returns. You don't overfit by adding *trees* the way you overfit by adding *depth* — the vote is a stabiliser, not an accelerator toward memorising.

## What it costs: you can no longer read it

Here's the catch, and we're banking it for next session. A single decision tree was our poster child for **interpretability** — you could read it aloud as if-then rules and show it to a parent or a loan applicant. A forest of 100 deep trees? You cannot read that aloud. It's a black box that votes. You can still ask it for feature importances, but you've lost the crisp, contestable "here is exactly why" that made a single tree special.

So the forest trades **interpretability for robustness.** Sometimes that's the right trade; sometimes it isn't. Session 18 forces the choice: forest vs single tree vs logistic regression, same problem, one metrics table — and a genuinely surprising answer about which one you'd actually ship.

## One more subtlety: voting cures variance, not bias

Voting cancels the *idiosyncratic* mistakes that trees make differently. It does **not** fix a mistake they **all** make. If every tree in the forest ignores a feature that actually matters, the majority ignores it too — no amount of voting rescues a shared blind spot. The crowd fixes *variance* (random, per-member error); it can't fix *bias* (a systematic error they share). Worth remembering when a forest confidently agrees with itself and is confidently wrong.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. What are the **two** sources of randomness that make a forest's trees different from one another, and why does the forest *need* them to be different?
2. On the fraud data the forest and the single tree both caught 11 of 18 frauds. So what did the forest actually improve, and who benefits?
3. A single decision tree and a random forest are both offered to a bank that must, by law, explain every declined transaction to the customer. Which has the edge here, and why?

---

<details>
<summary>Answers (open after attempting)</summary>

1. **Random rows** (each tree trains on a bootstrap sample of the data) and **random features at each split** (each split considers only a random subset of features). The forest needs the trees to differ because voting only cancels mistakes when the members are wrong in *different* ways — identical trees would just repeat the same error.
2. It improved **precision**: same recall (11 caught), but **fewer false alarms** (3 instead of 5). The people who benefit are the honest customers who would otherwise have had their cards wrongly frozen — two of them, here.
3. The **single decision tree** has the edge: it can be read aloud as if-then rules, so the bank can give the customer a concrete, contestable reason. The forest is more robust but is a black box of 100 voting trees — you can't hand its reasoning to the customer. (This is exactly the trade-off Session 18 makes you weigh.)

</details>
