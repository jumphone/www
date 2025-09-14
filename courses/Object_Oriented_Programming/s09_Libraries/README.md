


# Standard Library & Third-Party Libraries


## Question: Can you list some modules provided by the Python standard library?

"math", ...

</br></br></br>

## Section 1. Libraries, Package, Module ?

## What't the different among them three ? 

## Library: Focusing on the function. May include multiple pacakges and modules.

## Package: A folder with multiple Modules

## Module: A .py file

- **Pre-installed tools** with Python
- Examples: `math`
- Try this in Python:
  ```python
  import math
  print("Pi is approximately", math.pi)
  print("Square root of 16:", math.sqrt(16))
  ```


## Python's Built-in Help

- Discover all available standard libraries:
  ```python
  help('modules')
  ```

---

## Third-Party Libraries

- **Extra tools** you can download
- Massive collection at [PyPI.org](https://pypi.org/)
- Example popular libraries:
  - `pandas` (data wizardry)
  - `requests` (web communication)
  - `numpy` (number crunching)

---

## Three Ways to Use Libraries 

1. **Full Import** - Get the whole toolbox:
   ```python
   import math
   print("2^5 =", math.pow(2, 5))
   ```

---

## Import Method 2: Precision Pick 

2. **Specific Import** - Grab just what you need:
   ```python
   from random import randint
   print("Random dice roll:", randint(1, 6))
   ```

---

## Import Method 3: Nicknames

3. **Alias Import** - Make it short:
   ```python
   import pandas as pd
   data = {'Birds': ['Eagle', 'Penguin'], 'Speed': [320, 8]}
   df = pd.DataFrame(data)
   print(df)
   ```

---

## Why Different Import Methods? 

- **Full imports** prevent name conflicts
- **Specific imports** make code cleaner
- **Short Name** save typing long names

---

## Let's Mix Them Up! 

Combine different import styles:
```python
from math import sqrt as sq
print("Square root of 121:", sq(121))
```

---

## Your Coding Toolkit Now Has... 

- **Standard Library**: Always available 
- **Third-Party Libraries**: Expand your powers 
- **Import Skills**: Use any library effectively 

---

## Demo


```python
# Random password generator
from random import choice
chars = 'ABC123!@'
password = ''.join([choice(chars) for _ in range(8)])
print("Your new password:", password)
```

---

---

## Pro Tip: Explore Libraries! 

- Standard library documentation: [docs.python.org/3/library](https://docs.python.org/3/library)
- PyPI for new discoveries: [pypi.org](https://pypi.org/)
- Remember: Great programmers stand on the shoulders of giants 🏗


</br></br></br>

## Section 2. Standard Library

## math, time, random，os

## Other modules:

### datetime Module - Current Time
```python
import datetime

now = datetime.datetime.now()
print("Current time:", now)
```
Output shows:
- Year/Month/Day
- Hour:Minute:Second.Microsecond

---
### datetime Calculation with timedelta
```python
future_date = now + datetime.timedelta(days=3)
print("Date after 3 days:", future_date.date())
```
- `timedelta` supports: 
  - `days`
  - `hours`
  - `minutes`


######

</br></br></br>

## Quesion: How to add "datetime" functions into the "ai.py"?

</br></br></br>

---



## Section 3. Use pip to install third-party libraries.

## pip - Python's Package Manager
```bash
$ pip3 --version
pip 24.0 from ... (python 3.7)
```
- Built-in tool for package management
- Comes with Python 3.4+
- Main commands: install/uninstall/list

---

## Installing Your First Package
```bash
$ pip3 install requests
Collecting requests...
Successfully installed requests-2.31.0
```
- Installs from Python Package Index (PyPI)
- Installs to system/site-packages directory
- Verify with `pip list`

---

## Exploring Installed Packages
```bash
$ pip3 list
Package    Version
---------- -------
pip        21.2.4
requests   2.31.0
setuptools 57.4.0
```
- Shows all installed packages
- Includes version information
- Helps manage dependencies

---

## Speeding Up Downloads (use mirror)
```bash
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```
- Why mirrors matter
- Popular mirrors: Tsinghua, AliCloud
- Temporary vs permanent configuration

---

## Permanent Mirror Configuration
```bash
$ pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
- Create `pip.conf` file
- Location: ~/.config/pip/pip.conf
- Applies to all future installations

---

## Let's Use requests!
```python
import requests

response = requests.get("https://www.baidu.com")
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text[:100]}...")
```
- Popular HTTP library
- Simple API for web requests
- Handles JSON responses

---

## Real-World Example: Weather Check
```python
import requests

city = "Beijing"
url = f"http://wttr.in/{city}?format=3"
response = requests.get(url)
print(f"Weather in {city}: {response.text}")
```
Sample output:
```
Weather in Beijing:  +25°C
```

## Question: How can we add this function into ai.py?

## QuestionL How can we learn more about "requests"?

---

## Upgrading Packages
```bash
$ pip3 install --upgrade requests
$ pip3 install requests==2.31.0
```
- Get latest features
- Security updates
- Watch for breaking changes



---

</br></br></br>

---

## Section 4. A Formal Weather Reporter
**Goal:** Combine web data and time handling

---
## What We'll Use:
1. `requests` - Fetch data from websites
2. `datetime` - Handle dates/times

Try this first:
```python
import datetime
current_time = datetime.datetime.now()
print(f"Hello! It's {current_time:%H:%M} now!")
```

---

## Get Weather Data
Here's a simple weather API example:
```python
import requests

def get_weather(city):
    url = f"http://wttr.in/{city}?format=%t+%C"
    response = requests.get(url)
    return response.text

print(get_weather("London"))
```

---

## Combine Time & Weather
Let's make it friendly! ✨
```python
def weather_report(city):
    time_now = datetime.datetime.now().strftime("%H:%M")
    weather = get_weather(city)
    return f"[{time_now}] Weather in {city}: {weather}"

print(weather_report("NewYork"))
```

## Question: Is there something wrong? How can we fix it? Hint: we are using the Beijing Time.


---


</br></br></br>

## Section 5. File Backup Helper
**Goal:** Automate file copying

---

## File Tools:
1. `os` - Handle paths
2. `shutil` - File operations

Path check example:
```python
import os

my_folder = "documents"
if not os.path.exists(my_folder):
    os.makedirs(my_folder)
    print(f"Created {my_folder}!")
```

---

## Simple Backup Script
Copy all text files:
```python
import shutil

def backup_files(src_folder, dst_folder):
    for file in os.listdir(src_folder):
        if file.endswith(".txt"):
            shutil.copy2(os.path.join(src_folder, file), dst_folder)
            print(f"Copied {file}!")

backup_files("notes", "backup")
```
## Question: How can we add file operation functions into ai.py?







