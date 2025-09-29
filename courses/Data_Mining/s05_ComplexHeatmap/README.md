
# ComplexHeatmap


https://jokergoo.github.io/ComplexHeatmap-reference/book/

---

## Section 1. basic heatmaps v.s. ComplexHeatmap
### Quick Review: Basic heatmap()
```r
# Create sample matrix
set.seed(123)
mat <- matrix(rnorm(100), nrow=10, 
              dimnames = list(paste0("Gene",1:10), 
                             paste0("Sample",1:10)))

# Basic heatmap
heatmap(mat, 
        col = heat.colors(256),
        scale = "row",
        main = "Basic Heatmap Example")
```

---

### Key Parameters in heatmap()
- `col`: Color palette
- `scale`: "none"/"row"/"column"
- `Rowv/Colv`: Clustering (TRUE/FALSE)
- `margins`: Plot margins
- `cexRow/cexCol`: Label sizes

---

### Limitations of Base Heatmaps
1. Limited annotation capabilities
2. Basic color schemes
3. No multiple heatmap alignment
4. Difficult to add side annotations
5. Limited customization options

---

### Meet ComplexHeatmap!
```r
#install.packages("BiocManager")
#BiocManager::install("ComplexHeatmap")

library(ComplexHeatmap)
library(circlize) # For color gradients
```

---

### Case 1: Gene Expression Heatmap
```r
# Simulate gene expression data
expr_mat <- matrix(rnorm(50*20), nrow=50)
rownames(expr_mat) <- paste0("Gene", 1:50)
colnames(expr_mat) <- paste0("Patient", 1:20)

# Add simple row annotations
gene_type <- sample(c("TypeA","TypeB"), 50, replace=TRUE)
row_ha <- rowAnnotation(Type = gene_type)
```

---

### Plotting Gene Expression
```r
Heatmap(expr_mat,
        name = "Expression",
        col = colorRamp2(c(-2, 0, 2), 
                         c("blue", "white", "red")),
        top_annotation = HeatmapAnnotation(
          Bar = anno_barplot(colMeans(expr_mat))),
        left_annotation = row_ha,
        show_row_names = FALSE)
```

---

### Case 2: Clinical Annotations
```r
# Create clinical metadata
clinical_data <- data.frame(
  Age = rnorm(20, 50, 5),
  Stage = sample(c("I","II","III"), 20, replace=TRUE)
  )
  
col_ha <- HeatmapAnnotation(
  df = clinical_data,
  col = list(Stage = c("I" = "green", 
                      "II" = "yellow", 
                      "III" = "red")))
```

---

### Annotated Clinical Heatmap
```r
Heatmap(expr_mat,
        name = "Expression",
        top_annotation = col_ha,
        column_title = "Patient Samples with Clinical Data",
        show_row_names = FALSE)
```

---

### Case 3: Multi-omics Integration
```r
# Create dummy data
methyl_mat <- matrix(runif(50*20), nrow=50)
expr_mat2 <- matrix(rnorm(50*20), nrow=50)

ht1 <- Heatmap(methyl_mat, 
              name = "Methylation",
              col = colorRamp2(c(0,1), 
                              c("white", "purple")))

ht2 <- Heatmap(expr_mat2, 
              name = "Expression",
              col = colorRamp2(c(-2,0,2), 
                              c("blue","white","red")))
```

---

### Combining Heatmaps
```r
ht1 + ht2
```

---

### Pro Tips for Beginners
1. Always name your heatmaps (`name=` parameter)
2. Use `show_heatmap_legend` to control legends
3. Start with small matrices (10x10)
4. Use `anno_*` functions for annotations
5. Save plots with `pdf("plot.pdf"); draw(ht); dev.off()`

---

### Let's See It All Together!
```r
Heatmap(expr_mat,
        name = "Expression",
        top_annotation = col_ha,
        left_annotation = row_ha,
        column_split = clinical_data$Stage,
        row_title = "Gene Clusters",
        column_names_rot = 45)
```

---

### Why ComplexHeatmap Rocks!
1. Combine multiple plots
2. Rich annotation system
3. Flexible color control
4. Publication-ready outputs
5. Active developer community

---

### Next Steps
1. Experiment with different color schemes
2. Try adding multiple annotations
3. Explore different clustering methods
4. Combine 3+ heatmaps vertically/horizontally

---

### Help Resources
```r
?Heatmap
browseVignettes("ComplexHeatmap")
```



# Section 2. Basic Heatmap Plotting
**Zero to Hero in R Visualization**

---

## Table of Contents
1. Data Preparation Workflow
2. Generating Test Data
3. Reading Real Data Files
4. Heatmap() Core Function
5. Name Parameter
6. Color Control
7. Row/Column Settings

---

## 1. Data Preparation Workflow
**Two approaches for beginners:**
```r
# Method 1: Create test data
fake_data <- matrix(rnorm(100), ncol=10)

# Method 2: Read CSV file
real_data <- read.csv("your_data.csv")
```
*Always start with small test data before using real datasets!*

---

## 2. Generating Test Data
**Let's make playful sample data:**
```r
# Create a 10x10 matrix with random numbers
set.seed(123)
play_matrix <- matrix(rnorm(100), ncol=10,
                      dimnames = list(paste0("Gene",1:10),
                                      paste0("Sample",1:10)))
```
*Why 123? It makes random numbers repeatable!*

---

## 3. Reading Real Data
**Simple CSV import demonstration:**
```r
# Create sample CSV file first
write.csv(play_matrix, "demo_data.csv")

# Now read it back
my_data <- read.csv("demo_data.csv", row.names=1)
```
*Protip: Always check first 3 lines with head(my_data, 3)*

---

## 4. Meet Heatmap()
**Basic template to remember:**
```r
your_matrix=play_matrix
library(ComplexHeatmap)
Heatmap(your_matrix,
        name = "Legend Title",
        col = colorRamp2(c(-1, 0, 1), c("green", "white", "red")),
        show_row_names = FALSE)
```
*Three key parameters control 80% of basic plots*

---

## 5. Name Parameter
**What's this magic?**
```r
# Without name parameter
Heatmap(play_matrix)

# With name parameter
Heatmap(play_matrix, name = "Expression Level")
```
*Try both versions to see the legend title difference!*

---

## 6. Color Control
**Make rainbow heatmaps:**
```r
# Create color gradient
my_colors <- colorRamp2(c(-2, 0, 2), 
                       c("blue", "white", "red"))

# Apply colors
Heatmap(play_matrix, name = "Fun Colors",
        col = my_colors)
```
*colorRamp2() needs at least 2 color stops*

---

## 7. Hide Row Names
**When labels get messy:**
```r
# Original version
Heatmap(play_matrix)

# Clean version
Heatmap(play_matrix, 
        show_row_names = FALSE,
        show_column_names = TRUE)
```
*Perfect for data with many rows!*

---

## Final Example
**Combine all we learned:**
```r
set.seed(123)
final_data <- matrix(rnorm(50), ncol=5)

Heatmap(final_data,
        name = "Demo Values",
        col = colorRamp2(c(-2,0,2), 
                        c("green","black","yellow")),
        show_row_names = FALSE,
        column_names_side = "top")
```
*Now you're ready for basic heatmaps!*



# Section 3. ComplexHeatmap Annotation Systems

---

## What Are Heatmap Annotations?
Add extra information to rows/columns using:
- Colors
- Points
- Text labels
- Graphics

Example use cases:
- Show sample groups
- Display numeric trends
- Highlight genes

---

## Basic Column Annotation Setup

```R
# Create simple group annotation
ha <- HeatmapAnnotation(
  group = c(rep("Control",5), rep("Case",5))
)

# Draw heatmap with annotation
Heatmap(matrix(rnorm(100), ncol=10), top_annotation = ha)
```


---

## Add Numeric Annotations

Create age trends with points:
```R
ha <- HeatmapAnnotation(
  group = c(rep("Control",5), rep("Case",5)),
  age = anno_points(runif(10))  # Random values 0-1
)

Heatmap(matrix(rnorm(100), ncol=10), top_annotation = ha)
```

Parameters:
- `runif(10)` generates 10 random numbers
- `anno_points()` creates point plot annotation

---

## Row Annotation Basics

Add gene type information:
```R
row_ha <- rowAnnotation(
  gene_type = c(rep("Protein", 30), rep("RNA", 20))
)

Heatmap(matrix(rnorm(1000), nrow=50), 
       left_annotation = row_ha)
```

Features:
- Appears on left side
- Works with any categorical data

---

## Special Marker Annotations

Highlight important genes:
```R
row_ha <- rowAnnotation(
  mark = anno_mark(
    at = c(5, 15, 25),  # Row positions
    labels = c("GeneA", "GeneB", "GeneC"))
)

Heatmap(matrix(rnorm(100), nrow=25), 
       left_annotation = row_ha)
```

Effect: Shows labeled markers next to heatmap

---

## Split Columns by Group

Create visual separation:
```R
Heatmap(matrix(rnorm(100), ncol=10),
       column_split = c(rep("A",5), rep("B",5)))
```

Parameters:
- Split vector matches column count
- Creates divided headers

---

## Cluster Rows into Blocks

Automated grouping:
```R
ht=Heatmap(matrix(rnorm(1000), nrow=50),
       row_km = 3)  # Create 3 clusters
ht_out = draw(ht)
row_order(ht_out)
```

Features:
- K-means clustering
- Shows separation lines
- Each block gets unique color

---

## Full Example Combination

```R
ha <- HeatmapAnnotation(
  group = rep(c("Young","Old"), each=5),
  age = anno_points(20:29))

row_ha <- rowAnnotation(
  type = sample(c("A","B"), 50, replace=TRUE))

Heatmap(matrix(rnorm(500), nrow=50),
       top_annotation = ha,
       left_annotation = row_ha,
       column_split = rep(1:2, each=5),
       row_km = 2)
```

---

## Key Parameters Cheat Sheet

Column Annotations | Row Annotations | Splitting
-------------------|-----------------|----------
`top_annotation` | `left_annotation` | `column_split`
`anno_points()` | `anno_mark()` | `row_km`
`column_names_side` | `row_names_side` | `cluster_rows`

---

Remember: Type `?anno_points` to see all options!



# Section 4. Case Studies with ComplexHeatmap

---

### What We'll Learn Today
1. Biomedical case: Gene expression matrix annotation
2. Cross-platform data integration
3. Vertical heatmap concatenation
4. Shared legend system

---

## Part 1: Biomedical Case Setup
Let's create a simple gene expression matrix:
```R
# Create sample data
expr_matrix <- matrix(rnorm(100), nrow=10, 
                     dimnames=list(paste0("Gene",1:10),
                                 paste0("Patient",1:10)))
clinical_stage <- data.frame(
  Patient=paste0("Patient",1:10),
  Stage=sample(c("I","II","III"), 10, replace=TRUE)
)
```

---

## Adding Clinical Annotations
```R
library(ComplexHeatmap)

# Create color mapping
stage_colors <- c("I"="blue", "II"="green", "III"="red")

# Create top annotation
top_anno <- HeatmapAnnotation(
  Stage=clinical_stage$Stage,
  col=list(Stage=stage_colors)
)

Heatmap(expr_matrix, name="Expression", 
        top_annotation=top_anno)
```

---

## Adding Survival Status
```R
# Add survival data
survival_status <- sample(c(0,1), 10, replace=TRUE)

# Create bottom annotation
bottom_anno <- HeatmapAnnotation(
  Survival=survival_status,
  col=list(Survival=c("0"="gray", "1"="black"))
  )
  
Heatmap(expr_matrix, name="Expression",
        top_annotation=top_anno,
        bottom_annotation=bottom_anno)
```

---

## Adding Significance Stars
```R
# Create p-value matrix
p_values <- matrix(runif(100), 10)
signif_stars <- ifelse(p_values < 0.05, "*", "")

Heatmap(expr_matrix, name="Expression",
        cell_fun=function(j, i, x, y, w, h, col) {
          grid.text(signif_stars[i,j], x, y)
        })
```

---

## Part 2: Cross-Platform Integration
Prepare methylation data:
```R
methyl_matrix <- matrix(runif(100), nrow=10,
                       dimnames=list(paste0("Gene",1:10),
                                   paste0("Sample",1:10)))
```

---

## Creating Individual Heatmaps
```R
ht1 <- Heatmap(expr_matrix, name="Expression",
              column_title="Gene Expression")

ht2 <- Heatmap(methyl_matrix, name="Methylation",
              column_title="DNA Methylation",
              col=colorRamp2(c(0,1), c("white", "purple")))
```

---

## Vertical Concatenation
```R
ht1 %v% ht2  # Simple vertical combination
```

---

## Adding Shared Legend
```R
draw(ht1 %v% ht2, 
     heatmap_legend_side="right",
     annotation_legend_side="left")
```

---

### Key Takeaways
1. Heatmap annotations help add metadata
2. `%v%` operator enables vertical layout
3. Shared legends maintain visual consistency
4. Cell functions allow custom decorations

Ready for hands-on practice! 🚀

# Section 5: Plot Optimization & Export

---

## Today's Learning Goals
1. Adjust visualization parameters in R plots
2. Export high-quality figures for publications

---

## Why Optimization Matters
Bad default plot:
```R
heatmap(matrix(rnorm(100), nrow=10))
```
Problems:
- Overlapping labels
- Unreadable text
- Poor element arrangement

---

## Basic Heatmap Template
```R
library(ComplexHeatmap)
basic_heatmap <- Heatmap(
  matrix(rnorm(100),nrow=10), 
  name = "values")

draw(basic_heatmap)
```

---

## Control Plot Width
Make heatmap 8 inches wide:
```R
adjusted_heatmap <- Heatmap(
  matrix(rnorm(100),nrow=10),
  name = "values",
  row_title= 'row_title',
  width = unit(2, "in"),
  height = unit(2, "in")
)

draw(adjusted_heatmap)
```

---

## Rotate Row Titles
Rotate title 45 degrees:
```R
rotated_heatmap <- Heatmap(
  matrix(rnorm(100),nrow=10),
  name = "values",
   row_title= 'row_title',
  row_title_rot = 45,
   width = unit(2, "in"),
  height = unit(2, "in")
)
draw(rotated_heatmap)
```

---

## Combine Parameters
```R
final_heatmap <- Heatmap(
  matrix(rnorm(100),nrow=10),
  name = "My Data",
  width = unit(2, "cm"),
  height = unit(2, "cm"),
  row_title = "Genes",
  row_title_rot = 30,
  column_title = "Samples"
)
draw(final_heatmap)
```

---

## PDF Export Basics
Save to 8x8 inch PDF:
```R
pdf("my_plot.pdf", width=8, height=8)
draw(final_heatmap)
dev.off()
```

---

## High-Resolution PNG
300 dpi export:
```R
png("heatmap.png", 
    width=2400, 
    height=1600, 
    res=300)
draw(final_heatmap)
dev.off()
```

---

## Export Settings Matter!
Compare outputs:
- PDF: Vector format (good for editing)
- PNG: Raster format (good for web)
- TIFF: Lossless format (for publications)

---

## Quick Recap
Key parameters:
- `width`: Controls overall plot size
- `*_title_rot`: Rotates text labels
- `name`: Sets legend title

Export commands:
- `pdf()`, `png()`, `tiff()`
- Always use `dev.off()`

---

## Let's Make a Custom Plot!
Combine what we learned:
```R
custom_plot <- Heatmap(
  matrix(rnorm(400), nrow=20),
  name = "Expression",
  width = unit(15, "cm"),
  row_title_rot = 60,
  column_title = "Patient Cells"
)

pdf("final_figure.pdf", width=10, height=7)
draw(custom_plot)
dev.off()
```

---

## Common Mistakes
1. Forgetting `dev.off()`
2. Using pixel units for PDF exports
3. Not checking exported file dimensions
4. Over-rotating labels (>90°)

---

## How to Verify Exports
Always:
1. Open exported files
2. Check text clarity
3. Verify element spacing
4. Confirm dimensions match requirements

---

## Next Steps
1. Try different rotations (0°, 30°, 90°)
2. Experiment with PDF vs PNG outputs
3. Test various plot widths/heights

