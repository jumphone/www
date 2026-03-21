[Back](https://www.bioinfo-lab.com/courses/Programming_I/w04_Control_Flow/)

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b> on Moodle by 23:59 this Sunday. 

This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

### Tips

“tab” type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

“history” You can see all the commands you have run before.

Try "ai", "aiw", and "aid"

<br>

---

### 1. Log into the remote Linux Server.

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---

### 2. Conditional Statements Practice

```
# Create a new script file
cd ~
nano traffic_light.py

# Type the following code:
light_color = input("Traffic light color: ")

if light_color == "red":
    print("STOP")
elif light_color == "yellow":
    print("SLOW DOWN")
elif light_color == "green":
    print("GO")
else:
    print("INVALID COLOR")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 traffic_light.py
```

**Expected Output:** The program will ask for input. Try entering "red", "yellow", "green", and other values to see different results.

<br>

---

### 3. While Loops Practice

```
# Create a new script file
cd ~
nano morning_run.py

# Type the following code:
import time
runs_remaining = 3
while runs_remaining > 0:
    time.sleep(1) # suppose you are a superman, 400m in 1 second 
    print("Morning run #"+str(4 - runs_remaining)+" completed!")
    runs_remaining -= 1
print("All runs finished!")

# Save and exit nano
# Run the script
python3 morning_run.py
```

**Expected Output:** The program will pause for 1 second between each run announcement, counting down from run #1 to #3, then print "All runs finished!"

<br>

---

### 4. For Loops and range() Practice

```
# Create a new script file
cd ~
nano loop_practice.py

# Type the following code:
# For loop with list
groceries = ["apple", "milk", "bread"]
for item in groceries:
    print("Don't forget to buy:", item)

print("\n--- range() examples ---")

# range(5) - single argument
for num in range(5):
    print("range(5):", num)

print()

# range(2, 5) - two arguments
for num in range(2, 5):
    print("range(2, 5):", num)

print()

# range(0, 10, 2) - three arguments
for num in range(0, 10, 2):
    print("range(0, 10, 2):", num)

# Save and exit nano
# Run the script
python3 loop_practice.py
```

**Expected Output:** The groceries list will be printed, followed by number sequences demonstrating the three range() usage patterns.

<br>

---

### 5. Vending Machine Simulation

```
# Create a new script file
cd ~
nano vending_machine.py

# Type the following code:
coins = 0
while coins < 5:
    insert_coins = int(input("Insert coin (1-3): "))
    coins = coins + insert_coins
    print("Total inserted: "+str(coins))
print("Here's your drink!")

# Save and exit nano
# Run the script
python3 vending_machine.py
```

**Questions to consider:**
- How can we limit the number of inserted coins each time?
- How can we get the extra coins?

<br>

---

### 6. Smart Grade Rating System

```
# Create a new script file
cd ~
nano grade_system.py

# Type the following code:
while True:
    score = input("Enter score (q to quit): ")
    
    if score.lower() == 'q':
        break
        
    score = float(score)
    
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
        
    print("Grade: " + grade)

# Save and exit nano
# Run the script
python3 grade_system.py
```

**Test Cases:** Try scores like 95, 82, 75, 60, and 'q' to quit.

<br>

---

### 7. Number Guessing Game

```
# Create a new script file
cd ~
nano guessing_game.py

# Type the following code:
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
    attempts = attempts + 1

if guess == target:
    print("Victory in "+str(attempts)+" tries!")
else:
    print("Failed! Number was "+str(target))

# Save and exit nano
# Run the script
python3 guessing_game.py
```

**Expected Output:** You have 5 attempts to guess a random number between 1-100 with "Too high"/"Too low" hints.

<br>

---

### 8. Loop Control Statements Practice

```
# Create a new script file
cd ~
nano loop_control.py

# Type the following code:
# Break statement example
print("--- Break example ---")
passwords = ["123", "admin", "letmein"]
for pwd in passwords:
    if pwd == "admin":
        print("Security alert!")
        break
    print("Checking:", pwd)

print("\n--- Continue example ---")
# Continue statement example
for num in range(10):
    if num % 2 != 0:
        continue
    print(num, "is even")

print("\n--- Else clause example ---")
# Else clause example
numbers = [2, 4, 6]
for n in numbers:
    if n % 2 != 0:
        break
else:
    print("All numbers are even!")

# Save and exit nano
# Run the script
python3 loop_control.py
```

**Expected Output:** Demonstrates break (stops at "admin"), continue (skips odd numbers), and else clause (executes when loop completes without break).

<br>

---

### 9. Common Pitfalls and Debugging

```
# Create a new script file
cd ~
nano pitfalls.py

# Type the following code:
# Missing colon error demonstration (commented out)
# if temperature = 30
#     print("Hot")

# Correct version
temperature = 30
if temperature == 30:
    print("Hot")

print("\n--- Indentation example ---")
# Proper indentation
def greet(name):
    message = "Hello, " + name
    return message

print(greet("Student"))

print("\n--- Floating point comparison ---")
# Unreliable comparison
result = 0.1 + 0.2
print("0.1 + 0.2 =", result)
print("result == 0.3:", result == 0.3)

# Safe approach
tolerance = 1e-9
if abs(result - 0.3) < tolerance:
    print("Effectively equal (safe comparison)")

# Save and exit nano
# Run the script
python3 pitfalls.py
```

**Key Takeaways:**
- Always use `==` for comparison, not `=`
- Maintain consistent 4-space indentation
- Be cautious with floating-point comparisons

<br>

---

### 10. Nested Loops Practice

```
# Create a new script file
cd ~
nano nested_loops.py

# Type the following code:
# Multiplication table
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        print(str(i)+'x'+str(j)+'='+str(i*j), end="\t")
    print()  # New line after each row

print("\n--- Nested with condition ---")
# Nested loops with if statement
for x in range(2):
    for y in range(2):
        if x == y:
            print("Match at "+str(x)+','+str(y))
    print("----")

# Save and exit nano
# Run the script
python3 nested_loops.py
```

**Expected Output:** A 3x3 multiplication table and a demonstration of nested loops with conditional logic.

<br>

---

End
