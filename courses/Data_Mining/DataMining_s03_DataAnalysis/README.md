<img width="103" height="39" alt="image" src="https://github.com/user-attachments/assets/c885dacd-16c3-4d8f-bf92-41c8d365f9ef" /><img width="115" height="39" alt="image" src="https://github.com/user-attachments/assets/3f04d806-f659-4540-a303-e7a4b7f60835" />
Part 1. Statistical Tests

Part 2. Correlation & Regression

Part 3. Clustering & Dimension Reduction


## Part 1. Statistical Tests

Learning Goal: Testing whether the “means” or “distributions” differ across groups**.

| Scenario  | Normality | Equal-variance | Recommended test | R hint |
|-----------|-----------|----------------|------------------|----------------------|
| Two groups | Normal    | Yes  | Student’s t-test | t.test(..., var.equal = TRUE) |
| Two groups | Normal    | No | Welch’s t-test | t.test(..., var.equal = FALSE) |
| Two groups | Non-normal | No | Wilcoxon rank-sum | wilcox.test() |
| ≥3 groups | Normal    | Yes | One-way ANOVA |  oneway.test(..., var.equal = TRUE) |
| ≥3 groups | Normal    | No | Welch ANOVA | oneway.test(..., var.equal = FALSE) |
| ≥3 groups | Non-normal | No | Kruskal–Wallis | kruskal.test() |


**Null Hypothesis (H0)**: A default statement that there is no effect, no difference, or no association in the population; any apparent effect in the data is due to random variation.

**P-Value**: The probability of obtaining a sample result as extreme as, or more extreme than, the one observed, assuming the null hypothesis is true.

**Normality**: Shapiro-Wilk test, shapiro.test()

**Equal-variance**: Levene Test, leveneTest() #library(car)









## Part 2. Correlation & Regression

## Part 3. Clustering & Dimension Reduction




