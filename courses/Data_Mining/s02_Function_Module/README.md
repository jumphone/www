
---
# Section 1. Introduction to Function & Module

## Functions: Like a Microwave Preset Button

1. Real-life analogy:  
   - Preset buttons = Predefined functions  
   - "Popcorn" button = `def popcorn_mode()`  
   - "Beverage" button = `def reheat_drink()`
2. Python example:

```python

def start_microwave(preset):
    if preset == "popcorn":
        print('heat for 180 seconds')
    elif preset == "beverage":
        print('heat for 45 seconds')

start_microwave("popcorn")
```

---
# Why do We Need Functions
Problem without functions:  
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
# Creating Our First Function
Solution with functions:  
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
# Making Functions Flexible
Adding parameters:  
```python
def make_sandwich(filling):
    print(f"Making {filling} sandwich:")
    print("1. Get bread")
    print("2. Add "+ str(filling))
    print("3. Close sandwich")
    print("------")

make_sandwich("ham")
make_sandwich("cheese")
```

---
# Modules: Like Game Sound Library
1. Real-life example:  
   - Game sound module = `import sound_effects`  
   - Ready-to-use sounds = `jump_sound()`, `explosion_sound()`
2. Simple Python example:  
```python
# sound_module.py
def play_jingle():
    print("🎵 Happy tune playing! 🎵")

# main.py
import sound_module
sound_module.play_jingle()
```

---
# Building Our Own Module
1. Create `kitchen.py`:  
```python
def microwave_beep():
    print("BEEP! BEEP! BEEP!")

def oven_timer():
    print("DING! Food is ready!")
```

2. Use it:  
```python
import kitchen
kitchen.microwave_beep()
kitchen.oven_timer()
```

---
# Example: Cooking Module
Complete example:  
```python
# In cooking_module.py
def prepare_dish(dish_name):
    print("Preparing "+str(dish_name)+"...")
    print("1. Gather ingredients")
    print("2. Follow recipe steps")

# In main program
import cooking_module
cooking_module.prepare_dish("pasta")
cooking_module.prepare_dish("salad")
```

---
# Example: Game Sounds
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
# Key Takeaways
1. Functions are like preset shortcuts  
2. Parameters make functions flexible  
3. Modules help organize code  
4. Import lets reuse code  
5. Combine functions/modules for complex programs


---


# Section 2. Function Basic Syntax

---

## What is a Function?

Like a recipe:  
1. Receive ingredients (parameters)  
2. Follow steps (code block)  
3. Give result (return value)

---

## Function Structure
```python
def magic_oven(ingredient):  # Function header
    output=str(ingredient) +" cookie" #  Function body
    return(output)   
```

Three essential parts:  
1. `def` statement with function name  
2. Action-performing code block
3. return the result (optional)

---

## Demo 1: Greeting
```python
def greet(name):
    print("Hello, "+str(name))


greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

---

## Question: How can we write a function that only greets to Alice?
## Question: How can we write a function that greets Bob in another way?

---

## Shape-Shifting Greetings (Multiple Parameters)
```python
def flexible_greet(name, greeting):
    print(str(greeting)+' '+str(name)+'!')

flexible_greet("Charlie", "Good morning")  # 
flexible_greet("Diana", "Ni hao")          # 
flexible_greet("Eric", "Guten Tag")        # 
```

## Parameters order matters!  
`(greeting, name)` vs `(name, greeting)`

---

## Calculator Function (Return Value)
```python
def circle_area(radius):
    area =  3.14 * radius ** 2
    return(area)

print(circle_area(5))  # 78.5
print("Pizza area:", circle_area(30))  # 

pizza_price = circle_area(30) * 0.02

```

---

## Common Mistakes 
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

## Parameter-Free Functions
```python
import datetime

def show_time():
    now = datetime.datetime.now()
    print("Current time: "+str(now.hour)+':'+str(now.minute))

show_time()  
```

---

## Multi-Parameter Function (BMI)
```python
def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    bmi=weight / (height ** 2)
    return(bmi)

print("BMI:", calculate_bmi(70, 1.75))  
print("BMI:", calculate_bmi(65, 1.68)) 
```

Health tip:  
Normal BMI range: 18.5 - 24.9

## Question: BMI and weight => height
## Question: x**1/2 vs. x**(1/2)
## Question: How can we check the correctness of "BMI and weight => height"?

---

## Function Superpowers
1. Reusable code blocks  
2. Clear program structure   
3. Easy error tracking   
4. Team collaboration 

---

# Section 3. Advanced Parameters & Return Values

---

## Positional vs Keyword Arguments
### Pizza Ordering System Example
```python
def make_pizza(size, toppings):
    print("Making "+str(size)+"cm pizza with:")
    for topping in toppings:
        print(topping)

# Positional arguments
make_pizza(30, ["mushrooms", "olives"])

# Keyword arguments
make_pizza(toppings=["cheese"], size=20)
```

---

## When to Use Keyword Arguments?
1. When passing many parameters
2. When parameters have default values
3. To improve code readability

Try this bad example:
```python
# Confusing positional arguments
make_pizza(["pepperoni"], 25)
```

---

## Default Parameters
### Shipping Cost Calculator
```python
def calculate_shipping(weight, base_fee=5.0):
    price=weight * 1.2 + base_fee
    return(price)

print(calculate_shipping(3.5))       # Uses default base_fee
print(calculate_shipping(2.0, 4.0))  
```

---

## Multiple Return Values
### Box Dimension Calculator
```python
def box_calculator(length, width, height):
    volume = length * width * height
    surface = 2 * (length*width + length*height + width*height)
    return(volume, surface)  # Returns a tuple!

dimensions = box_calculator(5, 3, 2)
print("Volume: "+str(dimensions[0])+", Surface: "+str(dimensions[1]))
```

---

## Unpacking Return Values
```python
# Direct unpacking
vol, surf = box_calculator(2, 2, 2)
print("Perfect cube: "+str(vol)+" cubic units")

# Works with different variable names
v, s = box_calculator(1, 3, 5)
```

---

## Variable Scope Experiment
```python
temperature = 25  # Global variable

def adjust_temp():
    temperature = 18  # Local variable
    print("Inside: "+str(temperature)+"°C")

adjust_temp()
print("Outside: "+str(temperature)+"°C")  # Still 25
```

---

## Global Keyword Demo
```python
score = 0

def update_points():
    global score
    score = score+10
    print("New score: "+str(score))

update_points()  # Now modifies the global variable

print(score)
```

---

## Good Function Names
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

## Function Name Checklist
1. Use underscore separation
2. Be specific but concise
3. Keep under 3 words when possible

---

## Summary
Key concepts covered:
1. Argument types (positional/keyword)
2. Default parameter values
3. Returning multiple values
4. Variable scope
5. Naming best practices

---

# Section 4. Python Modules System

---

## Today's Learning Goals
- Understanding different import methods
- Working with Python standard libraries
- Creating and using custom modules
- Namespace concept

---

### Basic Module Import Methods

#### Full Module Import
```python
import math

print(math.sqrt(25))  # 5.0
print(math.pi)        # 3.141592653589793
```
![Down Arrow] Key points:
- Access elements with dot notation
- Avoids naming conflicts

---

#### Specific Function Import
```python
from random import randint

lottery = [randint(1, 50) for _ in range(6)]
print("Winning numbers:", lottery)
```
Example output:
``` 
Winning numbers: [14, 37, 5, 23, 42, 19]
```
![Warning] Be careful with name collisions!

---

### Math Library in Action
```python
import math

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f"The hypotenuse is: {c}")
```
Output:
```
The hypotenuse is: 5.00
```

## Question: change f-string (f"The hypotenuse is: {c}") into "+" format. 


---

### Random Library Fun
```python
from random import choice

participants = ["Alice", "Bob", "Charlie", "Diana"]
winner = choice(participants)
print(f"Congratulations {winner}!")
```
Possible output:
```
Congratulations Charlie!
```

---

### Time Library Demo
```python
import time

print("Starting countdown:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)


print("Blast off! ")
```

---

### Creating Your First Module
1. Create `mymodule.py`:
```python
def greet(name):
    return f"Hello {name}, from my module!"
```

2. In main program:
```python
import mymodule

print(mymodule.greet("Sarah"))
```

---

### Understanding Namespaces
```python
import math
import mymath  # Hypothetical custom math module

print(math.sqrt(16))  # 4.0
print(mymath.sqrt(16)) # Maybe different implementation
```
![Toolbox Analogy] Each module is like a separate toolbox

---

### Exploring Third-Party Libraries
```python
# requests example
import requests

response = requests.get("https://www.bioinfo-lab.com/")
print(f"Status code: {response.status_code}")
print(f"Response time: {response.elapsed.total_seconds()}s")
```



---

### Module Search Path
```python
import sys

print("Python looks in these locations:")
for path in sys.path:
    print("- "+str(path))
```

---

### Import Best Practices
1. Keep imports at top of file
2. Use aliases for long names:

```python
import numpy as np
import pandas as pd
```

---

# Section 5. Practical Python Examples for Beginners

---

## Roadmap
1. Auto-generated Password Program
2. Simple Calculator
3. Temperature Conversion System

---


## Example 1: Password Generator (1/2)
**Problem**: Create random secure passwords

```python
import random

def generate_password(length=8):
    chars = "abcdefghijkmnpqrstuvwxyz23456789"
    this_password =''
    i=1
    while(i<=length):
        this_password=this_password+random.choice(chars)
        i=i+1
    return(this_password)
```

---

## Example 1: Password Generator (2/2)
**Usage**:
```python
print(generate_password())   # Example: 'a3x7bk9m'
print(generate_password(12)) # Example: 'wxn58k2q9yr7'
```

## Question: how can we add random uppercase and lowercase characters?
## Hint: random.random(), lower(), upper()
---

## Example 2: Simple Calculator (1/2)
**Core logic**:
```python
def calculator(a, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b

```

## Question: how can we add "*" and "/"?

---

## Example 2: Simple Calculator (2/2)
**Using our calculator**:
```python
print(calculator(5, 3))           # 8 (uses default +)
print(calculator(5, 3, "-"))      # 2
print(calculator(2.5, 4, "+"))    # 6.5
```


---

## Example 3: Temperature Converter (1/2)
**Conversion formulas**:
```
Celsius to Fahrenheit: (C × 9/5) + 32

```

```python
def c_to_f(c):
    return (c * 9/5) + 32

```

---

## Example 3: Temperature Converter (2/2)
**Test conversions**:
```python
print(c_to_f(0))
print(c_to_f(100))
```

## Question: write the function "f_to_c"
## Question: How can we check the correctness of "f_to_c"

---


