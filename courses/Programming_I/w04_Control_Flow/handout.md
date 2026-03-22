# Lecture Handout: Control Flow in Python (90-Minute Session)

**Course:** Programming I  
**Week:** 4  
**Topic:** Control Flow Structures

---

## Learning Objectives (5 minutes)

By the end of this session, you will be able to:
- Write conditional statements using `if-elif-else` for decision-making logic
- Implement both `while` and `for` loops for repetitive tasks
- Use loop control statements (`break`, `continue`) effectively
- Apply comparison and logical operators in real scenarios
- Debug common control flow errors (indentation, colons, infinite loops)
- Build interactive programs with user input and validation

---

## Section 1: Conditional Statements (20 minutes)

### 1.1 The `if` Statement Basics

Control flow allows programs to make decisions. The simplest form is the `if` statement:

```python
age = 18
if age >= 18:
    print("You can vote!")
```

**Key Rules:**
- The colon `:` at the end is mandatory (syntax error without it)
- Indentation must be exactly 4 spaces per level (never mix with tabs)
- Each condition evaluates to `True` or `False`

### 1.2 Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |

**Critical Distinction:**
```python
# WRONG - assignment, not comparison
if temperature = 30:
    print("Hot")

# CORRECT
if temperature == 30:
    print("Hot")
```

### 1.3 Multi-Condition Flow with `elif`

When you have multiple exclusive conditions:

```python
score = float(input("Enter score (0-100): "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

**Execution Flow:** Python checks each condition sequentially and executes only the first block that evaluates to `True`.

### 1.4 Logical Operators

Combine multiple boolean expressions:

```python
is_raining = True
has_umbrella = False

if is_raining and has_umbrella:
    print("Go outside")
else:
    print("Stay home")
```

- `and`: Both must be `True`
- `or`: At least one must be `True`
- `not`: Reverses the boolean value

### 1.5 Nested Conditions

Conditions inside conditions (use sparingly - max 3 levels recommended):

```python
age = 20
is_student = True

if age < 18:
    print("50% discount")
else:
    if is_student:
        print("30% discount")
    else:
        print("No discount")
```

**Think About It:** How would you modify the ticket system to give both student AND membership discounts?

### 1.6 Truth Value Testing

These values evaluate to `False` in Python:
- `False`
- `None`
- `0` (integer or float)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)

```python
name = ""
if not name:
    print("Name is required!")
```

---

## Section 2: Loop Structures (25 minutes)

### 2.1 `while` Loops: Mechanics

Repeats code while a condition remains `True`:

```python
countdown = 3
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("Go!")
```

**Flowchart:**
```mermaid
graph TD
    A[Start] --> F[Initialize countdown]
    F --> B{countdown > 0?}
    B -->|Yes| C[Print countdown]
    C --> D[countdown -= 1]
    D --> B
    B -->|No| E[Print "Go!"]
```



### 2.2 Common `while` Loop Patterns

**Counter-controlled:**
```python
attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    print("Attempt:", attempts + 1)
    # Your code here
    attempts += 1
```

**Flag-controlled:**
```python
running = True
while running:
    user_input = input("Continue? (y/n): ")
    if user_input == "n":
        running = False
```

### 2.3 The `for` Loop Basics

Iterates over a sequence:

```python
groceries = ["apple", "milk", "bread"]
for item in groceries:
    print("Don't forget to buy:", item)
```

### 2.4 The `range()` Function

Three usage patterns:

```python
# Single argument: 0 to n-1
for num in range(5):
    print(num)  # 0, 1, 2, 3, 4

# Two arguments: start to end-1
for num in range(2, 5):
    print(num)  # 2, 3, 4

# Three arguments: start, end, step
for num in range(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8
```

### 2.5 Loop Control Statements

**`break` - Emergency Exit:**
```python
passwords = ["123", "admin", "letmein"]
for pwd in passwords:
    if pwd == "admin":
        print("Security alert!")
        break
    print("Checking:", pwd)
```

**`continue` - Skip Iteration:**
```python
for num in range(10):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(num, "is even")
```

**`else` Clause - Completion Handler:**
```python
numbers = [2, 4, 6]
for n in numbers:
    if n % 2 != 0:
        break
else:
    print("All numbers are even!")
# Executes only if loop completes without break
```

### 2.6 Nested Loops

```python
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f'{i}x{j}={i*j}', end="\t")
    print()  # New line
```

**Output:**
```
1x1=1   1x2=2   1x3=3
2x1=2   2x2=4   2x3=6
3x1=3   3x2=6   3x3=9
```

**Indentation Levels:** Each loop level adds 4 spaces. The inner block can access outer loop variables.

---

## Section 3: Practical Examples (20 minutes)

### 3.1 Smart Grade Rating System

```python
while True:
    score_input = input("Enter score (q to quit): ")
    
    if score_input.lower() == 'q':
        break
    
    try:
        score = float(score_input)
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'D'
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input. Please enter a number.")
```

### 3.2 Number Guessing Game (Complete)

```python
import random

def play_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    MAX_ATTEMPTS = 5
    
    print("Guess the number (1-100). You have 5 tries.")
    
    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            
            if guess == target:
                print(f"Victory in {attempts + 1} tries!")
                return
            
            elif guess > target:
                print("Too high")
            else:
                print("Too low")
                
            attempts += 1
            
        except ValueError:
            print("Please enter a valid integer.")
    
    print(f"Failed! Number was {target}")

# Run the game
play_guessing_game()
```

**Key Features:**
- Input validation with `try-except`
- Attempt counter with maximum limit
- Clear win/lose conditions
- Early exit on success

---

## Section 4: Special Considerations & Best Practices (15 minutes)

### 4.1 Avoiding Infinite Loops

**Dangerous Pattern:**
```python
# temperature = 25
# while temperature > 20:
#     print("AC running")
#     # Forgot to update temperature!
```

**Safe Pattern:**
```python
# Always write termination condition first
counter = 0
while counter < 10:
    print(counter)
    counter += 1  # Update condition variable
```

### 4.2 Code Readability

**Long Conditionals - Split for Clarity:**
```python
# Hard to read
if (num > 0 and num%2 == 0 and num < 100 and name != "admin"):
    pass

# Better
is_positive_even = num > 0 and num % 2 == 0
within_limit = num < 100
valid_user = name != "admin"

if is_positive_even and within_limit and valid_user:
    pass
```

**Multi-line Conditions:**
```python
if (temperature > 100 
    and humidity < 70 
    and is_sunny):
    print("Heat warning!")
```

### 4.3 Debugging with Print Statements

```python
counter = 0
while counter < 3:
    print(f"DEBUG: counter = {counter}")  # Remove after debugging
    counter += 1
```

### 4.4 Common Syntax Errors

**Missing Colon:**
```python
# Incorrect
while x < 5
    print(x)

# Correct
while x < 5:
    print(x)
```

**Indentation Errors:**
```python
# Wrong - mixed spaces/tabs or wrong level
def test():
while n > 0:  # Missing indentation
print(n)      # Wrong level

# Correct
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
```

### 4.5 Floating-Point Comparison

Never compare floats directly due to precision errors:

```python
# Unreliable
result = 0.1 + 0.2
if result == 0.3:  # May be False!
    print("Equal")

# Safe approach
tolerance = 1e-9
if abs(result - 0.3) < tolerance:
    print("Effectively equal")
```

---

## Section 5: Hands-On Exercises (5 minutes)

### Exercise 1: Vending Machine Logic
Complete the vending machine to:
- Limit coin insertion to 1-3 coins per transaction
- Return extra coins if total exceeds 5
- Display change amount

```python
coins = 0
while coins < 5:
    # Your code here
    pass
```

### Exercise 2: Traffic Light Controller
Extend the traffic light example to:
- Validate input (only accept "red", "yellow", "green")
- Loop until valid input is received
- Count invalid attempts

### Exercise 3: Multiplication Table Generator
Write a program that:
- Asks user for table size (e.g., 5x5, 10x10)
- Prints formatted table using nested loops
- Handles invalid input gracefully

---

## Key Takeaways

1. **Conditionals** (`if-elif-else`) enable decision-making based on boolean logic
2. **Loops** (`while`, `for`) automate repetitive tasks efficiently
3. **Indentation** (4 spaces) defines code blocks - no braces needed
4. **Update loop variables** to prevent infinite loops
5. **Validate user input** to avoid runtime errors
6. **Use `break`/`continue`** sparingly for clear flow control
7. **Debug with print statements** before using a debugger


---

*End

