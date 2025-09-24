
## Section 1. Introduction to Simple Statistical Tests

---

## 1. Checking Data Distribution

### 1.1 Basic Histogram Plotting
```r
# Create sample data
heights <- c(165, 170, 172, 168, 175, 169, 180, 167, 173, 171)

# Basic histogram
hist(heights)
```

- `hist()` creates frequency distribution visualization
- Default breaks may vary - we'll learn to customize later

---

### 1.2 Customizing Histograms
```r
# Add colors and labels
hist(heights,
     col = "lightblue",
     main = "Height Distribution",
     xlab = "Height (cm)",
     breaks = 5)
```

- `col` controls bar colors
- `main` adds title
- `breaks` specifies number of bins

---

## 2. Normality Checking

### 2.1 Shapiro-Wilk Test Basics
```r
# Generate normal data
normal_data <- rnorm(50)

# Generate non-normal data
non_normal <- rexp(30)

# Perform tests
shapiro.test(normal_data)
shapiro.test(non_normal)
```

- p-value > 0.05 suggests normal distribution
- Always check normality before parametric tests

---

## 3. Independent t-test

### 3.1 Preparing mtcars Data
```r
# View mtcars structure
head(mtcars)

# Split data by cylinders
mpg_4cyl <- mtcars[mtcars$cyl == 4, "mpg"]
mpg_6cyl <- mtcars[mtcars$cyl == 6, "mpg"]
```

- We're comparing 4-cylinder vs 6-cylinder cars
- Always check data structure before analysis

---

### 3.2 Performing t-test
```r
# Independent t-test
t_result <- t.test(mpg_4cyl, mpg_6cyl)
print(t_result)

# Check p-value
t_result$p.value
```

- Null hypothesis: No difference in means
- Alternative hypothesis: Means are different

---

## 4. Paired t-test Example

### 4.1 Simulating Blood Pressure Data
```r
# Simulate data
before <- round(rnorm(20, 130, 10))
after <- before - rnorm(20, 8, 3)

# Create data frame
bp_data <- data.frame(before, after)
```

- Simulated "before treatment" and "after treatment" measurements
- Paired data requires matching observations

---

### 4.2 Running Paired Test
```r
# Paired t-test
t.test(bp_data$before, bp_data$after, paired = TRUE)

# Calculate differences
diff <- bp_data$after - bp_data$before
hist(diff)
```

- `paired = TRUE` is crucial parameter
- Always visualize differences

---

## 5. Non-parametric Testing

### 5.1 Wilcoxon Test with Iris Data
```r
# Extract data
setosa <- iris[iris$Species == "setosa", "Petal.Width"]
versicolor <- iris[iris$Species == "versicolor", "Petal.Width"]

# Wilcoxon Rank Sum test
wilcox.test(setosa, versicolor)
```

- Alternative to t-test when normality fails
- Compares medians rather than means

---

### 5.2 Understanding Wilcoxon Results
```r
# Store and examine results
wilcox_result <- wilcox.test(setosa, versicolor)
names(wilcox_result)

# Check test statistic and p-value
wilcox_result$statistic
wilcox_result$p.value
```

- W statistic measures difference in ranks
- p-value interpretation same as t-test

---

<br>
<br>
<br>
<br>
<br>

## Section 2. Linear Regression Basics 

---

### **1. What is Linear Regression?**
- Simple mathematical relationship between variables  
- Example:  
  ```r
  # Advertising budget vs Sales (simulated)
  set.seed(123)
  ad_spend <- seq(100, 1000, by=100)
  sales <- 50 + 0.7*ad_spend + rnorm(10, 0, 30)
  ```

---

### **2. Creating a Linear Model**
- Using `lm()` function:  
  ```r
  model <- lm(sales ~ ad_spend)
  ```
- What each part means:  
  - `sales`: Dependent variable (what we predict)  
  - `ad_spend`: Independent variable (what we use to predict)  

---

### **3. Understanding Model Output**
- View basic results:  
  ```r
  summary(model)
  ```
- Key elements to check:  
  ```markdown
  1. Coefficients Estimate
  2. R-squared: 0-1 (Goodness of fit)
  3. p-value: <0.05 means significant
  ```

---

### **4. Visualizing Relationships**
- Basic plot with regression line:  
  ```r
  plot(ad_spend, sales, pch=19, col="blue",
       main="Ad Spending vs Sales")
  abline(model, col="red", lwd=2)
  ```
- Add labels and grid:  
  ```r
  grid()
  text(800, 400, paste("y =", 
       round(coef(model)[2],2),"x +",
       round(coef(model)[1],2)))
  ```

---

### **5. Residual Analysis Basics**
- What are residuals?  
  ```r
  residuals <- model$residuals
  ```
- Four diagnostic plots:  
  ```r
  par(mfrow=c(2,2))
  plot(model)
  par(mfrow=c(1,1))
  ```

---

### **6. Understanding Residual Plots**
1. **Residuals vs Fitted**: Check pattern randomness  
2. **Q-Q Plot**: Check normality assumption  
3. **Scale-Location**: Check equal variance  
4. **Residuals vs Leverage**: Identify outliers  

---

### **7. Practical Interpretation**
- Real-world example:  
  ```r
  # If coefficient is 0.72:
  cat("For every $1 increase in ad spending,
      sales increase by", 0.72*100, "units")
  ```
- Remember:  
  "Correlation ≠ Causation"  
  Always check practical significance!

---

<br>
<br>
<br>
<br>
<br>

---
## Section 3. PCA Dimension Reduction


## Why Dimension Reduction?

> "PCA helps simplify complex data while preserving patterns"

---

## Step 1: Data Standardization

### Why normalize?
- Ensures equal feature contribution
- Prevents scale-based bias

```R
# Original iris data (first 2 rows)
head(iris[,1:4], 2)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width
# 1          5.1         3.5          1.4         0.2
# 2          4.9         3.0          1.4         0.2

# Standardized data
scaled_iris <- scale(iris[,1:4])
head(scaled_iris, 2)
#      Sepal.Length Sepal.Width Petal.Length Petal.Width
# [1,]   -0.8976739  1.01560199    -1.335752   -1.311052
# [2,]   -1.1392005 -0.13153881    -1.335752   -1.311052
```

---

# PCA Core Function: prcomp()

### Essential parameters
```R
pca <- prcomp(
  x = scaled_iris,    # Standardized data
  center = FALSE,     # Already centered by scale()
  scale. = FALSE      # Already scaled
)
```

### Key outputs
```R
names(pca)
# [1] "sdev"     "rotation" "center"   "scale"    "x"
```

---

# Exploring PCA Results

### Principal components matrix
```R
pc_scores <- pca$x[,1:2]
head(pc_scores)
#            PC1        PC2
# [1,] -2.257141 -0.4784238
# [2,] -2.074013  0.6718827
# [3,] -2.356335  0.3407664
```

### Component relationships
```R
summary(pca)
# Importance of components:
#                          PC1    PC2     PC3     PC4
# Standard deviation     1.7084 0.9560 0.38309 0.14393
# Proportion of Variance 0.7296 0.2285 0.03669 0.00518
```

---

# Visualizing Species Separation

### Basic color coding
```R
plot(pc_scores, 
     col = c("red","green","blue")[iris$Species],
     pch = 19, main = "PCA: Iris Species")
```

### Adding legend
```R
legend("topright", legend=levels(iris$Species),
       fill=c("red","green","blue"), cex=0.7)
```

---

# Variance Explained Plot

### Simple barplot
```R
barplot(pca$sdev^2, 
        names.arg = paste0("PC",1:4),
        main = "Variance per Component",
        ylab = "Variance",
        col = "skyblue")
```

### Adding percentage labels
```R
variance_percent <- round(pca$sdev^2/sum(pca$sdev^2)*100, 1)
text(1:4, pca$sdev^2, labels=paste0(variance_percent,"%"), pos=3)
```

---

# PCA Interpretation Tips

1. PC1 captures maximum variation (72.96%)
2. Distinct species clustering visible
3. First two PCs explain 95.81% variance
4. Petal features dominate PC1 (check rotation matrix)

```R
pca$rotation[,1]
# Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
#   0.5210659   -0.2693474    0.5804131    0.5648565 
```

---

# Final PCA Workflow

```R
# 1. Standardize data
scaled_data <- scale(raw_data)

# 2. Run PCA
my_pca <- prcomp(scaled_data)

# 3. Extract components
components <- my_pca$x[,1:2]

# 4. Visualize
plot(components, col=groups)
barplot(my_pca$sdev^2)
```
---

</br>
</br>
</br>
</br>
</br>

## Section 4. K-means Clustering in Practice



## Today's Roadmap
1. Prepare data for clustering
2. Perform K-means clustering
3. Validate our results
4. Visualize outcomes

---

## Meet Our Dataset: Iris Flowers
```{r}
head(iris)
# Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1          5.1         3.5          1.4         0.2  setosa
# 2          4.9         3.0          1.4         0.2  setosa
```

We'll use:
- Petal.Length (3rd column)
- Petal.Width (4th column)

---

## Why We Need Data Scaling
Different scales can distort distances:
```{r}
summary(iris[,3:4])
# Petal.Length    Petal.Width   
# Min.   :1.000   Min.   :0.100  
# Max.   :6.900   Max.   :2.500
```

Let's standardize:
```{r}
scaled_data <- scale(iris[,3:4])
head(scaled_data)
```

---

## Meet kmeans() Function
Basic syntax:
```{r}
kmeans(x, centers, nstart)
```

Let's make 3 clusters:
```{r}
set.seed(123)
km_result <- kmeans(scaled_data, centers=3, nstart=10)
```

---

## Understanding kmeans() Output
Key components:
```{r}
names(km_result)
# [1] "cluster"      "centers"      "totss"        "withinss"    
# [5] "tot.withinss" "betweenss"    "size" 

km_result$size
# [1] 50 53 47
```

---

## The Elbow Method Explained
How to find optimal clusters:
1. Calculate SSE (Sum of Squared Errors) for different k values
2. Look for "elbow" bend point

```{r}
sse <- numeric(10)
for(k in 1:10){
    km <- kmeans(scaled_data, k)
    sse[k] <- km$tot.withinss
}
```

---

## Visualizing the Elbow
```{r}

plot(c(1:k), sse, type = "b", pch = 19, col = "steelblue",
     main = "Elbow Method Visualization",
     xlab = "Number of Clusters (k)",
     ylab = "Total Within-Cluster SSE")
grid()

```

---

## Reality Check: Clusters vs Species
Compare our clusters with actual species:
```{r}
table(Cluster=km_result$cluster, Species=iris$Species)
#        Species
# Cluster setosa versicolor virginica
#      1     50          0         0
#      2      0         23        30
#      3      0         27        20
```

---

## Visualizing Clusters (Part 1)
Color = Cluster, Shape = Species:
```{r}
plot_data <- data.frame(scaled_data, 
                       Cluster=factor(km_result$cluster),
                       Species=iris$Species)


colors <- c("red", "blue", "green", "orange", "purple")
shapes <- c(1, 2, 3)
cluster_colors <- colors[as.numeric(as.factor(plot_data$Cluster))]
species_shapes <- shapes[as.numeric(as.factor(plot_data$Species))]

plot(plot_data$Petal.Length, plot_data$Petal.Width,
     col = cluster_colors,
     pch = species_shapes,
     xlab = "Petal Length",
     ylab = "Petal Width",
     main = "Petal.Length vs Petal.Width by Cluster & Species",
     cex = 1.5)  
```

---

## Visualizing Clusters (Part 2)
Add cluster centers:

```{r}


centers=km_result$centers

colors <- c("red", "blue", "green", "orange", "purple")
shapes <- c(1, 2, 3)
cluster_colors <- colors[as.numeric(as.factor(plot_data$Cluster))]
species_shapes <- shapes[as.numeric(as.factor(plot_data$Species))]

plot(plot_data$Petal.Length, plot_data$Petal.Width,
     col = cluster_colors,
     pch = species_shapes,
     xlab = "Petal Length",
     ylab = "Petal Width",
     main = "Petal.Length vs Petal.Width by Cluster & Species",
     cex = 1.5)  

points(centers[,1], centers[,2],
       col = "black",
       pch = 8,     
       cex = 2.5)   
```

---

</br>
</br>
</br>
</br>
</br>

## Section 5. Play with Gene-expression Data

### 1: Welcome to Gene Expression Analysis! 🧬
**Learning Objectives:**
- Create simulated gene expression data
- Perform differential expression analysis
- Visualize results with volcano plots

---

### 2: Let's Make Fake Genes! 🧪
**Why simulate data?**
- Safe way to learn analysis
- Full control over parameters

```R
# Create 100 genes with 2 samples each
gene_data <- matrix(rnorm(600), ncol=6)
```

---

### 3: Peek at Our Data 🔍
**What does our matrix look like?**
```R
# First 5 rows
gene_data[1:5, ]
#       [,1]   [,2]
# [1,] 0.123 -1.234
# [2,] 1.456  0.789
# [3,] -0.345 2.101
# [4,] ...    ...
```

---

### 4: Name Your Samples 🏷️
**Add meaningful labels:**
```R
colnames(gene_data) <- c("c1",'c2','c3', 't1','t2','t3')
rownames(gene_data) <- paste("Gene", 1:100, sep="_")
```

---

### 5: The Magic of apply() ✨
**Run t-tests for all genes:**
```R
p_values <- apply(gene_data, 1, function(x) {
  t.test(x[c(1:3)], x[c(4:6)])$p.value
})
```

---

### 6: Fix Those P-values! 
**Multiple testing correction:**
```R
adj_p <- p.adjust(p_values, method="BH")
head(adj_p)
# Gene_1   Gene_2   Gene_3   Gene_4   Gene_5 
# 0.845    0.123    0.056    0.734    0.912
```

---

### 7: Calculate Fold Changes 
**Compute log2 differences:**
```R
logFC <- apply(gene_data[,c(1:3)],1,mean) - apply(gene_data[,c(4:6)],1,mean)
results <- data.frame(logFC, p_values, adj_p)
```

---

### 8: Make It Pretty with Colors 
**Prepare for volcano plot:**
```R
results$color = rep('grey',nrow(gene_data))
results$color[which(results$p_values<0.1)]='blue'
results$color[which(results$adj_p<0.1)]='red'
```

---

### 9: Let's Paint Volcanoes! 
**Basic volcano plot:**
```R
plot(results$logFC, -log10(results$adj_p),
     col = results$color, pch = 16,
     xlab = "log2 Fold Change", 
     ylab = "-log10(adjusted p-value)")
```

---

### 10: Volcano Upgrade 
**Add finishing touches:**
```R
abline(h = -log10(0.05), col = "blue", lty=2)
abline(v = c(-1,1), col = "green", lty=2)
title("Differential Expression Results")
```

---


