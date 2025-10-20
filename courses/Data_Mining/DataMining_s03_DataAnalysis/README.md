
Part 1. Statistical Tests

Part 2. Correlation & Regression

Part 3. Clustering & Dimension Reduction


## Part 1. Statistical Tests


| Scenario  | Normality | Equal-variance | Recommended test | R hint |
|-----------|-----------|----------------|------------------|----------------------|--------|
| **Two groups** | Normal    | Yes  | Student’s t-test | `t.test(..., var.equal = TRUE)` |
| **Two groups** | Normal    | No | Welch’s t-test | `t.test(..., var.equal = FALSE)` |
| **Two groups** | Non-normal | No | Wilcoxon rank-sum | `wilcox.test()` |
| **≥3 groups** | Normal    | Yes | One-way ANOVA |  `oneway.test(..., var.equal = TRUE)` |
| **≥3 groups** | Normal    | No | Welch ANOVA | `oneway.test(..., var.equal = FALSE)` |
| **≥3 groups** | Non-normal | No | Kruskal–Wallis | `kruskal.test()` |





## Part 2. Correlation & Regression

## Part 3. Clustering & Dimension Reduction




