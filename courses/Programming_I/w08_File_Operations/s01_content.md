[Back](https://www.bioinfo-lab.com/courses/Programming_I/w08_File_Operations/)

<br>


<a id="all"></a>

### Content:

[Section 1. File Operations Basics](#s1.0)

[Section 2. `with` Statement](#s2.0)

[Section 3. File System Operations](#s3.0)

[Section 4. Encoding in Python](#s4.0)

[Section 5. Practical Applications](#s5.0)

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. File Operations Basics

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1. What is a File?
- Data container stored on disk
- Like a water bottle stores liquid
- Two main types:
  - Text files: Human-readable (`.txt`, `.csv`)
  - Binary files: Special formats (`.jpg`, `.docx`)

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 2. File Paths Explained
```python
# Absolute path (full address)
"/home/student/documents/diary.txt"

# Relative path (from current location)
"../pictures/vacation.jpg"
```
- Think of paths like home addresses for files

<div align="left">
  <a href="#s1.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 3. Opening Files: The open() Function
```python
# Modes
f = open("list.txt", "r")   # Read
f = open("new.txt", "w")    # Write (overwrite)
f = open("log.txt", "a")    # Append
```

<div align="left">
  <a href="#s1.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.4"></a>

---

## 4. Reading Files - The read() Family
```python
file = open("classlist.txt", "r")
print(file.read())       # Read entire file
file.seek(0)            # Reset to beginning

print(file.readline())   # Read first line
file.seek(0)   

print(file.readlines())  # Read all lines as list
file.close()
```

<div align="left">
  <a href="#s1.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.5"></a>

---

## 5. Writing Files - write() vs writelines()
```python
# Write individual strings
file = open("groceries.txt", "w")
file.write("Milk\n")
file.write("Eggs\nBread\n")
file.close()

# Write multiple lines from list
items = ["Apples\n", "Coffee\n"]
file = open("shopping.txt", "w")
file.writelines(items)
file.close()
```

<div align="left">
  <a href="#s1.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.6"></a>

---

## 6. Case 1: Read Class List
```python
# File: classlist.txt
# Alice
# Bob
# Charlie

file = open("classlist.txt", "r")
students = file.readlines()
file.close()

for student in students:
    print("Hello " + student.strip() + "!")
```
Output:
```
Hello Alice!
Hello Bob!
Hello Charlie!
```

<div align="left">
  <a href="#s1.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.7"></a>

---

## 7. Case 2: Create Shopping List
```python
file = open("groceries.txt", "w")
file.write("Shopping List:\n")
file.write("- Milk\n- Eggs\n- Bread")
file.close()
```
File contents:
```
Shopping List:
- Milk
- Eggs
- Bread
```

<div align="left">
  <a href="#s1.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.8"></a>

---

## 8. Case 3: Append to Diary
```python
# Existing content:
# 2024-03-01: Learned Python basics

file = open("diary.txt", "a")
file.write("\n2024-06-01: Learned file operations!")
file.close()
```
Updated file:
```
2024-03-01: Learned Python basics
2024-06-01: Learned file operations!
```

<div align="left">
  <a href="#s1.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.9"></a>

---

## 9. Important Reminders
1. Always close files!
2. Double-check file modes
3. Use relative paths for portability
4. Test with small files first

<div align="left">
  <a href="#s1.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>
# Section 2. `with` Statement

<div align="left">
  <a href="#s1.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## What is `with`?
- Special syntax for resource management
- Makes code cleaner and safer
- Automatically handles cleanup

<div align="left">
  <a href="#s2.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## Why Use `with`? (1/2)
**Problem without `with`:**
```python
f = open('diary.txt', 'r')
content = f.read()
# What if we forget to close?
# f.close()
```
File remains open if exception occurs!

1. Data may not be fully written to the file (most dangerous!)
2. File handle leakage (exhaustion of file descriptors)
3. The file may be locked and inaccessible to other programs/processes
4. Automatic closing by garbage collection is unreliable

<div align="left">
  <a href="#s2.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.3"></a>

---

## Why Use `with`? (2/2)
**Solution with `with`:**
```python
with open('diary.txt', 'r') as f:
    content = f.read()
# File automatically closes here!
```
Guaranteed cleanup  
Safer code

<div align="left">
  <a href="#s2.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.4"></a>

---

## `with` Basic Syntax
```python
with expression as variable:
    # Your code block
```
Real example:
```python
with open('secrets.txt', 'r') as secret_file:
    print(secret_file.read())
```

<div align="left">
  <a href="#s2.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.5"></a>

---

## Handling Multiple Files
Copy file contents safely:
```python
with open('original.txt', 'r') as src: 
    with open('backup.txt', 'w') as dst:
        dst.write(src.read())
```
Two files managed at once!

<div align="left">
  <a href="#s2.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.6"></a>

---

## Case 1: Read Config File
Read server configuration:
```python
with open('config.cfg', 'r') as config_file:
    settings = config_file.readlines()

print("Server timeout:", settings[0])
print("Max users:", settings[1])
```

<div align="left">
  <a href="#s2.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.7"></a>

---

## Case 2: Safe File Copy
Copy cat pictures safely:
```python
with open('cat.jpg', 'rb') as source_cat:
    with open('cat_backup.jpg', 'wb') as backup_cat:
        backup_cat.write(source_cat.read())
```

<div align="left">
  <a href="#s2.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.8"></a>

---

## Case 3: Program Logging
Record program activity:
```python
with open('app.log', 'a') as log_file:
    log_file.write('Program started\n')
    # Your code here
    log_file.write('Operation completed\n')
```
📝 Logs always get saved!

<div align="left">
  <a href="#s2.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.9"></a>

---

## `with` Superpowers
1. Automatic cleanup
2. Error-safe operations
3. Cleaner code
4. Multiple resource handling

<div align="left">
  <a href="#s2.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.10"></a>

---

## When to Use `with`?
- File operations
- Database connections
- Network resources
- Any operation needing cleanup

<div align="left">
  <a href="#s2.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.11"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.11"></a>

---

## Final Demo: Recipe Reader
```python
with open('recipe.txt', 'r') as recipe:
    print("Today's Recipe:")
    for line in recipe:
        print(line.strip())

```
File closed automatically!

<div align="left">
  <a href="#s2.10">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>
# Section 3. File System Operations

<div align="left">
  <a href="#s2.11">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 01. Path Operations with `os.path`
- **Why check paths?**
  - Avoid errors when working with files
- **Basic methods**:
  ```python
  import os
  
  # Check if file exists
  print(os.path.exists("diary.txt"))  # Output: True/False
  
  # Check file type
  print(os.path.isfile("photos/"))    # Output: False
  print(os.path.isdir("photos/"))     # Output: True
  ```

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 02. Get File Size
- **Measure file content**:
  ```python
  size = os.path.getsize("secrets.txt")
  print("File size: " + str(size) + " bytes") 
  # Output: File size: 8 bytes
  ```
- **Note**: 1024 bytes = 1KB

<div align="left">
  <a href="#s3.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 03. Create Directories
- **Make new folders**:
  ```python
  os.mkdir("experiments")  # Simple directory
  os.mkdir("projects/2024") # Error! Parent must exist
  ```
- **Pro tip**: Use `os.makedirs()` for nested folders

<div align="left">
  <a href="#s3.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 04. List Directory Contents
- **See what's inside**:
  ```python
  files = os.listdir("photos/")
  print(files)
  # Output: []
  ```
- **Remember**: Returns names only, not full paths

<div align="left">
  <a href="#s3.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.5"></a>

---

## 05. Rename Files
- **Change names safely**:
  ```python
  # Rename single file
  os.rename("old.txt", "new.txt")
  
  # Rename directory
  os.rename("temp/", "backup/")
  ```

<div align="left">
  <a href="#s3.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.6"></a>

---

## Case 1: Auto-create Daily Folder
- **Problem**: Need date-based organization
- **Solution**:
  ```python
  from datetime import datetime
  
  today = datetime.now().strftime("%Y%m%d")
  os.mkdir("lab_" + today)
  print("Created: lab_" + today)
  
  ```

<div align="left">
  <a href="#s3.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.7"></a>

---

## Case 2: Batch Rename Photos

**"replace" function of String**

```python
  a="aaabbb"
  b=a.replace('bbb','ccc')
  print(b)
```

- **Before**: `photo_001.jpg`, `photo_002.jpg`
- **After**: `vacation_001.jpg`, `vacation_002.jpg`
  ```python
  for file in os.listdir("photos/"):
      if file.startswith("photo"):
          new_name = file.replace("photo", "vacation")
          os.rename("photos/" + file, "photos/" + new_name)
  ```

<div align="left">
  <a href="#s3.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.8"></a>

---

## Case 3: Find All Text Files
- **Goal**: Locate .txt files in directory
  ```python
  text_files = []
  
  for item in os.listdir("text/"):
      if item[len(item)-4:len(item)] =='.txt':   # or use item.endswith('.txt')
          text_files.append(item)
  
  print("Found text files:", text_files)
  # Output: Found text files: ['notes.txt', 'todo.txt']
  ```

<div align="left">
  <a href="#s3.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>
# Section 4. Encoding in Python

<div align="left">
  <a href="#s3.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## Why Encoding Matters?
- Computers only understand 0s and 1s
- Encoding = Dictionary for text ↔ numbers conversion
- Common encodings: ASCII, UTF-8, GBK

<div align="left">
  <a href="#s4.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## ASCII: The Basic Alphabet
- 128 characters (English letters, numbers, basic symbols)
- Example:
```python
# ASCII character codes
print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'
```

<div align="left">
  <a href="#s4.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.3"></a>

---

## UTF-8: The Global Standard
- Supports all languages 
- Variable-length encoding (1-4 bytes)
- Python 3's default encoding
```python
# Chinese character in UTF-8
汉字 = "中文"
print(len(汉字.encode('utf-8')))  # Output: 6 (3 bytes per character)
```

<div align="left">
  <a href="#s4.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.4"></a>

---

## GBK: Chinese Legacy Encoding
- Simplified Chinese standard
- Fixed 2 bytes per Chinese character
- Common in older systems
```python
# Same text in GBK
print(len("中文".encode('gbk')))  # Output: 4 (2 bytes per character)
```

<div align="left">
  <a href="#s4.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.5"></a>

---

## Setting Encoding Parameters
Always specify encoding when opening files:
```python
# Safe way to open files
file = open('data.txt', 'r', encoding='utf-8')
content = file.read()
file.close()
```

Common error types:
- `UnicodeDecodeError`: Can't decode bytes
- `UnicodeEncodeError`: Can't encode characters

<div align="left">
  <a href="#s4.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.6"></a>

---

## Handling Encoding Errors
Use `errors` parameter:
```python
# Ignore problematic characters
file = open('data.txt', 'r', encoding='utf-8', errors='ignore')

# Replace errors with ?
file = open('data.txt', 'r', encoding='utf-8', errors='replace')
```

<div align="left">
  <a href="#s4.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.7"></a>

---

## Case 1: GBK → UTF-8 Conversion
Convert legacy Chinese files:
```python
# Step 1: Read GBK file
source = open('old_data.txt', 'r', encoding='gbk')
content = source.read()
source.close()

# Step 2: Save as UTF-8
target = open('new_data.txt', 'w', encoding='utf-8')
target.write(content)
target.close()
```

<div align="left">
  <a href="#s4.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.8"></a>

---

## Case 2: Reading Chinese CSV
Handle common data formats:
```python
# data.csv contents:
# 姓名,年龄
# 张三,25
# 李四,30

file = open('data.csv', 'r', encoding='gbk')
for line in file:
    name, age = line.strip().split(',')
    print("Name: " + name + ", Age: " + age)
file.close()

file = open('data.csv', 'r', encoding='utf-8')
for line in file:
    name, age = line.strip().split(',')
    print("Name: " + name + ", Age: " + age)
file.close()
```

<div align="left">
  <a href="#s4.7">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.9"></a>

---

## Pro Tips
1. Always check file encoding before processing
2. Use UTF-8 for new projects
3. Test with `chardet` library if unsure
```python
# Detect encoding (install chardet first)
import chardet
rawdata = open('mystery.txt', 'rb').read()
result = chardet.detect(rawdata)
print(result['encoding'])
```

<div align="left">
  <a href="#s4.8">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>
# Section 5. Practical Applications

<div align="left">
  <a href="#s4.9">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 1. Log Analyzer: Count 404 Errors
```python
def count_404(log_file):
    counter = 0
    f = open(log_file, 'r')
    for line in f:
        if ' 404 ' in line:
            counter += 1
    f.close()
    return counter

# Usage example
print("Total 404 errors:", count_404('nginx.log'))
```

<div align="left">
  <a href="#s5.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 2. Log Analyzer: Time Filter
```python
def filter_by_time(log_file, start_time, end_time):
    results = []
    f = open(log_file, 'r')
    for line in f:
        timestamp = line.split('[')[1].split(']')[0]
        if start_time <= timestamp and timestamp <= end_time:
            results.append(line)
    f.close()
    return results

# Example usage
matches = filter_by_time('nginx.log', '01/Jan/2023:12:00', '01/Jan/2023:12:30')
print("Found " + str(len(matches)) + " entries in time range")
```

<div align="left">
  <a href="#s5.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 3. Backup Tool: Basic File Copy
```python
import shutil
from datetime import datetime

def simple_backup(source_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_name = "backups/" + source_dir + "_backup_" + timestamp
    shutil.copytree(source_dir, backup_name)
    print("Backup created: " + backup_name)

# Usage
simple_backup('important_files')
```

<div align="left">
  <a href="#s5.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.4"></a>

---

## 4. Backup Tool: Validate Backup
```python
import os

def verify_backup(source, backup):
    f1=open(source,'r')
    f2=open(backup,'r')
    f1_content=f1.read()
    f2_content=f2.read()
    f1.close()
    f2.close()
    if f1_content==f2_content:
       print('yes')
    else:
       print('no')

# Example usage
verify_backup('nginx.log','nginx_bac.log')
```

<div align="left">
  <a href="#s5.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.5"></a>

---

## 5. Text Encryption: Caesar Cipher
```python
def caesar_encrypt(text, shift=3):
    encrypted = []
    for char in text:
        encrypted.append(chr(ord(char) + shift))
    return ''.join(encrypted)

# Example
secret = caesar_encrypt("Hello Students!")
print("Encrypted:", secret)
```

<div align="left">
  <a href="#s5.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.6"></a>

---

## 6. Text Decryption: Caesar Cipher
```python
def caesar_decrypt(ciphertext, shift=3):
    decrypted = []
    for char in ciphertext:
        decrypted.append(chr(ord(char) - shift))
    return ''.join(decrypted)

# Test decryption
print("Decrypted:", caesar_decrypt(secret))
```

<div align="left">
  <a href="#s5.5">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.7"></a>

---

## 7. File Encryption Wrapper
```python
def encrypt_file(input_file, output_file):
    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')
    
    original_text = f_in.read()
    encrypted = caesar_encrypt(original_text)
    f_out.write(encrypted)
    
    f_in.close()
    f_out.close()

# Usage
encrypt_file('nginx.log', 'nginx.log.enc')
```

<div align="left">
  <a href="#s5.6">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.8"></a>

---

## 8. File Decryption Wrapper
```python
def decrypt_file(input_file, output_file):
    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')
    
    encrypted_text = f_in.read()
    decrypted = caesar_decrypt(encrypted_text)
    f_out.write(decrypted)
    
    f_in.close()
    f_out.close()

# Usage
decrypt_file('nginx.log.enc', 'nginx.log.enc.dec')
```

<div align="left">
  <a href="#s5.7">← Prev </a> | <a href="#all"> Home </a> 
</div>

<br>

End
