[Back](https://www.bioinfo-lab.com/courses/Programming_I/w05_Function_Module/)

<br>

<a id="all"></a>

### Content:

[Section 1. Introduction to Function & Module](#s1.0)

[Section 2. Function Basic Syntax](#s2.0)

[Section 3. Advanced Parameters & Return Values](#s3.0)

[Section 4. Python Modules System](#s4.0)

[Section 5. Practical Python Examples for Beginners](#s5.0)

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Introduction to Function & Module

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1.1. Functions: Like a Microwave Preset Button

### Real-life analogy:
- Preset buttons = Predefined functions
- "Popcorn" button = `def popcorn_mode()`
- "Beverage" button = `def reheat_drink()`

### Python example:

```python
def start_microwave(preset):
    if preset == "popcorn":
        print('heat for 180 seconds')
    elif preset == "beverage":
        print('heat for 45 seconds')

start_microwave("popcorn")
```

---

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Why do We Need Functions

### Problem without functions:

```python
# Making 3 sandwiches
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
```

---

<div align="left">
  <a href="#s1.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 1.3. Creating Our First Function

### Solution with functions:

```python
def make_sandwich():
    print("1. Get bread")
    print("2. Add filling")
    print("3. Close sandwich")
    print("------")

make_sandwich()
make_sandwich()
make_sandwich()
```

---

<div align="left">
  <a href="#s1.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.4"></a>

---

## 1.4. Making Functions Flexible

### Adding parameters:

```python
def make_sandwich(filling):
    print("Making " + str(filling) + " sandwich:")
    print("1. Get bread")
    print("2. Add " + str(filling))
    print("3. Close sandwich")
    print("------")

make_sandwich("ham")
make_sandwich("cheese")
```

---

<div align="left">
  <a href="#s1.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.5"></a>

---

## 1.5. Modules: Like Game Sound Library

### Real-life example:
- Game sound module = `import sound_effects`
- Ready-to-use sounds = `jump_sound()`, `explosion_sound()`

### Simple Python example:

```python
# sound_module.py
def play_jingle():
    print("🎵 Happy tune playing! 🎵")

# main.py
import sound_module
sound_module.play_jingle()
```

---

<div align="left">
  <a href="#s1.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.6"></a>

---

## 1.6. Building Our Own Module

### Create `kitchen.py`:

```python
def microwave_beep():
    print("BEEP! BEEP! BEEP!")

def oven_timer():
    print("DING! Food is ready!")
```

### Use it:

```python
import kitchen
kitchen.microwave_beep()
kitchen.oven_timer()
```

---

<div align="left">
  <a href="#s1.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.7"></a>

---

## 1.7. Example: Cooking Module

### Complete example:

```python
# In cooking_module.py
def prepare_dish(dish_name):
    print("Preparing " + str(dish_name) + "...")
    print("1. Gather ingredients")
    print("2. Follow recipe steps")

# In main program
import cooking_module
cooking_module.prepare_dish("pasta")
cooking_module.prepare_dish("salad")
```

---

<div align="left">
  <a href="#s1.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.8"></a>

---

## 1.8. Example: Game Sounds

```python
# sound_effects.py
def laser_blast():
    print("PEW! PEW! ")

def power_up():
    print(" ENERGY RESTORED!")

# game.py
import sound_effects
sound_effects.laser_blast()
sound_effects.power_up()
```

---

<div align="left">
  <a href="#s1.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.9"></a>

---

## 1.9. Key Takeaways

1. Functions are like preset shortcuts
2. Parameters make functions flexible
3. Modules help organize code
4. Import lets reuse code
5. Combine functions/modules for complex programs

---

<div align="left">
  <a href="#s1.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>

# Section 2. Function Basic Syntax

<div align="left">
  <a href="#s1.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. What is a Function?

Like a recipe:
1. Receive ingredients (parameters)
2. Follow steps (code block)
3. Give result (return value)

---

<div align="left">
  <a href="#s2.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. Function Structure

```python
def magic_oven(ingredient):  # Function header
    output = str(ingredient) + " cookie" # Function body
    return(output)
```

### Three essential parts:
1. `def` statement with function name
2. Action-performing code block
3. return the result (optional)

---

<div align="left">
  <a href="#s2.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.3"></a>

---

## 2.3. Demo 1: Greeting

```python
def greet(name):
    print("Hello, " + str(name))

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

---

<div align="left">
  <a href="#s2.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.4"></a>

---

## 2.4. Shape-Shifting Greetings (Multiple Parameters)

```python
def flexible_greet(name, greeting):
    print(str(greeting) + ' ' + str(name) + '!')

flexible_greet("Charlie", "Good morning")
flexible_greet("Diana", "Ni hao")
flexible_greet("Eric", "Guten Tag")
```

### Parameters order matters!
`(greeting, name)` vs `(name, greeting)`

---

<div align="left">
  <a href="#s2.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.5"></a>

---

## 2.5. Calculator Function (Return Value)

```python
def circle_area(radius):
    area = 3.14 * radius ** 2
    return(area)

print(circle_area(5))
print("Pizza area: " + str(circle_area(30)))

pizza_price = circle_area(30) * 0.02
```

---

<div align="left">
  <a href="#s2.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.6"></a>

---

## 2.6. Common Mistakes

### Case 1: Missing Colon

```python
# Wrong
def bad_function()
    print("Oops")

# Right
def good_function():
    print("Yay!")
```

### Case 2: Wrong Indentation

```python
# Wrong
def messy_function():
print("No indent!")

# Right
def clean_function():
    print("Perfect!")
```

---

<div align="left">
  <a href="#s2.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.7"></a>

---

## 2.7. Parameter-Free Functions

```python
import datetime

def show_time():
    now = datetime.datetime.now()
    print("Current time: " + str(now.hour) + ':' + str(now.minute))

show_time()
```

---

<div align="left">
  <a href="#s2.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.8"></a>

---

## 2.8. Multi-Parameter Function (BMI)

```python
def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    bmi = weight / (height ** 2)
    return(bmi)

print("BMI:", calculate_bmi(70, 1.75))
print("BMI:", calculate_bmi(65, 1.68))
```

### Health tip:
Normal BMI range: 18.5 - 24.9

### Question: BMI and weight => height

### Question: "x**1/2" vs. "x**(1/2)"

### Question: How can we check the correctness of "BMI and weight => height"?

---

<div align="left">
  <a href="#s2.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.9"></a>

---

## 2.9. Function Superpowers

1. Reusable code blocks
2. Clear program structure
3. Easy error tracking
4. Team collaboration

---

<div align="left">
  <a href="#s2.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>

# Section 3. Advanced Parameters & Return Values

<div align="left">
  <a href="#s2.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. Positional vs Keyword Arguments

### Pizza Ordering System Example

```python
def make_pizza(size, toppings):
    print("Making " + str(size) + "cm pizza with:")
    for topping in toppings:
        print(topping)

# Positional arguments
make_pizza(30, ["mushrooms", "olives"])

# Keyword arguments
make_pizza(toppings=["cheese"], size=20)
```

---

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. When to Use Keyword Arguments?

1. When passing many parameters
2. When parameters have default values
3. To improve code readability

### Try this bad example:

```python
# Confusing positional arguments
make_pizza(["pepperoni"], 25)
```

---

<div align="left">
  <a href="#s3.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 3.3. Default Parameters

### Shipping Cost Calculator

```python
def calculate_shipping(weight, base_fee=5.0):
    price = weight * 1.2 + base_fee
    return(price)

print(calculate_shipping(3.5))       # Uses default base_fee
print(calculate_shipping(2.0, 4.0))
```

---

<div align="left">
  <a href="#s3.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 3.4. Multiple Return Values

### Box Dimension Calculator

```python
def box_calculator(length, width, height):
    volume = length * width * height
    surface = 2 * (length*width + length*height + width*height)
    return(volume, surface)  # Returns a tuple!

dimensions = box_calculator(5, 3, 2)
print("Volume: " + str(dimensions[0]) + ", Surface: " + str(dimensions[1]))
```

---

<div align="left">
  <a href="#s3.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.5"></a>

---

## 3.5. Unpacking Return Values

```python
# Direct unpacking
vol, surf = box_calculator(2, 2, 2)
print("Perfect cube: " + str(vol) + " cubic units")

# Works with different variable names
v, s = box_calculator(1, 3, 5)
```

---

<div align="left">
  <a href="#s3.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.6"></a>

---

## 3.6. Variable Scope Experiment

```python
temperature = 25  # Global variable

def adjust_temp():
    temperature = 18  # Local variable
    print("Inside: " + str(temperature) + "°C")

adjust_temp()
print("Outside: " + str(temperature) + "°C")  # Still 25
```

---

<div align="left">
  <a href="#s3.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.7"></a>

---

## 3.7. Global Keyword Demo

```python
score = 0

def update_points():
    global score
    score = score + 10
    print("New score: " + str(score))

update_points()  # Now modifies the global variable

print(score)
```

---

<div align="left">
  <a href="#s3.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.8"></a>

---

## 3.8. Good Function Names

```python
# Good examples
def calculate_tax(income):
def get_user_profile(id):
def convert_to_fahrenheit(celsius):

# Bad examples
def tax(inc):          # Too vague
def user(id):          # Verb missing
def temp_conv(c):      # Unclear abbreviation
```

---

<div align="left">
  <a href="#s3.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.9"></a>

---

## 3.9. Function Name Checklist

1. Use underscore separation
2. Be specific but concise
3. Keep under 3 words when possible

---

<div align="left">
  <a href="#s3.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.10"></a>

---

## 3.10. Summary

Key concepts covered:
1. Argument types (positional/keyword)
2. Default parameter values
3. Returning multiple values
4. Variable scope
5. Naming best practices

---

<div align="left">
  <a href="#s3.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>

# Section 4. Python Modules System

<div align="left">
  <a href="#s3.10">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. Today's Learning Goals

- Understanding different import methods
- Working with Python standard libraries
- Creating and using custom modules
- Namespace concept

---

<div align="left">
  <a href="#s4.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Basic Module Import Methods

### Full Module Import

```python
import math

print(math.sqrt(25))  # 5.0
print(math.pi)        # 3.141592653589793
```

![Down Arrow] Key points:
- Access elements with dot notation
- Avoids naming conflicts

### Specific Function Import

```python
from random import randint

lottery = [randint(1, 50) for _ in range(6)]
print("Winning numbers: " + str(lottery))
```

Example output:
```
Winning numbers: [14, 37, 5, 23, 42, 19]
```

![Warning] Be careful with name collisions!

---

<div align="left">
  <a href="#s4.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.3"></a>

---

## 4.3. Math Library in Action

```python
import math

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print("The hypotenuse is: " + str(c))
```

Output:
```
The hypotenuse is: 5.0
```

### Question: change f-string (f"The hypotenuse is: {c}") into "+" format.

---

<div align="left">
  <a href="#s4.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.4"></a>

---

## 4.4. Random Library Fun

```python
from random import choice

participants = ["Alice", "Bob", "Charlie", "Diana"]
winner = choice(participants)
print("Congratulations " + winner + "!")
```

Possible output:
```
Congratulations Charlie!
```

---

<div align="left">
  <a href="#s4.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.5"></a>

---

## 4.5. Time Library Demo

```python
import time

print("Starting countdown:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Blast off! ")
```

---

<div align="left">
  <a href="#s4.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.6"></a>

---

## 4.6. Creating Your First Module

1. Create `mymodule.py`:

```python
def greet(name):
    return "Hello " + name + ", from my module!"
```

2. In main program:

```python
import mymodule

print(mymodule.greet("Sarah"))
```

---

<div align="left">
  <a href="#s4.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.7"></a>

---

## 4.7. Understanding Namespaces

```python
import math
import mymath  # Hypothetical custom math module

print(math.sqrt(16))  # 4.0
print(mymath.sqrt(16)) # Maybe different implementation
```

![Toolbox Analogy] Each module is like a separate toolbox

---

<div align="left">
  <a href="#s4.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.8"></a>

---

## 4.8. Exploring Third-Party Libraries

```python
# requests example
import requests

response = requests.get("https://www.bioinfo-lab.com/")
print("Status code: " + str(response.status_code))
print("Response time: " + str(response.elapsed.total_seconds()) + "s")
```

---

<div align="left">
  <a href="#s4.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.9"></a>

---

## 4.9. Module Search Path

```python
import sys

print("Python looks in these locations:")
for path in sys.path:
    print("- " + str(path))
```

---

<div align="left">
  <a href="#s4.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.10"></a>

---

## 4.10. Import Best Practices

1. Keep imports at top of file
2. Use aliases for long names:

```python
import numpy as np
import pandas as pd
```

---

<div align="left">
  <a href="#s4.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>

# Section 5. Practical Python Examples for Beginners

<div align="left">
  <a href="#s4.10">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Roadmap

1. Auto-generated Password Program
2. Simple Calculator
3. Temperature Conversion System

---

<div align="left">
  <a href="#s5.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Example 1: Password Generator (1/2)

**Problem**: Create random secure passwords

```python
import random

def generate_password(length=8):
    chars = "abcdefghijkmnpqrstuvwxyz23456789"
    this_password = ''
    i = 1
    while(i <= length):
        this_password = this_password + random.choice(chars)
        i = i + 1
    return(this_password)
```

---

<div align="left">
  <a href="#s5.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 5.3. Example 1: Password Generator (2/2)

**Usage**:

```python
print(generate_password())   # Example: 'a3x7bk9m'
print(generate_password(12)) # Example: 'wxn58k2q9yr7'
```

### Question: how can we add random uppercase and lowercase characters?

### Hint: random.random(), lower(), upper()

---

<div align="left">
  <a href="#s5.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.4"></a>

---

## 5.4. Example 2: Simple Calculator (1/2)

**Core logic**:

```python
def calculator(a, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
```

### Question: how can we add "*" and "/"?

---

<div align="left">
  <a href="#s5.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.5"></a>

---

## 5.5. Example 2: Simple Calculator (2/2)

**Using our calculator**:

```python
print(calculator(5, 3))           # 8 (uses default +)
print(calculator(5, 3, "-"))      # 2
print(calculator(2.5, 4, "+"))    # 6.5
```

---

<div align="left">
  <a href="#s5.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.6"></a>

---

## 5.6. Example 3: Temperature Converter (1/2)

**Conversion formulas**:
```
Celsius to Fahrenheit: (C × 9/5) + 32
```

```python
def c_to_f(c):
    return (c * 9/5) + 32
```

---

<div align="left">
  <a href="#s5.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.7"></a>

---

## 5.7. Example 3: Temperature Converter (2/2)

**Test conversions**:

```python
print(c_to_f(0))
print(c_to_f(100))
```

### Question: write the function "f_to_c"

### Question: How can we check the correctness of "f_to_c"

---

<div align="left">
  <a href="#s5.6">← Prev </a> | <a href="#all"> Home </a> 
</div>

<br>

End
