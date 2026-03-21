[Back](https://www.bioinfo-lab.com/courses/Programming_I/w05_Function_Module/)

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
