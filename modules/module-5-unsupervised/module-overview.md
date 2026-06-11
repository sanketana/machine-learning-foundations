# Module 5 — Unsupervised Learning

**Sessions 19–21 · Weeks 10–11**

## Module goals

By the end of this module the student can:

1. Articulate the unsupervised mindset shift: there is no label, no "right
   answer" column — the algorithm finds structure, and humans decide what it
   means.
2. Explain k-means intuitively (centroids as "magnets") and run it on real
   data.
3. Visualize and *interpret* clusters: naming what a cluster means is the
   human's job, not the algorithm's.
4. Choose k with the elbow method, and explain over-segmentation as the
   unsupervised cousin of overfitting.
5. Say when clustering misleads — and that an algorithm will happily find
   "clusters" in structureless data.

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 19 | Learning Without Labels | The label column is gone — and the algorithm still finds groups. |
| 20 | K-Means in Practice | Naming the clusters of students they've known since Module 1. |
| 21 | Choosing k + Limits of Clustering | The elbow plot, and why k=10 "fits better" but means less. |

## Datasets used

- `datasets/anchor/student_habits.csv` — *the anchor payoff.* Drop
  `test_score` and `passed` and cluster the same 420 students the learner
  has regressed and classified. The dataset has genuine latent structure
  (three habit personas; teacher notes in `datasets/README.md`), so k-means
  rediscovers something real. Seeing one dataset through a third lens makes
  the difference between the paradigms visceral (HANDOFF.md §10).
- `datasets/secondary/shoppers.csv` — homework and the Session 19 use case:
  shopper behavior segments with no predefined categories (latent k = 4).

## Thread checkpoints

- **Overfitting:** echoed in Session 21 — over-segmentation is the same
  disease in unsupervised clothing: more clusters always "fit better," and
  the elbow method is the discipline that resists it.
- **Ethics:** Sessions 19–21 carry a mandatory moment (HANDOFF.md §5): what
  happens when people get put in clusters they didn't choose — and get
  treated accordingly?
- **Numbers, not vibes:** stretched interestingly here — inertia and the
  elbow give numbers, but cluster *meaning* is judged by humans. Naming that
  tension is part of the lesson.
- **Workflow mantra:** still applies with no labels; *evaluation* changes
  shape, and *insight* carries more of the weight.
