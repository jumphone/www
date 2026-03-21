[Back](https://www.bioinfo-lab.com/courses/Programming_I/w11_Library/)

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b> on Moodle by 23:59 this Sunday. 

This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

### Tips

- `tab` type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.
- `history` You can see all the commands you have run before.
- Try `help('modules')` to see all available standard library modules.
- Use `pip list` to check installed packages.

<br>

---

### 1. Log into the remote Linux Server

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---

### 2. Understand Libraries, Packages, and Modules

```
# Create a new script file
cd ~
nano library_concepts.py

# Type the following code:
# Library: A collection focusing on functionality
# Package: A folder containing multiple modules
# Module: A single .py file

# Check Python's standard library path
import sys
print("Standard library location:")
print(sys.path)

# Show how modules are files
import math
print("\nMath module location:")
print(math.__file__)

# Show how packages are directories
import os
print("\nOS package location:")
print(os.__file__)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 library_concepts.py
```

<br>

---

### 3. Explore Python's Built-in Help System

```
# Enter Python interactive mode
python3

# In interactive mode, type:
# Discover all available standard library modules
help('modules')

# Get help on a specific module
import math
help(math)

# Check math module contents
dir(math)

# Exit interactive mode
exit()
```

<br>

---

### 4. Three Ways to Import Modules

```
# Create a new script file
cd ~
nano import_methods.py

# Type the following code:
# Method 1: Full Import - Get the whole toolbox
import math
print("Full import: 2^5 =", math.pow(2, 5))

# Method 2: Specific Import - Grab just what you need
from random import randint
print("Specific import: Random dice roll:", randint(1, 6))

# Method 3: Alias Import - Make it short
import pandas as pd
data = {'Birds': ['Eagle', 'Penguin'], 'Speed': [320, 8]}
df = pd.DataFrame(data)
print("Alias import:\n", df)

# Mix them up!
from math import sqrt as sq
print("Mixed style: Square root of 121:", sq(121))

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 import_methods.py
```

<br>

---

### 5. Practice with Standard Library Modules

```
# Create a new script file
cd ~
nano stdlib_practice.py

# Type the following code:
# Math module
import math
print("Pi is approximately", math.pi)
print("Square root of 16:", math.sqrt(16))

# Datetime module
import datetime
now = datetime.datetime.now()
print("\nCurrent time:", now)
print("Formatted time:", now.strftime("%H:%M:%S"))

# Timedelta calculation
future_date = now + datetime.timedelta(days=3)
print("Date after 3 days:", future_date.date())

# Random module
from random import choice, shuffle
chars = 'ABC123!@'
password = ''.join([choice(chars) for _ in range(8)])
print("\nRandom password:", password)

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print("Shuffled numbers:", numbers)

# OS module
import os
my_folder = "test_documents"
if not os.path.exists(my_folder):
    os.makedirs(my_folder)
    print(f"\nCreated folder: {my_folder}")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 stdlib_practice.py
```

<br>

---

### 6. Install Third-Party Libraries with pip

```
# Open terminal (not Python interactive mode)
# Check pip version
pip3 --version

# Install requests library
pip3 install requests

# List installed packages
pip3 list

# Speed up download using mirror (temporary)
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# Configure permanent mirror
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Verify configuration
pip3 config list

# Upgrade a package
pip3 install --upgrade requests

# Install specific version
pip3 install requests==2.31.0
```

<br>

---

### 7. Use the requests Library

```
# Create a new script file
cd ~
nano requests_demo.py

# Type the following code:
import requests

# Simple GET request
response = requests.get("https://www.baidu.com")
print(f"Status Code: {response.status_code}")
print(f"Response Text (first 100 chars): {response.text[:100]}...")

# Real-world weather check
city = "Beijing"
url = f"http://wttr.in/{city}?format=3"
response = requests.get(url)
print(f"\nWeather in {city}: {response.text}")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 requests_demo.py
```

<br>

---

### 8. Build a Formal Weather Reporter

```
# Create a new script file
cd ~
nano weather_reporter.py

# Type the following code:
import requests
import datetime

def get_weather(city):
    """Fetch weather data from wttr.in"""
    url = f"http://wttr.in/{city}?format=%t+%C"
    response = requests.get(url)
    return response.text.strip()

def weather_report(city):
    """Generate time-stamped weather report"""
    # Note: This uses local server time (UTC)
    time_now = datetime.datetime.now().strftime("%H:%M")
    weather = get_weather(city)
    return f"[{time_now}] Weather in {city}: {weather}"

# Test the function
print(weather_report("London"))
print(weather_report("NewYork"))

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 weather_reporter.py

# Question: Is there something wrong? How can we fix it? Hint: we are using the Beijing Time.
# Answer: The time shown is server time (UTC), not Beijing time (UTC+8).
# To fix, you would need timezone handling with pytz library.
```

<br>

---

### 9. Create a File Backup Helper

```
# Create a new script file
cd ~
nano backup_helper.py

# Type the following code:
import os
import shutil

def backup_files(src_folder, dst_folder):
    """Copy all .txt files from source to destination"""
    # Create destination folder if it doesn't exist
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print(f"Created backup folder: {dst_folder}")
    
    # Check if source folder exists
    if not os.path.exists(src_folder):
        print(f"Error: Source folder '{src_folder}' not found!")
        return
    
    # Copy all .txt files
    for file in os.listdir(src_folder):
        if file.endswith(".txt"):
            src_path = os.path.join(src_folder, file)
            dst_path = os.path.join(dst_folder, file)
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {file}")

# Test the backup function
# First create some test files
os.makedirs("notes", exist_ok=True)
with open("notes/test1.txt", "w") as f:
    f.write("Important notes")
with open("notes/test2.txt", "w") as f:
    f.write("More notes")

# Run backup
backup_files("notes", "backup")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 backup_helper.py
```

<br>

---

### 10. Explore Library Documentation

```
# Create a new script file
cd ~
nano explore_docs.py

# Type the following code:
# Standard library documentation
import webbrowser

# Open Python standard library docs
webbrowser.open("https://docs.python.org/3/library")

# Open PyPI for third-party libraries
webbrowser.open("https://pypi.org")

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 explore_docs.py

# Pro Tip: Great programmers stand on the shoulders of giants
# Always explore documentation before reinventing the wheel
```

<br>

---

End
