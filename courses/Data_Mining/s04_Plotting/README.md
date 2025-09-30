# Plotting


# Section 1. R Graphics Fundamentals

---

## Why Learn R Graphics?
- Visualize data patterns
- Create publication-quality figures
- Master fundamental plotting techniques

---

## Basic Workflow (3 Steps)

### 1. Create Canvas
```r
png("my_plot.png")
# or
pdf("my_plot.pdf")
```

---

### 2. Draw Graphics
```r
plot(1,1)
plot(c(1,2),c(2,3))
boxplot(rnorm(10),rnorm(10))
```

---

### 3. Save Output
```r
# Save 

dev.off()

```

---

## Graphic Devices

### Screen Preview
```r
plot(rnorm(100))  # Automatically displays in RStudio
```

### File Saving
```r
pdf("output.pdf")  # Start PDF device
hist(mtcars$mpg)   # Draw plot
dev.off()          # Save file
```

---

## Color Parameter (`col`)

### Basic Usage
```r
plot(1:5, col=c("red","green","blue","cyan","magenta"), pch=16, cex=3)
```
- Named colors: "red", "blue", etc
- RGB: `col="#FF0000"` for pure red

---

## Point Shapes (`pch`)

### Common Shapes
```r
# Plot different point styles
plot(1:6, rep(1,6), pch=16:21, col=rainbow(6), cex=3)
```
- Numbers 0-25 = different shapes
- 16= filled circle, 17=filled triangle

---

## Line Types (`lty`)

### Basic Patterns
```r
# Create empty plot
plot(1, type="n", xlim=c(0,6), ylim=c(0,7))

# Draw different lines
for(i in 1:6) {
  abline(h=i, lty=i-1, lwd=2)
}
```

---

## Parameter Combination

### Customized Plot
```r
plot(mtcars$wt, mtcars$mpg,
     col=ifelse(mtcars$am==1, "red", "blue"),
     pch=ifelse(mtcars$cyl==4, 16, 17),
     lty=2)
```

## Question: how to draw this plot using "if ... else ..." ?

---

## Key Takeaways
1. Always follow: Create → Draw → Save
2. Manage devices properly
3. Master basic parameters: col/pch/lty

---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">


# Section 2. Basic Plotting with plot()

---

## Today's Roadmap
1. Basic usage of `plot()`
2. Controlling graph types with `type` parameter
3. Live coding examples

---

### What is `plot()`?
- Simplest function to create graphs
- Works with vectors/data frames
- Automatically chooses axes ranges

```r
# Minimal example
plot(1:5)
```

---

### Scatterplot Basics (Numeric Vectors)
Create arithmetic sequence with `:` operator:
```r
x <- 1:10
y <- 1:10
plot(x, y)
```

---

### Formula Style Plotting
Use `y ~ x` syntax with datasets:
```r
# Using built-in mtcars data
plot(mpg ~ wt, data = mtcars)
```

---

### Understanding the `type` Parameter
Controls how points are displayed:

| Code | Meaning      |
|------|--------------|
| "p"  | Points       |
| "l"  | Lines        |
| "b"  | Both points and lines |

---

### Type "p" - Point Plot (Default)
```r
x <- 1:10
y <- rnorm(10)  # Random numbers
plot(x, y, type = "p")
```

---

### Type "l" - Line Plot
Connect points with lines:
```r
x <- seq(0, 2*pi, length=50)
y <- sin(x)
plot(x, y, type = "l")
```

---

### Type "b" - Both Points and Lines
Best of both worlds:
```r
x <- c(1,3,5,7,9)
y <- c(2,4,1,8,5)
plot(x, y, type = "b")
```

---

### Let's Make a Fancy Sine Wave
Combine parameters for better visualization:
```r
x <- seq(0, 2*pi, length=50)
y <- sin(x)
plot(x, y, 
     type = "b", 
     col = "blue",
     main = "Sine Wave Demo",
     xlab = "Angle (radians)",
     ylab = "sin(x)")
```

---

### Pro Tip: Plot Customization
You can add these to any plot:
```r
main = "Title"    # Add title
col = "red"       # Change color
pch = 17          # Change point shape
cex = 2           # Make points bigger
```

---

### Live Demo Time!
Let's create together:
1. Simple scatterplot of 20 random numbers
2. Line plot of cosine function
3. Combined plot with custom colors

---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 3. Layering Graphic Elements

---

## Why Layer Graphics?
- Build complex plots step-by-step
- Combine multiple elements in one visualization
- Customize existing plots with additional information

---

## Basic Plot Setup
```r
# Create base plot
plot(mtcars$mpg, mtcars$hp, 
     main = "Car Performance", 
     xlab = "MPG", ylab = "Horsepower",
     pch = 16, col = "gray")
```

---

## 1. Adding Points with `points()`
```r
# Highlight high-performance cars
special_cars <- mtcars[mtcars$hp > 300, ]
points(special_cars$mpg, special_cars$hp, 
       pch = 17,  # Triangle shape
       col = "red",
       cex = 1.5) # Size
```
**What's happening:**
- `pch=17`: Triangle plotting symbol
- `col="red"`: Makes points stand out
- `cex=1.5`: 50% larger than default

---

## 2. Adding Lines with `lines()`
```r
# Add linear regression line
model <- lm(hp ~ mpg, data = mtcars) # linear regression will be taught next week
x_values <- seq(10, 35, length.out = 100)
y_values <- predict(model, newdata = data.frame(mpg = x_values)) 
lines(x_values, y_values, 
      col = "blue", 
      lwd = 2,    # Line width
      lty = 2)    # Dashed line
```
**Note:** Always calculate prediction values first!

---

## 3. Drawing Rectangles with `rect()`
```r
# Highlight unusual MPG range
rect(xleft = 15, ybottom = 50, 
     xright = 20, ytop = 350,
     border = "red", 
     col = rgb(1, 0, 0, 0.2)) # Transparent red
```
**Parameters:**
- `xleft`, `xright`: X-axis boundaries
- `ybottom`, `ytop`: Y-axis boundaries
- `rgb()`: Creates transparent color

---

## 4. Adding Segments with `segments()`
```r
# Add mean reference lines to boxplot
boxplot(mpg ~ cyl, data = mtcars, col = "lightblue")
cyl_means <- aggregate(mpg ~ cyl, mtcars, mean) # aggregate function is use to stat X based on Y
segments(x0 = 1:3 - 0.4, y0 = cyl_means$mpg,
         x1 = 1:3 + 0.4, y1 = cyl_means$mpg,
         col = "darkred", lwd = 3)
```
**Breakdown:**
- `x0/x1`: Horizontal line positions
- `y0/y1`: Vertical positions (same for horizontal line)
- `lwd=3`: Thick line for visibility

---

## Layering Order Matters!
1. Always create base plot first
2. Add elements in desired z-order:
   - Background elements first
   - Main data points next
   - Annotations last
3. Use `par(new=TRUE)` carefully (not recommended for beginners)

---

## Try This!
Combine all elements we learned:
```r
plot(mtcars$mpg, mtcars$hp)
points(special_cars$mpg, special_cars$hp, col="red")
lines(x_values, y_values, col="blue")
rect(15, 50, 20, 350, border="red")
segments(10, 150, 30, 150, col="green")
```
Experiment with colors and positions!



---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 04. Essential Statistical Plots

# Let's Make Heatmaps!

## What is a Heatmap?
A picture that shows patterns in numbers using colors  
Example: Gene expression levels (high=red, low=white)

---

## Basic Heatmap Code
```r
# Create sample data
gene_data <- matrix(rnorm(100, mean=10), nrow=10)
colnames(gene_data) <- paste("Patient", 1:10)
rownames(gene_data) <- paste("Gene", LETTERS[1:10])

# Simple heatmap
heatmap(gene_data)
```

---

## Understanding the Output

- Colors show values (legend on left)
- Tree diagrams show grouping patterns
- Rows=Genes, Columns=Patients

---

## Customizing Heatmaps
Remove the tree diagrams:
```r
heatmap(gene_data, 
        Rowv = NA,  # No row clustering
        Colv = NA)  # No column clustering
```


---

# Boxplots Made Easy

## What's a Boxplot?
Shows data distribution through 5 numbers:  
📦 Minimum, Q1, Median, Q3, Maximum  
Perfect for comparing groups!

---

## Boxplot with Iris Flowers
```r
# Use built-in iris data
boxplot(Petal.Length ~ Species, 
        data = iris,
        col = c("pink", "lightblue", "yellowgreen"))
```

---

## Understanding the Parts

- Middle line = Median
- Box edges = Q1 and Q3
- Whiskers = Data range (Q1－1.5*IQR & Q3+1.5*IQR; IQR: Interquartile Range)
- Points = Outliers

---

## Making It Pretty
Add colors and labels:
```r
boxplot(Petal.Length ~ Species,
        data = iris,
        main = "Petal Length Comparison",
        xlab = "Iris Species",
        ylab = "Length (cm)",
        col = heat.colors(3))
```

---

# Why These Matter?
Heatmaps help see:  
🧬 Gene expression patterns  
🦠 Microbial communities  

Boxplots help compare:  
🌷 Flower measurements  
🏥 Medical test results  

---

# Try These Modifications!
Experiment with colors in heatmaps:
```r
heatmap(gene_data, col = terrain.colors(50))
```

Change boxplot orientation:
```r
boxplot(Petal.Length ~ Species, data=iris, horizontal=TRUE)
```

---

# Remember These Keys
Heatmap essentials:  
🔥 `heatmap()` needs a numeric matrix  
🎨 Use `col=` to change colors  

Boxplot basics:  
📦 Formula syntax: `y ~ group`  
🌈 Colors make comparisons easier  


---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">


Section 5. Practical Visualization Cases

---

# Today's Roadmap
1. Biomedical visualization cases
2. Graphical output techniques
3. Hands-on plotting examples

---

# Why Visualization Matters
**In biomedical research:**
```R
# Good visualization can reveal:
- Dose-response relationships 📈
- Group differences 🧪🔬
- Data quality issues ⚠️
```

---

# Case 1: Dose-Response Curve
**Scenario:** Test drug efficacy at different concentrations

```R
# Sample data
doses <- c(0, 10, 25, 50, 100)
response <- c(5, 15, 40, 65, 85)

# Basic plot
plot(doses, response, 
     type = "b", 
     main = "Drug Dose-Response Curve",
     xlab = "Dose (mg/mL)", 
     ylab = "Effect (%)",
     col = "darkred",
     pch = 19)
```

---

# Beautifying Our Plot
Add professional touches:
```R
# Add gridlines
grid(col = "lightgray")

# Add confidence intervals
arrows(doses, response-5, doses, response+5, 
       length=0.05, angle=90, code=3)
```

---

# Case 2: Metabolic Comparison
**Task:** Compare cholesterol levels between groups

```R
# Generate sample data
set.seed(123)
control <- rnorm(50, mean = 180, sd = 20)
treatment <- rnorm(50, mean = 160, sd = 15)

# Create boxplot
boxplot(list(Control=control, Treatment=treatment),
        col = c("#FFC107", "#2196F3"),
        main = "Cholesterol Levels Comparison",
        ylab = "mg/dL")
```

---

# Boxplot Interpretation Guide
```R
# Key elements:
- Central line: Median 
- Box: 25%-75% percentile 
- Whiskers: 1.5×IQR 
- Outliers: Beyond whiskers ⚠
```

---

# Saving as PNG
**Best for web/quick sharing**
```R
png("my_plot.png", width=800, height=600)

# Plotting commands
plot(doses, response)
dev.off() # IMPORTANT!
```
🔑 **Pro Tip:** Always close device with `dev.off()`!

---

# PDF Output
**Best for publications/editing**
```R
pdf("figure.pdf", 
    width=8, # inches
    height=6)
    
# Plotting commands
boxplot(control, treatment)
dev.off()
```
📄 **Advantage:** Vector graphics = Infinite zoom!

---

# Common Mistakes to Avoid
```R
1. Forgetting dev.off() -> Empty files ❌
2. Wrong plot dimensions -> Cropped labels 📏
3. Saving while plot window is open -> Conflicts 💥
4. Overwriting files -> Use unique names 🏷️
```

---

# Let's Practice Together!
Create a combined plot:
```R
# Set up PDF output
pdf("combined_plots.pdf", width=10, height=5)

# Split screen
par(mfrow=c(1,2))

plot(doses, response, main="Dose Response")
boxplot(list(C=control, T=treatment), main="Cholesterol")

dev.off()
```

---

# Key Takeaways
1. Basic plots reveal biological patterns
2. Always customize plots for clarity
3. Choose PNG/PDF based on needs
4. Device management is crucial
5. Combine plots for comparison



