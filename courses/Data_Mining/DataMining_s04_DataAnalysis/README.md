[Part 1. Statistical Tests](#part-1-statistical-tests)

[Part 2. Correlation & Regression](#part-2-correlation-&-regression)

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

print('var(x):')
print(var(x))
print('var(x1):')
print(var(x1))
print('var(x2):')
print(var(x2))

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

### step04. Student's t-test

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)
x2=rnorm(1000)+2

x1_result=t.test(x,x1)
x2_result=t.test(x,x2)

print(x1_result)
print(x1_result$p.value)

print(x2_result)
print(x2_result$p.value)

pdf('dm_s04_step04.pdf',width=3,height=4)
boxplot(x,x1,x2,names=c('x','x1','x2'),
        col=c('grey','royalblue1','indianred3'),pch='+')
dev.off()

```

<br>

### step05. Student's t-test (non Equal-variance)

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)*2
x2=rnorm(1000)*2+2

x1_result=t.test(x,x1,var.equal=FALSE)
x2_result=t.test(x,x2,var.equal=FALSE)

print(x1_result)
print(x1_result$p.value)

print(x2_result)
print(x2_result$p.value)

pdf('dm_s04_step05.pdf',width=3,height=4)
boxplot(x,x1,x2,names=c('x','x1','x2'),
        col=c('grey','royalblue1','indianred3'),pch='+')
dev.off()

```

<br>

### step06. Wilcoxon Test 

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]
y=this_data[,2]

xy_result=wilcox.test(x,y)

print(xy_result)
print(xy_result$p.value)


pdf('dm_s04_step06.pdf',width=3,height=4)
plot(density(x),xlim=c(-4,4),ylim=c(0,1.5),lwd=3,col='black')
points(density(y),lwd=3,col='red',type='l')
dev.off()

```

<br>

### step07. One-way ANOVA

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)+2
x2=rnorm(1000)+4

this_input=c(x,x1,x2)
group=c( rep('x',length(x)),
         rep('x1',length(x1)),
         rep('x2',length(x2))
         )

this_result=oneway.test(this_input ~ group, var.equal = TRUE)

print(this_result)
print(this_result$p.value)

pdf('dm_s04_step07.pdf',width=3,height=4)
boxplot(x,x1,x2,names=c('x','x1','x2'),
        col=c('grey','royalblue1','indianred3'),pch='+')
dev.off()

```

<br>

### step08. One-way ANOVA (non Equal-variance)

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=rnorm(1000)*2+2
x2=rnorm(1000)*3+4

this_input=c(x,x1,x2)
group=c( rep('x',length(x)),
         rep('x1',length(x1)),
         rep('x2',length(x2))
         )

this_result=oneway.test(this_input ~ group, var.equal = FALSE)

print(this_result)
print(this_result$p.value)

pdf('dm_s04_step08.pdf',width=3,height=4)
boxplot(x,x1,x2,names=c('x','x1','x2'),
        col=c('grey','royalblue1','indianred3'),pch='+')
dev.off()

```

<br>

### step09. Kruskal Test

```r
this_data=read.table('this_data.csv', sep=',', header=TRUE, row.names=NULL)
print(head(this_data))

x=this_data[,1]

set.seed(321)
x1=(runif(1000)-0.5)*6
x2=(rbeta(1000,shape1=0.5,shape2=2)-0.5)*6

this_input=c(x,x1,x2)
group=c( rep('x',length(x)),
         rep('x1',length(x1)),
         rep('x2',length(x2))
         )

this_result=kruskal.test(this_input ~ group)

print(this_result)
print(this_result$p.value)

pdf('dm_s04_step09.pdf')
plot(density(x),xlim=c(-6,6),ylim=c(0,0.7),lwd=3,col='black')
points(density(x1),lwd=3,col='red',type='l')
points(density(x2),lwd=3,col='blue',type='l')
dev.off()

```

<br>
<br>
<br>


## Part 2. Correlation & Regression

## Part 3. Clustering & Dimension Reduction




