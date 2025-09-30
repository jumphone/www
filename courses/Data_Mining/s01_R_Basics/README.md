
# Section 1. R Environment Quick Start & First Program

## Part 1: R Language Environment Quick Start

### 1.1 R Language Interface Walkthrough

- **Basic Command Execution**
  - Direct command input demonstration:
    ```R
    print("Hello World")
    2 + 3
    sqrt(25)
    ```
 
- **Essential Shortcuts**
  - `↑`/`↓` Arrow keys: Cycle through command history
  - `Tab`: Auto-complete for:
    - Function names
    - Variable names
    - File paths
  - `Ctrl + C`: Interrupt current command
  - `Ctrl + L`: Clear console screen

### 1.2 Environment Configuration Check
- Verify R version:
  ```R
  R.version.string
  ```
- Check working directory:
  ```R
  getwd()
  ```
- List installed packages:
  ```R
  installed.packages()
  ```

---

## Part 2: Your First R Program

### 2.1 Script File Management
- **File Operations Workflow**
  1. Create new file: `nano first_program.R`
  2. Edit content:
     ```R
     # My First R Script
     message <- "Welcome to Data Analysis!"
     print(message)
     ```
  3. Save: `Ctrl+O` → Enter → `Ctrl+X`
  4. Execute: `Rscript first_program.R`

- **File Organization Best Practices**
  - Use consistent naming: `lowercase_with_underscores`
  - Create dedicated project folders
  - Maintain version control basics:
    - `v01_initial_script.R`
    - `v02_updated_script.R`

### 2.2 Code Documentation Standards
- **Effective Commenting**
  - Section headers:
    ```R
    # Data Cleaning Section ------------------------
    ```
  - Function explanations:
    ```R
    # Calculates Euclidean distance between two points
    # Input: Numeric vectors x and y
    # Output: Scalar distance value
    ```
  - TODO notes:
    ```R
    # TODO: Implement error handling here
    ```

- **Debugging Annotation**
  ```R
  # TEST: Verify input dimensions
  print(dim(data_matrix))
  ```

### 2.3 Error Diagnosis Fundamentals

| Error Type          | Examples                      | Quick Checks               |
|---------------------|-------------------------------|----------------------------|
| Syntax Errors       | Missing `)`, `}`              | Color highlighting in editor |
| Runtime Errors      | `object 'var' not found`      | `ls()` to list variables   |
| Logical Errors      | Incorrect algorithm implementation | Add `print()` statements  |
| Package Errors      | `there is no package called...` | Verify installation with `install.packages()` |

---

## Supplemental Materials

### AI-Assisted Learning Tips
1. When encountering errors:
   - Copy-paste full error message to AI tools
   - Example prompt: "I get 'Error: unexpected symbol in...' when running my R script. Here's my code: [code snippet]"

2. For concept clarification:
   - Ask: "Explain R environments to a complete beginner"
   - Request: "Show comparison between vectors and lists in R"

### Recommended Practice Workflow
1. Write code in script file
2. Execute through terminal
3. Encounter error → analyze message
4. Consult AI helper with:
   - Exact error message
   - Relevant code section
   - Session info (`sessionInfo()`)

### Critical Linux-R Integration
- Server file management:
  - Transfer files using Termius SFTP
  - Navigate directories with `cd`
  - Verify file permissions: `ls -l script.R`

---

# Section 2. Variables & Data Types in R

---

## 1. Variable Fundamentals

### Naming Convention
```r
# Valid names
my_var <- 5
Var2 <- "text"
.height <- 7.2  # Hidden variable

# Invalid names
2var <- 10      # Error: Starts with number
if <- 20        # Error: Reserved word
```

**Key Rules**:
- Case sensitive: `myVar ≠ myvar`
- Avoid: 
  - Reserved words (`if`, `function`, `NULL`)
  - Special symbols (except `.` and `_`)
- Best practice: Use snake_case (`my_variable`)

---

### Assignment Operators
```r
x <- 5   # Recommended style
y = 10   # Works but less common
25 -> z  # Right assignment (rare)

# Scope differences in functions:
median(x = 1:10)    # Temporary assignment
median(x <- 1:10)   # Creates permanent object
```

**Community Preference**: 
- `<-` for object creation
- `=` for function arguments

---

### Variable Management
```r
# List objects
ls()                # All variables
ls(pattern = "^x")  # Filter by pattern

# Remove variables
rm(x)               # Remove single
rm(list = ls())     # Clear environment

# Environment comparison
.GlobalEnv         # Default workspace
search()           # Attached packages
```

---

## 2. Core Data Types

### Numeric Types
```r
# Default is double
num1 <- 15      # Type: double
num2 <- 15L     # Explicit integer

# Type checking
typeof(num1)    # "double"
is.integer(num2) # TRUE

# Scientific notation
1.2e3 == 1200   # TRUE
```

---

### Character Type
```r
# Quote variations
str1 <- "Hello's World"   # Double quotes
str2 <- 'He said "Hi"'    # Single quotes

# Escape characters
path <- "C:\\Documents\\file.txt" 
cat(path)  # C:\Documents\file.txt

# Concatenation
paste("RNA", "seq", sep = "-")  # "RNA-seq"
```

---

### Logical Type
```r
# Basic logic
is_valid <- TRUE
is_empty <- FALSE

# Quick input
T <- FALSE  # Dangerous! (T is redefined)
TRUE <- 5   # Error: Reserved word

# Best practice: Always spell out
valid <- TRUE  
```

---

### Type Conversion
```r
# Explicit conversion
as.numeric("123")     # 123
as.character(45.7)    # "45.7"
as.integer(TRUE)      # 1

# Automatic conversion
sum(c(TRUE, FALSE))   # 1 (logical → numeric)
"Value:" + 5          # Error (implicit failure)
```

**Watch for**:
```r
as.numeric("ABC")     # NA with warning
```

---

## 3. Special Values

### Missing Values (NA)
```r
# Detection
x <- c(1, NA, 3)
is.na(x)  # FALSE TRUE FALSE

# Operations
sum(x)               # NA
sum(x, na.rm=TRUE)   # 4

# Special cases
NA == NA   # NA (not TRUE)
```

---

### NULL vs NaN vs Inf
```r
# NULL (empty object)
length(NULL)  # 0
x <- NULL

# NaN (Not a Number)
0/0            # NaN
sqrt(-1)       # NaN with warning

# Inf/-Inf
1/0            # Inf
log(0)         # -Inf
```

**Checking Methods**:
```r
is.null(x)     # For NULL
is.nan(y)      # For NaN
is.infinite(z) # For Inf/-Inf
```

---

# Section 3. R Operator System

---

## 1. Arithmetic Operators

### Modulus Operator `%%`
```r
# Check divisibility
9 %% 3  # Returns 0
7 %% 2  # Returns 1

# Practical application: Batch processing
i=1
while(i<=10000){
    if(i %% 100 == 0){
        print(paste("Processing batch", i/10000))
    }
    Sys.sleep(0.001)
    i=i+1
}
```

### Exponentiation
```r
2^3    # 8
2**3   # 8 (equivalent)
```
- **Key Note:** Always use `^` for better code readability in R

---

## 2. Comparison Operators

### Floating Point Precision Warning
```r
0.1 + 0.2 == 0.3         # FALSE
all.equal(0.1+0.2, 0.3)  # TRUE
```
- **Rule:** Never use `==` with floating numbers

### Vectorized Comparisons (Preview)
```r
c(1,3,5) > 2  # Returns FALSE TRUE TRUE
```
- **Special Note:** Will be crucial for matrix operations (Lesson 04)

---

## 3. Logical Operators

### Element-wise vs Single-element
```r
# & (vectorized)
c(TRUE, FALSE) & c(FALSE, FALSE)  # FALSE FALSE

# && (single-element)
c(TRUE, FALSE) && c(FALSE, FALSE) # FALSE
```

### Common Pitfall
```r
x <- 5
x > 3 & x < 10
x > 3 && x < 10

x <- c(5,7)
x > 3 & x < 10
x > 3 && x < 10
```

### Short-circuit Evaluation
```r
# || stops at first TRUE
ppp = function(){
    print('ok')
    return(FALSE)}

TRUE || ppp()
FALSE || ppp()
```

---

## 4. Operator Precedence

### Essential Priority Levels
1. `()` - Parentheses
2. `^` - Exponentiation
3. `%%` - Modulus
4. `* /` - Multiplication/Division  
5. `+ -` - Addition/Subtraction
6. `> <` - Comparisons
7. `!` - NOT
8. `& &&` - AND
9. `| ||` - OR
10. `<-` - Assignment

### Critical Example
```r
3 + 5 * 2 ^ 2  # = 3 + (5*(2^2)) = 23
```

---

## Best Practices
1. Always use parentheses for complex expressions
2. Use spaces around operators: `x <- 5 + (a & b)`
3. Prefer `&`/`|` over `&&`/`||` unless specifically needed
4. Use `all.equal()` instead of `==` for numeric comparisons

---

# Section 4. String Manipulation in R

---

## 1. Basic String Operations

### Concatenation Functions
```r
# paste() with separator
paste("Hello", "World", sep = " ")  # "Hello World"

# paste0() for direct concatenation
paste0("File_", 1:3, ".txt")  # "File_1.txt" "File_2.txt" "File_3.txt"

**Key Difference:**
- `paste()`: Default space separator, customizable
- `paste0()`: No separator (equivalent to paste(..., sep=""))
```

---

### String Splitting
```r
# Basic splitting
result <- strsplit("apple,orange,banana", ",")
# Returns list: [[1]] [1] "apple"  "orange" "banana"

# Accessing elements
result[[1]][2]  # "orange"

**Important Characteristics:**
- Always returns a *list* structure
- Use `unlist()` to convert to vector: 
  unlist(strsplit("a-b-c", "-"))  # [1] "a" "b" "c"
```

---

## 2. Regular Expressions Basics

### Pattern Matching with grep()
```r
# Find matching elements
colors <- c("red", "blue", "green2", "yellow3")
grep("\\d", colors)  # Returns positions: 3 4

# Get actual values
grep("\\d", colors, value=TRUE)  # "green2" "yellow3"

**Common Flags:**
- `ignore.case=TRUE`: Case-insensitive matching
- `invert=TRUE`: Return non-matching elements
```

---

### Regular Expression Special Characters

| Character | Meaning                | Example          |
|-----------|------------------------|------------------|
| `^`       | Start of string        | `^A` matches "Apple" not "aPple" |
| `$`       | End of string          | `d$` matches "end" not "ending" |
| `.`       | Any single character   | `a.c` matches "abc", "a2c"       |
| `*`       | Zero or more repeats   | `lo*` matches "l", "lo", "loo"   |

**Example:**
```r
grep("^[A-Z]", c("Apple", "banana"))  # 1 (matches first element)
```

---

## 3. Practical Tips & Tricks

### Multi-line Strings
```r
# Good practice
long_text <- "This is a multi-line
string in R. Use explicit newline
characters for clarity."

# Problematic approach
bad_text <- "This might cause 
             unexpected indentation"
```

---

### Special Character Escaping
```r
# Common escape sequences
cat("Line1\nLine2")   # New line
cat("Column1\tColumn2")  # Tab
cat("C:\\Program Files\\R")  # Backslash

**Essential Escapes:**
- `\n`: New line
- `\t`: Tab
- `\\`: Literal backslash
- `\"`: Literal double quote
```

---

### String Length Pitfalls
```r
# Handling NA values
nchar(NA)         # Returns NA
nchar("NA")       # Returns 2

# Safe approach
nchar(na.omit(c("text", NA)))  # Length: 4

**Best Practice:**
- Always pre-process NA values before using nchar()
- Consider `stringi::stri_length()` for alternative NA handling
```

---

# Section 5. Control Flow in R Programming

---

## 1. Conditional Statements

### 1.1 Nested if-else Structure
```r
# Proper nested formatting example
a=5
if (a<1) {
  print('less than 1')
} else if (a<4) {
  print('a>=1 and a<4')
} else {
  print('a>=4')
}
```
**Key Points:**  
- Always use curly braces `{}` even for single-line statements
- Maintain consistent indentation (2/4 spaces)
- Limit nesting depth (<3 levels recommended)

---

### 1.2 Vectorized ifelse()
```r
x=c(5,7)
# Traditional approach
result <- vector()
for (i in 1:length(x)) {
  result[i] <- if (x[i] > 0) "Positive" else "Negative"
}

# Vectorized approach
result <- ifelse(x > 0, "Positive", "Negative")

```
**Advantages:**  
- 300% faster for large datasets (demonstrate with system.time())
- More readable & concise syntax
- Automatic type conversion handling

---

### 1.3 switch() for Multiple Branches
```r
# Basic syntax
operation <- function(op, x, y) {
  switch(op,
         "add" = x + y,
         "sub" = x - y,
         "mul" = x * y,
         stop("Invalid operation"))
}
```
**Use Cases:**  
- Menu-driven programs
- State machine implementations
- Alternative to long if-else chains

---

## 2. Loop Structures

### 2.1 for Loop Variations
```r
# Index styles comparison
for (i in 1:5) {...}          # Basic numeric range
for (i in seq_along(vec)) {...} # Safer for empty vectors
for (item in vector) {...}    # Direct element access
```
**Protection Tips:**  
- Always test `length(vector) > 0` before looping
- Use `seq_along()` instead of `1:length()` to handle empty vectors
- Consider `purrr::map()` for functional programming

---

### 2.2 While Loop Safety
```r
# Safe while template
counter <- 0
while (condition && counter < max_iter) {
  # loop body
  counter <- counter + 1
}
```
**Essential Checks:**  
- Define maximum iterations (e.g., `max_iter = 1e6`)
- Include fail-safe condition checks
- Update control variables at loop END

---

### 2.3 Loop Control Flow
```r
for (i in 1:10) {
  if (i %% 2 == 0) next  # Skip even numbers
  if (i > 7) break       # Early exit
  print(i)
}
```
**When to Use:**  
- `next`: Skip invalid/irrelevant cases
- `break`: Error conditions met, or early completion
- Use sparingly to maintain code readability

---

## 3. Best Practices

### 3.1 Defensive Programming
```r
# Before loop
if (length(data) == 0) {
  stop("Empty input dataset")
}

# In while loops
timeout <- Sys.time() + 300  # 5-minute timeout
while (condition) {
  if (Sys.time() > timeout) {
    stop("Execution timeout reached")
  }
  # ...
}
```

---

### 3.2 Vectorization Techniques
```r
# Loop approach
total <- 0
for (num in numbers) {
  total <- total + num
}

# Vectorized approach
total <- sum(numbers)

# Benchmark comparison (1M elements):
- Loop: 0.15s
- Vectorized: 0.0001s
```
**Key Functions:**  
- apply() family
- rowSums()/colMeans()
- pmap()/map_dbl() from purrr

---

### 3.3 Memory Pre-allocation
```r
# Poor practice
result <- c()
for (i in 1:1e5) {
  result <- c(result, i^2)
}

# Proper pre-allocation
result <- numeric(1e5)
for (i in 1:1e5) {
  result[i] <- i^2
}
```
**Performance Gain:**  
- 10,000 elements: 100x faster  
- 1M elements: Avoids 1M memory reallocations

---

## Recommended Practice
```r
# AI-Assisted Exercise
"Ask ChatGPT/Kimi to help write a function that:
1. Takes numeric vector input
2. Uses ifelse() to replace negative values with NA
3. Calculates mean with vectorized operations
4. Includes defensive programming checks"
```

---

## AI Tips

**When Stuck:**  
1. Try explaining your goal to AI in simple words  
2. Ask for R code examples with:  
   - Input data format  
   - Desired output  
3. Request debugging help with error messages  

**Example Prompt:**  
"Help me convert this for-loop to while-loop:  
for (i in 1:length(x)) { 
  print(i) 
}"

