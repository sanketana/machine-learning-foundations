# Curriculum Map — Machine Learning Foundations

24 sessions · 60 minutes each · twice weekly · Sanketana School of Code

Every session ends with a homework exercise; every session from Session 2
onward opens with ~10 minutes of homework review. This rhythm is mandatory —
it is spaced retrieval, not warm-up.

## The 24-Session Arc

### Module 1 — Foundations & Working with Real Data (Sessions 1–4)

| # | Session title | Core concepts |
|---|---|---|
| 1 | What Is Machine Learning? | ML vs traditional programming; supervised vs unsupervised; features, labels, datasets; *seed* overfitting vocabulary ("memorizing vs learning"). Use case: how Netflix/YouTube recommendations improve from past data. |
| 2 | Working with Real Data I | Loading datasets; exploring with pandas; missing values (detect, drop, fill); why garbage in = garbage out. |
| 3 | Working with Real Data II + Meet scikit-learn | Encoding categorical columns; feature scaling (intuition: "why salary in lakhs shouldn't drown out age"); the `fit`/`predict`/`score` API as an explicit teaching moment; train/test split — why we hide data from the model. |
| 4 | First Model, Full Workflow | Build the simplest possible end-to-end pipeline on a clean dataset. The win: "I trained a model today." Establish the workflow mantra: **data → model → evaluation → insight**. |

### Module 2 — Linear Models: Regression (Sessions 5–8)

| # | Session title | Core concepts |
|---|---|---|
| 5 | Linear Regression: The Idea | Predicting continuous values; the line of best fit, visually; features as "ingredients" of a prediction. Use case: house prices from size, location, rooms. |
| 6 | Error and the Cost Function | What "wrong" means numerically; cost function as a bowl we slide down (visual only, no calculus); model fit. |
| 7 | Multi-Feature Regression in Practice | From one feature to many; interpreting coefficients ("which ingredient matters most?"); building on the anchor dataset. |
| 8 | How Good Is My Model? Regression Metrics | MAE, RMSE, R²; what counts as "good" depends on the problem; comparing models with numbers, not vibes. |

### Module 3 — Classification (Sessions 9–13)

| # | Session title | Core concepts |
|---|---|---|
| 9 | KNN: Your First Classifier | "You're probably similar to your neighbors"; geometric intuition; choosing k; first decision boundary visualization. |
| 10 | Logistic Regression I | Why a straight line fails for yes/no questions; probability-based classification; the S-curve, intuition-first. Use case: spam vs not spam. |
| 11 | Logistic Regression II + Decision Boundaries | Thresholds; moving the threshold and watching predictions change; binary vs multi-class overview. |
| 12 | Evaluating Classifiers | Accuracy and its failure mode (the 99%-accurate fraud model that catches zero fraud); precision, recall; class imbalance. Use case: credit card fraud. |
| 13 | The Confusion Matrix | Reading the four quadrants; precision/recall trade-off as a real decision ("which mistake is worse?"); connecting metrics to consequences — **first major ethics thread moment**. |

### Module 4 — Tree-Based Models (Sessions 14–18)

| # | Session title | Core concepts |
|---|---|---|
| 14 | Decision Trees: Rules a Human Can Read | Rule-based learning; interpretability; building a tree by hand first, then with sklearn. Use case: will a student pass, based on attendance, practice time, test scores. |
| 15 | Growing and Reading Trees | Tree depth; feature importance; visualizing trees; why interpretability matters to real stakeholders. |
| 16 | **Overfitting: The Deep Dive** | The flagship experiential lesson: crank `max_depth`, watch training accuracy hit 100% while test accuracy falls; memorizing vs generalizing; connect back to Session 1's seed. |
| 17 | Random Forest I | Ensemble intuition: "ask 100 slightly different experts and take a vote"; why forests beat single trees. |
| 18 | Random Forest II | Robustness; comparing forest vs tree vs logistic on the same fraud-style problem; choosing a model is a judgment call. Use case: fraud detection via many trees. |

### Module 5 — Unsupervised Learning (Sessions 19–21)

| # | Session title | Core concepts |
|---|---|---|
| 19 | Learning Without Labels | The unsupervised mindset shift; pattern discovery; k-means intuition (centroids as "magnets"). Use case: grouping online shoppers into behavior segments with no predefined categories. |
| 20 | K-Means in Practice | Running k-means; visualizing clusters; interpreting what a cluster *means* (the human's job, not the algorithm's). |
| 21 | Choosing k + Limits of Clustering | The elbow method; over-segmentation as the unsupervised cousin of overfitting; when clustering misleads. |

### Module 6 — Capstone (Sessions 22–24)

| # | Session title | Core concepts |
|---|---|---|
| 22 | Capstone Kickoff: Choose and Frame | Student selects from 4–5 curated capstone datasets (or proposes their own); frames the question; plans the workflow; **Project Ethics Check**. |
| 23 | Capstone Studio | Full end-to-end execution with coach support: prep → model → evaluate → iterate. Instructor coaches, does not drive. |
| 24 | Demo Day | Student presents: the question, the workflow, the results, what the model gets wrong and about whom, and what they'd do next. Parents may attend. Course retrospective. |

## Recurring Threads

These must appear across sessions, not just once:

1. **The workflow mantra** — *data → model → evaluation → insight* —
   introduced Session 4, referenced in every module, structurally embodied in
   the capstone.
2. **Overfitting** — seeded S1, deep-dive S16, echoed S17–18 (forests as an
   antidote), S21 (over-segmentation), S24 (capstone reflection).
3. **"Numbers, not vibes"** — every model built after Session 8 must be
   evaluated with a named metric. Homework rubrics enforce this.
4. **Ethics & consequences** — threaded where it has teeth: S12–13 (which
   mistake is worse, and who bears its cost), S14–15 (why a stakeholder might
   demand an interpretable model), S19–21 (being put in a cluster you didn't
   choose), S22 (the written Project Ethics Check), S24 ("what the model gets
   wrong and about whom" is a mandatory Demo Day section).
5. **Interpretability vs accuracy** — first raised with trees (S14–15), made
   concrete in the S18 model comparison.
