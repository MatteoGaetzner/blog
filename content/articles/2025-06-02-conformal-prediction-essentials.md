Title: Conformal Prediction Under Exchangeability
Date: 2025-06-02 12:00
Author: Matteo Gätzner
Category: Statistics
Tags: conformal-prediction, exchangeability
Summary: A quick introduction to the basics of conformal prediction under exchangeability.

Hey all! As the title suggests, this blog post is a short introduction to conformal prediction under exchangeability. It is based on Chapter 3 of the book _Theoretical Foundations of Conformal Prediction_, which Anna Kosovskaya, Sarah Medding, and I presented at the Conformal and Probabilistic Prediction Seminar, led by Prof. Dr. Johanna Ziegel, at ETH Zurich.[^1] 

Download the slide deck here: [Download the slides](../files/conformal-slides.pdf){:target="_blank"}.

## Uncertainty Quantification for Predictions

Say you have data points $(X_i, Y_i) \in \mathcal{X} \times \mathcal{Y}$. For a
regression task, that could mean $(X_i, Y_i) \in \mathbb{R}^d \times
\mathbb{R}$. A common task is to then predict unknown label $Y_{n+1}$ given known
input $X_{n+1}$ using some predictive model $\hat{f}(X_{n+1})$ that could for
example be a neural network, linear model or a smoothing spline.

## References

[^1]: Angelopoulos, A. N., Foygel Barber, R., & Bates, S. (2020). _Conformal prediction under exchangeability_ (Chap. 3). In _Theoretical Foundations of Conformal Prediction_ (pp. 20–36). Cambridge University Press
