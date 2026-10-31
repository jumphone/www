# Libraries and Multi-tasking

# 库与多任务处理

---

<br>

## Section 1: Understanding Libraries, Packages, and Modules / 第一章：理解库、包与模块

To write efficient Python code, you don't need to reinvent the wheel. Python offers a rich ecosystem of reusable code. Let's understand the hierarchy of these code structures.
为了编写高效的 Python 代码，你不需要重复造轮子。Python 提供了一个丰富的可复用代码生态系统。让我们来了解这些代码结构的层级关系。

### 1.1 Core Concepts / 核心概念

*   **Module (模块)**: A single `.py` file containing functions, classes, and variables. It is the basic unit of code organization.
    **模块**：单个 `.py` 文件，包含函数、类和变量。它是代码组织的基本单元。
*   **Package (包)**: A folder containing multiple modules. It organizes related modules together.
    **包**：包含多个模块的文件夹。它将相关的模块组织在一起。
*   **Library (库)**: A broader term focusing on functionality. A library is a collection of reusable code that may include multiple packages and modules (e.g., a library for machine learning or web scraping).
    **库**：一个更宽泛的术语，侧重于功能。库是可复用代码的集合，可能包含多个包和模块（例如，用于机器学习或网页抓取的库）。

<br>

### 1.2 Three Import Methods / 三种导入方法

Python provides different ways to bring these tools into your code depending on your needs.
Python 提供了不同的方法将这些工具引入到你的代码中，具体取决于你的需求。

**Method 1: Full Import / 方法 1：完整导入**
Get the whole toolbox. You must prefix the function with the module name.
获取整个工具箱。你必须在函数前加上模块名作为前缀。
```python
import math
print("2^5 = " + str(math.pow(2, 5)))
```

**Method 2: Specific Import / 方法 2：特定导入**
Grab just what you need. This saves typing the module name later.
只获取你需要的工具。这样后续调用时可以省去输入模块名。
```python
from random import randint
print("Random dice roll: " + str(randint(1, 6)))
```

**Method 3: Alias Import / 方法 3：别名导入**
Make it short. Very common for data science libraries.
为其起个简短的别名。这在数据科学库中非常常见。
```python
import pandas as pd
data = {'Birds': ['Eagle', 'Penguin'], 'Speed': [320, 8]}
df = pd.DataFrame(data)
print(df)
```

<br>

### 1.3 Import Method Comparison / 导入方法比较

| Method (方法) | Advantage (优势) | Use Case (适用场景) |
| :--- | :--- | :--- |
| **Full Import** (`import x`) | Prevents name conflicts / 防止命名冲突 | Large libraries, avoid namespace pollution / 大型库，避免命名空间污染 |
| **Specific Import** (`from x import y`) | Cleaner code, less typing / 代码更整洁，输入更少 | Only need 1-2 functions from module / 只需要模块中的 1-2 个函数 |
| **Alias Import** (`import x as y`) | Saves typing long names / 节省输入长名字的时间 | Frequently used libraries like pandas/numpy / 频繁使用的库，如 pandas 或 numpy |

---

<br>

## Section 2: Python Standard Library / 第二章：Python 标准库

### 2.1 Core Standard Library Modules / 核心标准库模块

The Standard Library comes pre-installed with every Python installation. No additional downloading is required.
标准库随每个 Python 安装包预装。无需额外下载。

*   `math` - Mathematical functions / 数学函数
*   `time` - Time-related functions / 时间相关函数
*   `random` - Random number generation / 随机数生成
*   `os` - Operating system interface (files/folders) / 操作系统接口（文件/文件夹操作）
*   `datetime` - Date and time manipulation / 日期与时间操作
*   `shutil` - High-level file operations (copy, move) / 高级文件操作（复制、移动）

> **Pro Tip:** Learn to use `help('modules')` or `help(math)` in the interactive shell for self-study!
> **进阶提示：** 学会在交互式终端中使用 `help('modules')` 或 `help(math)` 进行自学！

<br>

### 2.2 Deep Dive: `datetime` Module / 深入探究：`datetime` 模块

Handling time is crucial for logs, backups, and data tracking.
处理时间对于日志记录、备份和数据追踪至关重要。

**Getting Current Time / 获取当前时间:**
```python
import datetime

now = datetime.datetime.now()
print("Current time: " + str(now))
# Output format: Year-Month-Day Hour:Minute:Second.Microsecond
# 输出格式：年-月-日 时:分:秒.微秒
```

**Time Calculation with `timedelta` / 使用 `timedelta` 进行时间计算:**
You can easily add or subtract time using `timedelta`.
你可以使用 `timedelta` 轻松地加上或减去时间。
```python
future_date = now + datetime.timedelta(days=3)
print("Date after 3 days: " + str(future_date.date()))
```
*Note: `timedelta` accepts parameters like `days`, `hours`, `minutes`, `seconds`, and `weeks`.*
*注意：`timedelta` 接受诸如 `days` (天)、`hours` (小时)、`minutes` (分钟)、`seconds` (秒) 和 `weeks` (周) 等参数。*

---

<br>

## Section 3: Third-Party Libraries and pip / 第三章：第三方库与 pip

### 3.1 Introduction / 简介

Third-party libraries are extra tools you can download from **PyPI.org** (Python Package Index) to extend Python's capabilities.
第三方库是你可以从 **PyPI.org** (Python 包索引) 下载的额外工具，用于扩展 Python 的功能。
*   `pandas` - Data manipulation / 数据处理
*   `requests` - HTTP library for web communication / 用于网络通信的 HTTP 库

<br>

### 3.2 The `pip` Package Manager / `pip` 包管理器

`pip` is Python's built-in package manager. You run it from your command line (Terminal/CMD), not inside Python.
`pip` 是 Python 内置的包管理器。你需要在命令行（终端/CMD）中运行它，而不是在 Python 解释器内。

**Essential Commands / 核心命令:**
```bash
# Check version / 检查版本
$ pip3 --version

# Install a package / 安装包
$ pip3 install requests

# Install a specific version / 安装特定版本
$ pip3 install requests==2.31.0

# Upgrade a package / 升级包
$ pip3 install --upgrade requests

# List all installed packages / 列出所有已安装的包
$ pip3 list

# Show dependencies in requirements format / 以依赖文件格式显示已安装的包
$ pip3 freeze

# Show details of a specific package / 显示特定包的详细信息
$ pip3 show requests
```

<br>

### 3.3 Package Installation Optimization (Mirrors) / 包安装优化（镜像源）

Sometimes downloading from the official PyPI server is slow. You can use local mirror servers (like Tsinghua University or AliCloud) to speed up downloads.
有时从官方 PyPI 服务器下载很慢。你可以使用本地镜像服务器（如清华大学或阿里云）来加速下载。

**Temporary usage / 临时使用:**
```bash
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

**Permanent Configuration / 永久配置:**
```bash
$ pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

<br>

### 3.4 Using the `requests` Library / 使用 `requests` 库

```python
import requests

# Basic GET Request / 基础 GET 请求
response = requests.get("https://www.baidu.com")
print("Status Code: " + str(response.status_code)) # 200 means OK / 200 表示成功
print("Response Text: " + response.text[:100] + "...")
```

---

<br>

## Section 4: Practical Application - Weather Reporter / 第四章：实战应用 - 天气预报员

Let's combine web data fetching (`requests`) and time handling (`datetime`) to create a useful tool.
让我们结合网络数据抓取 (`requests`) 和时间处理 (`datetime`) 来创建一个有用的工具。

### 4.1 Fetching and Formatting Data / 获取与格式化数据

We will use the `wttr.in` service, which returns weather data in plain text.
我们将使用 `wttr.in` 服务，它以纯文本形式返回天气数据。

```python
import datetime
import requests

def get_weather(city):
    # %t = Temperature, %C = Condition
    # %t = 温度, %C = 天气状况
    url = "http://wttr.in/" + city + "?format=%t+%C"
    response = requests.get(url)
    return response.text

def weather_report(city):
    # Format time to Hour:Minute / 将时间格式化为 时:分
    time_now = datetime.datetime.now().strftime("%H:%M")
    weather = get_weather(city)
    return "[" + time_now + "] Weather in " + city + ": " + weather

print(weather_report("NewYork"))
print(weather_report("Beijing"))
```

> **Potential Issue (潜在问题):** Time zones! `datetime.datetime.now()` gets the *local* time of the computer running the script. If your server is in Beijing, querying New York's weather will still show Beijing's local time.
> **时区问题：** `datetime.datetime.now()` 获取的是运行脚本的计算机的*本地*时间。如果你的服务器在北京，查询纽约的天气显示的仍然是北京的本地时间。

---

<br>

## Section 5: Practical Application - File Backup Helper / 第五章：实战应用 - 文件备份助手

Automate your file management using the `os` and `shutil` standard libraries.
使用 `os` 和 `shutil` 标准库自动化你的文件管理。

### 5.1 The Backup Script / 备份脚本

```python
import os
import shutil

def backup_files(src_folder, dst_folder):
    # 1. Create destination if it doesn't exist / 如果目标文件夹不存在则创建
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print("Created backup directory: " + dst_folder)
    
    # 2. Iterate through files and copy / 遍历文件并复制
    for file in os.listdir(src_folder):
        if file.endswith(".txt"):  # Only backup .txt files / 仅备份 .txt 文件
            # Create full absolute/relative paths / 创建完整的绝对/相对路径
            src_path = os.path.join(src_folder, file)
            dst_path = os.path.join(dst_folder, file)
            
            # Copy the file / 复制文件
            shutil.copy2(src_path, dst_path)
            print("Successfully copied " + file + "!")

# Usage / 使用方法
# Make sure a folder named 'notes' exists before running!
# 运行前请确保存在名为 'notes' 的文件夹！
backup_files("notes", "backup")
```

**`shutil.copy()` vs `shutil.copy2()`:**
*   `copy()`: Copies the file content and permissions. / 仅复制文件内容和权限。
*   `copy2()`: Copies content, permissions, AND metadata (like creation and modification timestamps). Best for backups! / 复制内容、权限以及元数据（如创建和修改时间戳）。最适合用于备份！

---

<br>

## Section 6: Multi-tasking in Python / 第六章：Python 中的多任务处理

### 6.1 What is Multi-tasking? / 什么是多任务处理？

Multi-tasking allows your program to perform multiple operations concurrently (seemingly at the same time), improving efficiency when dealing with tasks that involve a lot of waiting (I/O-bound) or heavy calculation.
多任务处理允许你的程序并发地（看起来同时地）执行多个操作，在处理涉及大量等待（I/O密集型）或繁重计算的任务时提高效率。

**Three Main Approaches in Python / Python 中的三种主要方法:**
1.  **Threading (多线程)**: Best for I/O-bound tasks (network requests, disk reading).
2.  **Subprocess (子进程)**: Best for running external programs or OS commands.
3.  **Multiprocessing (多进程)**: Best for CPU-bound tasks (heavy mathematical computations).

<br>

### 6.2 Threading vs. Subprocess / 多线程 vs 子进程

| Feature (特性) | Threading (多线程) | Subprocess (子进程) |
| :--- | :--- | :--- |
| **Memory (内存)** | Shared (All threads share the same memory) / 共享内存 | Isolated (Each process has its own memory) / 内存隔离 |
| **Startup Speed (启动速度)** | Fast / 较快 | Slower / 较慢 |
| **Use Case (适用场景)** | I/O-bound tasks (e.g., downloading files) / I/O 密集型任务 | Running external apps (e.g., calling FFmpeg) / 运行外部程序 |
| **Communication (通信方式)** | Direct (Easy but risky due to race conditions) / 直接通信（容易产生竞争条件风险） | Explicit channels (Pipes, stdout, files) / 显式通道（管道、标准输出等） |

<br>

### 6.3 Deep Dive: Threading / 深入探究：多线程

Threading allows multiple tasks to run without stopping the main program. This brings us to the concept of Blocking vs. Non-blocking.
多线程允许在不停止主程序的情况下运行多个任务。这引出了“阻塞”与“非阻塞”的概念。

*   **Blocking (阻塞)**: The program waits until a resource is available. Nothing else can happen. / 程序等待直到资源可用。期间不能进行其他操作。
*   **Non-blocking (非阻塞)**: The program starts a task in the background and moves on to do other things. / 程序在后台启动任务，然后继续做其他事情。

#### Threading Examples / 多线程代码示例

**1. Basic Non-blocking Thread / 基础非阻塞线程:**
```python
from threading import Thread
import time

def blocking_task():
    print("Background task started... / 后台任务开始...")
    time.sleep(5)
    print("Background task finished! / 后台任务完成！")

# Start task in a new thread / 在新线程中启动任务
this_thread = Thread(target=blocking_task)
this_thread.start()

print("Main thread continues working immediately! / 主线程立即继续工作！")
print("Is thread alive? " + str(this_thread.is_alive()))

# Wait for the thread to finish before closing the program / 等待线程完成再关闭程序
this_thread.join() 
```

**2. Passing Arguments to Threads / 向线程传递参数:**
Use the `args` tuple. Note the comma `(15,)` to make it a valid tuple.
使用 `args` 元组。注意逗号 `(15,)` 以确保它是一个合法的元组。
```python
def sleep_task(sleep_time=5):
    print("Sleep time is: " + str(sleep_time))
    time.sleep(sleep_time)

# Pass argument 3 to the function / 将参数 3 传递给函数
this_thread = Thread(target=sleep_task, args=(3,))
this_thread.start()
this_thread.join()
```

**3. Getting Results Using Queues / 使用队列获取线程返回结果:**
Threads share memory, but returning variables directly is tricky. We use `queue` for thread-safe communication.
线程共享内存，但直接返回变量比较麻烦。我们使用 `queue` 进行线程安全的通信。
```python
from threading import Thread
import queue
import time

def calculate_task(q, value):
    print("Calculating...")
    time.sleep(2)
    result = value * 2
    q.put(result)  # Put result into the queue / 将结果放入队列

# Create a queue / 创建一个队列
q = queue.Queue()

# Pass the queue as an argument / 将队列作为参数传递
this_thread = Thread(target=calculate_task, args=(q, 5))
this_thread.start()
this_thread.join() # Wait for completion / 等待计算完成

# Retrieve the result from the queue / 从队列中提取结果
final_result = q.get()
print("Final Result: " + str(final_result))
```

> **Self-Study Challenge (自学挑战):** 
> Research the `subprocess` library in Python 3. How would you use it to run a simple terminal command like `ping google.com` or `ls -l` directly from your Python script?
> 探索 Python 3 中的 `subprocess` 库。你将如何使用它直接从 Python 脚本中运行简单的终端命令（如 `ping google.com` 或 `ls -l`）？
