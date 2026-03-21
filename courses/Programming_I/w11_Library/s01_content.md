[Back](https://www.bioinfo-lab.com/courses/Programming_I/w11_Library/)

<br>

<a id="all"></a>

### Content:

[Section 1. Understanding Libraries, Packages, and Modules](#s1.0)

[Section 2. Python Standard Library](#s2.0)

[Section 3. Third-Party Libraries and pip](#s3.0)

[Section 4. Practical Application - Weather Reporter](#s4.0)

[Section 5. Practical Application - File Backup Helper](#s5.0)

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Understanding Libraries, Packages, and Modules

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1.1. Core Concepts

### Library
- Focusing on the function
- May include multiple packages and modules
- Collection of reusable code

### Package
- A folder containing multiple modules
- Must include `__init__.py` file
- Organizes related modules together

### Module
- A single `.py` file
- Contains functions, classes, and variables
- Basic unit of code organization

---

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Python Standard Library

### Pre-installed Tools
- Comes with every Python installation
- No additional installation required
- Examples: `math`, `random`, `datetime`, `os`

### Basic Usage Example
```python
import math
print("Pi is approximately " + str(math.pi))
print("Square root of 16: " + str(math.sqrt(16)))
```

### Discovering Available Modules
```python
help('modules')
```

---

<div align="left">
  <a href="#s1.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 1.3. Three Import Methods

### Method 1: Full Import
Get the whole toolbox:
```python
import math
print("2^5 = " + str(math.pow(2, 5)))
```

### Method 2: Specific Import
Grab just what you need:
```python
from random import randint
print("Random dice roll: " + str(randint(1, 6)))
```

### Method 3: Alias Import
Make it short:
```python
import pandas as pd
data = {'Birds': ['Eagle', 'Penguin'], 'Speed': [320, 8]}
df = pd.DataFrame(data)
print(df)
```

---

<div align="left">
  <a href="#s1.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.4"></a>

---

## 1.4. Import Method Comparison

### Why Different Import Methods?

| Method | Advantage | Use Case |
|--------|-----------|----------|
| **Full Import** | Prevents name conflicts | Large libraries, avoid namespace pollution |
| **Specific Import** | Cleaner code, less typing | Only need 1-2 functions from module |
| **Alias Import** | Saves typing long names | Frequently used libraries like pandas/numpy |

### Mixed Import Styles
Combine different approaches:
```python
from math import sqrt as sq
print("Square root of 121: " + str(sq(121)))
```

---

<div align="left">
  <a href="#s1.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>

# Section 2. Python Standard Library

<div align="left">
  <a href="#s1.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. Core Standard Library Modules

### Essential Modules
- `math` - Mathematical functions
- `time` - Time-related functions
- `random` - Random number generation
- `os` - Operating system interface
- `datetime` - Date and time manipulation
- `shutil` - High-level file operations

---

<div align="left">
  <a href="#s2.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. datetime Module

### Current Time
```python
import datetime

now = datetime.datetime.now()
print("Current time: " + str(now))
```
Output format: Year/Month/Day Hour:Minute:Second.Microsecond

### Time Calculation with timedelta
```python
future_date = now + datetime.timedelta(days=3)
print("Date after 3 days: " + str(future_date.date()))
```

### timedelta Parameters
- `days`
- `hours`
- `minutes`
- `seconds`
- `weeks`

---

<div align="left">
  <a href="#s2.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>

# Section 3. Third-Party Libraries and pip

<div align="left">
  <a href="#s2.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. Introduction to Third-Party Libraries

### What are Third-Party Libraries?
- Extra tools you can download
- Massive collection at PyPI.org
- Extend Python's capabilities

### Popular Examples
- `pandas` - Data manipulation and analysis
- `requests` - HTTP library for web communication
- `numpy` - Numerical computing

---

<div align="left">
  <a href="#s3.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. pip Package Manager

### Checking pip Version
```bash
$ pip3 --version
pip 24.0 from ... (python 3.7)
```

### Key Features
- Built-in tool for package management
- Comes with Python 3.4+
- Main commands: install, uninstall, list

### Installing Packages
```bash
$ pip3 install requests
Collecting requests...
Successfully installed requests-2.31.0
```

### Listing Installed Packages
```bash
$ pip3 list
Package    Version
---------- -------
pip        21.2.4
requests   2.31.0
setuptools 57.4.0
```

---

<div align="left">
  <a href="#s3.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 3.3. Package Installation Optimization

### Using Mirrors for Speed
```bash
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

### Popular Mirrors
- Tsinghua University
- AliCloud
- University of Science and Technology of China

### Permanent Mirror Configuration
```bash
$ pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
Creates `~/.config/pip/pip.conf` file

---

<div align="left">
  <a href="#s3.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 3.4. Using requests Library

### Basic GET Request
```python
import requests

response = requests.get("https://www.baidu.com")
print("Status Code: " + str(response.status_code))
print("Response Text: " + response.text[:100] + "...")
```

### Real-World Weather Example
```python
import requests

city = "Beijing"
url = "http://wttr.in/" + city + "?format=3"
response = requests.get(url)
print("Weather in " + city + ": " + response.text)
```

### Upgrading Packages
```bash
$ pip3 install --upgrade requests
$ pip3 install requests==2.31.0
```

---

<div align="left">
  <a href="#s3.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>

# Section 4. Practical Application - Weather Reporter

<div align="left">
  <a href="#s3.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. Project Overview

### Goal
Combine web data fetching and time handling to create a weather reporting tool.

### Required Libraries
1. `requests` - Fetch weather data from websites
2. `datetime` - Handle current time display

---

<div align="left">
  <a href="#s4.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Time Display Function

### Current Time Formatting
```python
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M")
print("Hello! It's " + formatted_time + " now!")
```

### Time Zone Consideration
When using datetime, be aware of your system's time zone settings. The example uses local system time.

---

<div align="left">
  <a href="#s4.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.3"></a>

---

## 4.3. Weather Data Function

### Fetching Weather Data
```python
import requests

def get_weather(city):
    url = "http://wttr.in/" + city + "?format=%t+%C"
    response = requests.get(url)
    return response.text

print(get_weather("London"))
```

### API Format Options
- `%t` - Temperature
- `%C` - Weather condition
- `%h` - Humidity
- `%w` - Wind speed

---

<div align="left">
  <a href="#s4.2">← Prev </a> | <a href="#all"> Home </a> | <a href="#s4.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.4"></a>

---

## 4.4. Complete Weather Reporter

### Combined Function
```python
import datetime
import requests

def get_weather(city):
    url = "http://wttr.in/" + city + "?format=%t+%C"
    response = requests.get(url)
    return response.text

def weather_report(city):
    time_now = datetime.datetime.now().strftime("%H:%M")
    weather = get_weather(city)
    return "[" + time_now + "] Weather in " + city + ": " + weather

print(weather_report("NewYork"))
```

### Potential Issues
If you are in Beijing but checking New York weather, the time displayed will be Beijing Time, not local New York time.

---

<div align="left">
  <a href="#s4.3">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>

# Section 5. Practical Application - File Backup Helper

<div align="left">
  <a href="#s4.4">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Project Overview

### Goal
Automate file copying operations for backup purposes.

### Required Libraries
1. `os` - Handle file paths and directory operations
2. `shutil` - High-level file operations (copy, move, etc.)

---

<div align="left">
  <a href="#s5.0">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Directory Management

### Checking and Creating Directories
```python
import os

my_folder = "documents"
if not os.path.exists(my_folder):
    os.makedirs(my_folder)
    print("Created " + my_folder + "!")
```

### Path Operations
```python
# Join path components
full_path = os.path.join("backup", "file.txt")
print(full_path)
```

---

<div align="left">
  <a href="#s5.1">← Prev </a> | <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 5.3. File Backup Script

### Copying Specific File Types
```python
import os
import shutil

def backup_files(src_folder, dst_folder):
    # Create destination if it doesn't exist
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    
    # Copy all .txt files
    for file in os.listdir(src_folder):
        if file.endswith(".txt"):
            src_path = os.path.join(src_folder, file)
            dst_path = os.path.join(dst_folder, file)
            shutil.copy2(src_path, dst_path)
            print("Copied " + file + "!")

# Usage example
backup_files("notes", "backup")
```

### shutil.copy2() vs shutil.copy()
- `copy2()` - Preserves metadata (timestamps, permissions)
- `copy()` - Only copies file content

---

<div align="left">
  <a href="#s5.2">← Prev </a> | <a href="#all"> Home </a> 
</div>

<br>

### Pro Tip: Explore Libraries!
- Standard library documentation: [docs.python.org/3/library](https://docs.python.org/3/library)
- PyPI for new discoveries: [pypi.org](https://pypi.org/)
- Remember: Great programmers stand on the shoulders of giants 🏗

<br>

End
