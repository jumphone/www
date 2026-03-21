
<script src="https://cdn.jsdelivr.net/npm/mermaid@11.13.0/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({
  startOnLoad: true,
  securityLevel: 'loose', 
  flowchart: {
    defaultRenderer: 'svg',
    nodeSpacing: 80,
    rankSpacing: 40
  }
});
</script>

[Back](https://www.bioinfo-lab.com/courses/Programming_I/w04_Control_Flow/)

<br>

<a id="all"></a>

### Content:

[Section 1. Control Flow](#s1.0)

[Section 2. Conditionals in Python](#s2.0)

[Section 3. Loop Structures in Python](#s3.0)

[Section 4. Control Flow - Practical Examples](#s4.0)

[Section 5. Special Considerations](#s5.0)

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Control Flow

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1.1. Conditional Statements

Like traffic lights control vehicles:
```python
light_color = input("Traffic light color: ")

if light_color == "red":
    print("STOP")
elif light_color == "yellow":
    print("SLOW DOWN")
elif light_color == "green":
    print("GO")
else:
    print("INVALID COLOR")
```

---

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Flowchart - Decision Making

<div class="mermaid">
graph TD
    A[Start] --> B{Light Color?}
    B --> |Red| C[Stop]
    B --> |Yellow| D[Slow Down]
    B --> |Green| E[Go]
    C --> F[End]
    D --> F
    E --> F
</div>


---

<div align="left">
  <a href="#s1.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 1.3. While Loops

Like repeating morning runs:
```python
import time
runs_remaining = 3
while runs_remaining > 0:
    time.sleep(1) # suppose you are a superman, 400m in 1 second 
    print("Morning run #"+str(4 - runs_remaining)+" completed!")
    runs_remaining -= 1
print("All runs finished!")
```

---

<div align="left">
  <a href="#s1.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.4"></a>

---

## 1.4. Flowchart - Loop Execution


<div class="mermaid">
graph TD
    A[Start] --> B{Runs Left?}
    B -->|Yes| C[Run]
    C --> D[Reduce Count]
    D --> B
    B -->|No| E[End]
</div>


---

<div align="left">
  <a href="#s1.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.5"></a>

---

## 1.5. Why Control Flow Matters

1. Programs need to make decisions
2. Handle different situations
3. Repeat tasks efficiently
4. Makes code adaptable

Example: Automatic door control
```python

# since we don't have a sensor, we just pretend to be a sensor.

import time

def object_detected():
    # get signal from the sensor
    signal = input('detected(y/n):')
    if signal=='y':
        result=True
        print('detected!')
    else:
        result=False
        print('no object!')
    time.sleep(1)
    return(result)

def keep_open():
    print('open door!')
    # send signal to the door
    time.sleep(1)

def close_door():
    print('close door!')
    # send signal to the door
    time.sleep(1)

sensor_active = True

while sensor_active:
    if object_detected():
        keep_open()
    else:
        close_door()

```

---

<div align="left">
  <a href="#s1.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.6"></a>

---

## 1.6. Vending Machine Example

Let's code a drink machine:
```python
coins = 0
while coins < 5:
    insert_coins = int(input("Insert coin (1-3): "))
    coins = coins + insert_coins
    print("Total inserted: "+str(coins))
print("Here's your drink!")
```

<br>

### Q: how can we limit the number of inserted coins each time

<br>

### Q: how can we get the extra coins

<br>

---

<div align="left">
  <a href="#s1.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.7"></a>

---

## 1.7. Common Loop Patterns

1. Flag-controlled loops
```python
running = True
while running:
    user_input = input("Continue? (y/n): ")
    if user_input == "n":
        running = False
```

2. Counter-controlled loops
```python
attempts = 3
while attempts > 0:
    # code here
    attempts=attempts-1

attempts = 0
while attempts < 10:
    # code here
    attempts=attempts+1
```

---

<div align="left">
  <a href="#s1.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.8"></a>

---

## 1.8. Take-home Message

1. `if-elif-else` for decisions
2. `while` for repeating tasks
3. Condition evaluation (True/False)
4. Loop control variables (i, counter)
5. Avoid infinite loops!
```python
# Always update condition!
i = 0
while i < 10:
    print(i)
    i = i+1  # Don't forget this!
```

---

<div align="left">
  <a href="#s1.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>

# Section 2. Conditionals in Python

<div align="left">
  <a href="#s1.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. `if` Statement Basics

```python
# Basic structure
age = 18
if age >= 18:
    print("You can vote!")
```

- `if` = Program's "what if" question
- Colon `:` is mandatory (show error without colon)
- Indentation = 4 spaces (never mix with Tab)

---

<div align="left">
  <a href="#s2.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. Indentation Demo

```python
# Correct vs Wrong
if True:
    print("Right")  # ← 4 spaces

if True:
print("Wrong")     # ← No indentation
```

---

<div align="left">
  <a href="#s2.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.3"></a>

---

## 2.3. Comparison Operators

```python
height = 175
print(height > 160)  # True
print(height == 170) # False

# Real-life example
bus_height_limit = 200
luggage_height = 210
if luggage_height > bus_height_limit:
    print("Cannot take bus")
```

---

<div align="left">
  <a href="#s2.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.4"></a>

---

## 2.4. Logical Operators

```python
# Weather check
is_raining = True
has_umbrella = False

if is_raining and has_umbrella:
    print("Go outside")
else:
    print("Stay home")
```

- `and`: Both must be True
- `or`: At least one True
- `not`: Reverse boolean

---

<div align="left">
  <a href="#s2.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.5"></a>

---

## 2.5. Common Mistake Fix

```python
# Wrong
if temperature = 30:
    print("Hot")

# Correct
if temperature == 30:
    print("Hot")
```

- Single `=` is assignment
- Double `==` is comparison

---

<div align="left">
  <a href="#s2.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.6"></a>

---

## 2.6. Multi-Condition Flow

```python
age = 15

if age < 13:
    print("Child ticket")
elif age < 18:
    print("Teen ticket")
else:
    print("Adult ticket")
```

---

<div align="left">
  <a href="#s2.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.7"></a>

---

## 2.7. Nested Conditions

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

- Each level needs 4-space indent
- Max 3 nesting levels recommended

---

<div align="left">
  <a href="#s2.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.8"></a>

---

## 2.8. Ticket System Example

```python
# Full example
age = 25
is_student = False
has_membership = True

if age < 5:
    print("Free ticket")
elif age < 18:
    print("Child ticket")
elif is_student:
    print("Student discount")
elif has_membership:
    print("Membership discount")
else:
    print("Regular ticket")
```

<br>

### Q: what if you are a 19 years old student without membership.

<br>

### Q: what if you are a 19 years old student with membership.

<br>

### Q: how can we get both the Student discount and the Membership discount

<br>

---

<div align="left">
  <a href="#s2.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.9"></a>

---

## 2.9. Truth Value Testing

```python
# Common False values:
- False
- None
- 0
- "" (empty string)
- [] (empty list)

name = ""
if not name:
    print("Name is required!")
```

---

<div align="left">
  <a href="#s2.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.10"></a>

---

## 2.10. Short-form Conditional Expression

```python
# Short form
temperature = 28
message = "Hot" if temperature > 25 else "OK"
print(message)

# preferred
temperature = 28
if temperature >25:
    message='Hot'
else:
    message='OK'
print(message)

```

- Use for simple two-way choices
- Not recommended for complex logic

---

<div align="left">
  <a href="#s2.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>

# Section 3. Loop Structures in Python

<div align="left">
  <a href="#s2.10">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. For Loop Basics

```python
# Like checking a shopping list
groceries = ["apple", "milk", "bread"]
for item in groceries:
    print("Don't forget to buy:", item)
```

<div class="mermaid">
flowchart TD
    A[Start] --> B{Items left?}
    B -->|Yes| C[Process item]
    C --> B
    B -->|No| D[End]
</div>


---

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. The range() Function

**Three usages:**
```python
# Single argument
for num in range(5):
    print(num)  # 0-4

# Two arguments
for num in range(2, 5):
    print(num)  # 2-4

# Three arguments
for num in range(0, 10, 2):
    print(num)  # 0,2,4,6,8
```

---

<div align="left">
  <a href="#s3.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 3.3. String Traversal with Index

```python
word = "hello"
for index, letter in enumerate(word):
    print("Character at position "+str(index)+": "+letter)
```
Output:
```
Character at position 0: h
Character at position 1: e
...
```

---

<div align="left">
  <a href="#s3.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 3.4. While Loop Mechanics

```python
# Like a persistent alarm clock
countdown = 3
while countdown > 0:
    print(countdown)
    countdown = countdown-1
print("Go!")
```

---

<div align="left">
  <a href="#s3.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.5"></a>

---

## 3.5. Termination Condition Design

```python
# Dangerous version (for demonstration)
# temperature = 25
# while temperature > 20:
#     print("AC running")
# Forgot to decrease temperature!
```

---

<div align="left">
  <a href="#s3.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.6"></a>

---

## 3.6. Safe Loop Writing Technique

**Always write termination first:**
```python
# 1. Set initial value
counter = 0
# 2. Define termination
MAX_ATTEMPTS = 3

while counter < MAX_ATTEMPTS:
    print("Attempt:", counter+1)
    counter += 1
```

---

<div align="left">
  <a href="#s3.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.7"></a>

---

## 3.7. Break Statement

```python
# Emergency exit example
passwords = ["123", "admin", "letmein"]
for pwd in passwords:
    if pwd == "admin":
        print("Security alert!")
        break
    print("Checking:", pwd)
```

---

<div align="left">
  <a href="#s3.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.8"></a>

---

## 3.8. Continue Statement

```python
# Skip odd numbers
for num in range(10):
    if num % 2 != 0:
        continue
    print(num, "is even")
```

---

<div align="left">
  <a href="#s3.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.9"></a>

---

## 3.9. Else Clause in Loops

```python
# Only executes if loop completes normally
numbers = [2, 4, 6]
for n in numbers:
    if n % 2 != 0:
        break
else:
    print("All numbers are even!")
```

---

<div align="left">
  <a href="#s3.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.10"></a>

---

## 3.10. Nested Loops: Multiplication Table

```python
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        print(str(i)+'x'+str(j)+'='+str(i*j), end="\t")
    print()  # New line after each row
```
Output:
```
1x1=1   1x2=2   1x3=3
2x1=2   2x2=4   2x3=6
3x1=3   3x2=6   3x3=9
```

---

<div align="left">
  <a href="#s3.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.11"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.11"></a>

---

## 3.11. Understanding Indentation Levels

```python
# Outer loop (level 1)
for x in range(2):
    # Inner loop (level 2)
    for y in range(2):
        # Nested block (level 3)
        if x == y:
            print("Match at "+str(x)+','+str(y))
    # Back to level 1
    print("----")
```

---

<div align="left">
  <a href="#s3.10">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>

# Section 4. Control Flow - Practical Examples

<div align="left">
  <a href="#s3.11">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. Smart Grade Rating System

### Basic Structure
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

<div class="mermaid">
flowchart TD
    A[Start] --> B[Input Score]
    B --> C{Score >=90?}
    C -->|Yes| D[Grade A]
    C -->|No| E{Score >=80?}
    E -->|Yes| F[Grade B]
    E -->|No| G{Score >=70?}
    G -->|Yes| H[Grade C]
    G -->|No| I[Grade D]
</div>


---

### Adding Loop for Multiple Inputs

### Continuous Processing
```python
while True:
    score = input("Enter score (q to quit): ")
    
    if score.lower() == 'q':
        break
        
    # Grade logic here
    print(f"Grade: {grade}")
```



<div class="mermaid">
flowchart TD
    A[Start] --> B{Input Score}
    B -->|q| C[Exit]
    B -->|Number| D[Process Grade]
    D --> B
</div>


---

<div align="left">
  <a href="#s4.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Number Guessing Game

### Core Game Loop
```python
import random
target = random.randint(1,100)

while True:
    guess = int(input("Guess (1-100): "))
    
    if guess == target:
        print("Correct!")
        break
    elif guess > target:
        print("Too high")
    else:
        print("Too low")
```

<div class="mermaid">
flowchart TD
    A[Generate Random Number] --> B{Guess?}
    B -->|Correct| C[Win]
    B -->|High| D[Prompt Lower]
    B -->|Low| E[Prompt Higher]
    D --> B
    E --> B
</div>


---

### Tracking Attempts

### Counter Implementation
```python
attempts = 0
while attempts < 5:
    # Game logic
    attempts += 1
    
if attempts == 5:
    print("Game Over! Number was", target)
```

---

### Victory/Failure Branches

### Final Conditions
```python
if guess == target:
    print(f"Victory in {attempts} tries!")
else:
    print(f"Failed! Number was {target}")
```

---

### Key Concepts Summary

1. `if-elif-else` for decision making
2. `while` loops for repeated actions
3. `try-except` for basic error handling
4. Counter variables for tracking state
5. Random module for game mechanics

---

### Final Complete Code Demo

### Grade System
```python
while True:
    # quit
    score = input("Enter score (q to quit): ")    
    if score.lower() == 'q':
        break
    # grade 
    score = float(input("Enter score (0-100): "))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    print("Grade:"+grade)

```

### Guessing Game
```python
import random
target = random.randint(1,100)
attempts = 0

while attempts < 5:
    guess = int(input("Guess (1-100): "))
    if guess == target:
        print("Correct!")
        break
    elif guess > target:
        print("Too high")
    else:
        print("Too low")
    attempts=attempts+1

if guess == target:
    print("Victory in"+str(attempts)+" tries!")
else:
    print("Failed! Number was "+str(target))

```

---

<div align="left">
  <a href="#s4.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>

# Section 5. Special Considerations

<div align="left">
  <a href="#s4.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Multi-line Conditional Statements

```python
# Recommended style
if (temperature > 100 
    and humidity < 70 
    and is_sunny == True):
    print("Heat warning!")
```


<div class="mermaid">
flowchart TD
    A[Check Conditions] --> B{All True?}
    B -->|Yes| C[Execute Code]
    B -->|No| D[Skip Block]
</div>


---

<div align="left">
  <a href="#s5.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Splitting Long Logical Expressions

```python
# Before
if (num > 0 and num%2 == 0 and num < 100 and name != "admin"):

# After
is_positive_even = num > 0 and num%2 == 0
within_limit = num < 100
valid_user = name != "admin"

if is_positive_even and within_limit and valid_user:
```

---

<div align="left">
  <a href="#s5.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 5.3. Debugging with Print Statements

```python
counter = 0
while counter < 3:
    print(f"DEBUG: Current counter - {counter}")  # Debug line
    counter += 1
```



<div class="mermaid">
flowchart TD
    S[Start] --> I[counter=0]
    I --> C{counter < 3?}
    C -->|Yes| P[Print counter]
    P --> U[counter +=1]
    U --> C
    C -->|No| E[End]
</div>


---

<div align="left">
  <a href="#s5.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.4"></a>

---

## 5.4. Using TODO Comments

```python
def calculate_discount(price):
    # TODO: Add seasonal discount logic
    # TODO: Implement user tier system
    return price * 0.9  # Temporary 10% discount
```

---

<div align="left">
  <a href="#s5.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.5"></a>

---

## 5.5. Missing Colon Error

```python
# Incorrect
while x < 5
    print(x)
    x += 1

# Correct
while x < 5:
    print(x)
    x += 1
```

---

<div align="left">
  <a href="#s5.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.6"></a>

---

## 5.6. Indentation Error Examples

```python
# Wrong mixing of spaces/tabs
def count_down(n):
while n > 0:  # Missing indentation
print(n)      # Wrong level
    n -= 1

# Correct
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
```

---

<div align="left">
  <a href="#s5.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.7"></a>

---

## 5.7. Floating Point Comparison

```python
# Unreliable
result = 0.1 + 0.2
if result == 0.3:
    print("Equal")

# Safe approach
tolerance = 1e-9
if abs(result - 0.3) < tolerance:
    print("Effectively equal")
```

---

<div align="left">
  <a href="#s5.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.8"></a>

---

## 5.8. While Loop Flow Control

```python
# Safe loop pattern
max_retries = 3
attempt = 0

while attempt < max_retries:
    print(f"Attempt {attempt+1}")
    # Your code here
    attempt = attempt + 1
```



<div class="mermaid">
flowchart TD
    S[Start] --> I[attempt=0]
    I --> C{attempt < 3?}
    C -->|Yes| L[Execute loop]
    L --> U[attempt +=1]
    U --> C
    C -->|No| E[End]
</div>


---

<div align="left">
  <a href="#s5.7">← Prev </a> | <a href="#all"> Home </a> 
</div>

<br>

End

