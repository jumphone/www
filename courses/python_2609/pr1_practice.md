
<br>

---------------------

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 


This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---------------------

### Tips

“tab” type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

“history” You can see all the commands you have run before.

Try "ai", "aiw", and "aid"


<br>

---------------------

### 1. Download & Install Termius

* Baidu Cloud Disk: [click](https://pan.baidu.com/s/10TpxA_oQHuVs4DL2qPQUdg?pwd=biuh) 

* Official Website: [https://termius.com/index.html](https://termius.com/index.html)

* Iphone & Android Phones: Download from App Store

<br>

---------------------

### 2. Register a Termius account.

<b> Termius is FREE! Do NOT subscribe! Use the free version directly. </b>

<br>

---------------------

### 3. Log into the remote Linux Server.

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dtX20260001)

Password: dt + Student ID + @biuh2026 (e.g. dtX20260001@biuh2026)

<br>

---------------------

### 4. Linux Basics

#### pwd, cd, ls

```
# show the path of your home directory
cd ~
pwd

# changes the current working directory to its immediate parent directory
cd ..
pwd

# show all the files and folders under current working directory
ls

# changes the current working directory to your home directory
cd ~
pwd
```

#### mkdir, touch

```
cd ~

# make sure that you are in your home directory
pwd

# create a new folder named "new_folder"
mkdir new_folder

# create a new empty file named "new_file.txt"
touch new_file.txt

# show all the files and folders under current working directory
ls
```

#### less, cat

```
# use less to check the content of a demo file. press "q" to quit
less /home/students/dt2026/resource/demo.txt

# use cat to show the entire content of a demo file.
cat /home/students/dt2026/resource/demo.txt

```

#### cp, mv rm

```
cd ~

# copy the demo.txt to your home directory
cp /home/students/dt2026/resource/demo.txt ~/demo.txt
ls

# move the your demo.txt to demo_mv.txt
mv demo.txt demo_mv.txt
ls

# remove the demo_mv.txt
rm demo_mv.txt
ls

# copy a folder
cp -r new_folder copy_folder
ls

# move a folder
mv new_folder move_folder
ls

# remove a folder
rm -rf copy_folder
ls

```

#### nano

```
cd ~
nano new_nano_file.txt

# write something into "new_nano_file.txt"
# save: Ctrl + O
# Exit: Ctrl + X

ls

# see the content of "new_nano_file.txt"
cat new_nano_file.txt

```

#### SFTP

```
# Use SFTP to upload and download some files.

```

<br>

---------------------

End

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 


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

### 2. Open Python Interactive Mode

Open your terminal (Termius or local terminal)

Type `python3` to enter interactive mode

You should see the Python version and the `>>>` prompt

<br>

---

### 3. Basic Python Commands in Interactive Mode

```
# Check Python version
import sys
print(sys.version)

# Simple arithmetic operations
2 + 3
10 - 4
5 * 6
20 / 4

# Exit interactive mode
exit()
```

<br>

---

### 4. Create and Run Your First Python Script

```
# Create a new Python script file
cd ~
nano hello.py

# Type the following code in nano:
print("Hello, World!")
name = "Python"
print("I am learning", name)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 hello.py
```

<br>

---

### 5. Variables and Data Types

```
# Create a new script file
cd ~
nano variables.py

# Type the following code:
# Integer
age = 25
print("Age:", age)
print("Type:", type(age))

# Float
height = 1.75
print("Height:", height)
print("Type:", type(height))

# String
name = "Alice"
print("Name:", name)
print("Type:", type(name))

# Type conversion
age_str = str(age)
print("Age as string:", age_str)
print("Type:", type(age_str))

# Save and exit nano
# Run the script
python3 variables.py
```

<br>

---

### 6. Operators Practice

```
# Create a new script file
cd ~
nano operators.py

# Type the following code:
# Arithmetic operators
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Comparison operators
print("a > b:", a > b)
print("a == b:", a == b)

# Logical operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Save and exit nano
# Run the script
python3 operators.py
```

<br>

---

### 7. String Operations

```
# Create a new script file
cd ~
nano strings.py

# Type the following code:
# String creation
greeting = "Hello, Python!"
print(greeting)

# String concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)

# String indexing
print("First character:", greeting[0])
print("Last character:", greeting[-1])

# String slicing
print("First 5 characters:", greeting[0:5])
print("Characters 7-12:", greeting[7:13])

# String methods
text = "  Hello World  "
print("Original:", text)
print("Stripped:", text.strip())
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

# Find and split
sentence = "Python is easy to learn"
print("Find 'easy':", sentence.find("easy"))
print("Split:", sentence.split())

# Join
words = ["Python", "is", "fun"]
joined = " ".join(words)
print("Joined:", joined)

# Save and exit nano
# Run the script
python3 strings.py
```

<br>

---

### 8. Comments and Indentation

```
# Create a new script file
cd ~
nano structure.py

# Type the following code:
# This is a single-line comment
# The following code demonstrates proper indentation

def greet(name):
    # This is an indented block (4 spaces)
    message = "Hello, " + name
    return message

# Main program
user = "Student"
result = greet(user)
print(result)

# Multi-line example with proper indentation
if user == "Student":
    print("Welcome to the course!")
    print("You are in the right place.")
else:
    print("Please check your user type.")

# Save and exit nano
# Run the script
python3 structure.py
```

<br>

---

### 9. Escape Characters and String Formatting

```
# Create a new script file
cd ~
nano formatting.py

# Type the following code:
# Escape characters
print("Line 1\nLine 2")  # Newline
print("Column 1\tColumn 2")  # Tab
print("He said \"Hello\"")  # Quotes

# String formatting examples
name = "Bob"
age = 20
print("Name: " + name + ", Age: " + str(age))

# Using f-strings (modern Python)
print(f"Name: {name}, Age: {age}")

# Using format method
print("Name: {}, Age: {}".format(name, age))

# Save and exit nano
# Run the script
python3 formatting.py
```

<br>

---

End


<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 

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

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 

This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

### Tips

“tab” type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

“history” You can see all the commands you have run before.

Try "ai", "aiw", and "aid"

<br>

---

### 1. Creating Your First Function

```
# Create a new Python script file
cd ~
nano sandwich_without_function.py

# Type the following code to show repetitive code:
print("1. Get bread")
print("2. Add filling")
print("3. Close sandwich")
print("------")
print("1. Get bread")
print("2. Add filling")
print("3. Close sandwich")
print("------")
print("1. Get bread")
print("2. Add filling")
print("3. Close sandwich")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 sandwich_without_function.py
```

Now create a function to solve this:

```
# Create a new script file
cd ~
nano sandwich_function.py

# Type the following code:
def make_sandwich():
    print("1. Get bread")
    print("2. Add filling")
    print("3. Close sandwich")
    print("------")

make_sandwich()
make_sandwich()
make_sandwich()

# Save and exit nano
# Run the script
python3 sandwich_function.py
```

<br>

---

### 2. Functions with Parameters

```
# Create a new script file
cd ~
nano flexible_sandwich.py

# Type the following code:
def make_sandwich(filling):
    print(f"Making {filling} sandwich:")
    print("1. Get bread")
    print("2. Add " + str(filling))
    print("3. Close sandwich")
    print("------")

make_sandwich("ham")
make_sandwich("cheese")
make_sandwich("tuna")

# Save and exit nano
# Run the script
python3 flexible_sandwich.py
```

## Question: How can we write a function that only greets Alice specially?

```
# Create a new script file
cd ~
nano greet_alice.py

# Type the following code:
def greet(name):
    if name == "Alice":
        print("Hello, " + str(name) + "! Welcome back!")
    else:
        print("Hello, " + str(name))

greet("Alice")
greet("Bob")

# Save and exit nano
# Run the script
python3 greet_alice.py
```

<br>

---

### 3. Functions with Return Values

```
# Create a new script file
cd ~
nano circle_calculator.py

# Type the following code:
def circle_area(radius):
    area = 3.14 * radius ** 2
    return area

# Use the function
result1 = circle_area(5)
print("Circle area:", result1)

result2 = circle_area(30)
print("Pizza area:", result2)

# Use return value in calculation
pizza_price = circle_area(30) * 0.02
print("Pizza price: $", pizza_price)

# Save and exit nano
# Run the script
python3 circle_calculator.py
```

<br>

---

### 4. Creating and Using Modules

```
# Create a module file
cd ~
nano kitchen.py

# Type the following code:
def microwave_beep():
    print("BEEP! BEEP! BEEP!")

def oven_timer():
    print("DING! Food is ready!")

# Save and exit nano
```

Now create a script that uses this module:

```
# Create a new script file
cd ~
nano use_kitchen.py

# Type the following code:
import kitchen

kitchen.microwave_beep()
kitchen.oven_timer()

# Save and exit nano
# Run the script
python3 use_kitchen.py
```

Create another module example:

```
# Create a cooking module
cd ~
nano cooking_module.py

# Type the following code:
def prepare_dish(dish_name):
    print("Preparing " + str(dish_name) + "...")
    print("1. Gather ingredients")
    print("2. Follow recipe steps")

# Save and exit nano
```

Use the cooking module:

```
# Create a new script file
cd ~
nano make_dinner.py

# Type the following code:
import cooking_module

cooking_module.prepare_dish("pasta")
cooking_module.prepare_dish("salad")

# Save and exit nano
# Run the script
python3 make_dinner.py
```

<br>

---

### 5. Advanced Function Parameters

```
# Create a new script file
cd ~
nano pizza_order.py

# Type the following code:
def make_pizza(size, toppings):
    print("Making " + str(size) + "cm pizza with:")
    for topping in toppings:
        print("- " + str(topping))

# Positional arguments
make_pizza(30, ["mushrooms", "olives"])

# Keyword arguments
make_pizza(toppings=["cheese", "tomato"], size=20)

# Save and exit nano
# Run the script
python3 pizza_order.py
```

## Question: What happens if you swap the order of positional arguments?

```
# Try this bad example:
make_pizza(["pepperoni"], 25)
```

Now create a function with default parameters:

```
# Create a new script file
cd ~
nano shipping_calculator.py

# Type the following code:
def calculate_shipping(weight, base_fee=5.0):
    price = weight * 1.2 + base_fee
    return price

# Use default base_fee
print("Shipping 3.5kg:", calculate_shipping(3.5))

# Override default base_fee
print("Shipping 2.0kg with discount:", calculate_shipping(2.0, 4.0))

# Save and exit nano
# Run the script
python3 shipping_calculator.py
```

<br>

---

### 6. Variable Scope

```
# Create a new script file
cd ~
nano scope_demo.py

# Type the following code:
temperature = 25  # Global variable

def adjust_temp():
    temperature = 18  # Local variable
    print("Inside function: " + str(temperature) + "°C")

adjust_temp()
print("Outside function: " + str(temperature) + "°C")

# Save and exit nano
# Run the script
python3 scope_demo.py
```

Now test the global keyword:

```
# Create a new script file
cd ~
nano global_demo.py

# Type the following code:
score = 0  # Global variable

def update_points():
    global score
    score = score + 10
    print("New score: " + str(score))

update_points()
update_points()
print("Final score:", score)

# Save and exit nano
# Run the script
python3 global_demo.py
```

<br>

---

### 7. Practical Example: Password Generator

```
# Create a new script file
cd ~
nano password_generator.py

# Type the following code:
import random

def generate_password(length=8):
    chars = "abcdefghijkmnpqrstuvwxyz23456789"
    this_password = ''
    i = 1
    while(i <= length):
        this_password = this_password + random.choice(chars)
        i = i + 1
    return this_password

# Test the function
print("Default 8-char password:", generate_password())
print("12-char password:", generate_password(12))

# Save and exit nano
# Run the script
python3 password_generator.py
```

## Question: How can we add random uppercase and lowercase characters?
## Hint: random.random(), lower(), upper()

```
# Create an enhanced version
cd ~
nano password_enhanced.py

# Type the following code:
import random

def generate_password_enhanced(length=8):
    chars = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    this_password = ''
    i = 1
    while(i <= length):
        this_password = this_password + random.choice(chars)
        i = i + 1
    return this_password

print("Enhanced password:", generate_password_enhanced(10))

# Save and exit nano
# Run the script
python3 password_enhanced.py
```

<br>

---

### 8. Practical Example: Simple Calculator

```
# Create a new script file
cd ~
nano calculator.py

# Type the following code:
def calculator(a, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"

# Test the calculator
print("5 + 3 =", calculator(5, 3))
print("5 - 3 =", calculator(5, 3, "-"))
print("5 * 3 =", calculator(5, 3, "*"))
print("6 / 2 =", calculator(6, 2, "/"))
print("2.5 + 4 =", calculator(2.5, 4, "+"))

# Save and exit nano
# Run the script
python3 calculator.py
```

## Question: How can we add "*" and "/"? (Already included above)

<br>

---

### 9. Practical Example: Temperature Converter

```
# Create a new script file
cd ~
nano temperature_converter.py

# Type the following code:
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Test conversions
print("0°C =", c_to_f(0), "°F")
print("100°C =", c_to_f(100), "°F")
print("32°F =", f_to_c(32), "°C")
print("212°F =", f_to_c(212), "°C")

# Save and exit nano
# Run the script
python3 temperature_converter.py
```

## Question: How can we check the correctness of "f_to_c"?

```
# Create a verification script
cd ~
nano verify_converter.py

# Type the following code:
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Check if conversions are inverse operations
test_temp = 25
converted = c_to_f(test_temp)
back_to_original = f_to_c(converted)

print("Original:", test_temp, "°C")
print("Converted:", converted, "°F")
print("Back to Celsius:", back_to_original, "°C")
print("Verification:", "PASS" if abs(test_temp - back_to_original) < 0.01 else "FAIL")

# Save and exit nano
# Run the script
python3 verify_converter.py
```

<br>

---

### 10. Multi-Return Values and Unpacking

```
# Create a new script file
cd ~
nano box_calculator.py

# Type the following code:
def box_calculator(length, width, height):
    volume = length * width * height
    surface = 2 * (length*width + length*height + width*height)
    return volume, surface  # Returns a tuple!

# Method 1: Get as tuple
dimensions = box_calculator(5, 3, 2)
print("Volume: " + str(dimensions[0]) + ", Surface: " + str(dimensions[1]))

# Method 2: Direct unpacking
vol, surf = box_calculator(2, 2, 2)
print("Perfect cube volume: " + str(vol) + " cubic units")

# Save and exit nano
# Run the script
python3 box_calculator.py
```

<br>

---

### 11. BMI Calculator Function

```
# Create a new script file
cd ~
nano bmi_calculator.py

# Type the following code:
def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    bmi = weight / (height ** 2)
    return bmi

# Test with different values
print("BMI (70kg, 1.75m):", calculate_bmi(70, 1.75))
print("BMI (65kg, 1.68m):", calculate_bmi(65, 1.68))

# Health tip: Normal BMI range is 18.5 - 24.9

# Save and exit nano
# Run the script
python3 bmi_calculator.py
```

## Question: BMI and weight => height (reverse calculation)

```
# Create a new script file
cd ~
nano weight_to_height.py

# Type the following code:
def calculate_height_for_bmi(weight, target_bmi):
    """Calculate required height for a target BMI"""
    # BMI = weight / height^2
    # height^2 = weight / BMI
    # height = sqrt(weight / BMI)
    return (weight / target_bmi) ** 0.5

# Example: What height gives BMI 22 for 70kg?
height_needed = calculate_height_for_bmi(70, 22)
print("For 70kg to have BMI 22, height should be: " + str(round(height_needed, 2)) + "m")

# Save and exit nano
# Run the script
python3 weight_to_height.py
```

<br>

---

### 12. Math Library Practice

```
# Create a new script file
cd ~
nano math_practice.py

# Type the following code:
import math

# Calculate hypotenuse
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is: " + str(c))

# Use math.pi
radius = 5
area = math.pi * radius ** 2
print("Circle area with pi: " + str(area))

# Use math.pow
power_result = math.pow(2, 3)
print("2 to the power of 3: " + str(power_result))

# Save and exit nano
# Run the script
python3 math_practice.py
```

## Question: Change f-string into "+" format

```
# Create a version without f-strings
cd ~
nano math_practice_plus.py

# Type the following code:
import math

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is: " + str(c))

radius = 5
area = math.pi * radius ** 2
print("Circle area with pi: " + str(area))

# Save and exit nano
# Run the script
python3 math_practice_plus.py
```

<br>

---

### 13. Random Library Practice

```
# Create a new script file
cd ~
nano random_practice.py

# Type the following code:
from random import randint, choice

# Random integer
lottery = [randint(1, 50) for _ in range(6)]
print("Winning numbers:", lottery)

# Random choice
participants = ["Alice", "Bob", "Charlie", "Diana"]
winner = choice(participants)
print("Congratulations " + winner + "!")

# Save and exit nano
# Run the script
python3 random_practice.py
```

<br>

---

### 14. Time Library Demo

```
# Create a new script file
cd ~
nano countdown.py

# Type the following code:
import time

print("Starting countdown:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Blast off!")

# Save and exit nano
# Run the script
python3 countdown.py
```

<br>

---

### 15. Good Function Naming Practice

```
# Create a new script file
cd ~
nano good_names.py

# Type the following code:
# Good examples
def calculate_tax(income):
    return income * 0.15

def get_user_profile(user_id):
    return "Profile for user " + str(user_id)

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Bad examples (avoid these)
def tax(inc):          # Too vague
    return inc * 0.15

def user(id):          # Verb missing
    return "User " + str(id)

def temp_conv(c):      # Unclear abbreviation
    return (c * 9/5) + 32

# Test good functions
print("Tax on 50000:", calculate_tax(50000))
print("User profile:", get_user_profile(123))
print("25°C to °F:", convert_to_fahrenheit(25))

# Save and exit nano
# Run the script
python3 good_names.py
```

<br>

---

### 16. Module Search Path

```
# Create a new script file
cd ~
nano module_path.py

# Type the following code:
import sys

print("Python looks for modules in these locations:")
for path in sys.path:
    print("- " + str(path))

# Save and exit nano
# Run the script
python3 module_path.py
```

<br>

---

### 17. Import Best Practices

```
# Create a new script file
cd ~
nano import_best_practice.py

# Type the following code:
# Keep imports at top of file
import math
import random as rd
from time import sleep

# Use alias for long module names
print("Random number:", rd.randint(1, 100))

# Use specific function import
print("Countdown:")
for i in range(3, 0, -1):
    print(i)
    sleep(1)

print("Done!")

# Save and exit nano
# Run the script
python3 import_best_practice.py
```

<br>

---

End

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 

This is an important part of your "General Performance". Please ensure timely submission!!!

### Recommended: 2、3、4、5、6、8、14、15、18、22


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

### 2. Create and Run Your First List Script

```
# Create a new Python script file
cd ~
nano list_demo.py

# Type the following code in nano:
# Shopping list example
groceries = ["apples", "milk", "eggs", "bread"]
print("My shopping list:", groceries)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 list_demo.py
```

<br>

---

### 3. Four Ways to Create Lists

```
# Create a new script file
cd ~
nano list_creation.py

# Type the following code:
# Method 1: Square brackets
colors = ["red", "green", "blue"]
print("Colors:", colors)

# Method 2: list() constructor
numbers = list((1, 2, 3))
print("Numbers:", numbers)

# Method 3: List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# Method 4: Convert from string
word = list("hello")
print("Word as list:", word)

# Save and exit nano
# Run the script
python3 list_creation.py
```

<br>

---

### 4. Accessing and Slicing List Elements

```
# Create a new script file
cd ~
nano list_access.py

# Type the following code:
games = ["Mario", "Zelda", "Pokémon"]
print("First game:", games[0])
print("Last game:", games[-1])

months = ["Jan", "Feb", "Mar", "Apr", "May"]
print("Months 1-3:", months[1:3])
print("First two:", months[:2])
print("Last two:", months[3:])

# Save and exit nano
# Run the script
python3 list_access.py
```

<br>

---

### 5. Modifying Lists - Adding Items

```
# Create a new script file
cd ~
nano list_add.py

# Type the following code:
todo = ["wake up"]
todo.append("brush teeth")
todo.insert(1, "make bed")
print("Todo list:", todo)

# Demonstrate insert positions
todo.insert(0, 'start')  # Add at beginning
print("After insert(0, 'start'):", todo)

todo.insert(len(todo), 'end1')  # Add at end (like append)
print("After insert(len(todo), 'end1'):", todo)

todo.insert(-1, 'end2')  # Insert before last element
print("After insert(-1, 'end2'):", todo)

# Save and exit nano
# Run the script
python3 list_add.py
```

<br>

---

### 6. Modifying Lists - Removing Items

```
# Create a new script file
cd ~
nano list_remove.py

# Type the following code:
pets = ["cat", "dog", "hamster"]
pets.remove("dog")
last = pets.pop()
print("Pets after removal:", pets)
print("Popped item:", last)

# Demonstrate remove with duplicates
pets = ["dog", "bird", "dog", "cat", "dog"]
pets.remove("dog")  # Only removes first occurrence
print("After removing first 'dog':", pets)

# Find index of an element
dog_index = pets.index('dog')
print("Index of 'dog':", dog_index)

# Save and exit nano
# Run the script
python3 list_remove.py
```

<br>

---

### 7. Sorting Lists

```
# Create a new script file
cd ~
nano list_sort.py

# Type the following code:
scores = [88, 92, 75, 100]
scores.sort()
print("Sorted scores:", scores)

scores.sort(reverse=True)
print("Reverse sorted:", scores)

# Save and exit nano
# Run the script
python3 list_sort.py
```

<br>

---

### 8. Student Grades System Practice

```
# Create a new script file
cd ~
nano student_grades.py

# Type the following code:
students = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

# Calculate average
total = sum(scores)
average = total / len(scores)
print(f"Class average: {average}")

# Alternative format using concatenation
print("Class average: " + str(average))

# Combine and sort by score
combined = []
i = 0
while i < len(scores):
    combined.append([scores[i], students[i]])
    i = i + 1

combined.sort()
print("Ranking (low to high):")
for one in combined:
    print(f"{one[1]}: {one[0]}")

# Sort in reverse order
combined.sort(reverse=True)
print("Ranking (high to low):")
for one in combined:
    print(f"{one[1]}: {one[0]}")

# Save and exit nano
# Run the script
python3 student_grades.py
```

<br>

---

### 9. Understanding Tuples - Immutability Demo

```
# Create a new script file
cd ~
nano tuple_demo.py

# Type the following code:
# Lists are mutable
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"
print("Modified list:", fruits)

# Tuples are immutable
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Attempting to modify will cause error
# colors[0] = "pink"  # Uncomment to see TypeError

# Valid tuple usage
black = (0, 0, 0)
current_position = (37.7749, -122.4194)
print("Color tuple:", black)
print("Position tuple:", current_position)

# Save and exit nano
# Run the script
python3 tuple_demo.py
```

<br>

---

### 10. Tuple Unpacking

```
# Create a new script file
cd ~
nano tuple_unpack.py

# Type the following code:
# Basic unpacking
dimensions = (1920, 1080)
width, height = dimensions
print(f"Screen: {width}x{height}")

# Swapping variables
a = 5
b = 10
a, b = b, a
print(f"Swapped: a={a}, b={b}")

# Ignoring values
coordinates = (45, -73, 100)
lat, lon, _ = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Multiple assignment with *middle
numbers = (3, 1, 4, 1, 5, 9)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Save and exit nano
# Run the script
python3 tuple_unpack.py
```

<br>

---

### 11. Single-element Tuple Trap

```
# Create a new script file
cd ~
nano tuple_single.py

# Type the following code:
# Common mistake
not_a_tuple = (42)
print("Type of (42):", type(not_a_tuple))

# Correct way
proper_tuple = (42,)
print("Type of (42,):", type(proper_tuple))

# Accessing elements
print("First element:", proper_tuple[0])
# print("Second element:", proper_tuple[1])  # Uncomment to see IndexError

# Save and exit nano
# Run the script
python3 tuple_single.py
```

<br>

---

### 12. Returning Multiple Values from Functions

```
# Create a new script file
cd ~
nano tuple_return.py

# Type the following code:
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return (area, circumference)

# Using tuple return
results = circle_calc(5)
print(f"Area: {results[0]}, Circumference: {results[1]}")

# Better usage with unpacking
area, circ = circle_calc(7)
print(f"Area is {area} units")
print(f"Circumference is {circ} units")

# Save and exit nano
# Run the script
python3 tuple_return.py
```

<br>

---

### 13. When to Use Tuples and Tuple Operations

```
# Create a new script file
cd ~
nano tuple_usage.py

# Type the following code:
# Dictionary keys (tuples work, lists don't)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
print("Location lookup:", locations[(40.7128, -74.0060)])

# Tuple operations
my_tuple = (1, 2, 3, 2, 2)
print("Length:", len(my_tuple))
print("Count of 2:", my_tuple.count(2))
print("Index of 3:", my_tuple.index(3))
print("2 in tuple:", 2 in my_tuple)

# Remember: No append/remove/pop methods for tuples

# Save and exit nano
# Run the script
python3 tuple_usage.py
```

<br>

---

### 14. Creating Dictionaries

```
# Create a new script file
cd ~
nano dict_create.py

# Type the following code:
# Method 1: Curly braces
student = {"name": "Emma", "age": 20, "major": "CS"}
print("Student:", student)

# Method 2: dict() constructor
colors = dict(red="#FF0000", green="#00FF00")
print("Colors:", colors)

# Method 3: List of tuples
weekdays = dict([(1, "Mon"), (2, "Tue"), (3, "Wed")])
print("Weekdays:", weekdays)

# Phone book example
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print("Alice's number:", phone_book["Alice"])

# Save and exit nano
# Run the script
python3 dict_create.py
```

<br>

---

### 15. Modifying Dictionaries

```
# Create a new script file
cd ~
nano dict_modify.py

# Type the following code:
animal_sounds = {}
animal_sounds["dog"] = "Woof!"
animal_sounds["cat"] = "Mew"
animal_sounds["cat"] = "Meow"  # Update existing
print("Animal sounds:", animal_sounds)

# Removing entries
del animal_sounds["dog"]
removed = animal_sounds.pop("cat")
print("Removed value:", removed)
print("After removals:", animal_sounds)

# Safe access with get()
grades = {"Math": 90, "Science": 85}
print("History grade:", grades.get("History", "Subject not found"))

# Save and exit nano
# Run the script
python3 dict_modify.py
```

<br>

---

### 16. Building a Simple Translator

```
# Create a new script file
cd ~
nano translator.py

# Type the following code:
translator = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}

word = input("Enter English word: ").lower()
translation = translator.get(word, "Translation not available")
print(f"Spanish: {translation}")

# Handle unknown words
if translation == "Translation not available":
    print("Please check spelling!")
    print("Current dictionary words:", list(translator.keys()))

# Save and exit nano
# Run the script
python3 translator.py
```

<br>

---

### 17. Dictionary Methods and Real-World Example

```
# Create a new script file
cd ~
nano dict_methods.py

# Type the following code:
my_dict = {"a": 1, "b": 2}
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))

# Movie ratings example
movies = {
    "Moana": 7.5,
    "Toy Story": 8.6,
    "Frozen": 8.5
}

movie = input("Enter movie title: ")
print(f"Rating: {movies.get(movie, 'Not in database')}/10")

# Mixed data types in dictionaries
mixed_example = {
    1: "Number key",
    (2,3): "Tuple key",
    "list": ["can", "be", "value"]
}
print("Mixed dictionary:", mixed_example)

# Save and exit nano
# Run the script
python3 dict_methods.py
```

<br>

---

### 18. Understanding Sets - Automatic Deduplication

```
# Create a new script file
cd ~
nano set_dedup.py

# Type the following code:
# List vs Set comparison
fruits_list = ['apple', 'banana', 'apple', 'orange']
fruits_set = {'apple', 'banana', 'apple', 'orange'}

print(f"List: {fruits_list}")
print(f"Set: {fruits_set}")

# Removing duplicate votes
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_voters = set(votes)
print(f"Total votes: {len(votes)}")
print(f"Unique voters: {len(unique_voters)}")

# Get unique letters in a name
name = "yourname"
unique_letters = set(name)
print(f"Unique letters in '{name}': {unique_letters}")

# Save and exit nano
# Run the script
python3 set_dedup.py
```

<br>

---

### 19. Set Operations

```
# Create a new script file
cd ~
nano set_operations.py

# Type the following code:
art_students = {'Tom', 'Alice', 'Bob', 'Eve'}
music_students = {'Alice', 'Eve', 'John'}

# Intersection (common elements)
both = art_students & music_students
print(f"Students in both clubs: {both}")

# Union (combine sets)
week1_customers = {'Alice', 'Bob'}
week2_customers = {'Bob', 'Charlie'}
all_customers = week1_customers | week2_customers
print(f"All customers: {all_customers}")

# Difference (elements in first but not second)
available_colors = {'red', 'blue', 'green'}
used_colors = {'blue', 'yellow'}
remaining = available_colors - used_colors
print(f"Remaining colors: {remaining}")

# Save and exit nano
# Run the script
python3 set_operations.py
```

<br>

---

### 20. Set Methods and Voting System

```
# Create a new script file
cd ~
nano set_voting.py

# Type the following code:
# Counting unique votes with vote frequency
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
unique_votes = set(votes)
print(f"Candidates: {', '.join(unique_votes)}")

# Get vote counts using dictionary
vote_counts = {}
for candidate in votes:
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1
print("Vote counts:", vote_counts)

# Friend finder system
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Charlie', 'Diana', 'Eve'}
common = alice_friends & bob_friends
print(f"Common friends: {common}")

alice_friends.add('Eve')
print(f"Updated Alice's friends: {alice_friends}")

# Set methods demo
s = {'a', 'b', 'c'}
s.add('x')
print("After add:", s)
s.remove('b')
print("After remove:", s)

# Save and exit nano
# Run the script
python3 set_voting.py
```

<br>

---

### 21. Data Structures in Action - Mutable vs Immutable

```
# Create a new script file
cd ~
nano data_structure_mutable.py

# Type the following code:
# List (mutable)
a = []
def add_list():
    a.append(1)
add_list()
print("List after function call:", a)

# Set (mutable)
a = set()
def add_set():
    a.add(1)
add_set()
print("Set after function call:", a)

# Dictionary (mutable)
a = {}
def add_dict():
    a[1] = 1
add_dict()
print("Dict after function call:", a)

# Integer (immutable)
a = 0
def add_int():
    # This would cause error: a = a + 1
    # Because 'a' is local to function
    pass
add_int()
print("Integer unchanged:", a)

# Save and exit nano
# Run the script
python3 data_structure_mutable.py
```

<br>

---

### 22. Student Information System

```
# Create a new script file
cd ~
nano student_system.py

# Type the following code:
students = []

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")
    
    new_student = {
        "name": name,
        "age": age,
        "major": major
    }
    students.append(new_student)
    print("Student added!")

# Add two students
add_student()
add_student()

# Sort students by age
students.sort(key=lambda x: x['age'])
print("\nStudents sorted by age:")
for s in students:
    print(f"{s['name']}: {s['age']} years, {s['major']}")

# Save and exit nano
# Run the script
python3 student_system.py
```

<br>

---

### 23. Word Frequency Analyzer

```
# Create a new script file
cd ~
nano word_frequency.py

# Type the following code:
text = "apple banana orange apple pear orange apple ok yes yes ok no no want"
words = text.lower().split()
print("Words:", words)

# Count word frequencies
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Word counts:", word_counts)

# Find top 5 words
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 words:")
for i in range(min(5, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{i+1}. {word}: {count}")

# Save and exit nano
# Run the script
python3 word_frequency.py
```

<br>

---

End

<br>

---

## Python File Operations Practice Guide

<br>

#### Recommended: 3, 4, 5, 10, 12, 15, 17, 19, 23, 33, 35 

<br>

---

### Section 1: File Operations Basics

#### 1: Understanding File Types
```python
# Text files vs Binary files
# Text files: .txt, .csv, .py (human-readable)
# Binary files: .jpg, .docx, .exe (special format)
```

#### 2: Working with File Paths
```python
# Absolute path (full address)
absolute_path = "/home/student/documents/diary.txt"

# Relative path (from current location)
relative_path = "../pictures/vacation.jpg"

# Current working directory
import os
print(os.getcwd())
```

#### 3: Opening Files in Different Modes
```python
# Create a test file first
with open("test.txt", "w") as f:
    f.write("Hello\nWorld\n")

# Read mode
f = open("test.txt", "r")
content = f.read()
f.close()
print("Read mode:", content)

# Write mode (overwrites)
f = open("test.txt", "w")
f.write("New content")
f.close()

# Append mode
f = open("test.txt", "a")
f.write("\nAppended line")
f.close()

```

#### 4: Reading Files with read(), readline(), readlines()
```python
# Create test file
with open("classlist.txt", "w") as f:
    f.write("Alice\nBob\nCharlie")

# Read entire file
file = open("classlist.txt", "r")
print("read():", file.read())
file.close()

# Read line by line
file = open("classlist.txt", "r")
print("readline():", file.readline().strip())
print("readline():", file.readline().strip())
file.close()

# Read all lines as list
file = open("classlist.txt", "r")
lines = file.readlines()
print("readlines():", lines)
file.close()

# Process lines with strip()
file = open("classlist.txt", "r")
for student in file.readlines():
    print(f"Hello {student.strip()}!")
file.close()
```

#### 5: Writing Files with write() vs writelines()
```python
# Using write()
file = open("groceries.txt", "w")
file.write("Milk\n")
file.write("Eggs\nBread\n")
file.close()

# Using writelines()
items = ["Apples\n", "Coffee\n", "Sugar\n"]
file = open("shopping.txt", "w")
file.writelines(items)
file.close()

# Verify content
with open("groceries.txt", "r") as f:
    print("groceries.txt:\n", f.read())

with open("shopping.txt", "r") as f:
    print("shopping.txt:\n", f.read())
```

#### 6: Complete Case - Read Class List
```python
# Create the file
with open("classlist.txt", "w") as f:
    f.write("Alice\nBob\nCharlie")

# Read and process
file = open("classlist.txt", "r")
students = file.readlines()
file.close()

for student in students:
    print(f"Hello {student.strip()}!")

# Expected output:
# Hello Alice!
# Hello Bob!
# Hello Charlie!
```

#### 7: Complete Case - Create Shopping List
```python
# Create shopping list
file = open("groceries.txt", "w")
file.write("Shopping List:\n")
file.write("- Milk\n- Eggs\n- Bread")
file.close()

# Verify
with open("groceries.txt", "r") as f:
    print(f.read())

# Expected file contents:
# Shopping List:
# - Milk
# - Eggs
# - Bread
```

#### 8: Complete Case - Append to Diary
```python
# Create initial diary entry
with open("diary.txt", "w") as f:
    f.write("2024-03-01: Learned Python basics")

# Append new entry
file = open("diary.txt", "a")
file.write("\n2024-06-01: Learned file operations!")
file.close()

# Verify
with open("diary.txt", "r") as f:
    print(f.read())

# Expected file contents:
# 2024-03-01: Learned Python basics
# 2024-06-01: Learned file operations!
```

#### 9: Important Reminders
```python
# 1. Always close files!
f = open("test.txt", "w")
f.write("content")
f.close()  # Don't forget!

# 2. Double-check file modes
# "w" overwrites, "a" appends - be careful!

# 3. Use relative paths for portability
# Good: "data/file.txt"
# Bad: "/home/user/specific/path/data/file.txt"

# 4. Test with small files first
# Always test file operations on test files
```

<br>
<br>
<br>
<br>
<br>

---

### Section 2: The Magic of `with` Statement

#### 10: Understanding `with` Syntax
```python
# Basic syntax
with open('test.txt', 'w') as f:
    f.write("Using with statement")
# File automatically closes here

# Verify it's closed
print("File closed?", f.closed)
```

#### 11: Compare with/without `with`
```python
# Without with (problematic)
f = open('test.txt', 'r')
content = f.read()
# If exception occurs here, file remains open
# f.close() might be skipped

# With with (safe)
with open('test.txt', 'r') as f:
    content = f.read()
# File automatically closes, even with exceptions
```

#### 12: Handling Multiple Files
```python
# Create source file
with open('original.txt', 'w') as f:
    f.write("This is the original content")

# Copy file contents safely
with open('original.txt', 'r') as src:
    with open('backup.txt', 'w') as dst:
        dst.write(src.read())

# Verify both files
with open('original.txt', 'r') as f:
    print("Original:", f.read())

with open('backup.txt', 'r') as f:
    print("Backup:", f.read())
```

#### 13: Complete Case - Read Config File
```python
# Create config file
with open('config.cfg', 'w') as f:
    f.write("30\n100")

# Read configuration
with open('config.cfg', 'r') as config_file:
    settings = config_file.readlines()

print("Server timeout:", settings[0].strip())
print("Max users:", settings[1].strip())
```

#### 14: Complete Case - Safe File Copy (Binary)
```python
# Create a binary file (simulate image)
with open('cat.jpg', 'wb') as f:
    f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR')

# Copy binary file safely
with open('cat.jpg', 'rb') as source_cat:
    with open('cat_backup.jpg', 'wb') as backup_cat:
        backup_cat.write(source_cat.read())

# Verify file sizes
import os
print("Original size:", os.path.getsize('cat.jpg'))
print("Backup size:", os.path.getsize('cat_backup.jpg'))
```

#### 15: Complete Case - Program Logging
```python
# Log program activity
with open('app.log', 'a') as log_file:
    log_file.write('Program started\n')
    # Simulate some operations
    log_file.write('Operation 1 completed\n')
    log_file.write('Operation 2 completed\n')

# Read log
with open('app.log', 'r') as log_file:
    print("Log contents:\n", log_file.read())
```

#### 16: Recipe Reader Demo
```python
# Create recipe file
with open('recipe.txt', 'w') as f:
    f.write("Pasta\nBoil water\nAdd pasta\nCook for 10 min")

# Read recipe
with open('recipe.txt', 'r') as recipe:
    print("Today's Recipe:")
    for line in recipe:
        print(f"{line.strip()}")

# File closed automatically!
```

<br>
<br>
<br>
<br>
<br>

---

### Section 3: File System Operations

#### 17: Path Operations with `os.path`
```python
import os

# Check if file exists
print("Does test.txt exist?", os.path.exists("test.txt"))

# Check file type
print("Is test.txt a file?", os.path.isfile("test.txt"))
print("Is current directory a dir?", os.path.isdir("."))

# Get absolute path
print("Absolute path:", os.path.abspath("test.txt"))
```

#### 18: Get File Size
```python
import os

# Create test file
with open("secrets.txt", "w") as f:
    f.write("password")

# Get file size
size = os.path.getsize("secrets.txt")
print(f"File size: {size} bytes")

# Note: 1024 bytes = 1KB, 1024KB = 1MB
```

#### 19: Create Directories
```python
import os

# Create simple directory
os.mkdir("experiments")
print("Created: experiments")

# Try creating nested directory (will fail)
try:
    os.mkdir("projects/2024")
except FileNotFoundError as e:
    print("Error:", e)

# Create nested directories properly
os.makedirs("projects/2024", exist_ok=True)
print("Created: projects/2024")
```

#### 20: List Directory Contents
```python
import os

# Create some files first
with open("file1.txt", "w") as f: f.write("1")
with open("file2.txt", "w") as f: f.write("2")
os.mkdir("subdir")

# List contents
files = os.listdir(".")
print("Directory contents:", files)

# Remember: Returns names only, not full paths
for item in files:
    print(f"Item: {item}, Full path: {os.path.join('.', item)}")
```

#### 21: Rename Files and Directories
```python
import os

# Create test file
with open("old.txt", "w") as f: f.write("content")

# Rename file
os.rename("old.txt", "new.txt")
print("Renamed: old.txt -> new.txt")

# Create and rename directory
os.mkdir("temp")
os.rename("temp", "backup")
print("Renamed: temp/ -> backup/")
```

#### 22: Complete Case - Auto-create Daily Folder
```python
from datetime import datetime
import os

# Get today's date
today = datetime.now().strftime("%Y%m%d")
folder_name = f"lab_{today}"

# Create folder if it doesn't exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created: {folder_name}")
else:
    print(f"Folder {folder_name} already exists")
```

#### 23: Complete Case - Batch Rename Photos
```python
import os

# Create test directory and files
os.makedirs("photos", exist_ok=True)
with open("photos/photo_001.jpg", "w") as f: f.write("img1")
with open("photos/photo_002.jpg", "w") as f: f.write("img2")

# Batch rename: photo_*.jpg -> vacation_*.jpg
for file in os.listdir("photos/"):
    if file.startswith("photo"):
        new_name = file.replace("photo", "vacation")
        os.rename(f"photos/{file}", f"photos/{new_name}")
        print(f"Renamed: {file} -> {new_name}")

# Verify
print("After rename:", os.listdir("photos/"))
```

#### 24: Complete Case - Find All Text Files
```python
import os

# Create test directory and files
os.makedirs("text", exist_ok=True)
with open("text/notes.txt", "w") as f: f.write("notes")
with open("text/todo.txt", "w") as f: f.write("todo")
with open("text/image.jpg", "w") as f: f.write("jpg")

# Find all .txt files
text_files = []
for item in os.listdir("text/"):
    if item.endswith('.txt'):  # Better than slicing
        text_files.append(item)

print("Found text files:", text_files)

# Alternative using glob
import glob
text_files_glob = glob.glob("text/*.txt")
print("Using glob:", text_files_glob)
```

<br>
<br>
<br>
<br>
<br>

---

### Section 4: Encoding in Python

#### 25: Understanding ASCII Encoding
```python
# ASCII: 128 characters (English letters, numbers, symbols)
print("ASCII code for 'A':", ord('A'))  # Output: 65
print("Character for code 65:", chr(65))   # Output: A

# ASCII range is 0-127
print("ASCII for '0':", ord('0'))  # 48
print("ASCII for 'a':", ord('a'))  # 97
```

#### 26: Understanding UTF-8 Encoding
```python
# UTF-8: Global standard, supports all languages
# Variable-length: 1-4 bytes per character

# English characters (1 byte)
print("Length of 'ABC':", len("ABC".encode('utf-8')))  # 3

# Chinese characters (3 bytes each)
chinese_text = "中文"
utf8_bytes = chinese_text.encode('utf-8')
print(f"'{chinese_text}' in UTF-8:", utf8_bytes)
print(f"Length in bytes: {len(utf8_bytes)}")  # 6 (3 bytes per char)

# Python 3's default encoding is UTF-8
```

#### 27: Understanding GBK Encoding
```python
# GBK: Chinese legacy encoding, fixed 2 bytes per Chinese char
chinese_text = "中文"
gbk_bytes = chinese_text.encode('gbk')
print(f"'{chinese_text}' in GBK:", gbk_bytes)
print(f"Length in bytes: {len(gbk_bytes)}")  # 4 (2 bytes per char)

# GBK is common in older Chinese systems
```

#### 28: Setting Encoding Parameters
```python
# Always specify encoding when opening files!

# Safe way to open files
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Hello 世界")

# Reading with correct encoding
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Content:", content)

# Wrong encoding will cause errors
try:
    with open('data.txt', 'r', encoding='ascii') as f:
        print(f.read())
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
```

#### 29: Handling Encoding Errors
```python
# Create file with mixed content
with open('mixed.txt', 'wb') as f:
    f.write(b'Hello \xff\xfe World')  # Invalid UTF-8 sequence

# Default error handling (strict)
try:
    with open('mixed.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError as e:
    print("Error:", e)

# Ignore errors
with open('mixed.txt', 'r', encoding='utf-8', errors='ignore') as f:
    print("Ignore errors:", f.read())

# Replace errors with ?
with open('mixed.txt', 'r', encoding='utf-8', errors='replace') as f:
    print("Replace errors:", f.read())
```

#### 30: Complete Case - GBK to UTF-8 Conversion
```python
# Step 1: Create a GBK file
gbk_content = "姓名,年龄\n张三,25"
with open('old_data.txt', 'w', encoding='gbk') as f:
    f.write(gbk_content)
print("Created GBK file")

# Step 2: Read GBK file
with open('old_data.txt', 'r', encoding='gbk') as source:
    content = source.read()
    print("Read from GBK:", content)

# Step 3: Save as UTF-8
with open('new_data.txt', 'w', encoding='utf-8') as target:
    target.write(content)
    print("Saved as UTF-8")

# Verify encoding
print("UTF-8 file content:")
with open('new_data.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

#### 31: Complete Case - Reading Chinese CSV
```python
# Create CSV file in GBK
csv_content = "姓名,年龄\n张三,25\n李四,30"
with open('data.csv', 'w', encoding='gbk') as f:
    f.write(csv_content)

# Read Chinese CSV (GBK)
print("Reading with GBK encoding:")
with open('data.csv', 'r', encoding='gbk') as file:
    for line in file:
        name, age = line.strip().split(',')
        print(f"Name: {name}, Age: {age}")

# If file was UTF-8, use utf-8 encoding
# with open('data.csv', 'r', encoding='utf-8') as file:
#     ...
```

#### 32: Detecting File Encoding
```python
# Install chardet first: pip install chardet
import chardet

# Detect encoding of a file
with open('data.csv', 'rb') as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)
    print("Detected encoding:", result)

# Use detected encoding to read
encoding = result['encoding']
with open('data.csv', 'r', encoding=encoding) as f:
    print("Content using detected encoding:")
    print(f.read())
```

<br>
<br>
<br>
<br>
<br>

---

### Section 5: Practical Applications

#### 33: Log Analyzer - Count 404 Errors
```python
# Create a sample log file
log_content = """192.168.1.1 - - [01/Jan/2023:12:00:01] "GET /page1" 200
192.168.1.2 - - [01/Jan/2023:12:00:02] "GET /missing" 404
192.168.1.3 - - [01/Jan/2023:12:00:03] "GET /page2" 200
192.168.1.4 - - [01/Jan/2023:12:00:04] "GET /notfound" 404
"""
with open('nginx.log', 'w') as f:
    f.write(log_content)

# Count 404 errors
def count_404(log_file):
    counter = 0
    with open(log_file, 'r') as f:
        for line in f:
            if ' 404 ' in line:
                counter += 1
    return counter

# Usage
total_404 = count_404('nginx.log')
print("Total 404 errors:", total_404)
# Expected output: Total 404 errors: 2
```

#### 34: Log Analyzer - Time Filter
```python
def filter_by_time(log_file, start_time, end_time):
    results = []
    with open(log_file, 'r') as f:
        for line in f:
            # Extract timestamp between [ and ]
            timestamp = line.split('[')[1].split(']')[0]
            if start_time <= timestamp <= end_time:
                results.append(line)
    return results

# Example usage
matches = filter_by_time('nginx.log', '01/Jan/2023:12:00:01', '01/Jan/2023:12:00:03')
print(f"Found {len(matches)} entries in time range")
for match in matches:
    print(match.strip())
```

#### 35: Backup Tool - Basic File Copy
```python
import shutil
from datetime import datetime

def simple_backup(source_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_name = f"{source_file}_backup_{timestamp}"
    shutil.copy2(source_file, backup_name)  # copy2 preserves metadata
    print(f"Backup created: {backup_name}")

# Usage
with open('important.txt', 'w') as f:
    f.write("Important data")
simple_backup('important.txt')
```

#### 36: Backup Tool - Validate Backup
```python
def verify_backup(source, backup):
    with open(source, 'r') as f1, open(backup, 'r') as f2:
        f1_content = f1.read()
        f2_content = f2.read()
    
    if f1_content == f2_content:
        print('Backup verification: PASS')
    else:
        print('Backup verification: FAIL')

# Create files
with open('nginx.log', 'r') as src:
    with open('nginx_bac.log', 'w') as dst:
        dst.write(src.read())

# Verify
verify_backup('nginx.log', 'nginx_bac.log')
```

#### 37: Validate First 3 Lines Only
```python
def verify_backup_first3(source, backup):
    with open(source, 'r') as f1, open(backup, 'r') as f2:
        # Read first 3 lines from each
        src_lines = [next(f1).strip() for _ in range(3)]
        bak_lines = [next(f2).strip() for _ in range(3)]
    
    if src_lines == bak_lines:
        print('First 3 lines verification: PASS')
    else:
        print('First 3 lines verification: FAIL')
        for i, (s, b) in enumerate(zip(src_lines, bak_lines)):
            print(f"Line {i+1}: src='{s}', bak='{b}'")

# Usage
verify_backup_first3('nginx.log', 'nginx_bac.log')
```

#### 38: Text Encryption - Caesar Cipher
```python
def caesar_encrypt(text, shift=3):
    encrypted = []
    for char in text:
        if char.isprintable():  # Only encrypt printable chars
            encrypted.append(chr(ord(char) + shift))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

# Example
secret = caesar_encrypt("Hello Students!")
print("Encrypted:", secret)
# Expected: Khoor#VwxghqwV$
```

#### 39: Text Decryption - Caesar Cipher
```python
def caesar_decrypt(ciphertext, shift=3):
    decrypted = []
    for char in ciphertext:
        if char.isprintable():
            decrypted.append(chr(ord(char) - shift))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Test decryption
print("Decrypted:", caesar_decrypt("Khoor#VwxghqwV$"))
# Expected: Hello Students!
```

#### 40: File Encryption Wrapper
```python
def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        original_text = f_in.read()
        encrypted = caesar_encrypt(original_text)
        f_out.write(encrypted)

# Usage
encrypt_file('nginx.log', 'nginx.log.enc')
print("Encrypted file created")
```

#### 41: File Decryption Wrapper
```python
def decrypt_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        encrypted_text = f_in.read()
        decrypted = caesar_decrypt(encrypted_text)
        f_out.write(decrypted)

# Usage
decrypt_file('nginx.log.enc', 'nginx.log.enc.dec')
print("Decrypted file created")

# Verify
with open('nginx.log', 'r') as original:
    with open('nginx.log.enc.dec', 'r') as decrypted:
        if original.read() == decrypted.read():
            print("Encryption/Decryption: SUCCESS")
```

#### 42: Handling Newlines in Encryption
```python
# The Caesar cipher above handles \n as they are printable
# Let's test explicitly
test_text = "Line1\nLine2\nLine3"
encrypted = caesar_encrypt(test_text)
print("Encrypted with newlines:")
print(repr(encrypted))

decrypted = caesar_decrypt(encrypted)
print("Decrypted:")
print(repr(decrypted))
print("Original matches decrypted:", test_text == decrypted)
```

<br>
<br>
<br>
<br>
<br>

---

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b>. 

This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

#### Recommended: 3, 5, 6, 7, 9, 10, 12, 14, 15, 16

<br>
<br>


### Tips

- `tab` type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.
- `history` You can see all the commands you have run before.
- In Python interactive mode, use `help()` or `?` to view documentation for errors and exceptions.
- Try `ai`, `aiw`, and `aid` for AI assistance.

<br>

---

### 1. Log into the remote Linux Server

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---

### 2. Create Practice Directory and Files

```
cd ~
mkdir w10_error_handling
cd w10_error_handling
```

<br>

---

### 3. Common Python Errors Practice

Create a script to demonstrate the five most common errors:

```
nano common_errors.py
```

Type the following code:

```python
# 1. SyntaxError
# while True

# 2. NameError
# print(new_variable)

# 3. TypeError
# 1+'a'

# 4. FileNotFoundError
# fi=open('okokokokok.txt','r')

# 5. IndentationError
# while True:
# print('yes')

# Uncomment each line one by one to see the errors
print("Step 1: Uncomment the SyntaxError line")
```

Save: Ctrl + O
Exit: Ctrl + X

Run the script:

```
python3 common_errors.py
```

<br>

---

### 4. Understanding Error Messages

Create a script to generate a NameError and analyze the traceback:

```
nano traceback_demo.py
```

Type the following code:

```python
print(undefined_var)
```

Save and exit, then run:

```
python3 traceback_demo.py
```

You will see:

```
Traceback (most recent call last):
  File "traceback_demo.py", line 1, in <module>
    print(undefined_var)
NameError: name 'undefined_var' is not defined
```

**Error breakdown:**
- **Traceback**: Error roadmap showing the call stack
- **File "traceback_demo.py"**: Location of the error
- **line 1**: Exact line number
- **NameError**: Error type
- **name 'undefined_var' is not defined**: Specific error message

<br>

---

### 5. Basic Exception Handling

Create a script with try-except structure:

```
nano basic_try_except.py
```

Type the following code:

```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero!")
```

Save and run:

```
python3 basic_try_except.py
```

Expected output: `Oops! Can't divide by zero!`

<br>

---

### 6. BMI Calculator with Error Handling

Create a practical BMI calculator:

```
nano bmi_calculator.py
```

Type the following code:

```python
try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / height
except ZeroDivisionError:
    print("Alert! Did you enter height as zero?")
except ValueError:
    print("Please enter valid numbers!")
```

Save and run:

```
python3 bmi_calculator.py
```

Test with height = 0 to trigger ZeroDivisionError.

<br>

---

### 7. File Handling with Exception Handling

Create a file detective script:

```
nano file_detective.py
```

Type the following code:

```python
try:
    with open("ghost_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Pssst... this file doesn't exist!")
```

Save and run:

```
python3 file_detective.py
```

Expected output: `Pssst... this file doesn't exist!`

<br>

---

### 8. Catch-All Exception Handler

Create a script to catch any unexpected error:

```
nano catch_all.py
```

Type the following code:

```python
try:
    magic_number = "100" + 5
except Exception as e:
    print("Error details:", e)
```

Save and run:

```
python3 catch_all.py
```

Expected output shows the TypeError details.

<br>

---

### 9. User-Friendly Error Messages

Create an age input validator:

```
nano friendly_errors.py
```

Type the following code:

```python
try:
    user_age = int(input("Enter age: "))
except ValueError:
    print("Hey! Numbers only please :)")
```

Save and run:

```
python3 friendly_errors.py
```

Test with non-numeric input.

<br>

---

### 10. Handling Multiple Exception Types

Create a script with multiple except blocks:

```
nano multiple_exceptions.py
```

Type the following code:

```python
try:
    age = int(input("Age: "))
    print(str(100/age))
except ValueError:
    print("Numbers only!")  
except ZeroDivisionError:
    print("Age can't be zero!") 
```

Save and run:

```
python3 multiple_exceptions.py
```

Test with:
- Input `0` → ZeroDivisionError
- Input `string` → ValueError
- Input `4` → Successful division

<br>

---

### 11. Tuple-Style Exception Catching

Create a script catching multiple exceptions together:

```
nano tuple_catch.py
```

Type the following code:

```python
try:
    with open("grades.txt") as f:
        print(f.read())
except (FileNotFoundError, PermissionError):
    print("File problem! Check if:")
    print("- File exists")
    print("- You have access")
```

Save and run:

```
python3 tuple_catch.py
```

<br>

---

### 12. Grade Calculator Exercise

Create a grade calculator:

```
nano grade_calculator.py
```

Type the following code:

```python
try:
    total = float(input("Total points: "))
    earned = float(input("Earned points: "))
    percentage = (earned/total)*100
    print(f"Percentage: {percentage}%")
except ValueError:
    print("Numbers only!")
except ZeroDivisionError:
    print("Total can't be zero!")
```

**Question:** Modify this to use tuple-style catching.

<br>

---

### 13. Pet Age Calculator

Create a pet age calculator:

```
nano pet_age.py
```

Type the following code:

```python
try:
    human_years = int(input("Dog's age: "))
    dog_years = human_years * 7
    print(f"Dog age: {dog_years}")
except ValueError:
    print("Enter whole number!")
except Exception:
    print("Something unexpected happened!")
```

**Question:** Change it into tuple-style. Do we really need to do that?

<br>

---

### 14. The `finally` Clause

Create a script demonstrating `finally`:

```
nano finally_demo.py
```

Type the following code:

```python
try:
    file = open("diary.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Diary not found!")
finally:
    print("This always runs - cleanup completed")
```

Save and run:

```
python3 finally_demo.py
```

The `finally` block executes regardless of whether an exception occurs.

<br>

---

### 15. The `else` Clause

Create a script demonstrating `else`:

```
nano else_demo.py
```

Type the following code:

```python
try:
    num = float(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result is {result}")  # Only runs if no exception
```

Save and run:

```
python3 else_demo.py
```

The `else` block runs only when the `try` block succeeds.

<br>

---

### 16. Complete Exception Handling Pattern

Create a safe config loader:

```
nano safe_config.py
```

Type the following code:

```python
config_file = False
try:
    config_file = open("game_config.cfg")
except FileNotFoundError:
    print("⚠ Config file missing!")
else:
    settings = config_file.read()
    print("Game configuration loaded!")
finally:
    if config_file:
        config_file.close()
    print("Resource cleanup completed")
```

Save and run:

```
python3 safe_config.py
```

<br>

---

### 17. Safe Divide Function

Create a function with complete exception handling:

```
nano safe_divide.py
```

Type the following code:

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"Result is {result}")
    finally:
        print("Operation complete")

safe_divide(10, 2)
safe_divide(5, 0)
```

Save and run:

```
python3 safe_divide.py
```

<br>

---

### 18. Network Request Error Handling

Create a network request handler (requires internet):

```
nano network_request.py
```

Type the following code:

```python
import requests
try:
    response = requests.get("https://www.baidu.com", timeout=3)
    print("Connection successful!")
except requests.exceptions.ConnectTimeout:
    print("Oops! Connection took too long!")
```

Save and run:

```
python3 network_request.py
```

<br>

---

### 19. Retry Mechanism with Dynamic Wait Time

Create a retry script:

```
nano retry_dynamic.py
```

Type the following code:

```python
import time,requests

wait_times = [3, 2, 1]  # Dynamic wait times

for attempt in range(3):
    try:
        requests.get("https://www.baidu.com",timeout=3)
        print(f"Attempt {attempt+1} succeeded!")
        break
    except Exception:
        print(f"Attempt {attempt+1} failed")
        time.sleep(wait_times[attempt])
```

**Question:** How can we dynamically change the wait-time? First time: 3s, Second time: 2s, Third time: 1s

<br>

---

### 20. Username Validation with Custom Exception

Create a username checker:

```
nano username_check.py
```

Type the following code:

```python
existing_users = ["alice", "bob", "charlie"]

try:
    new_user = input("Choose username: ")
    if new_user in existing_users:
        raise ValueError("Username taken!")
    print("Username available!")
except ValueError as e:
    print(e)
```

**Question:** How can we use while-loop to add multiple users?

<br>

---

### 21. Password Strength Checker

Create a password validator using `raise`:

```
nano password_check.py
```

Type the following code:

```python
def check_password(pwd):
    if len(pwd) < 8:
        raise Exception("Password too short!")
    if not any(c.isdigit() for c in pwd):
        raise Exception("Add numbers!")

try:
    check_password("weak")
except Exception as e:
    print("Weak password: " + str(e))
```

Save and run:

```
python3 password_check.py
```

<br>

---

### 22. Fahrenheit to Celsius Converter

Create a temperature converter:

```
nano fahrenheit_celsius.py
```

Type the following code:

```python
try:
    fahr = float(input("Enter Fahrenheit: "))
except ValueError:
    print("Numbers only please!")
else:
    celsius = (fahr - 32) * 5/9
    print(f"{fahr}F = {celsius:.1f}C")
```

**Question:** Create a Celsius to Fahrenheit converter.

<br>

---

### 23. Temperature Range Validation

Create a temperature range checker:

```
nano temp_range.py
```

Type the following code:

```python
try:
    temp = float(input("Enter temp (-100 to 212F): "))
    if not (-100 <= temp <= 212):
        raise ValueError("Unrealistic temperature!")
    print("Temperature accepted!")
except ValueError as e:
    print(f"Invalid input: {e}")
```

**Question:** Put "Range Check" into the "Fahrenheit-to-Celsius" converter.

<br>

---

End

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b> on Moodle by 23:59 this Sunday. 

This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

### Tips

- `tab` type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.
- `history` You can see all the commands you have run before.
- Try `help('modules')` to see all available standard library modules.
- Use `pip list` to check installed packages.

<br>

---

### 1. Log into the remote Linux Server

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---

### 2. Understand Libraries, Packages, and Modules

```
# Create a new script file
cd ~
nano library_concepts.py

# Type the following code:
# Library: A collection focusing on functionality
# Package: A folder containing multiple modules
# Module: A single .py file

# Check Python's standard library path
import sys
print("Standard library location:")
print(sys.path)

# Show how modules are files
import math
print("\nMath module location:")
print(math.__file__)

# Show how packages are directories
import os
print("\nOS package location:")
print(os.__file__)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 library_concepts.py
```

<br>

---

### 3. Explore Python's Built-in Help System

```
# Enter Python interactive mode
python3

# In interactive mode, type:
# Discover all available standard library modules
help('modules')

# Get help on a specific module
import math
help(math)

# Check math module contents
dir(math)

# Exit interactive mode
exit()
```

<br>

---

### 4. Three Ways to Import Modules

```
# Create a new script file
cd ~
nano import_methods.py

# Type the following code:
# Method 1: Full Import - Get the whole toolbox
import math
print("Full import: 2^5 =", math.pow(2, 5))

# Method 2: Specific Import - Grab just what you need
from random import randint
print("Specific import: Random dice roll:", randint(1, 6))

# Method 3: Alias Import - Make it short
import pandas as pd
data = {'Birds': ['Eagle', 'Penguin'], 'Speed': [320, 8]}
df = pd.DataFrame(data)
print("Alias import:\n", df)

# Mix them up!
from math import sqrt as sq
print("Mixed style: Square root of 121:", sq(121))

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 import_methods.py
```

<br>

---

### 5. Practice with Standard Library Modules

```
# Create a new script file
cd ~
nano stdlib_practice.py

# Type the following code:
# Math module
import math
print("Pi is approximately", math.pi)
print("Square root of 16:", math.sqrt(16))

# Datetime module
import datetime
now = datetime.datetime.now()
print("\nCurrent time:", now)
print("Formatted time:", now.strftime("%H:%M:%S"))

# Timedelta calculation
future_date = now + datetime.timedelta(days=3)
print("Date after 3 days:", future_date.date())

# Random module
from random import choice, shuffle
chars = 'ABC123!@'
password = ''.join([choice(chars) for _ in range(8)])
print("\nRandom password:", password)

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print("Shuffled numbers:", numbers)

# OS module
import os
my_folder = "test_documents"
if not os.path.exists(my_folder):
    os.makedirs(my_folder)
    print(f"\nCreated folder: {my_folder}")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 stdlib_practice.py
```

<br>

---

### 6. Install Third-Party Libraries with pip

```
# Open terminal (not Python interactive mode)
# Check pip version
pip3 --version

# Install requests library
pip3 install requests

# List installed packages
pip3 list

# Speed up download using mirror (temporary)
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# Configure permanent mirror
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Verify configuration
pip3 config list

# Upgrade a package
pip3 install --upgrade requests

# Install specific version
pip3 install requests==2.31.0
```

<br>

---

### 7. Use the requests Library

```
# Create a new script file
cd ~
nano requests_demo.py

# Type the following code:
import requests

# Simple GET request
response = requests.get("https://www.baidu.com")
print(f"Status Code: {response.status_code}")
print(f"Response Text (first 100 chars): {response.text[:100]}...")

# Real-world weather check
city = "Beijing"
url = f"http://wttr.in/{city}?format=3"
response = requests.get(url)
print(f"\nWeather in {city}: {response.text}")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 requests_demo.py
```

<br>

---

### 8. Build a Formal Weather Reporter

```
# Create a new script file
cd ~
nano weather_reporter.py

# Type the following code:
import requests
import datetime

def get_weather(city):
    """Fetch weather data from wttr.in"""
    url = f"http://wttr.in/{city}?format=%t+%C"
    response = requests.get(url)
    return response.text.strip()

def weather_report(city):
    """Generate time-stamped weather report"""
    # Note: This uses local server time (UTC)
    time_now = datetime.datetime.now().strftime("%H:%M")
    weather = get_weather(city)
    return f"[{time_now}] Weather in {city}: {weather}"

# Test the function
print(weather_report("London"))
print(weather_report("NewYork"))

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 weather_reporter.py

# Question: Is there something wrong? How can we fix it? Hint: we are using the Beijing Time.
# Answer: The time shown is server time (UTC), not Beijing time (UTC+8).
# To fix, you would need timezone handling with pytz library.
```

<br>

---

### 9. Create a File Backup Helper

```
# Create a new script file
cd ~
nano backup_helper.py

# Type the following code:
import os
import shutil

def backup_files(src_folder, dst_folder):
    """Copy all .txt files from source to destination"""
    # Create destination folder if it doesn't exist
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print(f"Created backup folder: {dst_folder}")
    
    # Check if source folder exists
    if not os.path.exists(src_folder):
        print(f"Error: Source folder '{src_folder}' not found!")
        return
    
    # Copy all .txt files
    for file in os.listdir(src_folder):
        if file.endswith(".txt"):
            src_path = os.path.join(src_folder, file)
            dst_path = os.path.join(dst_folder, file)
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {file}")

# Test the backup function
# First create some test files
os.makedirs("notes", exist_ok=True)
with open("notes/test1.txt", "w") as f:
    f.write("Important notes")
with open("notes/test2.txt", "w") as f:
    f.write("More notes")

# Run backup
backup_files("notes", "backup")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 backup_helper.py
```

<br>

---

### 10. Explore Library Documentation

```
# Create a new script file
cd ~
nano explore_docs.py

# Type the following code:
# Standard library documentation
import webbrowser

# Open Python standard library docs
webbrowser.open("https://docs.python.org/3/library")

# Open PyPI for third-party libraries
webbrowser.open("https://pypi.org")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 explore_docs.py

# Pro Tip: Great programmers stand on the shoulders of giants
# Always explore documentation before reinventing the wheel
```

<br>

---

End
