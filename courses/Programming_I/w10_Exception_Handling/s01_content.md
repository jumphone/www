
## Section 1. Errors in Python

---

## When Coding Meets Real Life
### Example 1: The Missing Classroom
```python
open("non_existent_file.txt") 
# Like searching for classroom 404 that doesn't exist
```

---

## When Coding Meets Real Life 
### Example 2: Zero Division Drama
```python
total_people = 0
cake_slices = 8 / total_people
# Like preparing cake slices when no one comes to party
```

---

## Meet Python's Error Messages
### The 5 Most Common Errors

1. SyntaxError

```python
while True
```

2. NameError

```python
print(new_variable)
```

3. TypeError

```python
1+'a'
```

4. FileNotFoundError

```python
fi=open('okokokokok.txt','r')
```

5. IndentationError

```python
while True:
print('yes')
```

---

## Let's Read Error Messages Together! 
### Sample Error Stack

python3 demo.py

```python
Traceback (most recent call last):
  File "demo.py", line 3, in <module>
    print(undefined_var)
NameError: name 'undefined_var' is not defined
```

---

## Error Message Breakdown 
### What Each Part Means:
1. **Traceback**: Error roadmap
2. **File demo.py**: Where error happened
3. **Line 3**: Exact line number  
4. **NameError**: Error type
5. **undefined_var**: variable leading to error

---

## Question: What's the error here?
```python
def greet():
print("Hello!")  # Missing indentation

greet()
```

---

## Question: What's the error here?
```python
age = "20"
years_to_drive = age - 16
```


---

## Section 2. Exception Handling in Python

---

## Basic Try-Except Structure
```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Can't divide by zero!")
```
- `try`: Contains risky code
- `except`: Handles specific errors
- Like seatbelts for your code!

---

## Case: Let's Break a Calculator! 
What if someone tries to calculate BMI with zero height?
```python
try:
    weight = 70
    height = 0
    bmi = weight / height
except ZeroDivisionError:
    print("Alert! Did you enter height as zero?")
```
- Catches **specific** error type
- Prevents program crash

---

## Case: File Detective Game
What if student list file is missing?
```python
try:
    with open("ghost_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Pssst... this file doesn't exist!")
```
- `FileNotFoundError` specific handler
- Gives clear feedback

---

## The Safety Net (Catch-All)
When you're not sure what might go wrong:
```python
try:
    magic_number = "100" + 5
except Exception as e:
    print(e)
```
- `Exception` catches all errors
- `as e` stores error details

---

## Friendly Error Messages when building software
Make technical errors human-friendly:
```python
try:
    user_age = int(input("Enter age: "))
except ValueError:
    print("Hey! Numbers only please :)")
```
- Converts confusing errors
- Helps users understand mistakes

---

## Guess: What will happen ?

```python
try:
    guests = int(input("Number of guests: "))
    1+'2'
    sugar_per_person = 50
    total_sugar = sugar_per_person * guests
    print("Needed sugar: "+str(total_sugar)+"g")
except ValueError:
    print("Numbers only for guests please!")
except Exception as e:
    print(e)
```

---

## Section 3. Handling Multiple Exceptions


## Basic Exception Handling
```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Numbers only please!")
```

---

## Handling Different Error Types
### Multiple except Blocks
```python
try:
    age = int(input("Age: "))
    print(str(100/age))
except ValueError:
    print("Numbers only!")  
except ZeroDivisionError:
    print("Age can't be zero!") 
```
## Question: What will happen if we input 0 ? string ? 4 ? 
---

### How It Works
- First checks for `ValueError`
- Then checks for `ZeroDivisionError`
- Only one except block executes

---

## Handling Cases Together
### Tuple-style Catching
```python
try:
    with open("grades.txt") as f:
        print(f.read())
except (FileNotFoundError, PermissionError):
    print("File problem! Check if:")
    print("- File exists")
    print("- You have access")
```

---

## Grade Calculator: Base Code
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

## Question: Change it into Tuple-style ? 

---

## Practice Example: Pet Age
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
## Question: Change it into Tuple-style ? Do we really need to do that?


# Section 4: Exception Handling - finally and else

---

## finally
### Always Executes!
- Runs **whether exceptions occur or not**
- Perfect for cleanup operations
- Example situations:
  - Closing files
  - Releasing database connections
  - Freeing network resources

---

## File Handling with `finally`

## Guess: What will happen?
```python
try:
    file = open("diary.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Diary not found!")
finally:
    file.close()  # This always runs
    print("File handler cleaned up")
```

---

## The Special `else` Clause
### Runs Only When...
- No exceptions occurred in `try` block
- Useful for separating success logic
```python
try:
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Result is {result}")  # Only if successful
```

---

## Why Use `else`? 
- Makes code clearer than putting code at end of `try` block
- Avoids catching unexpected exceptions
- Example before/after comparison:

```python
# Without else
try:
    config = open("settings.cfg")
    # More code here...
    # Could accidentally catch exceptions from this code

# With else
try:
    config = open("settings.cfg")
except:
    #...
else:
    # Safe code here
```

---
## Question: who can explain the following program?
## Real-World Example: Safe Config Loader
```python
config_file = False
try:
    config_file = open("game_config.cfg")
except FileNotFoundError:
    print("⚠ Config file missing!")
else:
    settings = config_file.read()
    print(" Game configuration loaded!")
finally:
    if config_file:
        config_file.close()
    print("Resource cleanup completed")
```

---

## Common Patterns
### Resource Management Trio
1. `try`: Attempt risky operation
2. `except`: Handle known errors
3. `else`: Process success case
4. `finally`: Cleanup resources

---
## Question: who can explain the following function?
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

---

# Section 5. Exception Handling in Action


## 1 Network Requests: Connection Timeout
```python
import requests
try:
    response = requests.get("https://www.google.com", timeout=3)
except requests.exceptions.ConnectTimeout:
    print("Oops! Connection took too long!")

```
**What happens:**
- Waits 3 seconds for connection
- Shows message if server doesn't respond
---

## 2 Retry
```python
import time,requests
wait_time=3

for attempt in range(3):
    try:
        requests.get("https://www.google.com",timeout=3)
        break
    except Exception:
        print(f"Attempt {attempt+1} failed")
        time.sleep(wait_time)
```
## Question: How can we dynamically change the wait-time? 
First time: 3s
Second time: 2s
Third time: 1s

---

## 3 Checking Duplicate Usernames
```python
existing_users = ["alice", "bob", "charlie"]

try:
    new_user = input("Choose username: ")
    if new_user in existing_users:
        raise ValueError("Username taken!")
except ValueError as e:
    print(e)
```

## Question: How can we use while-loop to add multiple users? 

---

## 4 Password Strength Check (Use "raise" to define error)
```python
def check_password(pwd):
    if len(pwd) < 8:
        raise Exception("Password too short!")
    if not any(c.isdigit() for c in pwd):
        raise Exception("Add numbers!")

   
try:
    check_password("weak")
except Exception as e:
    print("Weak password: "+str(e))
```

---



---

## 5 Fahrenheit Input Validation
```python
try:
    fahr = float(input("Enter Fahrenheit: "))
except ValueError:
    print("Numbers only please!")
else:
    celsius = (fahr - 32) * 5/9
    print(f"{fahr}F = {celsius:.1f}C")
```

## Question: celsius to fahrenheit? 

---

## 6 Temperature Range Check (use "raise")
```python
try:
    temp = float(input("Enter temp (-100 to 212F): "))
    if not (-100 <= temp <= 212):
        raise ValueError("Unrealistic temperature!")
except ValueError as e:
    print(f"Invalid input: {e}")
```

---
## Question: put "Range Check" into the "Fahrenheit-to-Celsius"? 


