Title: Conformal Prediction Under Exchangeability
Date: 2025-06-02 12:00
Author: Matteo Gätzner
Category: Statistics
Tags: conformal-prediction, exchangeability
Summary: A quick introduction to the basics of conformal prediction under exchangeability.

Hey all! As the title suggests, this blog post is a short introduction to conformal prediction under exchangeability. It is based on Chapter 3 of the book[^1] _Theoretical Foundations of Conformal Prediction_, which Anna Kosovskaya, Sarah Medding, and I presented at the Conformal and Probabilistic Prediction Seminar, led by Prof. Dr. Johanna Ziegel, at ETH Zurich. 

Download the slide deck here: [Download the slides](files/conformal-slides.pdf){:target="_blank"}.

## Uncertainty Quantification for Predictions

Say you have data points $(X_i, Y_i) \in \mathcal{X} \times \mathcal{Y}$. For a
regression task, that could mean $(X_i, Y_i) \in \mathbb{R}^d \times
\mathbb{R}$. A common task is to then predict unknown label $Y_{n+1}$ given known
input $X_{n+1}$ using some predictive model $\hat{f}(X_{n+1})$ that could for
example be a neural network, linear model or a smoothing spline.

Now, even if the model's performance seems good empirically — say it has a low
cross-validated $R^2$ score — we have no real guarantee that inference time
predictions are accurate. 

The solution that conformal prediction proposes is to construct a _prediction
set_ $\, \mathcal{C}(X_{n+1}) \subseteq \mathcal{Y}$ based on $\hat{f}$ and get
guarantees for $\mathcal{C}(X_{n+1}).$ The guarantee is called _marginal coverage_
and says that the prediction set contains the true label $Y_{n+1}$ with high
probability, symbolically
$$
\Pr(Y_{n+1} \in \mathcal{C}(X_{n+1})) \geq 1 - \alpha
$$
where $\alpha \in (0, 1)$ is a user-specified error level that shrinks or
expands the prediction set accordingly. A large prediction set implies high
uncertainty while a small one implies low uncertainty.

Of course, there are other solutions for quantifying predictive uncertainty,
however most rely on assumptions about the predictive model, asymptotics, limit
theorems, Gaussian approximations or strong assumptions on the data-generating
distribution. What makes conformal prediction such a powerful method is that it
doesn't do that. It doesn't need assumptions about the predictive model, like
that its linear, only uses certain (neural network) layers, makes
deterministic predictions or that its predictions accurate. 

Although we get marginal coverage for poor models too, its still worth
investing into a good predictive model since the corresponding prediction sets
depend on its performance. Good models tend to produce tight, informative
prediction sets. Weak models tend to produce large, uninformative ones.

Furthermore, marginal coverage isn't a asymptotic guarantee; it can be achieved
with finite datasets, finite model sizes and finite time. 

We do need a minimal assumption on the data-generating distribution though,
namely _exchangeability_.

---

## Exchangeability

Let $Z_1, \dots Z_n \in \mathcal{Z}$ be random variables with a joint
distribution. We say that the random vector $ (Z_1, \dots, Z_n) $ is
_exchangeable_ if, for every permutation $\sigma \in \mathcal{S}_n,$

$$
(Z_1, \dots, Z_n) 
\overset{d}{=}
(Z_{\sigma(1)}, \dots, Z_{\sigma(n)})
$$

where $\overset{d}{=}$ denotes equality in distribution, and $S_n$ is the set
of all permutations on $ [n] \coloneqq \\{1, \dots, n\\} $.

## Equality in Distribution

Recall that two real‐valued random variables $Z_1$ and $Z_2$ are *equal in distribution*, written

$$
Z_1 \;\overset{d}{=}\; Z_2,
$$

if for every $z\in\mathbb{R},$

$$
\Pr\bigl(Z_1 \le z\bigr)
\;=\;
\Pr\bigl(Z_2 \le z\bigr).
$$

Equivalently, for every (Borel) set $A\subseteq\mathbb{R},$

$$
\Pr\bigl(Z_1\in A\bigr)
\;=\;
\Pr\bigl(Z_2\in A\bigr).
$$

In the context of exchangeability, we require that any finite tuple $(Z_1,\dots,Z_n)$ has the same joint law as its arbitrarily permuted version $(Z_{\sigma(1)},\dots,Z_{\sigma(n)})$.

## Exchangeability for Infinite Sequences

An infinite sequence $Z_1,Z_2,Z_3,\dots$ taking values in the same space $\mathcal{Z}$ is called *exchangeable* if every finite truncation $(Z_1,\dots,Z_n)$ is exchangeable in the sense above. In particular, for every $n$ and every permutation $\sigma$ of $\{1,\dots,n\},$

$$
(Z_1,\dots,Z_n)
\;\overset{d}{=}\;
(Z_{\sigma(1)},\dots,Z_{\sigma(n)}).
$$

This simply ensures that no matter how many observations one looks at—$n=1,2,3,\dots$—their joint distribution does not change when you reorder them.

## Exchangeability Intuition

Informally put, an exchangeable sequence "doesn’t care" about the order in which data arrive. Any permutation of the observations is equally likely. Here are two common scenarios in which exchangeability holds.

**Scenario 1 (i.i.d. data):**
If $Z_1,\dots,Z_n$ are i.i.d. draws from some distribution $P,$ then obviously

$$
\Pr(Z_1=z_1,\dots,Z_n=z_n)
\;=\;
\prod_{i=1}^n P(Z_i=z_i)
\;=\;
\Pr(Z_{\sigma(1)}=z_1,\dots,Z_{\sigma(n)}=z_n)
$$

for any permutation $\sigma$. Hence i.i.d. implies exchangeable.

**Scenario 2 (sampling without replacement):**
Suppose you draw $n$ items from a finite population $\{z_1,\dots,z_N\}$ uniformly *without replacement*. Then each ordered‐tuple of $n$ distinct draws is equally likely, so any reordering of those $n$ draws has the same probability. Thus the sequence is exchangeable (though not independent).

## Setting

Let's summarize our assumptions and goal. We'll assume an exchangeable dataset of size $n+1$:

$$
(X_1,Y_1),\,(X_2,Y_2),\,\dots,\,\bigl(X_n,Y_n\bigr),\,\bigl(X_{n+1},Y_{n+1}\bigr)
\;\in\;
\mathcal{X}\times\mathcal{Y},
$$

all drawn from some (possibly unknown) joint distribution on $\mathcal{X}\times\mathcal{Y}$. Our goal is to predict $Y_{n+1}$ given $X_{n+1}$ and the first $n$ pairs. In order to do that with guarantees will construct a prediction set

$$
\mathcal{C}\bigl(X_{n+1}\bigr)\;\subseteq\;\mathcal{Y}
$$

that satisfies marginal coverage:

$$
\Pr\Bigl(Y_{n+1}\in \mathcal{C}(X_{n+1})\Bigr) \ge 1-\alpha,
$$

for a user‐specified $\alpha\in(0,1)$. 

---

## Score Functions

There are two flavours of conformal predicion, split conformal prediction and
full conformal prediction. We'll define those procedures properly later and
focus on a key ingredient in both for now.
This key ingredient is a **score function**. Formally, a score function is any mapping

$$
s:\;\bigl(\mathcal{X}\times\mathcal{Y}\bigr)\;\times\;\bigl(\mathcal{X}\times\mathcal{Y}\bigr)^k\;\longrightarrow\;\mathbb{R},
$$

where:

* The first argument $(x,y)$ is the _test point_.
* The second argument $\mathcal{D} = \{(x_1,y_1),\dots,(x_k,y_k)\}$ is any
dataset (of size $k$) that you use to train your predictive model.

Intuitively, $s\bigl((x,y);\mathcal{D}\bigr)$ measures how "badly" a model trained on $\mathcal{D}$ would predict $y$ at $x$. Larger scores indicate larger error.

### Example Score Functions

**Residual score (regression):**
If $\hat{f}(\cdot, {\mathcal{D})$ is a regression model (neural net, linear regressor, etc.) trained on $\mathcal{D},$ then
$$s\bigl((x,y);\mathcal{D}\bigr)
\;=\;
\bigl|\,y - \hat f(x; \mathcal{D})\bigr|.$$
This is nonnegative and smaller when the prediction is good.

**Conformal quantile regression (CQR) score (regression):**
Suppose $\hat{\tau}(x; z, \mathcal{D})$ estimates the $z$-th conditional quantile of $Y$ given $X = x$. One way to obtain $\hat{\tau}$ is to use a quantile regression method. We call 
$$ s\bigl((x,y);\mathcal{D}\bigr)
\;=\; \max\\{\hat{\tau}(x; \alpha / 2, \mathcal{D}) - y, y - \hat{\tau}(x; 1 - \alpha / 2, \mathcal{D})\\}$$
the _CQR score_.
This score function is nonnegative, and adapts to the conditional distribution of $Y,$ producing smaller scores when $y$ lies near the estimated quantile and larger scores otherwise. This produces tighter prediction intervals where the model is more accurate and wider ones where it is less so. Because of its adaptability it is often considered a state-of-the-art score function for regression tasks.

**Misclassification error (classification):**
If $\hat f(x; \mathcal{D})$ produces a predicted class label $\hat y,$ then
$$ s\bigl((x,y);\mathcal{D}\bigr)
\;=\;
\begin{cases}
0, &\text{if }\hat f(x; \mathcal{D}) = y, \newline
1, &\text{otherwise.}
\end{cases} $$

## Symmetry and When It’s Needed

Whether the score function must be *symmetric* (defined further below) in its dataset argument depends on which conformal flavor you use.

### Split Conformal Prediction (no symmetry required)

In split conformal, one first partitions the available data into a *training set* $\mathcal{D}\_{\text{train}}$ and a **calibration set** $\mathcal{D}$.  A single model $\hat f$ is fitted on the fixed training set, and then calibration scores are computed as

$$
S_i
\;=\;
s\Bigl((X_i,Y_i)\;;\;\mathcal{D}_{\text{train}}\Bigr)
\quad\text{for each index }i.
$$

Since the model $\hat{f}$ is trained once on the training set, the only
"dataset argument" in each score is that fixed $\mathcal{D}\_{\text{train}}$.
In other words, each calibration score uses the same
$\mathcal{D}\_{\text{train}},$ so there is no need for the score function to
be invariant under permuting different calibration points.  **No symmetry
condition is required** for split conformal.

### Full (Leave‐One‐Out) Conformal Prediction (symmetry required)

In full conformal, for each $i \in \\{1,\dots,n\\},$ one trains a model $\hat f_{-i}$ on the data with $(X_i,Y_i)$ held out, defines

$$
S_i \;=\; s\Bigl((X_i,Y_i)\;;\;\mathcal{D}\setminus\{(X_i,Y_i)\}\Bigr),
$$

and then also scores the test point $(X_{n+1},y)$ via

$$
S_{n+1}
\;=\;
s\Bigl((X_{n+1},y)\;;\;\mathcal{D}\Bigr).
$$

Here $\mathcal{D} = \{(X_1,Y_1),\dots,(X_n,Y_n)\}$.  Because each held‐out model $\hat f_{-i}$ depends on the dataset $\mathcal{D}\setminus\{(X_i,Y_i)\},$ we need the score function to be *symmetric* in its second argument.  Concretely, 

A score function

$$
s:\;\bigl(\mathcal{X}\times\mathcal{Y}\bigr)\;\times\;\bigl(\mathcal{X}\times\mathcal{Y}\bigr)^k\;\longrightarrow\;\mathbb{R}
$$

is called *symmetric* if, for any $(x,y)$ and any dataset $\mathcal{D}=\\{(x_1,y_1),\dots,(x_k,y_k)\\},$ and for every permutation $\sigma,$

$$
s\bigl((x,y);\mathcal{D}\bigr)
\;=\;
s\bigl((x,y);\mathcal{D}_\sigma\bigr),
$$

where $\mathcal{D}\_\sigma = \\{(x\_{\sigma(1)},y\_{\sigma(1)}),\dots,(x\_{\sigma(k)},y\_{\sigma(k)})\\}$.

In other words, if you permute the order of the training points in $\mathcal{D},$ the score does not change. 

---

## The Full Conformal Prediction Procedure

In full conformal prediction, we “invert” a chosen score function to determine which candidate labels $y$ are consistent with our data. In other words, for each possible $y\in\mathcal{Y},$ we check whether inserting $(X_{n+1},y)$ into our dataset yields a conformity score that is not unreasonably large compared to the other scores.

### Notation

To make precise statements further below we'll first need to get some notation
out of the way.
To that end, denote the training set with $n$ data points as
$$ \mathcal{D}\_n 
\;=\; 
\bigl((X_1, Y_1),\,(X_2, Y_2),\,\dots,\,(X_n, Y_n)\bigr), $$
and the training set with the additional test point as
$$ \mathcal{D}\_{n+1} 
\;=\; 
\bigl((X_1, Y_1),\,\dots,\,(X_n, Y_n),\,(X\_{n+1}, Y\_{n+1})\bigr). $$
Of course, in reality, $Y\_{n+1}$ is unknown, so we cannot form $\mathcal{D}\_{n+1}$ directly.

To see whether a particular label $y$ "fits" with the existing data, define the
_augmented dataset_ as
$$ \mathcal{D}\_{n+1}^y 
\;=\; 
\bigl((X_1, Y_1),\,\dots,\,(X_n, Y_n),\;(X_{n+1},\,y)\bigr). $$
In this notation, $(X_{n+1},\,y)$ is what we call the *hypothesized test
point*. The question becomes: if we pretend $Y_{n+1} = y,$ does the full
dataset $\mathcal{D}\_{n+1}^y$ look "typical" under our chosen score function?

For a given $y,$ we compute a conformal score for each data point in $\mathcal{D}\_{n+1}^y,$ symbolically
$$ S_i^y 
\;=\; 
\begin{cases}
  s\bigl((X_i, Y_i);\,\mathcal{D}\_{n+1}^y\bigr),
    & \text{for } i = 1,2,\ldots,n, \newline
  s\bigl((X_{n+1},\,y);\,\mathcal{D}\_{n+1}^y\bigr),
    & \text{for } i = n+1.
\end{cases} $$
In other words:

* For $i\le n,$ we score the existing pair $(X_i,Y_i)$ against the entire augmented set.
* For $i=n+1,$ we score the hypothesized test point $(X_{n+1},y)$ in the same way.

## Full Conformal Prediction Set

Given our notation, fix any candidate label $y \in \mathcal{Y}$. By inserting $\,(X_{n+1},y)$ into the original training set $\mathcal{D}\_n,$ we obtain the augmented dataset

$$
\mathcal{D}\_{n+1}^y \;=\; \bigl((X_1, Y_1),\,\dots,\,(X_n, Y_n),\,(X_{n+1},\,y)\bigr).
$$

Next, for each $i=1,\dots,n+1,$ we compute the conformal score

$$
S_i^y 
\;=\; 
\begin{cases}
  s\bigl((X_i,\,Y_i);\;\mathcal{D}\_{n+1}^y\bigr), 
    & i = 1,2,\dots,n, \newline
  s\bigl((X_{n+1},\,y);\;\mathcal{D}\_{n+1}^y\bigr), 
    & i = n+1.
\end{cases}
$$

That is, each existing data point $(X_i,Y_i)$ is scored against the entire augmented set, and the hypothesized test point $(X_{n+1},y)$ receives its own score in exactly the same manner. If $S_{n+1}^y$ ends up being large relative to $\{S_1^y,\dots,S_n^y\},$ then $y$ does not conform well to the data and should be excluded from the prediction set. Conversely, when $S_{n+1}^y$ is among the smallest $\lceil(n+1)(1-\alpha)\rceil$ values of the combined list $\{S_1^y,\dots,S_{n+1}^y\},$ we deem $y$ sufficiently consistent and include it in our full conformal prediction set. Formally, letting

$$
\hat{q}^y 
\;=\; 
\text{Quantile}\bigl(S_1^y,\,S_2^y,\,\dots,\,S_n^y;\;(1-\alpha)(1 + 1/n)\bigr),
$$

we define

$$
\mathcal{C}(X_{n+1}) 
\;=\; 
\bigl\\{\,y\in\mathcal{Y} : S\_{n+1}^y \;\le\;\hat{q}^y \bigr\\}.
$$

In other words, $\mathcal{C}(X_{n+1})$ is exactly the set of hypothesized labels whose conformal score does not exceed the appropriate quantile of the $n$ scores from $\{(X_i,Y_i)\}\_{i=1}^n$. This construction intuitively inverts the score function: only those $y$ that are not "unreasonably large" compared to how well the existing points conform are allowed into the prediction set.

---

## Computing $\mathcal{C}(X_{n+1})$

In practice, the way one actually computes $\mathcal{C}(X_{n+1})$ depends on whether $\mathcal{Y}$ is discrete or continuous. When $\mathcal{Y}$ is a finite set (for example, in multiclass classification), one simply iterates through each label $y\in\mathcal{Y},$ forms $\mathcal{D}\_{n+1}^y,$ computes $\\{S_i^y\\}\_{i=1}^{n+1},$ finds the conformal quantile $\hat{q}^y,$ and includes $y$ precisely when $S_{n+1}^y \le \hat{q}^y$. In the continuous‐label case (e.g. regression), we cannot loop over uncountably many $y$. Instead, various strategies are used. For certain models—such as linear regression or LASSO—one can exploit analytic properties and compute 
$$
\\{\,y: S_{n+1}^y \le \hat q^y\\}
$$
directly.
A more brute‐force but generally applicable approach is to discretize the original label space $\mathcal{Y}$ and work with the newly constructed discrete label space. Section 9.2 of the book provides further details on this.

## Marginal Coverage for Full Conformal Prediction

Under the following two conditions—first, that

$$
(X_1,Y_1),\,\dots,\,(X_{n+1},Y_{n+1})
$$

is exchangeable, and second, that the score function $s$ is symmetric in its dataset argument—the full conformal set $\mathcal{C}(X_{n+1})$ satisfies the marginal coverage guarantee

$$
\Pr\bigl(Y_{n+1}\in\mathcal{C}(X_{n+1})\bigr) \ge 1-\alpha.
$$

We omit the proof here but it can be found on the slides and in the book. 

## Full Conformal Prediction Pseudocode

Below is the full conformal prediction routine in Python‐style pseudocode. It takes as input the observed training pairs `training_data`, a new feature vector `X_new`, a target miscoverage level `alpha`, a conformal `score_function`, and the label space `Y`. It outputs the prediction set `C`, consisting of all `y_candidate` whose score does not exceed the appropriate quantile of the calibration scores.

```python
def full_conformal_prediction(training_data, X_new, alpha, score_function, Y):
    C = set()
    n = len(training_data)

    for y_candidate in Y:
        D_aug = training_data.copy()
        D_aug.append((X_new, y_candidate))

        scores = []
        for (X_i, Y_i) in training_data:
            scores.append(score_function((X_i, Y_i), D_aug))

        score_new = score_function((X_new, y_candidate), D_aug)
        q = quantile(scores, (1 - alpha) * (1 + 1/n))

        if score_new <= q:
            C.add(y_candidate)

    return C
```

Full conformal gives exact coverage by retraining on every $(X_{n+1},y),$ but this can be expensive in practice. A more computationally efficient alternative is split conformal, where you explicitly choose a training set $\mathcal{D}\_{\text{train}}$ and a separate calibration set $\mathcal{D},$ fit the model once on $\mathcal{D}\_{\text{train}},$ and use $\mathcal{D}$ only to compute the calibration scores.

## Split Conformal Prediction Pseudocode

```python
def split_conformal_prediction(
    D_train,
    D,
    X_new,
    alpha,
    score_function,
    Y
):
    calib_scores = [
        score_function((X_i, Y_i), D_train)
        for (X_i, Y_i) in D_calib
    ]
    q = quantile(calib_scores, (1 - alpha) * (len(D) + 1))

    C = set()
    for y_candidate in Y:
        s_new = score_function((X_new, y_candidate), D)
        if s_new <= q:
            C.add(y_candidate)

    return C
```

Under exchangeability, this split conformal procedure still guarantees

$$
\Pr\bigl(Y_{n+1}\in\mathcal{C}(X_{n+1})\bigr)\;\ge\;1-\alpha,
$$

but requires only a single model fit on $\mathcal{D}\_{\text{train}}$ and straightforward calibration on $\mathcal{D}$.

## Full vs. Split Conformal: Trade-Offs

As we have seen, full conformal prediction uses every available data point both to train the model and to compute calibration scores. In practice, this means that for each candidate label $y,$ one must retrain $\hat f$ on the augmented dataset that includes $(X_{n+1},y)$. Because the score function $s\bigl((x,y);\mathcal{D}\bigr)$ is evaluated anew for each hypothetical $(X_{n+1},y),$ full conformal requires a symmetric score function and incurs a large computational cost whenever $\mathcal{Y}$ is large or continuous.

By contrast, split conformal divides the data into two disjoint subsets—one for fitting the model and one for calibration. After training $\hat f$ on the first portion, calibration scores are computed only once on the held-out subset, and the same quantile threshold is used to test all $y\in\mathcal{Y}$. Because no retraining is needed when evaluating different labels, split conformal greatly reduces computational effort and works with any (pretrained) score function $s$.

From a statistical perspective, however, full conformal enjoys an advantage: it leverages all $n$ observations both to fit $\hat f$ and to calibrate, yielding typically tighter prediction sets $\mathcal{C}(X_{n+1})$. Split conformal, which trains on only part of the data, often produces larger sets because less information is available during model fitting. In other words, split conformal is **computationally** more efficient (one model fit versus many), while full conformal is **statistically** more efficient (using all data for both training and calibration).


## Summary

In this post, we introduced conformal prediction under the sole assumption of exchangeability. We began by motivating the need for reliable uncertainty quantification—showing that even a high cross‐validated $R^2$ offers no formal guarantee at inference time. Conformal prediction remedies this by constructing a prediction set $\mathcal{C}(X_{n+1})\subseteq\mathcal{Y}$ that enjoys finite‐sample marginal coverage:

$$
\Pr\bigl(Y_{n+1}\in\mathcal{C}(X_{n+1})\bigr)\;\ge\;1-\alpha,
$$

without any distributional or model‐specific assumptions beyond exchangeability. We defined exchangeability (finite and infinite sequences) and saw intuitive examples—i.i.d. draws and sampling without replacement—where the joint law remains invariant under permutation.

We then introduced the central notion of a conformal score $s\bigl((x,y);\mathcal{D}\bigr),$ which measures how "nonconforming" a hypothetical label $y$ is at feature $x$ given dataset $\mathcal{D}$. Common choices include the absolute residual and the quantile‐based CQR score. In split conformal prediction, a single model is trained on half the data, calibration scores are computed on the other half, and the quantile of those scores determines the prediction set—requiring only one model fit. In full conformal prediction, we "invert" the score by hypothetically appending $(X_{n+1},y)$ to the entire dataset for each $y\in\mathcal{Y},$ computing all $n+1$ scores, and including those $y$ whose score is no larger than the appropriate quantile. Python‐style pseudocode was provided for both full and split conformal, with split conformal being computationally lighter yet still guaranteeing marginal coverage under exchangeability.

While this post distilled—and in some places almost verbatim reproduced—Section 3 of *Theoretical Foundations of Conformal Prediction*, the book[^1] goes much further. Chapters beyond Chapter 3 explore conditional coverage, a model‐based perspective on conformal prediction, and various extensions (e.g. weighted or cross-validation based methods). The authors Anastasios N. Angelopoulos, Rina Foygel Barber, and Stephen Bates also address whether conformal sets can be overly conservative and how to use conformal prediction under weaker or different assumptions.

[^1]: Angelopoulos, A. N., Foygel Barber, R., & Bates, S. (2020). _Conformal prediction under exchangeability_ (Chap. 3). In _Theoretical Foundations of Conformal Prediction_ (pp. 20–36). Cambridge University Press
