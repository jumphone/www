# Matrix


# Section 1. Matrix

### Basic Characteristics
- **2D structure** with rows and columns
- Contains **same data type** elements
- Example matrix:

```r

this_mat = matrix(c(1:9),ncol=3)
this_mat

     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

---

## Matrix vs Vector vs List

### Key Differences

| Type      | Dimensions | Data Types     |
|-----------|------------|----------------|
| Vector    | 1D         | Single type    |
| List      | Mixed      | Multiple types |
| Matrix    | 2D         | Single type    |

### Example Comparison
```r
my_vector <- 1:9       # 1D
my_matrix <- matrix(1:9, nrow=3)  # 2D
my_list <- list(c(1,2,3), "a", TRUE)     # Mixed types
```

---

## Method 1: matrix() Function

### Basic Syntax
```r
matrix(data, nrow, ncol, byrow)
```

### Example 1 - Default
```r
matrix(1:6, nrow=2)
# Output:
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6
```

---

## byrow Parameter

### Column-wise vs Row-wise
```r
# Column-wise (default)
matrix(1:4, nrow=2) 

# Row-wise
matrix(1:4, nrow=2, byrow=TRUE)
```

### Visual Comparison
```
Default:       byrow=TRUE:
1 3            1 2
2 4            3 4
```

---

## Method 2: Vector to Matrix

### Dimension Assignment
```r
my_vector <- c(5,3,9,1,6,4)
dim(my_vector) <- c(2,3)
```

### Result
```r
     [,1] [,2] [,3]
[1,]    5    9    6
[2,]    3    1    4
```

---

## Method 3: Row/Column Binding

### rbind() for Rows
```r
rbind(c(1,2,3), c(4,5,6))
# Output:
#      [,1] [,2] [,3]
# [1,]    1    2    3
# [2,]    4    5    6
```

### cbind() for Columns
```r
cbind(c(1,4), c(2,5), c(3,6))
```

---

## Method 4: Random Matrices

### Normal Distribution
```r
matrix(rnorm(4), nrow=2)
# Example output:
#            [,1]       [,2]
# [1,] -0.5604756 -0.9957987
# [2,] -0.2301775  1.0670417
```

---

## Matrix Properties: Dimensions

### Check Structure
```r
my_matrix <- matrix(1:12, nrow=3)
dim(my_matrix)   # Returns c(3,4)
nrow(my_matrix)  # Returns 3
ncol(my_matrix)  # Returns 4
```

---

## Matrix Properties: Naming

### Add Row/Column Names
```r
rownames(my_matrix) <- c("Alice", "Bob", "Charlie")
colnames(my_matrix) <- c("Math", "Science", "History", "Art")
```

### Result
```r
         Math Science History Art
Alice       1       4       7  10
Bob         2       5       8  11
Charlie     3       6       9  12
```

---

### Create Student Grade Matrix

## Question: NROW ? BYROW ? 

```r

student_grade= c(85, 90, 78, 92, 88, 95, 76, 89, 92)
student_name= c('Alice','Alice','Alice','Bob','Bob','Bob','Carol','Carol','Carol')
subject_name = c('Math','Biology','English','Math','Biology','English','Math','Biology','English') 

NROW = ?
BYROW = ? 

grades <- matrix(student_grade,  nrow=NROW, byrow=BYROW)

rownames(grades) <- c("Alice", "Bob", "Carol")
colnames(grades) <- c("Math", "Bio", "Chem")
```

### Final Result
```r
      Math Bio Chem
Alice   85  90   78
Bob     92  88   95
Carol   76  89   92
```


<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">


---

# Section 2. Matrix Operations in R

---

## 1. Creating Matrices
Basic matrix creation example:
```r
# Create a 2x3 matrix
my_matrix <- matrix(1:6, nrow=2)
print(my_matrix)
```
Output:
```
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
```

---

## 2. Accessing Elements
### Basic Indexing
```r
# Get element at 2nd row, 3rd column
my_matrix[2, 3]

# Get entire first row
my_matrix[1, ]

# Get first and third columns
my_matrix[, c(1,3)]
```

---

## 3. Conditional Filtering
Extract elements meeting conditions:
```r
# Create temperature matrix
temps <- matrix(c(22, 25, 18, 30, 15, 28), nrow=2)

# Find temperatures > 25
hot_days <- temps[temps > 25]
print(hot_days)  # Output: 30 28

```

---

## 4. Merging Matrices
### Row Binding (rbind)
```r
classA <- matrix(c(80, 75, 90), nrow=1)
classB <- matrix(c(88, 82, 95), nrow=1)

combined <- rbind(classA, classB)
```

---

## 5. Merging Matrices
### Column Binding (cbind)
```r
quiz_scores <- matrix(c(15, 18, 20), ncol=1)
exam_scores <- matrix(c(45, 48, 50), ncol=1)

full_scores <- cbind(quiz_scores, exam_scores)
```

---

## 6. Matrix Splitting
Extract matrix subsets:
```r
# Original 4x4 matrix
big_matrix <- matrix(1:16, nrow=4)

# Extract first two rows
top_section <- big_matrix[1:2, ]
```

---

## 7. Basic Math Operations
Element-wise operations:
```r
# Create two matrices
m1 <- matrix(1:4, nrow=2)
m2 <- matrix(5:8, nrow=2)

# Element-wise multiplication
m1 * 2

# Matrix addition
m1 + m2
```

---

## 8. Row & Column Operations
Calculate totals and averages:
```r
# Student score matrix
scores <- matrix(c(80,75,90, 85,88,92), nrow=2)

# Calculate total scores
rowSums(scores)

# Calculate subject averages
colMeans(scores)
```

---

## 9. Transposition
Flip matrix dimensions:
```r
# Original gene matrix (genes x samples)
gene_matrix <- matrix(rnorm(9), nrow=3)

# Transposed matrix (samples x genes)
t(gene_matrix)
```

---

## 10. Dimension Adjustment
Reshaping matrices:
```r
# Original 2x3 matrix
original <- matrix(1:6, nrow=2)

# Reshape to 3x2
dim(original) <- c(3,2)
```

---

## Summary
- Matrix indexing starts at [1,1]
- Use rbind/cbind for combining data
- rowSums/colMeans for quick statistics
- Transpose with t() for different perspectives



---
<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 3. apply()

## What is apply()?
- Simplifies matrix/array operations
- Avoid writing loops manually
- Basic syntax:

  ```r
  apply(matrix, margin, function)
  ```
  
- `margin=1`: row-wise
- `margin=2`: column-wise

---

## apply() Example 1: Sum Rows
Create a score matrix:
```r
scores <- matrix(c(80, 90, 75, 
                   85, 88, 92, 
                   78, 85, 90), ncol=3)
colnames(scores) <- c("Math", "Science", "English")
```

Calculate row sums:
```r
apply(scores, 1, sum)
```
Output:
```
[1] 245 265 253
```

---

## apply() Example 2: Find Max Columns
Same score matrix:
```r
scores
```
```
     Math Science English
[1,]   80      85      78
[2,]   90      88      85
[3,]   75      92      90
```

Find column maxima:
```r
apply(scores, 2, max)
```
```
   Math Science English 
     90      92      90 
```

---

## lapply(): List Processor
Works on **lists/vectors**:
```r
student_ages <- list(c(18,19,20), c(21,22,19))
```

Calculate average ages:
```r
lapply(student_ages, mean)
```
Output:
```
[[1]]
[1] 19

[[2]]
[1] 20.66667
```

---

## sapply(): Simplified Output
Same age data:
```r
student_ages <- list(c(18,19,20), c(21,22,19))
```

Get simplified vector:
```r
sapply(student_ages, mean)
```
Output:
```
[1] 19.00000 20.66667
```

---

## Compare lapply vs sapply
Input list:
```r
weather <- list(rainy_days = c(3,5,2), 
                sunny_days = c(8,6,7))
```

lapply output:
```r
[[1]]
[1] 3.333333

[[2]]
[1] 7
```

sapply output:
```r
rainy_days sunny_days 
  3.333333   7.000000 
```

---

## tapply(): Group Statistics
Create sample data:
```r
classes <- c("A", "B", "A", "B")
exam_scores <- c(88, 92, 85, 90)
```

Calculate class averages:
```r
tapply(exam_scores, classes, mean)
```
Output:
```
  A   B 
86.5 91.0 
```

---

## Real Case: Gene Matrix
Create sample data:
```r
gene_expr <- matrix(rnorm(15, mean=50, sd=10), 
                   nrow=5)
rownames(gene_expr) <- paste("Gene", 1:5)
```

Show matrix:
```r
          [,1]     [,2]     [,3]
Gene 1 52.3     48.7     55.1
Gene 2 61.8     43.2     59.4
...
```

---

## Z-score Standardization
Calculate row-wise Z-scores:
```r
getZ = function(x){
    z=(x - mean(x)) / sd(x)
    return(z)}

z_scores <- apply(gene_expr, 1,  getZ)
```

Transpose the result:
```r
z_scores <- t(z_scores)
```

Final matrix:
```r
          [,1]    [,2]    [,3]
Gene 1  0.12   -0.45    0.33
Gene 2  0.87   -1.02    0.15
...
```

---
## Question: how can we get the averaged expression level (original value) of each gene?
## Question: how can we find the highest z-score of each gene?



---

# Summary Table

| Function | Input      | Output     | Best For          |
|----------|------------|------------|-------------------|
| apply()  | Matrix     | Matrix      | 2D calculations |
| lapply() | List/Vector| List       | Multiple objects |
| sapply() | List/Vector| Vector     | Clean results   |
| tapply() | Vector     | Vector     | Group analysis |

---




<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">



---

# Section 4. Using which() for Matrix Operations in R

---

## What is which()?  
- Finds positions where condition is TRUE  
- Works with vectors, matrices, and arrays  
- Returns numeric indices  

```r
# Simple vector example
scores <- c(78, 92, 85, 100, 65)
which(scores == 100)  # Returns 4
```

---

## which.max() - Find Maximum  
- Fast way to find highest value position  

```r
exam_scores <- matrix(c(80, 92, 75, 
                       100, 88, 82,
                       73, 95, 67), ncol=3)
                       
which.max(exam_scores)  # Returns position 4 (value 100)
```

---

## Basic Position Finding  
- Find exact matches in matrix  

```r
# Create sample score matrix
mat <- matrix(c(80, 100, 75,
               100, 85, 90,
               95, 88, 100), nrow=3)

# Find all perfect scores
perfect <- which(mat == 100)
print(perfect)  # Returns positions 2, 4, 9
```

---

## Combined Conditions  
- Use logical operators: & (AND), | (OR)  

```r
# Students with math >80 AND english <60
math_scores <- c(85, 92, 78, 88)
english_scores <- c(55, 58, 72, 61)

which(math_scores > 80 & english_scores < 60)
# Returns positions 1 and 2
```

---

## Matrix Filter Example  
- Find students with total score >250  

```r
# Create score matrix (5 students x 3 subjects)
student_scores <- matrix(c(80, 75, 90,
                          92, 88, 85,
                          78, 82, 95,
                          85, 90, 88,
                          90, 92, 94), nrow=5, byrow=TRUE)

# Get row indices where sum >250
good_students <- which(rowSums(student_scores) > 250)
print(good_students)  # Returns 2,3,4,5
```

---

## Creating Sub-matrices  
- Extract rows meeting criteria  

```r
# Continue from previous matrix
high_scores <- student_scores[which(rowSums(student_scores) > 250), ]
print(high_scores)
# Shows rows for students 2,3,4,5
```

---

## Real-world Application  
- Filter experimental data  

```r
# Gene expression matrix (genes x samples)
gene_data <- matrix(rnorm(100, mean=10), ncol=5)
rownames(gene_data)=paste0('gene',c(1:20))

```
## Question: how can we find genes with high expression (>10) in all samples ?
## Hint: use "min()"


<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

---

# Section 5. R Programming Practical Cases

---
## Case 1: Student Grade Analysis System

### Step 1: Create Grade Matrix
```r
# Create matrix with 5 students' scores for 3 subjects
grades <- matrix(c(85, 92, 78,
                   90, 95, 88,
                   78, 89, 92,
                   95, 91, 87,
                   82, 93, 84), 
                 nrow = 5, byrow = TRUE)
colnames(grades) <- c("Math", "Science", "English")
rownames(grades) <- paste("Student", 1:5)
```

---
### Step 2: Calculate Total Scores
```r
# Using apply() to calculate row sums
total_scores <- apply(grades, 1, sum)
names(total_scores) <- rownames(grades)
total_scores
```
**Output:**  
```
 Student 1 Student 2 Student 3 Student 4 Student 5 
      255       273       259       273       259
```

---
### Step 3: Calculate Average Scores
```r
# Using apply() with mean function
average_scores <- apply(grades, 1, mean)
round(average_scores, 1) # round to 1 decimal place
```
**Output:**  
```
Student 1 Student 2 Student 3 Student 4 Student 5 
     85.0      91.0      86.3      91.0      86.3 
```

---
### Step 4: Find Math High Achievers
```r
# Using which() to find high scorers
math_scores <- grades[, "Math"] # or grades[,1]
top_math <- which(math_scores >= 90)
grades[top_math, ]
```
**Output:**  
```
          Math Science English
Student 2   90      95      88
Student 4   95      91      87
```

---
## Case 2: Gene Expression Data Cleaning

### Step 1: Create Simulation Data
```r
# Generate 100 genes x 10 samples matrix
set.seed(123)
gene_expr <- matrix(rnorm(1000, mean = 7, sd = 3), 
                    nrow = 100)
colnames(gene_expr) <- paste("Sample", 1:10)
rownames(gene_expr) <- paste("Gene", 1:100)
```

---
### Step 2: Filter Low Expression Genes
```r
# Calculate row means and filter
row_means <- apply(gene_expr, 1, mean)
high_expr_genes <- gene_expr[row_means > 7, ]
dim(high_expr_genes)
```
**Output:**  
```
[1] 52 10  # 52 genes remaining
```

---
### Step 3: Log2 Transformation
```r
# Apply log2 transformation column-wise

log2trans<-function(x){
    result=log2(x + 1)
    return(result)
    }
log2_expr <- apply(high_expr_genes, 2, log2trans)
head(log2_expr[, 1:3])
```

---
### Step 4: Find Top Expressed Genes
```r
# Find top 10 genes by mean expression
top10_idx <- order(row_means, decreasing = TRUE)[1:10]
gene_expr[top10_idx, 1:3]  # Show first 3 samples
```

## Question: what's the function of "order()" ? 
## Question: please check the function of "rank()" after class.

---
## Key Functions Recap
`apply()`:  
- `MARGIN = 1` for row operations  
- `MARGIN = 2` for column operations  

`which()`:  
- Returns indices meeting conditions  
- Works with matrices and vectors  

`rbind()`:  
- Combine matrices vertically  
- Ensure same number of columns

