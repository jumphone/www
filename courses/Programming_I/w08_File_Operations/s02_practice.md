[Back](https://www.bioinfo-lab.com/courses/Programming_I/w08_File_Operations/)

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
