[Back](https://www.bioinfo-lab.com/courses/Programming_I/w10_Exception_Handling/)

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
- In Python interactive mode, use `help()` or `?` to view documentation for errors and exceptions.
- Try `ai`, `aiw`, and `aid` for AI assistance.

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

### 2. Create Practice Directory and Files

```
cd ~
mkdir -p w02_error_handling
cd w02_error_handling
```

<br>

---

### 3. Common Python Errors Practice

Create a script to demonstrate the five most common errors:

```
nano common_errors.py
```

Type the following code:

```python
# 1. SyntaxError
# while True

# 2. NameError
# print(new_variable)

# 3. TypeError
# 1+'a'

# 4. FileNotFoundError
# fi=open('okokokokok.txt','r')

# 5. IndentationError
# while True:
# print('yes')

# Uncomment each line one by one to see the errors
print("Step 1: Uncomment the SyntaxError line")
```

Save: Ctrl + O
Exit: Ctrl + X

Run the script:

```
python3 common_errors.py
```

<br>

---

### 4. Understanding Error Messages

Create a script to generate a NameError and analyze the traceback:

```
nano traceback_demo.py
```

Type the following code:

```python
print(undefined_var)
```

Save and exit, then run:

```
python3 traceback_demo.py
```

You will see:

```
Traceback (most recent call last):
  File "traceback_demo.py", line 1, in <module>
    print(undefined_var)
NameError: name 'undefined_var' is not defined
```

**Error breakdown:**
- **Traceback**: Error roadmap showing the call stack
- **File "traceback_demo.py"**: Location of the error
- **line 1**: Exact line number
- **NameError**: Error type
- **name 'undefined_var' is not defined**: Specific error message

<br>

---

### 5. Basic Exception Handling

Create a script with try-except structure:

```
nano basic_try_except.py
```

Type the following code:

```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero!")
```

Save and run:

```
python3 basic_try_except.py
```

Expected output: `Oops! Can't divide by zero!`

<br>

---

### 6. BMI Calculator with Error Handling

Create a practical BMI calculator:

```
nano bmi_calculator.py
```

Type the following code:

```python
try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / height
except ZeroDivisionError:
    print("Alert! Did you enter height as zero?")
except ValueError:
    print("Please enter valid numbers!")
```

Save and run:

```
python3 bmi_calculator.py
```

Test with height = 0 to trigger ZeroDivisionError.

<br>

---

### 7. File Handling with Exception Handling

Create a file detective script:

```
nano file_detective.py
```

Type the following code:

```python
try:
    with open("ghost_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Pssst... this file doesn't exist!")
```

Save and run:

```
python3 file_detective.py
```

Expected output: `Pssst... this file doesn't exist!`

<br>

---

### 8. Catch-All Exception Handler

Create a script to catch any unexpected error:

```
nano catch_all.py
```

Type the following code:

```python
try:
    magic_number = "100" + 5
except Exception as e:
    print("Error details:", e)
```

Save and run:

```
python3 catch_all.py
```

Expected output shows the TypeError details.

<br>

---

### 9. User-Friendly Error Messages

Create an age input validator:

```
nano friendly_errors.py
```

Type the following code:

```python
try:
    user_age = int(input("Enter age: "))
except ValueError:
    print("Hey! Numbers only please :)")
```

Save and run:

```
python3 friendly_errors.py
```

Test with non-numeric input.

<br>

---

### 10. Handling Multiple Exception Types

Create a script with multiple except blocks:

```
nano multiple_exceptions.py
```

Type the following code:

```python
try:
    age = int(input("Age: "))
    print(str(100/age))
except ValueError:
    print("Numbers only!")  
except ZeroDivisionError:
    print("Age can't be zero!") 
```

Save and run:

```
python3 multiple_exceptions.py
```

Test with:
- Input `0` → ZeroDivisionError
- Input `string` → ValueError
- Input `4` → Successful division

<br>

---

### 11. Tuple-Style Exception Catching

Create a script catching multiple exceptions together:

```
nano tuple_catch.py
```

Type the following code:

```python
try:
    with open("grades.txt") as f:
        print(f.read())
except (FileNotFoundError, PermissionError):
    print("File problem! Check if:")
    print("- File exists")
    print("- You have access")
```

Save and run:

```
python3 tuple_catch.py
```

<br>

---

### 12. Grade Calculator Exercise

Create a grade calculator:

```
nano grade_calculator.py
```

Type the following code:

```python
try:
    total = float(input("Total points: "))
    earned = float(input("Earned points: "))
    percentage = (earned/total)*100
    print(f"Percentage: {percentage}%")
except ValueError:
    print("Numbers only!")
except ZeroDivisionError:
    print("Total can't be zero!")
```

**Question:** Modify this to use tuple-style catching.

<br>

---

### 13. Pet Age Calculator

Create a pet age calculator:

```
nano pet_age.py
```

Type the following code:

```python
try:
    human_years = int(input("Dog's age: "))
    dog_years = human_years * 7
    print(f"Dog age: {dog_years}")
except ValueError:
    print("Enter whole number!")
except Exception:
    print("Something unexpected happened!")
```

**Question:** Change it into tuple-style. Do we really need to do that?

<br>

---

### 14. The `finally` Clause

Create a script demonstrating `finally`:

```
nano finally_demo.py
```

Type the following code:

```python
try:
    file = open("diary.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Diary not found!")
finally:
    print("This always runs - cleanup completed")
```

Save and run:

```
python3 finally_demo.py
```

The `finally` block executes regardless of whether an exception occurs.

<br>

---

### 15. The `else` Clause

Create a script demonstrating `else`:

```
nano else_demo.py
```

Type the following code:

```python
try:
    num = float(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result is {result}")  # Only runs if no exception
```

Save and run:

```
python3 else_demo.py
```

The `else` block runs only when the `try` block succeeds.

<br>

---

### 16. Complete Exception Handling Pattern

Create a safe config loader:

```
nano safe_config.py
```

Type the following code:

```python
config_file = False
try:
    config_file = open("game_config.cfg")
except FileNotFoundError:
    print("⚠ Config file missing!")
else:
    settings = config_file.read()
    print("Game configuration loaded!")
finally:
    if config_file:
        config_file.close()
    print("Resource cleanup completed")
```

Save and run:

```
python3 safe_config.py
```

<br>

---

### 17. Safe Divide Function

Create a function with complete exception handling:

```
nano safe_divide.py
```

Type the following code:

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"Result is {result}")
    finally:
        print("Operation complete")

safe_divide(10, 2)
safe_divide(5, 0)
```

Save and run:

```
python3 safe_divide.py
```

<br>

---

### 18. Network Request Error Handling

Create a network request handler (requires internet):

```
nano network_request.py
```

Type the following code:

```python
import requests
try:
    response = requests.get("https://www.google.com", timeout=3)
    print("Connection successful!")
except requests.exceptions.ConnectTimeout:
    print("Oops! Connection took too long!")
```

Save and run:

```
python3 network_request.py
```

<br>

---

### 19. Retry Mechanism with Dynamic Wait Time

Create a retry script:

```
nano retry_dynamic.py
```

Type the following code:

```python
import time,requests

wait_times = [3, 2, 1]  # Dynamic wait times

for attempt in range(3):
    try:
        requests.get("https://www.google.com",timeout=3)
        print(f"Attempt {attempt+1} succeeded!")
        break
    except Exception:
        print(f"Attempt {attempt+1} failed")
        time.sleep(wait_times[attempt])
```

**Question:** How can we dynamically change the wait-time? First time: 3s, Second time: 2s, Third time: 1s

<br>

---

### 20. Username Validation with Custom Exception

Create a username checker:

```
nano username_check.py
```

Type the following code:

```python
existing_users = ["alice", "bob", "charlie"]

try:
    new_user = input("Choose username: ")
    if new_user in existing_users:
        raise ValueError("Username taken!")
    print("Username available!")
except ValueError as e:
    print(e)
```

**Question:** How can we use while-loop to add multiple users?

<br>

---

### 21. Password Strength Checker

Create a password validator using `raise`:

```
nano password_check.py
```

Type the following code:

```python
def check_password(pwd):
    if len(pwd) < 8:
        raise Exception("Password too short!")
    if not any(c.isdigit() for c in pwd):
        raise Exception("Add numbers!")

try:
    check_password("weak")
except Exception as e:
    print("Weak password: " + str(e))
```

Save and run:

```
python3 password_check.py
```

<br>

---

### 22. Fahrenheit to Celsius Converter

Create a temperature converter:

```
nano fahrenheit_celsius.py
```

Type the following code:

```python
try:
    fahr = float(input("Enter Fahrenheit: "))
except ValueError:
    print("Numbers only please!")
else:
    celsius = (fahr - 32) * 5/9
    print(f"{fahr}F = {celsius:.1f}C")
```

**Question:** Create a Celsius to Fahrenheit converter.

<br>

---

### 23. Temperature Range Validation

Create a temperature range checker:

```
nano temp_range.py
```

Type the following code:

```python
try:
    temp = float(input("Enter temp (-100 to 212F): "))
    if not (-100 <= temp <= 212):
        raise ValueError("Unrealistic temperature!")
    print("Temperature accepted!")
except ValueError as e:
    print(f"Invalid input: {e}")
```

**Question:** Put "Range Check" into the "Fahrenheit-to-Celsius" converter.

<br>

---

End
