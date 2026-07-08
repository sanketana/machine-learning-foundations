# When Accuracy Lies: Precision, Recall, and Who Pays

*Session 12 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## A 96%-accurate model that is completely useless

Here is the most important cautionary tale in classification. Imagine a credit-card fraud detector. In the data, only about **4%** of transactions are actually fraud — the other 96% are legit. Now I write the laziest "model" imaginable: it ignores every feature and predicts **"legit"** for *every single transaction*.

What's its accuracy? **96%.** It is right 96% of the time — because 96% of transactions really are legit. On paper that's an A. In reality it is worthless: it caught **zero** fraud. Every thief sailed straight through. The metric said "excellent" about a model that does the one thing it exists to prevent — nothing.

This is why, from today on, **accuracy alone is retired as a judge.** When one class is rare — fraud, disease, spam in a clean inbox — a model can score gloriously high just by always guessing the common class, while failing completely at the job that matters.

## The two mistakes have names

Last session we kept trading two nameless mistakes by moving the threshold. Here they are, named, on the fraud problem:

- **False positive** — a **false alarm**. The model shouts "fraud!" at an honest transaction. An innocent customer's card gets frozen at the worst possible moment.
- **False negative** — a **miss**. The model says "legit" about a real fraud. A thief gets through and someone is robbed.

Together with the two *correct* outcomes (fraud correctly caught, legit correctly cleared), those are the only four things that can happen. Next session we lay all four in a grid called the confusion matrix; today we turn the two *mistakes* into two metrics.

## Precision and recall

Instead of one blunt "fraction correct," we ask two sharper questions:

- **Recall** — *of all the real fraud, how much did we catch?* If there were 15 real frauds and we caught 9, recall is 9/15 = **0.60**. Recall is about **misses**: low recall means fraud is slipping through.
- **Precision** — *when the model cries "fraud," how often is it right?* If it raised 10 alarms and 9 were real fraud, precision is 9/10 = **0.90**. Precision is about **false alarms**: low precision means honest customers keep getting flagged.

Now watch them work. On our fraud data:

| "model" | accuracy | recall | what it really did |
|---|---|---|---|
| always-legit baseline | **0.96** | **0.00** | caught 0 of 15 frauds |
| real logistic model | **0.98** | **0.60** | caught 9 of 15 frauds |

Look at the **accuracy** column: 0.96 vs 0.98 — a tiny, meaningless-looking gap. Now look at **recall**: 0.00 vs 0.60 — the difference between a model that does nothing and one that catches most of the fraud. *Accuracy literally could not see the difference that recall makes obvious.* That is the entire reason precision and recall exist.

## Which mistake is worse? Whoever pays decides

Here's where machine learning stops being only math. The two mistakes are not equally bad — but *which* is worse depends entirely on **who bears the cost**:

- **Miss a fraud (false negative):** the bank and the defrauded customer lose money; trust erodes.
- **Freeze an honest card (false positive):** a real person is stranded at a petrol station at midnight, humiliated and unable to pay; the bank annoys a loyal customer.

For a bank chasing losses, missing fraud (recall) often feels worse — so they'd tune the model to catch more, accepting more false alarms. But push that too far and you're freezing thousands of honest cards to catch a few thieves, and now the *customers* are paying for the bank's caution. There is **no universal right answer.** The "best" model depends on a human decision about which harm you're willing to cause, and to whom.

This is the question the rest of the course keeps returning to, and it's why "just report accuracy" was never enough. A number can tell you *what* the model does; only a person can decide *whether that's acceptable, and for whom.*

## ⚠️ Common confusion: recall = 100% is not the goal

It's tempting to say "just catch all the fraud — get recall to 1.0." You can! Flag *every* transaction as fraud and you'll miss nothing. But then your **precision** collapses — almost every alarm is a false alarm, and you've frozen the whole bank's customers to catch 15 thieves. Recall and precision **pull against each other**, and next session we'll watch exactly that trade-off as we slide the threshold. The skill isn't maximising one number; it's choosing the balance that fits the real-world costs.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. A disease test is 99% accurate, but the disease affects 1% of people. How could a useless test score 99%? Which metric would expose it?
2. In plain words, what is the difference between precision and recall?
3. A hospital screening test and a spam filter might reasonably choose *different* balances of precision and recall. Why isn't there one correct choice?

---

<details>
<summary>Answers (open after attempting)</summary>

1. A "test" that says **"healthy" for everyone** is right 99% of the time (since 99% are healthy) — 99% accuracy, but it catches **0%** of the sick. **Recall** (of all the truly sick, how many did we catch?) would expose it immediately as 0.00.
2. **Recall** = of all the *real positives* (real fraud/disease), what fraction did the model catch? **Precision** = of all the cases the model *flagged*, what fraction were real? Recall is about misses; precision is about false alarms.
3. Because the **costs of the two mistakes differ** and are borne by different people. Missing a disease can be fatal (favour recall); a spam filter that's too aggressive deletes real mail (favour precision). The right balance is a human judgement about acceptable harm, not a formula.

</details>
