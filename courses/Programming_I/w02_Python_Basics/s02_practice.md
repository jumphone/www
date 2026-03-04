
[Back](https://www.bioinfo-lab.com/courses/Programming_I/w02_Python_Basics/)

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b> on Moodle by 23:59 this Sunday. 


This is an important part of your "General Performance". Please ensure timely submission!!!

<br>

---

### Tips

“tab” type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

“history” You can see all the commands you have run before.

Try "ai", "aiw", and "aid"


<br>

---

### 1. Log into the remote Linux Server.

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---

1. Open Python Interactive Mode

Open your terminal (Termius or local terminal)

Type `python3` to enter interactive mode

You should see the Python version and the `>>>` prompt

<br>

---

2. Basic Python Commands in Interactive Mode

```
# Check Python version
import sys
print(sys.version)

# Simple arithmetic operations
2 + 3
10 - 4
5 * 6
20 / 4

# Exit interactive mode
exit()
```

<br>

---

3. Create and Run Your First Python Script

```
# Create a new Python script file
cd ~
nano hello.py

# Type the following code in nano:
print("Hello, World!")
name = "Python"
print("I am learning", name)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 hello.py
```

<br>

---

4. Variables and Data Types

```
# Create a new script file
cd ~
nano variables.py

# Type the following code:
# Integer
age = 25
print("Age:", age)
print("Type:", type(age))

# Float
height = 1.75
print("Height:", height)
print("Type:", type(height))

# String
name = "Alice"
print("Name:", name)
print("Type:", type(name))

# Type conversion
age_str = str(age)
print("Age as string:", age_str)
print("Type:", type(age_str))

# Save and exit nano
# Run the script
python3 variables.py
```

<br>

---

5. Operators Practice

```
# Create a new script file
cd ~
nano operators.py

# Type the following code:
# Arithmetic operators
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Comparison operators
print("a > b:", a > b)
print("a == b:", a == b)

# Logical operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Save and exit nano
# Run the script
python3 operators.py
```

<br>

---

6. String Operations

```
# Create a new script file
cd ~
nano strings.py

# Type the following code:
# String creation
greeting = "Hello, Python!"
print(greeting)

# String concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)

# String indexing
print("First character:", greeting[0])
print("Last character:", greeting[-1])

# String slicing
print("First 5 characters:", greeting[0:5])
print("Characters 7-12:", greeting[7:13])

# String methods
text = "  Hello World  "
print("Original:", text)
print("Stripped:", text.strip())
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

# Find and split
sentence = "Python is easy to learn"
print("Find 'easy':", sentence.find("easy"))
print("Split:", sentence.split())

# Join
words = ["Python", "is", "fun"]
joined = " ".join(words)
print("Joined:", joined)

# Save and exit nano
# Run the script
python3 strings.py
```

<br>

---

7. Comments and Indentation

```
# Create a new script file
cd ~
nano structure.py

# Type the following code:
# This is a single-line comment
# The following code demonstrates proper indentation

def greet(name):
    # This is an indented block (4 spaces)
    message = "Hello, " + name
    return message

# Main program
user = "Student"
result = greet(user)
print(result)

# Multi-line example with proper indentation
if user == "Student":
    print("Welcome to the course!")
    print("You are in the right place.")
else:
    print("Please check your user type.")

# Save and exit nano
# Run the script
python3 structure.py
```

<br>

---

8. Escape Characters and String Formatting

```
# Create a new script file
cd ~
nano formatting.py

# Type the following code:
# Escape characters
print("Line 1\nLine 2")  # Newline
print("Column 1\tColumn 2")  # Tab
print("He said \"Hello\"")  # Quotes

# String formatting examples
name = "Bob"
age = 20
print("Name: " + name + ", Age: " + str(age))

# Using f-strings (modern Python)
print(f"Name: {name}, Age: {age}")

# Using format method
print("Name: {}, Age: {}".format(name, age))

# Save and exit nano
# Run the script
python3 formatting.py
```

<br>

---

End

