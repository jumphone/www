
# Functions & Modules

# 函数与模块

Welcome to one of the most important milestones in your programming journey! Up until now, you may have been writing code straight down, line by line. But as programs get larger, this becomes difficult to manage. In this chapter, we will learn how to organize, reuse, and share our code using **Functions** and **Modules**.

欢迎来到你编程之旅中最重要的里程碑之一！到目前为止，你可能一直都是从上到下、逐行编写代码。但随着程序变得越来越庞大，这种方式会变得难以管理。在本章中，我们将学习如何使用 **函数（Functions）** 和 **模块（Modules**来组织、重用和分享我们的代码。

<br>

---

## Section 1. Introduction to Functions & Modules

## 第 1 节：函数与模块简介

### 1.1. Functions: Like a Microwave Preset Button / 函数：就像微波炉的预设按钮

Think about how you use a microwave. When you want to make popcorn, you don't manually set the power level to 80% and the timer to 3 minutes. Instead, you just press the "Popcorn" preset button.

想想你是如何使用微波炉的。当你想爆爆米花时，你不会去手动把火力调到 80% 并把时间设定为 3 分钟，而是直接按下“爆米花”的预设按钮。

In programming, **functions** are exactly like these preset buttons. They are named blocks of code designed to do one specific job. Once you define a function, you can "press the button" (call the function) whenever you need it.

在编程中，**函数**就和这些预设按钮一模一样。它们是被命名的代码块，专门用来完成某一项特定的工作。一旦你定义好了一个函数，你就可以在任何需要的时候“按下按钮”（即调用函数）。

```python
# Defining our microwave preset function
def start_microwave(preset):
    if preset == "popcorn":
        print('Heating for 180 seconds...')
    elif preset == "beverage":
        print('Heating for 45 seconds...')

# "Pressing" the button
start_microwave("popcorn")

```

<br>

### 1.2. Why Do We Need Functions? / 为什么我们需要函数？

Imagine you are writing a game where a character makes sandwiches. Without functions, you have to type out the instructions every single time:

想象一下你正在编写一个游戏，游戏里的角色需要制作三明治。如果没有函数，你每次都得把这些指令重新打一遍：

```python
# Making 3 sandwiches without functions
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

This violates a core rule of programming: **DRY (Don't Repeat Yourself)**. If you suddenly want to add "Cut sandwich in half" to the recipe, you have to change your code in three different places!

这违反了编程中的一个核心原则：**DRY（Don't Repeat Yourself / 不要重复自己）**。如果你突然想在食谱里加上“把三明治切成两半”，你就得在代码里的三个不同地方进行修改！

<br>

### 1.3. Creating Our First Function / 创建我们的第一个函数

Let's solve the sandwich problem by packaging those steps into a function:

让我们把这些步骤打包进一个函数里，以此来解决三明治的问题：

```python
def make_sandwich():
    print("1. Get bread")
    print("2. Add filling")
    print("3. Close sandwich")
    print("------")

# Now we just call the function 3 times!
make_sandwich()
make_sandwich()
make_sandwich()

```

<br>

### 1.4. Making Functions Flexible (Parameters) / 让函数更灵活（参数）

A function that only makes plain sandwiches is boring. We can make our functions flexible by passing them information. We call these pieces of information **parameters**.

一个只会做一种普通三明治的函数是很无聊的。我们可以通过传递信息来让函数变得灵活。我们把这些传递的信息称为**参数（parameters）**。

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

<br>

### 1.5. Modules: The Game Sound Library / 模块：游戏音效库

If functions are preset buttons, **Modules** are the whole appliance! A module is simply a Python file containing a set of functions that you want to include in your application.

如果说函数是预设按钮，那么模块（Modules）就是整台机器！模块简单来说就是一个 Python 文件，里面包含了你想在你的程序中引用的一系列函数。

Imagine you are building a video game. Instead of writing all the sound code in your main game file, you can `import` a pre-made module:

想象你正在开发一款电子游戏。你可以使用 `import`（导入）一个预先写好的模块，而不用把所有音效代码都写在游戏主文件里：

```python
# sound_module.py (A separate file)
def play_jingle():
    print("🎵 Happy tune playing! 🎵")

# main.py (Your main program)
import sound_module
sound_module.play_jingle()

```

<br>

### 1.6. Building Our Own Module / 构建我们自己的模块

You can organize your own code easily. Create a file named `kitchen.py`:

你可以轻松地组织自己的代码。创建一个名为 `kitchen.py` 的文件：

```python
# kitchen.py
def microwave_beep():
    print("BEEP! BEEP! BEEP!")

def oven_timer():
    print("DING! Food is ready!")

```

Now, in a different file in the same folder, you can use these tools:

现在，在同一个文件夹下的另一个文件里，你就可以使用这些工具了：

```python
import kitchen
kitchen.microwave_beep()
kitchen.oven_timer()

```

**Key Takeaways from Section 1 / 本节核心要点:**

1. Functions are like preset shortcuts. / 函数就像是预设的快捷方式。
2. Parameters make functions flexible. / 参数让函数具有灵活性。
3. Modules help organize code into separate files. / 模块帮你把代码整理到不同的文件中。
4. `import` lets you reuse code across different programs. / `import`（导入）让你能够在不同程序间重用代码。

<br>

---

## Section 2. Function Basic Syntax

## 第 2 节：函数基础语法

### 2.1. What is a Function Structurally? / 从结构上看，函数是什么？

Think of a function like a recipe or a small factory:

可以把函数看作是一份食谱或一家小工厂：

1. **Receive ingredients** (Parameters/Arguments) / **接收原料**（参数）
2. **Follow steps** (The internal code block) / **遵循步骤**（内部的代码块）
3. **Give a result** (Return value) / **交付成果**（返回值）

<br>

### 2.2. Function Structure in Python / Python 中的函数结构

Every Python function follows this strict syntax:

每一个 Python 函数都遵循这种严格的语法：

```python
def magic_oven(ingredient):  # Function header (def keyword, name, and parameters)
    output = str(ingredient) + " cookie"  # Function body (indented code)
    return output  # Giving back the result

```

* `def`: Tells Python you are defining a function. / 告诉 Python 你正在定义一个函数。
* `: ` (Colon): Placed at the end of the header. It tells Python "the instructions are starting now." / （冒号）：放在函数头的末尾。它告诉 Python“指令现在开始了”。
* **Indentation**: The code inside the function *must* be indented (usually 4 spaces). / **缩进**：函数内部的代码**必须**缩进（通常为 4 个空格）。

<br>

### 2.3. Multiple Parameters: Shape-Shifting Greetings / 多个参数：会变形的问候语

A function can take as many parameters as you need. Just separate them with commas.

一个函数可以接收任意数量的参数。只需要用逗号把它们隔开即可。

```python
def flexible_greet(name, greeting):
    print(str(greeting) + ' ' + str(name) + '!')

flexible_greet("Charlie", "Good morning")
flexible_greet("Diana", "Ni hao")

```

**Warning:** The order matters! If you type `flexible_greet("Good morning", "Charlie")`, it will print "Charlie Good morning!".

**警告：** 顺序很重要！如果你写成 `flexible_greet("Good morning", "Charlie")`，它会打印出“Charlie Good morning!”。

<br>

### 2.4. Return Values: The Calculator Function / 返回值：计算器函数

Sometimes we don't want a function to print something to the screen; we want it to calculate a value and give it back to us so we can use it later. We use the `return` keyword for this.

有时候我们并不希望函数在屏幕上打印内容；我们希望它计算出一个值并把它交还给我们，以便后续使用。为此我们使用 `return`（返回）关键字。

```python
def circle_area(radius):
    area = 3.14 * radius ** 2
    return area

# We save the returned value to a variable
pizza_area = circle_area(30)
pizza_price = pizza_area * 0.02
print("Pizza price is: $" + str(pizza_price))

```

<br>

### 2.5. Common Beginner Mistakes / 初学者常见错误

Watch out for these frequent syntax errors:

小心这些高频的语法错误：

**Case 1: Missing Colon / 情况 1：漏写冒号**

```python
# Wrong (SyntaxError)
def bad_function()
    print("Oops")

# Right
def good_function():
    print("Yay!")

```

**Case 2: Wrong Indentation / 情况 2：错误的缩进**

```python
# Wrong (IndentationError)
def messy_function():
print("No indent!")

# Right
def clean_function():
    print("Perfect!")

```

<br>

### 2.6. Multi-Parameter Function Demo: BMI Calculator / 多参数函数演示：BMI计算器

Let's build a practical function that calculates Body Mass Index (BMI).

让我们编写一个实用的函数来计算身体质量指数（BMI）。

```python
def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    bmi = weight / (height ** 2)
    return bmi

# Weight in kg, height in meters
print("BMI:", calculate_bmi(70, 1.75)) 

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question 1: If we know BMI and weight, how do we find height? / 问题 1：如果我们知道 BMI 和体重，如何求身高？**
> * *Math derivation (数学推导):* Since $BMI = Weight / Height^2$, we can rearrange it to $Height^2 = Weight / BMI$. Therefore, $Height = \sqrt{Weight / BMI}$.
> （既然 $BMI = 体重 / 身高^2$，我们可以变形为 $身高^2 = 体重 / BMI$。因此，$身高 = \sqrt{体重 / BMI}$。）
> 
> 
> * **Question 2: What is the difference between `x**1/2` and `x**(1/2)`? / 问题 2：`x**1/2` 和 `x**(1/2)` 有什么区别？**
> * Order of operations! `x**1/2` means $(x^1) / 2$, which just cuts $x$ in half.
> （运算顺序的区别！`x**1/2` 意思是 $(x^1) / 2$，也就是把 $x$ 劈成两半。）
> * `x**(1/2)` correctly forces the fraction to calculate first, performing a square root ($\sqrt{x}$).
> （`x**(1/2)` 会正确地强制先计算分数部分，从而执行开平方根操作 ($\sqrt{x}$)。）
> 
> 
> * **Question 3: How check if the height formula is correct? / 问题 3：如何验证身高公式是否正确？**
> * Plug in known values! If `calculate_bmi(70, 1.75)` gives roughly `22.85`, then calculating $\sqrt{70 / 22.85}$ should give us back `1.75`.
> （代入已知数值测试！如果 `calculate_bmi(70, 1.75)` 得到的大约是 `22.85`，那么计算 $\sqrt{70 / 22.85}$ 应该能让我们重新得到 `1.75`。）
> 
> 
> 
> 

<br>

---

## Section 3. Advanced Parameters & Return Values

## 第 3 节：进阶参数与返回值

### 3.0. Parameter V.S. Argument / 形式参数 V.S. 实际参数

* **Parameter**: A parameter is a variable listed inside the parentheses in the function definition. It acts as a placeholder for values that will be supplied later when the function is called.

* **形参（Parameter）**: 形参是写在**函数定义**的圆括号内的变量。它充当占位符，用于接收后续调用函数时传入的值。

* **Argument**: An argument is the actual value passed into a function when the function is called. It is the real data that fills the parameter placeholder.

* **实参（Argument）**: 实参是**调用函数**时传入函数的真实值。它是填充到形参占位符里的实际数据。


<br>


### 3.1. Positional vs Keyword Arguments / 位置参数与关键字参数

When passing multiple arguments into a function, Python matches them by their position by default. But you can also explicitly state which parameter you are targeting.

当向函数传递多个参数时，Python 默认会根据它们的位置进行匹配。但你也可以明确指出你想给哪个参数赋值。

```python
def make_pizza(size, toppings):
    print("Making " + str(size) + "cm pizza with " + str(toppings))

# Positional (Order matters)
make_pizza(30, "mushrooms")

# Keyword (Order doesn't matter!)
make_pizza(toppings="cheese", size=20)

```

**Why use keyword arguments?** It makes your code highly readable. Imagine seeing `make_pizza(25, ["pepperoni"])`. It's somewhat confusing. `make_pizza(size=25, toppings=["pepperoni"])` is crystal clear.

**为什么要用关键字参数？** 它能让你的代码极具可读性。想象一下看到 `make_pizza(25, ["pepperoni"])`，可能有点让人迷惑。而 `make_pizza(size=25, toppings=["pepperoni"])` 则一目了然。

<br>

### 3.2. Default Parameters / 默认参数

You can give a parameter a default value. If the user doesn't provide that argument, Python will automatically use the default.

你可以给参数一个默认值。如果用户没有提供该参数，Python 会自动使用这个默认值。

```python
def calculate_shipping(weight, base_fee=5.0):
    price = weight * 1.2 + base_fee
    return price

print(calculate_shipping(3.5))       # Uses the default base_fee of 5.0
print(calculate_shipping(2.0, 4.0))  # Overrides the default with 4.0

```

<br>

### 3.3. Multiple Return Values (Tuple Unpacking) / 多个返回值（元组解包）

In many programming languages, a function can only return one thing. In Python, a function can return multiple values separated by commas. Python packages them into a "Tuple".

在许多编程语言中，函数只能返回一样东西。但在 Python 中，函数可以返回由逗号分隔的多个值。Python 会把它们打包成一个“元组（Tuple）”。

```python
def box_calculator(length, width, height):
    volume = length * width * height
    surface = 2 * (length*width + length*height + width*height)
    return volume, surface  # Returns multiple values!

# Direct unpacking: Python assigns volume to 'vol' and surface to 'surf'
vol, surf = box_calculator(2, 2, 2)
print("Perfect cube volume: " + str(vol))

```

<br>

### 3.4. Variable Scope (Local vs. Global) / 变量作用域（局部与全局）

Variables inside a function are **Local**. They only exist inside that function. Variables created outside all functions are **Global**.

函数内部的变量是**局部变量（Local）**。它们只存在于该函数内部。在所有函数外部创建的变量则是**全局变量（Global）**。

```python
temperature = 25  # Global variable

def adjust_temp():
    temperature = 18  # This creates a NEW, Local variable!
    print("Inside function: " + str(temperature) + "C")

adjust_temp()
print("Outside function: " + str(temperature) + "C")  # Still 25!

```

If you *must* change a global variable from inside a function, you must use the `global` keyword to tell Python: "Don't create a local copy, use the outside one."

如果你**必须**从函数内部去修改一个全局变量，你必须使用 `global` 关键字来告诉 Python：“不要创建局部副本，去用外面那个变量。”

```python
score = 0
def update_points():
    global score
    score = score + 10  # Now modifies the global variable

```

<br>

### 3.5. Naming Best Practices / 命名最佳实践

A good function name should tell you exactly what it does.

一个好的函数名应该能准确告诉你它在做什么。

* **Good / 好的示例:** `calculate_tax()`, `get_user_profile()`, `convert_to_fahrenheit()`
* **Bad / 坏的示例:** `tax()` (Is it calculating tax? Paying tax? / 是在算税还是在交税?), `user()` (Verb is missing / 缺少动词), `temp_conv()` (Abbreviations get confusing / 缩写容易造成困惑).
* **Checklist / 检查清单:** Use lowercase words separated by underscores (`snake_case`), start with a verb, and keep it under 3 words.
（使用由下划线分隔的小写单词即`蛇形命名法`，以动词开头，并尽量控制在 3 个单词以内。）

<br>

---

## Section 4. The Python Modules System

## 第 4 节：Python 模块系统

### 4.1. Basic Module Import Methods / 基本模块导入方法

Python comes with a "Standard Library"—a massive collection of built-in modules. You just have to import them.

Python 附带了一个“标准库”——一个巨大的内置模块集合。你只需要将它们导入即可使用。

**Method 1: Full Module Import / 方法 1：导入整个模块**

```python
import math
print(math.sqrt(25))  # We must specify math. before the function

```

**Method 2: Specific Function Import / 方法 2：导入特定函数**

```python
from random import randint
print(randint(1, 50)) # No need to type random. before the function

```

*Warning:* Be careful with `from X import *`. It can cause "name collisions" where an imported function overwrites a function you wrote with the same name!

*警告：* 请慎用 `from X import *`。它可能会导致“命名冲突”，也就是说，导入的函数可能会覆盖掉你自己写的同名函数！

<br>

### 4.2. Upgrading our Print Statements (f-strings) / 升级我们的 Print 语句（f-strings）

Let's calculate the hypotenuse using the `math` library. Up until now, we've been using `+` to combine strings and variables. Let's learn a modern Python trick called **f-strings**.

让我们使用 `math` 库来计算直角三角形的斜边。到目前为止，我们一直在用 `+` 号来拼接字符串和变量。现在我们来学习一个现代 Python 的小技巧，叫做 **f-strings（格式化字符串）**。

By putting an `f` before a string, you can inject variables directly inside curly braces `{}`.

通过在字符串前加一个字母 `f`，你就可以将变量直接注入到大括号 `{}` 里面。

```python
import math

a = 3
b = 4
c = math.sqrt(a**2 + b**2)

# Old way:
# print("The hypotenuse is: " + str(c))

# New f-string way (Cleaner and faster):
print(f"The hypotenuse is: {c}")

```

<br>

### 4.3. Standard Libraries Demo / 标准库演示

Python's standard modules can do amazing things right out of the box:

Python 的标准模块开箱即用，能实现非常棒的功能：

**The `random` library / `random`（随机）库:**

```python
from random import choice
participants = ["Alice", "Bob", "Charlie", "Diana"]
winner = choice(participants)
print(f"Congratulations {winner}!")

```

**The `time` library / `time`（时间）库:**

```python
import time
for i in range(3, 0, -1):
    print(i)
    time.sleep(1) # Pauses the program for 1 second
print("Blast off! 🚀")

```

<br>

### 4.4. Understanding Namespaces / 理解命名空间

Think of modules as separate **toolboxes**.

可以把模块当成独立的**工具箱**。

If you have a hammer in your Garage toolbox and a hammer in your Kitchen toolbox, you need to specify which one you want.

如果你车库的工具箱里有一把锤子，厨房的工具箱里也有一把锤子，你就必须指明你要的是哪一把。

```python
import math
import mymath  # Hypothetical custom module

math.sqrt(16)   # Grabs sqrt from the math toolbox
mymath.sqrt(16) # Grabs sqrt from your custom toolbox

```

<br>

---

## Section 5. Practical Python Examples for Beginners

## 第 5 节：适合初学者的实用 Python 案例

Let's combine everything we've learned into three real-world projects.

让我们把前面学到的所有知识结合起来，做三个现实世界的小项目。

### Example 1: Auto-generated Password Program / 案例 1：自动生成密码程序

**Goal:** Create a function that generates a random, secure password of a given length.

**目标：** 创建一个函数，能够生成指定长度的随机、安全密码。

```python
import random

def generate_password(length=8):
    # Characters we want to choose from
    chars = "abcdefghijkmnpqrstuvwxyz23456789"
    this_password = ''
    i = 1
    
    while(i <= length):
        this_password = this_password + random.choice(chars)
        i = i + 1
        
    return this_password

print(generate_password(10)) # Generates a 10-character password

```

> **🧠 Exercise: How can we add random uppercase and lowercase characters? / 练习：如何添加随机的大写和小写字符？**
> *Solution (答案):* We can use the `random.random()` function (which gives a decimal between 0 and 1) to simulate a coin toss.
> （我们可以使用 `random.random()` 函数（它会给出一个 0 到 1 之间的小数）来模拟抛硬币。）
> ```python
>         char = random.choice(chars)
>         if random.random() > 0.5:
>             char = char.upper() # 50% chance to make it uppercase
>         this_password = this_password + char
> 
> ```
> 
> 

<br>

### Example 2: Simple Calculator / 案例 2：简易计算器

**Goal:** A function that performs basic math operations based on a string input.

**目标：** 一个能根据传入的字符串符号来执行基础数学运算的函数。

```python
def calculator(a, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":  # Added multiplication!
        return a * b
    elif operator == "/":  # Added division!
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

print(f"5 * 3 = {calculator(5, 3, '*')}")

```

<br>

### Example 3: Temperature Conversion System / 案例 3：温度转换系统

**Goal:** Convert between Celsius and Fahrenheit. / **目标：** 在摄氏度和华氏度之间进行转换。
Formula (公式): $F = (C \times 9/5) + 32$

```python
def c_to_f(c):
    return (c * 9/5) + 32

print(f"0C is {c_to_f(0)}F")

```

> **🧠 Exercise: Write the function `f_to_c` and verify it. / 练习：编写函数 `f_to_c` 并验证其正确性。**
> *Solution (答案):* We have to reverse the math. Subtract 32, then multiply by 5/9.
> （我们必须把数学公式反过来。先减去 32，再乘以 5/9。）
> ```python
> def f_to_c(f):
>     return (f - 32) * 5/9
> 
> ```
> 
> 
> *How to verify correctness? / 如何验证其正确性？* A "round-trip" test. If we convert 100°C to Fahrenheit, and then convert that result back to Celsius, we should get exactly 100 back.
> （做一个“往返”测试。如果我们把 100°C 转换成华氏度，然后再把结果转回摄氏度，我们应该能完美地得到 100。）
> ```python
> temp_f = c_to_f(100)       # becomes 212.0
> test_c = f_to_c(temp_f)    # becomes 100.0
> print(test_c == 100)       # Prints True! Our math is correct.
> 
> ```
> 
> 

---

**Congratulations! / 恭喜你！** You have mastered the fundamentals of Python Functions and Modules. You now have the skills to write reusable, clean, and organized code. Keep practicing by organizing your future scripts into functions!

你已经掌握了 Python 函数与模块的基础知识。你现在已经具备了编写可重用、整洁且结构清晰的代码的技能。在未来的学习中，请继续练习把你写下的脚本组织成一个个函数吧！


