# Errors and Exception Handling

错误与异常处理

---

<br>

## Section 1. Errors in Python / 第一章：Python 中的错误

### 1.1 When Coding Meets Real Life / 当编程遇上现实生活

Errors are an inevitable part of programming, much like unexpected events in real life. Understanding them is the first step to writing robust code.
错误是编程中不可避免的一部分，就像现实生活中的意外事件一样。理解它们是编写健壮代码的第一步。

**Example 1: The Missing Classroom / 案例 1：消失的教室**

```python
open("non_existent_file.txt") 
# Like searching for classroom 404 that doesn't exist
# 就像在寻找一个根本不存在的 404 教室

```

*Explanation / 解释：* This triggers a `FileNotFoundError`. The program is trying to interact with a resource that is not there. / 这会引发 `FileNotFoundError`（文件未找到错误）。程序正在尝试访问一个不存在的资源。

**Example 2: Zero Division Drama / 案例 2：零除闹剧**

```python
total_people = 0
cake_slices = 8 / total_people
# Like preparing cake slices when no one comes to the party
# 就像在没有人来参加派对的情况下准备分发蛋糕

```

*Explanation / 解释：* This triggers a `ZeroDivisionError`. Mathematically and programmatically, dividing by zero is impossible. / 这会引发 `ZeroDivisionError`（零除错误）。在数学和编程中，除以零都是不可能的。

<br>

### 1.2 Meet Python's Error Messages / 认识 Python 的错误信息

Here are the 5 most common errors you will encounter:
以下是你最常遇到的 5 种错误：

1. **SyntaxError (语法错误)**
*Code:* `while True` (Missing colon / 缺少冒号)
*Meaning:* You broke the grammatical rules of Python. / 你违反了 Python 的语法规则。
2. **NameError (名称错误)**
*Code:* `print(new_variable)`
*Meaning:* You are trying to use a variable that hasn't been created yet. / 你正在尝试使用一个尚未被创建的变量。
3. **TypeError (类型错误)**
*Code:* `1 + 'a'`
*Meaning:* You are combining incompatible data types (e.g., adding a number to a string). / 你正在组合不兼容的数据类型（例如，将数字与字符串相加）。
4. **FileNotFoundError (文件未找到错误)**
*Code:* `fi = open('okokokokok.txt','r')`
*Meaning:* The file path provided does not lead to an existing file. / 提供的文件路径没有指向一个存在的文件。
5. **IndentationError (缩进错误)**
*Code:*
```python
while True:
print('yes') # Missing 4 spaces / 缺少 4 个空格

```


*Meaning:* Python relies on indentation for structure. Missing spaces ruin the structure. / Python 依赖缩进来区分代码结构。缺失空格会破坏这种结构。


<br>

### 1.3 & 1.4 Let's Read Error Messages Together! / 让我们一起阅读错误信息

When Python crashes, it provides a "Traceback". This is your roadmap to fixing the bug.
当 Python 崩溃时，它会提供一个 "Traceback"（回溯）。这是你修复 bug 的路线图。

```python
Traceback (most recent call last):
  File "demo.py", line 3, in <module>
    print(undefined_var)
NameError: name 'undefined_var' is not defined

```

**Breakdown / 信息拆解：**

1. **Traceback (回溯)**: The start of the error roadmap. / 错误路线图的起点。
2. **File "demo.py"**: Tells you *where* the error happened. / 告诉你错误发生在哪一个文件。
3. **line 3**: The exact line number of the crash. / 崩溃的确切行号。
4. **NameError**: The type of error. / 错误的类型。
5. **undefined_var**: The specific variable causing the issue. / 导致问题的具体变量。

<br>

### 1.5 Practice Questions / 练习题

**Question 1: What's the error here? / 这里是什么错误？**

```python
def greet():
print("Hello!")  # Missing indentation
greet()

```

> **Answer / 答案:** `IndentationError`. The code inside a function must be indented. / 缩进错误。函数内部的代码必须缩进。

**Question 2: What's the error here? / 这里是什么错误？**

```python
age = "20"
years_to_drive = age - 16

```

> **Answer / 答案:** `TypeError`. You cannot subtract an integer (`16`) from a string (`"20"`). / 类型错误。你不能从字符串（`"20"`）中减去整数（`16`）。

---

<br>

## Section 2. Exception Handling in Python / 第二章：Python 中的异常处理

### 2.1 Basic Try-Except Structure / 基础的 Try-Except 结构

Exception handling prevents your program from crashing when an error occurs.
异常处理可以防止你的程序在发生错误时崩溃。

```python
try:
    # Code that might fail / 可能失败的代码
    result = 10 / 0
except ZeroDivisionError:
    # What to do if it fails / 如果失败了该怎么办
    print("Oops! Can't divide by zero! / 糟糕！不能除以零！")

```

* `try`: Contains the risky code. / 包含有风险的代码。
* `except`: Catches and handles specific errors. Like a seatbelt for your code! / 捕获并处理特定的错误。就像你代码的安全带！

<br>

### 2.2 Case: Let's Break a Calculator! / 案例：搞坏计算器！

What if someone tries to calculate BMI with zero height?
如果有人试图用零身高来计算 BMI 会怎样？

```python
try:
    weight = 70
    height = 0
    bmi = weight / height
except ZeroDivisionError:
    print("Alert! Did you enter height as zero?")
    print("警告！你输入的身高是零吗？")

```

This catches the **specific** error and provides feedback instead of a program crash.
这会捕获**特定**的错误并提供反馈，而不是让程序崩溃。

<br>

### 2.3 Case: File Detective Game / 案例：文件侦探游戏

What if a student list file is missing?
如果学生名单文件丢失了怎么办？

```python
try:
    with open("ghost_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Pssst... this file doesn't exist!")
    print("嘘... 这个文件不存在！")

```

<br>

### 2.4 The Safety Net (Catch-All) / 安全网（捕获所有异常）

When you aren't sure exactly what might go wrong, use the general `Exception`.
当你不确定究竟会出什么错时，使用通用的 `Exception`。

```python
try:
    magic_number = "100" + 5
except Exception as e:
    print(f"An error occurred: {e}") 
    # Outputs: An error occurred: can only concatenate str (not "int") to str

```

`Exception as e` catches the error and stores the detailed message in the variable `e`.
`Exception as e` 会捕获错误，并将详细信息存储在变量 `e` 中。

<br>

### 2.5 Friendly Error Messages / 友好的错误提示

Convert technical errors into human-friendly messages for your software users.
为你的软件用户将技术错误转换为友好的提示信息。

```python
try:
    user_age = int(input("Enter age / 输入年龄: "))
except ValueError:
    print("Hey! Numbers only please :) / 嘿！请只输入数字 :)")

```

<br>

### 2.6 Challenge Question / 挑战问题

**Guess: What will happen in this code? / 猜猜看：这段代码会发生什么？**

```python
try:
    guests = int(input("Number of guests: "))
    1 + '2'  # Intentional bug
    sugar_per_person = 50
    total_sugar = sugar_per_person * guests
    print("Needed sugar: " + str(total_sugar) + "g")
except ValueError:
    print("Numbers only for guests please!")
except Exception as e:
    print(e)

```

> **Answer / 答案:**
> 1. If the user types a word (e.g., "five"): `int()` fails immediately. It triggers a `ValueError`, printing `"Numbers only for guests please!"`. / 如果用户输入字母（如"five"）：`int()` 立即失败，触发 `ValueError`，打印 "Numbers only..."。
> 2. If the user types a valid number (e.g., `5`): `int()` succeeds, but the next line `1 + '2'` triggers a `TypeError`. Because `TypeError` is not a `ValueError`, it falls to the catch-all `except Exception as e`. It will print: `unsupported operand type(s) for +: 'int' and 'str'`. / 如果用户输入有效数字（如 `5`）：走到下一行 `1 + '2'` 时会触发 `TypeError`，被通用的 `Exception` 捕获，打印出类型不匹配的系统错误信息。
> 
> 

---

<br>

## Section 3. Handling Multiple Exceptions / 第三章：处理多个异常

### 3.1 & 3.2 Handling Different Error Types / 处理不同的错误类型

You can stack multiple `except` blocks to handle different scenarios uniquely.
你可以堆叠多个 `except` 块，以针对不同情况进行独特的处理。

```python
try:
    age = int(input("Age: "))
    print(str(100/age))
except ValueError:
    print("Numbers only! / 只能输入数字！")  
except ZeroDivisionError:
    print("Age can't be zero! / 年龄不能为零！") 

```

**Question: What will happen if we input 0? string? 4? / 如果我们输入 0？字符串？4 会怎样？**

> * **Input `0`:** Triggers `ZeroDivisionError`. Prints "Age can't be zero!".
> * **Input `"string"`:** Triggers `ValueError`. Prints "Numbers only!".
> * **Input `4`:** Calculation succeeds (`100/4`). Prints `25.0`.
> 
> 

<br>

### 3.3 How It Works / 运行机制

* Python checks the error against the `except` blocks top-to-bottom. / Python 自上而下检查 `except` 块中的错误。
* Only the **first matching** block executes; the rest are skipped. / 只有**第一个匹配**的块会执行；其余的将被跳过。

<br>

### 3.4 Tuple-style Catching / 元组形式的异常捕获

If you want to handle different errors with the *exact same response*, group them in a tuple.
如果你想用**完全相同的响应**来处理不同的错误，可以将它们放在一个元组中。

```python
try:
    with open("grades.txt") as f:
        print(f.read())
except (FileNotFoundError, PermissionError):
    print("File problem! Check if the file exists and you have access.")
    print("文件问题！请检查文件是否存在以及你是否有权限。")

```

<br>

### 3.5 Grade Calculator Conversion / 成绩计算器转换

**Original:**

```python
try:
    total = float(input("Total points: "))
    earned = float(input("Earned points: "))
    percentage = (earned/total)*100
except ValueError:
    print("Numbers only!")
except ZeroDivisionError:
    print("Total can't be zero!")

```

**Question: Change it into Tuple-style? / 将其改为元组形式？**

```python
try:
    total = float(input("Total points: "))
    earned = float(input("Earned points: "))
    percentage = (earned/total)*100
except (ValueError, ZeroDivisionError) as e:
    print(f"Invalid input error / 输入无效错误: {e}")

```

*(Note: While possible, separating them as in the original code is often better for giving users specific instructions). / (注意：虽然可以这么做，但像原代码那样分开处理通常更能给用户提供具体的指导)。*

<br>

### 3.6 Practice Example: Pet Age / 练习：宠物年龄

```python
try:
    human_years = int(input("Dog's age: "))
    dog_years = human_years * 7
    print("Dog age: " + str(dog_years))
except ValueError:
    print("Enter whole number!")
except Exception:
    print("Something unexpected happened!")

```

**Question: Change it into Tuple-style? Do we really need to do that? / 将其改为元组形式？我们真的需要这么做吗？**

> **Answer / 答案:** We *should not* do that here. `Exception` is a catch-all that already includes `ValueError`. Grouping them as `except (ValueError, Exception)` is redundant. Furthermore, it is a best practice to separate known, expected errors (`ValueError`) from unknown, unexpected crashes (`Exception`) so you can provide tailored feedback. / 我们**不应该**在这里这样做。`Exception` 已经是一个包含 `ValueError` 的通用捕获器。将它们组合成 `except (ValueError, Exception)` 是多余的。此外，最佳实践是将已知的错误与未知的崩溃分开，以便提供量身定制的反馈。

---

<br>

## Section 4. Exception Handling - finally and else / 第四章：异常处理的 finally 与 else

### 4.1 `finally`: Always Executes! / 总是执行！

The `finally` block runs **no matter what happens**—whether an error occurred or not. It is primarily used for cleanup tasks like closing files or closing database connections.
无论是否发生错误，`finally` 块**总是会运行**。它主要用于清理任务，如关闭文件或断开数据库连接。

<br>

### 4.2 File Handling with `finally` / 使用 finally 处理文件

**Guess: What will happen? / 猜猜看：会发生什么？**

```python
try:
    file = open("diary.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Diary not found!")
finally:
    # Note: If file failed to open, 'file' might not exist here.
    # In a real app, you should check if 'file' exists before closing it.
    print("File handler cleaned up")

```

> **Answer / 答案:** If `diary.txt` doesn't exist, it prints "Diary not found!", and then it immediately proceeds to the `finally` block and prints "File handler cleaned up". / 如果文件不存在，它会打印 "Diary not found!"，然后直接进入 `finally` 块，打印 "File handler cleaned up"。

<br>

### 4.3 & 4.4 The Special `else` Clause / 特殊的 else 子句

The `else` block runs **only if the `try` block was 100% successful** (no exceptions).
`else` 块**仅在 `try` 块 100% 成功时（无异常发生）** 才会运行。

**Why use `else`? / 为什么使用 else？**
It keeps your `try` block short and focused only on the code that might actually fail. It prevents you from accidentally catching errors in the code that follows the risky operation.
它使你的 `try` 块保持简短，且仅关注可能真正失败的代码。这可以防止你意外捕获后续安全代码中的错误。

<br>

### 4.5 Real-World Example: Safe Config Loader / 真实案例：安全的配置加载器

**Question: Who can explain the following program? / 谁能解释下面的程序？**

```python
config_file = False
try:
    config_file = open("game_config.cfg")
except FileNotFoundError:
    print("⚠ Config file missing! / 配置文件丢失！")
else:
    # Only runs if the file opened successfully
    # 仅在文件成功打开时运行
    settings = config_file.read()
    print("Game configuration loaded! / 游戏配置已加载！")
finally:
    # Always runs, ensures the file is closed if it was opened
    # 总是运行，确保如果文件被打开了，就一定会被关闭
    if config_file:
        config_file.close()
    print("Resource cleanup completed / 资源清理完成")

```

<br>

### 4.6 & 4.7 The Complete Pattern / 完整模式

The ultimate exception handling structure follows: `try` -> `except` -> `else` -> `finally`.
终极异常处理结构遵循：`try` -> `except` -> `else` -> `finally`。

**Question: Who can explain the following function? / 谁能解释下面的函数？**

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero! / 零除错误！")
    else:
        print("Result is " + str(result))
    finally:
        print("Operation complete / 操作完成\n")

safe_divide(10, 2)
safe_divide(5, 0)

```

> **Explanation / 解释:**
> * For `safe_divide(10, 2)`: The `try` succeeds (result=5.0). The `except` is skipped. The `else` runs (prints Result). The `finally` runs (prints Complete). / 成功执行，跳过 except，执行 else 和 finally。
> * For `safe_divide(5, 0)`: The `try` fails. The `except` catches it (prints Division by zero). The `else` is skipped. The `finally` runs (prints Complete). / 发生错误，执行 except，跳过 else，执行 finally。
> 
> 

---

<br>

## Section 5. Exception Handling in Action / 第五章：异常处理实战

### 5.1 Network Requests: Connection Timeout / 网络请求：连接超时

```python
import requests
try:
    response = requests.get("https://www.baidu.com", timeout=3)
except requests.exceptions.ConnectTimeout:
    print("Oops! Connection took too long! / 糟糕！连接耗时太长！")

```

*It waits up to 3 seconds. If the server doesn't respond, the program handles the timeout gracefully instead of crashing. / 它最多等待 3 秒。如果服务器未响应，程序会优雅地处理超时，而不是直接崩溃。*

<br>

### 5.2 Retry Mechanism / 重试机制

**Question: How can we dynamically change the wait-time? (e.g., First time 3s, second 2s, third 1s) / 如何动态改变等待时间？**

```python
import time, requests

for attempt in range(3): # attempt will be 0, 1, 2
    try:
        requests.get("https://www.baidu.com", timeout=3)
        print("Success! / 成功！")
        break # Exit loop on success / 成功后退出循环
    except Exception:
        print("Attempt " + str(attempt+1) + " failed / 尝试失败")
        # Dynamic wait time: 3 minus the current attempt index (0, 1, 2)
        # 动态等待时间：3 减去当前的尝试索引
        wait_time = 3 - attempt 
        print(f"Waiting {wait_time} seconds... / 等待 {wait_time} 秒...")
        time.sleep(wait_time)

```

<br>

### 5.3 Checking Duplicate Usernames (Using `raise`) / 检查重复用户名 (使用 raise)

You can use `raise` to manually trigger an error when a business rule is violated.
当违反业务规则时，你可以使用 `raise` 手动触发错误。

**Question: How can we use a while-loop to add multiple users? / 如何使用 while 循环添加多个用户？**

```python
existing_users = ["alice", "bob", "charlie"]

while True:
    try:
        new_user = input("Choose username (or 'q' to quit): ")
        if new_user.lower() == 'q':
            break
            
        if new_user in existing_users:
            raise ValueError("Username taken! / 用户名已被占用！")
            
        existing_users.append(new_user)
        print(f"Welcome, {new_user}! / 欢迎！")
        
    except ValueError as e:
        print(e)

```

<br>

### 5.4 Password Strength Check / 密码强度检查

```python
def check_password(pwd):
    if len(pwd) < 8:
        raise Exception("Password too short! / 密码太短！")
    if not any(c.isdigit() for c in pwd):
        raise Exception("Add numbers! / 需包含数字！")

try:
    check_password("weak")
except Exception as e:
    print("Weak password: " + str(e))

```

<br>

### 5.5 Fahrenheit Input Validation / 华氏度输入验证

**Question: Celsius to Fahrenheit? / 摄氏度转华氏度？**

```python
try:
    celsius = float(input("Enter Celsius / 输入摄氏度: "))
except ValueError:
    print("Numbers only please! / 请只输入数字！")
else:
    # Formula: F = (C * 9/5) + 32
    fahr = (celsius * 9/5) + 32
    print(str(celsius) + "C = " + str(round(fahr, 1)) + "F")

```

<br>

### 5.6 Temperature Range Check & Combination / 温度范围检查与整合

**Question: Put "Range Check" into the "Fahrenheit-to-Celsius" program? / 将"范围检查"整合到温度转换程序中？**

Here is the robust, combined version:
这是健壮的整合版本：

```python
try:
    fahr = float(input("Enter Fahrenheit (-100 to 212F): "))
    
    # 1. Logic Validation (Range Check) / 逻辑验证（范围检查）
    if not (-100 <= fahr <= 212):
        raise ValueError("Unrealistic temperature! / 不切实际的温度！")
        
except ValueError as e:
    # 2. Handle both typing letters AND unrealistic numbers
    # 处理输入字母和输入超出范围数字两种错误
    if str(e) == "Unrealistic temperature! / 不切实际的温度！":
        print("Invalid input: " + str(e))
    else:
        print("Numbers only please! / 请只输入数字！")
        
else:
    # 3. Execution / 成功执行转换
    celsius = (fahr - 32) * 5/9
    print(str(fahr) + "F = " + str(round(celsius, 1)) + "C")

```
