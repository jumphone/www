# File Operations
# 文件操作

<br>

---

## Section 1: File Operations Basics / 第一章：文件操作基础

### 1.1 What is a File? / 什么是文件？

A file is essentially a data container stored on a permanent storage device, such as a hard disk. You can think of it metaphorically as a water bottle—just as a bottle stores liquid for later use, a file stores data so it can be retrieved and manipulated by programs. 

文件本质上是存储在硬盘等持久化存储设备上的数据容器。你可以把它形象地比作一个水瓶——就像瓶子用来储存液体以备后用一样，文件用来存储数据，以便程序随后检索和操作。

There are two main types of files you will encounter:
主要有两种类型的文件：
*   **Text files (文本文件)**: These are human-readable files that contain plain text characters (e.g., `.txt`, `.csv`, `.py`).
*   **Binary files (二进制文件)**: These use special formats designed for computers to read and process, such as images, compiled programs, or word documents (e.g., `.jpg`, `.docx`, `.exe`).

<br>

### 1.2 File Paths Explained / 文件路径详解

To open a file, your computer needs to know exactly where it is located. We use "paths" to describe this location, much like a home address.
要打开一个文件，计算机需要知道它的确切位置。我们使用“路径”来描述这个位置，就像家庭住址一样。

*   **Absolute path (绝对路径)**: The complete, full address starting from the root of the file system. 
*   **Relative path (相对路径)**: The address relative to your current working directory.

```python
# Absolute path (full address) / 绝对路径（完整地址）
"/home/student/documents/diary.txt"

# Relative path (from current location) / 相对路径（相对于当前位置）
"../pictures/vacation.jpg"
```

<br>

### 1.3 Opening Files: The `open()` Function / 打开文件：`open()` 函数

In Python, you interact with files using the built-in `open()` function. You must specify the "mode" in which you want to open the file.
在 Python 中，通过内置的 `open()` 函数与文件进行交互。你必须指定打开文件的“模式”。

```python
# File Opening Modes / 文件打开模式
f = open("list.txt", "r")   # Read mode: Read existing content / 读模式：读取现有内容
f = open("new.txt", "w")    # Write mode: Overwrites existing file or creates a new one / 写模式：覆盖现有文件或创建新文件
f = open("log.txt", "a")    # Append mode: Adds new content to the end of the file / 追加模式：在文件末尾添加新内容
```

<br>

### 1.4 Reading Files / 读取文件

Python provides several methods to read data from a file, collectively known as the `read()` family.
Python 提供了几种从文件中读取数据的方法，统称为 `read()` 系列函数。

```python
file = open("classlist.txt", "r")

print(file.read())       # Reads the entire file content as a single string / 将整个文件内容作为一个字符串读取
file.seek(0)             # Resets the "cursor" back to the beginning of the file / 将文件“光标”重置回开头

print(file.readline())   # Reads only the first/next line / 仅读取第一行/下一行
file.seek(0)   

print(file.readlines())  # Reads all lines and returns them as a list of strings / 读取所有行并作为字符串列表返回

file.close()             # Always remember to close the file! / 永远记得关闭文件！
```

<br>

### 1.5 Writing Files / 写入文件

When writing data, you can choose to write individual strings or multiple lines from a list.
在写入数据时，你可以选择写入单个字符串，或者从列表中写入多行内容。

```python
# Writing individual strings / 写入单个字符串
file = open("groceries.txt", "w")
file.write("Milk\n")          # \n represents a newline / \n 代表换行符
file.write("Eggs\nBread\n")
file.close()

# Writing multiple lines from a list / 写入列表中的多行
items = ["Apples\n", "Coffee\n"]
file = open("shopping.txt", "w")
file.writelines(items)        # Writes a list of strings directly / 直接写入字符串列表
file.close()
```

<br>

### 1.6 Practical Cases / 实战案例

**Case 1: Read a Class List / 案例 1：读取班级名单**
```python
# Assuming 'classlist.txt' contains Alice, Bob, and Charlie on separate lines
# 假设 'classlist.txt' 分行包含 Alice, Bob 和 Charlie

file = open("classlist.txt", "r")
students = file.readlines()
file.close()

for student in students:
    # strip() removes the hidden newline (\n) characters / strip() 用于移除隐藏的换行符
    print("Hello " + student.strip() + "!")
```

**Case 2: Create a Shopping List / 案例 2：创建购物清单**
```python
file = open("groceries.txt", "w")
file.write("Shopping List:\n")
file.write("- Milk\n- Eggs\n- Bread")
file.close()
```

**Case 3: Append to a Diary / 案例 3：追加日记内容**
```python
# Using 'a' mode ensures we don't delete previous entries
# 使用 'a' 模式确保我们不会删除以前的记录
file = open("diary.txt", "a")
file.write("\n2024-06-01: Learned file operations!")
file.close()
```

<br>

### 1.7 Important Reminders / 重要提醒

1.  **Always close files!** (`file.close()`) / **永远记得关闭文件！** 
2.  **Double-check file modes** (Don't accidentally use `w` when you mean `a`). / **仔细检查文件模式**（不要在想追加内容时误用了 `w` 覆盖模式）。
3.  **Use relative paths for portability** so your code works on other computers. / **使用相对路径以提高代码的可移植性**，从而使代码可以在其他计算机上运行。
4.  **Test with small files first** before processing massive datasets. / **先用小文件进行测试**，然后再处理大型数据集。

---

<br>

## Section 2: The `with` Statement / 第二章：`with` 语句

### 2.1 What is `with`? / 什么是 `with`？

The `with` statement in Python provides a special syntax for resource management. It acts as a context manager, meaning it makes your code cleaner, safer, and automatically handles cleanup tasks (like closing files) behind the scenes.

Python 中的 `with` 语句提供了一种用于资源管理的特殊语法。它充当上下文管理器的角色，这意味着它可以让你的代码更简洁、更安全，并且能在后台自动处理清理任务（比如关闭文件）。

<br>

### 2.2 Why Use `with`? / 为什么要使用 `with`？

**The Problem without `with` / 不使用 `with` 的问题:**
```python
f = open('diary.txt', 'r')
content = f.read()
# If an error occurs here, the code crashes and f.close() is never reached!
# 如果这里发生错误，代码会崩溃，永远不会执行到 f.close()！
```
If a file remains open unexpectedly, several dangerous things can happen:
如果文件意外保持打开状态，可能会发生以下几种危险情况：
1. Data may not be fully written to the disk (the most dangerous scenario!). / 数据可能没有完全写入磁盘（最危险的情况！）。
2. File handle leakage (exhaustion of system file descriptors). / 文件句柄泄漏（耗尽系统的文件描述符）。
3. The file may be locked, making it inaccessible to other programs. / 文件可能被锁定，导致其他程序无法访问。
4. Relying on Python's automatic garbage collection to close it is unreliable. / 依赖 Python 的自动垃圾回收机制来关闭它是不靠谱的。

**The Solution with `with` / 使用 `with` 的解决方案:**
```python
with open('diary.txt', 'r') as f:
    content = f.read()
# The file automatically closes right here, even if errors occurred above!
# 即使上面发生了错误，文件也会在这里自动关闭！
```
This guarantees cleanup and creates highly secure code.
这保证了资源的清理，并创建了高度安全的代码。

<br>

### 2.3 Syntax and Handling Multiple Files / 语法与多文件处理

**Basic Syntax / 基本语法:**
```python
with open('secrets.txt', 'r') as secret_file:
    print(secret_file.read())
```

**Handling Multiple Files / 处理多个文件:**
You can manage two or more files simultaneously, which is perfect for copying data safely.
你可以同时管理两个或更多文件，这非常适合安全地复制数据。
```python
with open('original.txt', 'r') as src: 
    with open('backup.txt', 'w') as dst:
        dst.write(src.read())
```

<br>

### 2.4 Practical Cases for Context Managers / 上下文管理器实战案例

**Case 1: Read Config File / 案例 1：读取配置文件**
```python
with open('config.cfg', 'r') as config_file:
    settings = config_file.readlines()

print("Server timeout:", settings[0])
print("Max users:", settings[1])
```

**Case 2: Safe File Copy (Binary) / 案例 2：安全的文件复制（二进制）**
*Note the 'rb' and 'wb' modes for reading/writing binary files like images.*
*注意处理图片等二进制文件时需要使用 'rb' 和 'wb' 模式。*
```python
with open('cat.jpg', 'rb') as source_cat:
    with open('cat_backup.jpg', 'wb') as backup_cat:
        backup_cat.write(source_cat.read())
```

**Case 3: Program Logging / 案例 3：程序日志记录**
```python
with open('app.log', 'a') as log_file:
    log_file.write('Program started\n')
    # ... Your main code here / 你的主要代码 ...
    log_file.write('Operation completed\n')
```

<br>

### 2.5 `with` Superpowers / `with` 的核心优势

1. **Automatic cleanup**: No more forgetting `close()`. / **自动清理**：再也不用担心忘记写 `close()`。
2. **Error-safe operations**: Closes files even during crashes. / **防错操作**：即使程序崩溃也能安全关闭文件。
3. **Cleaner code**: Less boilerplate code to read. / **代码更整洁**：减少了冗余的样板代码。
4. **Multiple resource handling**: Easy to nest. / **多资源处理**：极易嵌套使用。

*Use `with` for file operations, database connections, and network resources!*
*在进行文件操作、数据库连接和网络资源调用时，请务必使用 `with`！*

---

<br>

## Section 3: File System Operations / 第三章：文件系统操作

Beyond reading and writing content, Python's `os` module allows you to interact with the underlying operating system to manage files and folders.
除了读写内容之外，Python 的 `os` 模块允许你与底层操作系统交互，以管理文件和文件夹。

### 3.1 Path Operations with `os.path` / 使用 `os.path` 进行路径操作

Checking paths helps avoid errors (like trying to open a file that doesn't exist).
检查路径有助于避免错误（比如试图打开一个不存在的文件）。

```python
import os

# Check if file/folder exists / 检查文件/文件夹是否存在
print(os.path.exists("diary.txt"))  # Output: True or False

# Check if it is specifically a file or a directory / 检查具体是文件还是目录
print(os.path.isfile("photos/"))    # Output: False
print(os.path.isdir("photos/"))     # Output: True
```

<br>

### 3.2 Get File Size / 获取文件大小

You can measure the size of a file in bytes. (Remember: 1024 bytes = 1 KB).
你可以以字节（bytes）为单位测量文件大小。（切记：1024 字节 = 1 KB）。

```python
size = os.path.getsize("secrets.txt")
print("File size: " + str(size) + " bytes") 
```

<br>

### 3.3 Create Directories / 创建目录

```python
os.mkdir("experiments")  # Creates a simple directory / 创建一个普通目录
# os.mkdir("projects/2024") # Error! The parent 'projects' must exist first / 错误！父目录 'projects' 必须先存在

# Pro tip: Use os.makedirs() to create nested folders automatically
# 进阶提示：使用 os.makedirs() 可以自动创建嵌套的文件夹
```

<br>

### 3.4 List and Rename Directory Contents / 列出目录内容与重命名

```python
# See what's inside a folder (returns names only, not full paths)
# 查看文件夹中的内容（仅返回名称，不返回完整路径）
files = os.listdir("photos/")
print(files)

# Change names safely / 安全地更改名称
os.rename("old.txt", "new.txt")      # Rename file / 重命名文件
os.rename("temp/", "backup/")        # Rename directory / 重命名目录
```

<br>

### 3.5 Real-world Scenarios / 综合实战案例

**Case 1: Auto-create Daily Folder / 案例 1：自动创建每日文件夹**
Perfect for organizing lab results or daily logs automatically based on the current date.
非常适合根据当前日期自动整理实验结果或每日日志。
```python
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
os.mkdir("lab_" + today)
print("Created: lab_" + today)
```

**Case 2: Batch Rename Photos / 案例 2：批量重命名照片**
Using Python's string `replace()` function, we can rename hundreds of files in seconds.
利用 Python 字符串的 `replace()` 函数，我们可以在几秒钟内重命名数百个文件。
```python
# Quick string replace review / 快速复习字符串替换:
# a = "aaabbb"
# b = a.replace('bbb', 'ccc')  -> Output: "aaaccc"

for file in os.listdir("photos/"):
    if file.startswith("photo"):
        new_name = file.replace("photo", "vacation")
        # Combine the folder path with the filenames / 将文件夹路径与文件名结合
        os.rename("photos/" + file, "photos/" + new_name)
```

**Case 3: Find All Text Files / 案例 3：查找所有文本文件**
```python
text_files = []

for item in os.listdir("text/"):
    # Check string slicing: item[len(item)-4:len(item)] == '.txt'
    # A better, Pythonic way is using item.endswith('.txt')
    # 检查字符串切片，或者更好的 Python 式写法是使用 item.endswith('.txt')
    if item.endswith('.txt'):   
        text_files.append(item)

print("Found text files:", text_files)
```

---

<br>

## Section 4: Encoding in Python / 第四章：Python 中的编码

### 4.1 Why Encoding Matters / 为什么编码很重要？

Computers fundamentally only understand 0s and 1s. An "encoding" is essentially a translation dictionary that converts human-readable text into numeric binary formats and vice-versa. 
计算机底层只认识 0 和 1。“编码”本质上是一本翻译字典，用于在人类可读的文本和数字二进制格式之间进行相互转换。

<br>

### 4.2 Common Encodings / 常见编码格式

1.  **ASCII**: The fundamental alphabet. It contains 128 characters (English letters, numbers, and basic symbols). 
    **ASCII**：基础字符集。包含 128 个字符（英文字母、数字和基本符号）。
    ```python
    print(ord('A'))  # Output: 65 (ASCII numerical code)
    print(chr(65))   # Output: 'A' (Character representation)
    ```
2.  **UTF-8**: The global standard. It supports all languages worldwide using a variable-length encoding (1 to 4 bytes per character) and is Python 3's default.
    **UTF-8**：全球通行标准。它支持全球所有语言，采用可变长度编码（每个字符 1-4 个字节），也是 Python 3 的默认编码。
    ```python
    汉字 = "中文"
    print(len(汉字.encode('utf-8')))  # Output: 6 (3 bytes per Chinese character)
    ```
3.  **GBK**: A legacy encoding standard for Simplified Chinese. It uses a fixed 2 bytes per Chinese character, commonly found in older Windows systems.
    **GBK**：简体中文的传统编码标准。每个中文字符固定占用 2 个字节，常见于较老的 Windows 系统中。
    ```python
    print(len("中文".encode('gbk')))  # Output: 4 (2 bytes per character)
    ```

<br>

### 4.3 Setting Parameters & Handling Errors / 设置参数与处理错误

To avoid `UnicodeDecodeError` (can't decode bytes) or `UnicodeEncodeError` (can't encode characters), always specify the encoding explicitly when opening text files.
为了避免解码错误或编码错误，在打开文本文件时一定要显式地指定编码格式。

```python
# The safe way to open files / 打开文件的安全方式
file = open('data.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# Handling problematic characters / 处理有问题的字符
# Ignore them entirely / 完全忽略它们
f1 = open('data.txt', 'r', encoding='utf-8', errors='ignore')

# Replace them with a question mark (?) / 用问号 (?) 替换它们
f2 = open('data.txt', 'r', encoding='utf-8', errors='replace')
```

<br>

### 4.4 Real-world Encoding Cases / 编码实战应用

**Case 1: GBK to UTF-8 Conversion / 案例 1：GBK 转 UTF-8**
Converting legacy Chinese text files into the modern standard.
将传统的中文文本文件转换为现代标准格式。
```python
# Step 1: Read GBK file / 第一步：读取 GBK 文件
with open('old_data.txt', 'r', encoding='gbk') as source:
    content = source.read()

# Step 2: Save as UTF-8 / 第二步：保存为 UTF-8
with open('new_data.txt', 'w', encoding='utf-8') as target:
    target.write(content)
```

**Case 2: Reading Chinese CSV / 案例 2：读取中文 CSV 文件**
Depending on where the CSV came from, you must match the encoding.
根据 CSV 文件的来源，你必须匹配相应的编码格式。
```python
# Assuming data.csv contains: 姓名,年龄 (Name, Age)
with open('data.csv', 'r', encoding='gbk') as file:
    for line in file:
        name, age = line.strip().split(',')
        print("Name: " + name + ", Age: " + age)
```

**Pro Tip**: If you don't know a file's encoding, use the `chardet` library!
**进阶技巧**：如果你不知道文件的编码格式，可以使用 `chardet` 库！
```python
import chardet
rawdata = open('mystery.txt', 'rb').read()
result = chardet.detect(rawdata)
print(result['encoding'])
```

---

<br>

## Section 5: Practical Applications / 第五章：综合实战应用

Let's combine everything we've learned into functional, real-world scripts.
让我们把学到的所有知识结合起来，编写功能完善的实战脚本。

### 5.1 Log Analyzer / 服务器日志分析器

**1. Count 404 Errors / 统计 404 错误数量**
```python
def count_404(log_file):
    counter = 0
    with open(log_file, 'r') as f:
        for line in f:
            if ' 404 ' in line:
                counter += 1
    return counter

print("Total 404 errors:", count_404('nginx.log'))
```

**2. Filter Logs by Time / 按时间段筛选日志**
```python
def filter_by_time(log_file, start_time, end_time):
    results = []
    with open(log_file, 'r') as f:
        for line in f:
            # Assuming log format: [01/Jan/2023:12:05:00]
            timestamp = line.split('[')[1].split(']')[0]
            if start_time <= timestamp and timestamp <= end_time:
                results.append(line)
    return results

matches = filter_by_time('nginx.log', '01/Jan/2023:12:00', '01/Jan/2023:12:30')
print(f"Found {len(matches)} entries in time range.")
```

<br>

### 5.2 Backup Tool / 系统备份工具

**1. Basic Directory Copy / 基础目录备份**
```python
import shutil
from datetime import datetime

def simple_backup(source_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_name = "backups/" + source_dir + "_backup_" + timestamp
    shutil.copytree(source_dir, backup_name)
    print("Backup created: " + backup_name)

simple_backup('important_files')
```

**2. Validate Backup Integrity / 验证备份完整性**
```python
def verify_backup(source, backup):
    with open(source, 'r') as f1, open(backup, 'r') as f2:
        if f1.read() == f2.read():
            print('Backup verification successful (yes).')
        else:
            print('Backup verification failed (no).')

verify_backup('nginx.log', 'nginx_bac.log')
```

<br>

### 5.3 Text and File Encryption (Caesar Cipher) / 文本与文件加密（凯撒密码）

**1. Core Encryption/Decryption Logic / 核心加解密逻辑**
```python
def caesar_encrypt(text, shift=3):
    encrypted = []
    for char in text:
        encrypted.append(chr(ord(char) + shift))
    return ''.join(encrypted)

def caesar_decrypt(ciphertext, shift=3):
    decrypted = []
    for char in ciphertext:
        decrypted.append(chr(ord(char) - shift))
    return ''.join(decrypted)

secret = caesar_encrypt("Hello Students!")
print("Encrypted:", secret)
print("Decrypted:", caesar_decrypt(secret))
```

**2. File Encryption Wrappers / 文件级加密封装**
```python
def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        original_text = f_in.read()
        encrypted = caesar_encrypt(original_text)
        f_out.write(encrypted)

def decrypt_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        encrypted_text = f_in.read()
        decrypted = caesar_decrypt(encrypted_text)
        f_out.write(decrypted)

# Usage / 使用方法
encrypt_file('nginx.log', 'nginx.log.enc')
decrypt_file('nginx.log.enc', 'nginx.log.enc.dec')
```

<br>
