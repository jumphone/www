# Python Programming Fundamentals

# Python 编程基础

---

<br>


> **Q: What makes a good programming language?**
> **问：什么是一门好的编程语言？**
> 
> A good programming language balances **Readability** (easy for humans to understand), **Efficiency** (runs fast enough for its purpose), **Versatility** (can build different types of applications), and a **Strong Community** (lots of libraries and support). Python excels particularly in readability and community support, making it an excellent language for both beginners and professionals.
> 一门好的编程语言需要在**可读性**（易于人类理解）、**高效性**（运行速度满足需求）、**通用性**（能开发各种应用）以及**强大的社区**（丰富的库和支持）之间取得平衡。Python 在可读性和社区支持方面表现尤为突出，是初学者和专业人士的绝佳选择。

---

<br>

## Section 1: Python Basic Syntax Fundamentals / 第一章：Python 基础语法

### 1.1 Python Execution Modes / Python 的执行模式

Python code can be executed in two primary ways depending on your needs: Interactive Mode and Script Mode.
根据需求，Python 代码主要有两种执行方式：交互模式和脚本模式。

**Interactive Mode (交互模式)**
This mode is like a conversation with Python. You type a line, and Python responds immediately.
这种模式就像是和 Python 对话。你输入一行代码，Python 立即给出响应。

```python
$ python3
>>> print("Hello World!")
Hello World!
>>> exit()
```
* **Features / 特点**: Immediate feedback (即时反馈); Good for quick testing (适合快速测试); Type commands directly (直接输入命令).

**Script Mode (脚本模式)**
For larger programs, you write all your code in a file (script) and tell Python to execute the whole file at once.
对于较大的程序，你会将所有代码写在一个文件（脚本）中，然后让 Python 一次性执行整个文件。

```bash
$ nano hello.py  # Create file using a text editor like nano / 使用 nano 等文本编辑器创建文件
$ python3 hello.py
```
* **Features / 特点**: Save code permanently (永久保存代码); Better for complex programs (更适合复杂的程序); Use text editor (nano/vim) (使用文本编辑器).

<br>

### 1.2 Core Syntax Rules / 核心语法规则

**Indentation Rules / 缩进规则**
Unlike other languages that use brackets `{}` to group code, Python uses indentation (spaces). The standard is the **4-space principle**.
与其他使用大括号 `{}` 来组织代码的语言不同，Python 使用缩进（空格）。标准做法是**4空格原则**。

```python
# Correct / 正确
if True:
    print("This is properly indented")

# Error / 错误
if True:
print("This will cause IndentationError") # 会引发缩进错误
```

> **Q: Why do we need the "4-space principle"?**
> **问：为什么我们需要“4空格原则”？**
> 
> Indentation forces developers to write clean, readable code. The 4-space rule creates a visually distinct hierarchy, making it easy to see which blocks of code belong together, preventing nested code from becoming an unreadable mess.
> 缩进强制开发者编写整洁、可读的代码。4个空格的规则在视觉上创造了清晰的层级关系，让人很容易看清哪些代码块属于同一组，防止嵌套的代码变成一团乱麻。

**Code Comments / 代码注释**
Comments are notes left in the code for humans; the computer ignores them.
注释是留在代码中供人类阅读的笔记；计算机会忽略它们。

```python
# Single-line comment / 单行注释

'''
Multi-line comment
Spanning multiple lines
多行注释
跨越多行
'''

def calculate():
    """Docstring comments for functions / 用于函数的文档字符串注释"""
```

> **Q: Why do we need "Code Comments"?**
> **问：为什么我们需要“代码注释”？**
> 
> Comments explain the *why* behind the code. They help your future self remember your logic and help teammates understand your work without deciphering every line.
> 注释解释了代码背后的*原因 (Why)*。它们能帮助未来的你回忆起当时的逻辑，也能帮助团队成员理解你的工作，而无需逐行破译代码。

**Statement Separation / 语句分隔**
```python
# Use semicolon ";". Valid but not recommended / 使用分号 ";"。合法但不推荐
x=1; y=2; print(x+y)

# Preferred (line break) / 推荐方式（换行）
x = 1
y = 2
print(x + y)
```

<br>

### 1.3 Reserved Keywords / 保留关键字

Python has 35 reserved keywords (as of Python 3.7). **Important:** These cannot be used as variable or function names!
Python 有 35 个保留关键字（截至 Python 3.7）。**重要提示：** 这些关键字不能用作变量名或函数名！

|          |         |        |         |         |
|----------|---------|--------|---------|---------|
| False    | None    | True   | and     | as      |
| assert   | async   | await  | break   | class   |
| continue | def     | del    | elif    | else    |
| except   | finally | for    | from    | global  |
| if       | import  | in     | is      | lambda  |
| nonlocal | not     | or     | pass    | raise   |
| return   | try     | while  | with    | yield   |

<br>

### 1.4 Your First Python Program / 你的第一个 Python 程序

**Execution Steps on a Server / 服务器上的执行步骤**:
1. Login to Linux Server using Termius. / 使用 Termius 登录到 Linux 服务器。
2. Create file: `nano hello.py` / 创建文件。
3. Write code: `print('Hello World!')` / 编写代码。
4. Save: `Ctrl+O` → Press "enter" → `Ctrl+X` / 保存并退出。
5. Run: `python3 hello.py` / 运行代码。

<br>

### 1.5 Common Errors & Debugging / 常见错误与调试

When programming, you will inevitably make mistakes. Learning to read errors is a superpower.
在编程时，你不可避免地会犯错。学会阅读错误信息是一项超能力。

1. **NameError (命名错误)**: Using a variable or function that doesn't exist.
   ```python
   prin("Missing t")  # NameError: name 'prin' is not defined
   ```
2. **IndentationError (缩进错误)**: Breaking the spacing rules.
3. **TypeError (类型错误)**: Mixing incompatible data types.
   ```python
   "5" + 3  # TypeError: can only concatenate str (not "int") to str
   ```

**Debugging Techniques / 调试技巧**: Read errors carefully, check line numbers, use `print()` statements to track variables, and utilize AI assistants (like Kimi/ChatGPT) to explain confusing errors. / 仔细阅读错误，检查行号，使用 `print()` 追踪变量，并利用 AI 助手解释令人困惑的错误。

---

<br>

## Section 2: Variables & Data Types / 第二章：变量与数据类型

### 2.1 The Nature of Variables / 变量的本质

Think of variables as labeled boxes in a warehouse.
把变量想象成仓库里贴着标签的盒子。

```python
box_label = "item_count"  # Variable name / 变量名 (标签)
box_content = 17          # Stored value / 存储的值 (内容)
```

* **Binding (绑定)**: Variables are references (pointers) to objects in memory. / 变量是对内存中对象的引用（指针）。
* **Garbage Collection (垃圾回收)**: Python automatically cleans up data that no variables point to. / Python 会自动清理没有变量指向的数据。
* **Reassignment (重新赋值)**: 
  ```python
  x = 10    # Create object 10, bind to x / 创建对象 10，绑定到 x
  x = "cat" # Create new object "cat", rebind x / 创建新对象 "cat"，重新绑定 x
  ```

<br>

### 2.2 Variable Naming Rules / 变量命名规则

Variables can contain numbers, letters (`abcABC`), and underscores (`_`), but **cannot start with a number**.
变量可以包含数字、字母和下划线，但**不能以数字开头**。

```python
# Valid but discouraged examples / 合法但不推荐的例子 (不符合 PEP8 标准)
_privateVar = 1
MAX_LIMIT = 100
tempVar2 = 3.14

# Invalid examples / 非法例子
3attempt = 5              # SyntaxError (Cannot start with number)
special-chars = "text"    # SyntaxError (Hyphens act like minus signs)
```

**PEP8 Pro Practices / PEP8 专业实践 (Python Enhancement Proposal 8)**: Use `snake_case` (lowercase with underscores) for variables. / 变量使用 `snake_case`（全小写加下划线）。
* `studentname` → `student_name`
* `calcVal` → `calculate_value`

<br>

### 2.3 Dynamic Typing / 动态类型系统

Python figures out the data type automatically when you run the code.
Python 会在运行代码时自动推断数据类型。

```python
dynamic_var = 100          # int (整数)
print(type(dynamic_var))   # <class 'int'>

dynamic_var = "Python"     # str (字符串)
print(type(dynamic_var))   # <class 'str'>
```

**Static (C++) vs Dynamic (Python) / 静态类型 (C++) 与 动态类型 (Python)**:
In C++, you must declare the type, and it is locked forever. In Python, variables can change types freely.
在 C++ 中，你必须声明类型，且类型永久锁定。在 Python 中，变量可以自由更改类型。

> **Q: "Insufficient Computing Power" V.S. "Computing Power Redundancy" ?**
> **问：“算力不足” 与 “算力冗余” 是什么意思？**
> 
> Historically, computers had *insufficient computing power*. Languages like C++ used static typing because it allows the machine to run as fast and efficiently as possible, saving memory and CPU cycles. Today, we often have *computing power redundancy* (excess power). Python uses dynamic typing, which requires more computing power under the hood, but drastically saves *developer time*. We trade abundant computer power for precious human time.
> 历史上，计算机面临着*算力不足*的问题。像 C++ 这样的语言使用静态类型，因为它允许机器尽可能快速高效地运行，节省内存和 CPU。今天，我们通常拥有*算力冗余*（过剩的算力）。Python 使用动态类型，虽然底层需要消耗更多的算力，但极大地节省了*开发者的开发时间*。我们用丰富的计算机算力来换取宝贵的人类时间。

<br>

### 2.4 Core Data Types / 核心数据类型

Python has four primary primitive types: Integer, Float, String, and Boolean.
Python 有四种主要的原始类型：整型、浮点型、字符串和布尔型。

**1. Integer Representations (整型)**
```python
binary_num = 0b1010     # 10 (binary / 二进制)
octal_num = 0o177       # 127 (octal / 八进制)
hex_num = 0x1af         # 431 (hexadecimal / 十六进制)
number = 33             # 33 (decimal / 十进制)
```

**2. Floating-Point Precision (浮点型精度问题)**
Computers struggle to represent decimals perfectly in binary.
计算机在二进制中很难完美地表示小数。
```python
print(0.1 + 0.2 == 0.3)           # False
print(f"{0.1 + 0.2:.17f}")        # 0.30000000000000004

# Solution using Decimal library / 使用 Decimal 库解决
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # Exact 0.3
```

**3. Strings (字符串)**
```python
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes preserve
line breaks and "both" quote types''' # 三引号保留换行和引号
```

**4. Boolean (布尔型)**
```python
A = True
B = False
print(A and B) # False
print(A or B)  # True
```

<br>

### 2.5 Type Conversions / 类型转换

**Explicit Conversion / 显式转换**
```python
age = int("25")       # String to integer
pi = float("3.1415")  # String to float
price = str(9.99)     # Float to string

# Truthy conversions (What is considered True/False?) / 真值转换
bool(0)     # False (Zero is false / 0 为假)
bool("")    # False (Empty string is false / 空字符串为假)
bool("a")   # True  (Any content is true / 有内容即为真)
```

**Automatic Conversion / 自动转换**
```python
3 + 5.0         # int promoted to float -> 8.0 / 整型自动提升为浮点型
True + 10       # bool treated as int(1) -> 11 / True 被当作数字 1 计算
```

---

<br>

## Section 3: Python Operator System / 第三章：Python 运算符系统

### 3.1 Arithmetic Operators / 算术运算符

| Operator (运算符) | Description (描述)      | Example (示例)  | Result (结果) |
|-------------------|-------------------------|-----------------|---------------|
| `+`               | Addition (加)           | `5 + 3`         | 8             |
| `-`               | Subtraction (减)        | `7 - 2`         | 5             |
| `*`               | Multiplication (乘)     | `3 * 4`         | 12            |
| `/`               | True Division (真除法)  | `10 / 3`        | 3.333...      |
| `//`              | Floor Division (整除)   | `10 // 3`       | 3             |
| `%`               | Modulus (取模/求余数)   | `10 % 3`        | 1             |
| `**`              | Exponentiation (幂运算) | `2 ** 3`        | 8             |

<br>

### 3.2 Comparison Operators / 比较运算符

**Numeric / 数值比较**: `a > b`, `a == b`, `a != b` (Not equal).

**String Comparison Rules / 字符串比较规则**:
1. Compare character by character using ASCII values. / 使用 ASCII 码逐字符比较。
2. Shorter strings are considered smaller if everything else matches. / 如果前面都一样，较短的字符串更小。
3. Case-sensitive. / 区分大小写。

```python
print('Apple' < 'Banana')  # True (A=65 < B=66)
print('cat1' > 'cat')      # True (longer > shorter)
print('cat' > 'CAT')       # True (lowercase a(97) > uppercase A(65))
print('10' < '2')          # True (character '1'(49) vs '2'(50))
```

<br>

### 3.3 Logical Operators / 逻辑运算符

| X     | Y     | X and Y (与) | X or Y (或) | not X (非) |
|-------|-------|-------------|------------|------------|
| True  | True  | True        | True       | False      |
| True  | False | False       | True       | False      |
| False | True  | False       | True       | True       |
| False | False | False       | False      | True       |

**Short-Circuiting / 短路计算**: Python stops evaluating logical statements as soon as the outcome is known. / 一旦结果已知，Python 就会停止计算逻辑表达式。
```python
def check():
    print("Called!")
    return False

print(True or check())  # True is enough for 'or', check() is never called! / 短路，无输出
print(False and check())# False ruins 'and', check() is never called! / 短路，无输出
```

**Precedence Table (Order of Operations) / 优先级表**
Parentheses `()` always have the highest priority. / 括号 `()` 永远拥有最高优先级。
1. `**` Exponentiation (指数)
2. `+x`, `-x` (正负号)
3. `*`, `/`, `//`, `%` (乘除取余)
4. `+`, `-` (加减)
5. `<, >, ==, !=` Comparisons (比较)
6. `not` (非)
7. `and` (与)
8. `or` (或)

<br>

### 3.4 Assignment Operators / 赋值运算符

**Compound Operators / 复合运算符**
```python
counter = 5
counter += 3    # Equivalent to: counter = counter + 3
counter **= 2   # 8^2 = 64
```

**Mutable Object Pitfall / 可变对象陷阱**
```python
list1 = list2 = []  # Both variables point to the exact same list memory / 指向同一内存
list1.append(5)
print(list2)  # [5] (Modifying one affects the other / 牵一发而动全身)
```

<br>

### 3.5 Precedence Practice / 优先级实战练习

```python
result = 5 + 3 * 2 ** 2 // (4 % 3) - 1
# Step-by-step evaluation / 逐步计算:
# 1. Parentheses: (4 % 3) = 1
# 2. Exponent: 2 ** 2 = 4
# 3. Multiplication/Division (Left to right): 3 * 4 = 12 -> 12 // 1 = 12
# 4. Addition/Subtraction: 5 + 12 - 1 = 16
```

---

<br>

## Section 4: String Operations / 第四章：字符串操作

### 4.1 Indexing & Slicing / 索引与切片

* **Positive Index**: `0` to `Length-1`
* **Negative Index**: `-1` (last character) to `-Length`

**Slice Syntax / 切片语法**: `string[start:end:step]` (end index is NOT included / 不包含结束索引).

```python
text = "programming"
print(text[3:7])    # 'gram'
print(text[::-1])   # 'gnimmargorp' (Reverse string trick / 字符串反转)
print(text[::2])    # 'pormig' (Step by 2 / 步长为2)
```

<br>

### 4.2 String Methods Library / 字符串内置方法

```python
# Split & Join / 分割与拼接
csv = "apple,banana,cherry"
items = csv.split(",")     # ['apple', 'banana', 'cherry']
new_str = "-".join(items)  # "apple-banana-cherry"

# Stripping (Removing whitespace) / 去除空白符 (\n=换行, \t=制表符)
s = "   hello world  \t\n"
print(s.strip())    # "hello world" (Removes from both sides)
print(s.lstrip())   # "hello world  \t\n" (Left only)

# Searching / 查找
s = "Python Programming"
print(s.find('thon'))   # Returns 2 (index). Returns -1 if not found.

# Case Conversion / 大小写转换
print("Hello".lower())       # 'hello'
print("world".upper())       # 'WORLD'
print("title case".title())  # 'Title Case'
```

> **Q: What are the real-world applications of string operations?**
> **问：字符串操作在现实世界中有哪些应用？**
> 
> String operations are critical for **Data Cleaning** (removing extra spaces or fixing capitalization in datasets), **Log Parsing** (extracting error codes or timestamps from server logs), **Web Scraping** (finding specific text on websites), and **Natural Language Processing (NLP)** (breaking sentences into words for AI models).
> 字符串操作对于**数据清洗**（去除数据集中多余空格或修正大小写）、**日志解析**（从服务器日志中提取错误代码或时间戳）、**网页抓取**（在网页上查找特定文本）以及**自然语言处理 (NLP)**（将句子分解为单词供 AI 模型使用）至关重要。

<br>


### 4.3 Formatting Methods / 格式化方法

Modern Python relies heavily on formatting strings to insert variables dynamically.
现代 Python 高度依赖格式化字符串来动态插入变量。

**1. %-formatting (Legacy / 传统格式)**
```python
name = "Alice"
print("Hello, %s! You have %d messages." % (name, 5))
```

**2. str.format() (Versatile / 多功能)**
```python
print("{} + {} = {}".format(2, 3, 2+3))
print("{1} appears before {0}".format("apple", "banana")) # Ordering
```

**3. f-strings (Modern & Best, Python 3.6+ / 现代且最佳)**
```python
price = 19.99
print(f"Total: ${price * 1.1:.2f}") # .2f formats to 2 decimal places
print(f"Binary: {42:b}")            # '101010'
```

**Beginner friendly fallback / 适合新手的回退拼接方法:**
```python
name = 'John'
number = 5
print("Hello, " + name + "! You have " + str(number) + " messages.")
```

<br>

### 4.4 Escape Characters & Raw Strings / 转义字符与原始字符串

**Common Escapes / 常见转义字符**:
* `\n`: Newline (换行)
* `\t`: Tab (制表符)
* `\\`: Literal Backslash (反斜杠)
* `\"`: Double quote (双引号)

**Raw Strings / 原始字符串**: Place an `r` before the quote. It ignores escape characters. Excellent for file paths!
在引号前加 `r`。它会忽略转义字符。非常适合处理文件路径！

```python
path_raw = r"C:\new_folder\test.txt" 
print(path_raw)  # Prints exactly as written, no newline from \n
```

<br>

### 4.5 Multi-line Strings / 多行字符串

Using triple quotes allows strings to span multiple lines without needing `\n`.
使用三引号允许字符串跨越多行，而无需手动添加 `\n`。

```python
long_text = """First line
Second line
Third line"""
```
