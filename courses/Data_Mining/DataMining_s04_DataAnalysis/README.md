Part 1. Statistical Tests

Part 2. Correlation & Regression

Part 3. Clustering & Dimension Reduction


<br>
<br>


## Part 1. Statistical Tests

Learning Goal: Testing whether the “means” or “distributions” differ across groups.

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

<br>

### step01. Generate Random Data

```r
set.seed(123)
x = rnorm(1000) # generate 1000 values following normal distribution
y = runif(1000) # generate 1000 values following uniform distribution

pdf('dm_s04_step01.pdf')
hist(x)
hist(y)
dev.off()

this_data=cbind(x,y)
write.table(this_data, file='this_data.csv',sep=',',quote=FALSE,row.names=FALSE,col.names=TRUE)

```

<br>

### step02. Normality Test


```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]
y=this_data[,2]

x_result=shapiro.test(x)
y_result=shapiro.test(y)

print(x_result)
print(x_result$p.value)

print(y_result)
print(y_result$p.value)
```

<br>


### step03. Equal-variance Test


```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)+2
x2=rnorm(1000)*2

group1=as.factor( c( rep('x',length(x)), rep('x1',length(x1)) ) )
x1_result = car::leveneTest( c(x,x1), group=group1 )

group2=as.factor( c( rep('x',length(x)), rep('x2',length(x2)) ) )
x2_result = car::leveneTest( c(x,x2), group=group2 )

print(x1_result)
print(x1_result$'Pr(>F)'[1])

print(x2_result)
print(x2_result$'Pr(>F)'[1])


pdf('dm_s04_step03.pdf')
plot(density(x),xlim=c(-6,6),lwd=3,col='black')
points(density(x1),lwd=3,col='red',type='l')
points(density(x2),lwd=3,col='blue',type='l')
dev.off()

```

<br>

### step03. Student's t-test


```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)+2
x2=rnorm(1000)*2

group1=as.factor( c( rep('x',length(x)), rep('x1',length(x1)) ) )
x1_result = car::leveneTest( c(x,x1), group=group1 )

group2=as.factor( c( rep('x',length(x)), rep('x2',length(x2)) ) )
x2_result = car::leveneTest( c(x,x2), group=group2 )

print(x1_result)
print(x1_result$'Pr(>F)'[1])

print(x2_result)
print(x2_result$'Pr(>F)'[1])


pdf('dm_s04_step03.pdf')
plot(density(x),xlim=c(-6,6),lwd=3,col='black')
points(density(x1),lwd=3,col='red',type='l')
points(density(x2),lwd=3,col='blue',type='l')
dev.off()

```





## Part 2. Correlation & Regression

## Part 3. Clustering & Dimension Reduction




