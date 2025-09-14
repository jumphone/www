
# Section 1. Python Basic Syntax Fundamentals

## 1. Objectives
- Understand Python execution modes
- Master basic syntax rules
- Recognize reserved keywords
- Write first Python program
- Handle common syntax errors

---

## 1. Python Execution Modes (Interactive vs Script)

### Interactive Mode
```python
$ python3
>>> print("Hello World!")
Hello World!
>>> exit()
```
**Features**:
- Immediate feedback
- Good for quick testing
- Type commands directly

### Script Mode
```bash
$ nano hello.py  # Create file using nano
$ python3 hello.py
```
**Features**:
- Save code permanently
- Better for complex programs
- Use text editor (nano/vim)

---

## 2. Core Syntax Rules

### Indentation Rules (4-space principle)
```python
# Correct
if True:
    print("This is properly indented")

# Error
if True:
print("This will cause IndentationError")
```

### Code Comments
```python
# Single-line comment

'''
Multi-line comment
Spanning multiple lines
'''

def calculate():
    """Docstring comments for functions"""
```

### Statement Separation
```python
# Use semicolon ";". Valid but not recommended
x=1; y=2; print(x+y)

# Preferred
x = 1
y = 2
print(x + y)
```

---

## 3. Reserved Keywords (35 in Python 3.7)

|          |         |        |         |         |
|----------|---------|--------|---------|---------|
| False    | None    | True   | and     | as      |
| assert   | async   | await  | break   | class   |
| continue | def     | del    | elif    | else    |
| except   | finally | for    | from    | global  |
| if       | import  | in     | is      | lambda  |
| nonlocal | not     | or     | pass    | raise   |
| return   | try     | while  | with    | yield   |

**Important**: These cannot be used as variable/function names!

---

## 4. First Python Program

### Interactive Version
```python
>>> print("Hello World!")
Hello World!
```

### Script Version (hello.py)
```python

### Full version #####
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

#### Ok to run #######

print('Hello World!')

```

**Execution Steps**:
1. Login to Linux Server using Termius
2. Create file: `nano hello.py`
3. Write code
4. Save: `Ctrl+O` → Press "enter": `Ctrl+X`
5. Run: `python3 hello.py`

---

## 5. Common Errors & Debugging

### Error Types
1. **SyntaxError**: 
```python
prin("Missing t")  # NameError
```

2. **IndentationError**:
```python
def test():
print("Missing indent")
```

3. **TypeError**:
```python
"5" + 3  # str + int
```

### Debugging Techniques
1. Read error messages carefully
2. Check line numbers
3. Use print() debugging
4. Validate indentation
5. Test code snippets in interactive mode
6. **AI Assistant Tip**: Use Kimi/ChatGPT to explain errors

---

## Best Practices Checklist
- Always use 4-space indentation
- Write full comments
- Avoid semicolons ";" for multiple statements
- Check for reserved keywords
- Test code frequently

---





# Section 2. Variables & Data Types


---

## 1. The Nature of Variables
### Variable
```python
# Think of variables as labeled boxes in warehouse (memory in the computer)
box_label = "item_count"  # Variable name
box_content = 17          # Stored value
```

### Key Mechanisms
- **Binding**: Variables are references to objects
- **Garbage Collection**: Automatic memory reclaiming
- **Reassignment Dynamics**:
  ```python
  x = 10    # Create object 10, bind to x
  x = "cat" # Create new object, rebind x
  ```

---

## 2. Variable Naming Deep Dive
### Rule Enforcement Demo
```python
# Number('123'), underline ('_'), characters ('abcABC')
# No number at the beginning.

# Valid but discouraged examples
_privateVar = 1
MAX_LIMIT = 100
tempVar2 = 3.14

# Invalid examples (with error simulation)
3attempt = 5              # SyntaxError
special-chars = "text"    # SyntaxError
```

### PEP8 Pro Practices

PEP8: Python Enhancement Proposal 8

```python
# Good vs Better
studentname → student_name
tmpf → temporary_file
calcVal → calculate_value
```

---

## 3. Dynamic Typing in Action
### Demo
```python
dynamic_var = 100          # int
print(type(dynamic_var))   # <class 'int'>

dynamic_var = "Python"     # str
print(type(dynamic_var))   # <class 'str'>

dynamic_var = [1, 2, 3]    # list
print(type(dynamic_var))   # <class 'list'>
```

### Variable Type: Static (c++) vs Dynamic (python)

```c++
// C++ static typing (comparison)
// type_error.cpp
#include <iostream>
int main() {
   int number = 5;       // Type locked
   number = "text";
   std::cout << "The number is: " << number << std::endl;
}
// g++ type_error -o type_error
```

```python
# Python dynamic typing
number = 5           # int
number = "text"      # Valid
print(number)
```

---

## 4. Core Data Types
### Integer Representations
```python
binary_num = 0b1010     # 10 (binary representation)
octal_num = 0o177       # 127 (octal)
hex_num = 0x1af         # 431 (hex)
number = 33             # 33 (decimal)
```

### Floating-Point Precision
```python
# Demonstration of precision issues
print(0.1 + 0.2 == 0.3)           # False
print(f"{0.1 + 0.2:.17f}")        # 0.30000000000000004, approximately equal to 0.3

# Mitigation strategies
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # Exact 0.3
```

### String Definition Variants
```python
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes preserve
line breaks and "both" quote types'''
```

---

## 5. Type Conversions
### Conversion Examples
```python
# String to number
age = int("25")
pi = float("3.1415")

# Number to string
price = str(9.99)

# Truthy conversions
bool(0)     # False
bool(1)     # True
bool("")    # False
bool("a")   # True
bool([])    # False
bool([1])   # True
```

### Automatic Conversion Examples
```python
3 + 5.0         # int promoted to float
True + 10       # bool treated as int(1)
"ID:" + str(100)# Required explicit conversion
```

---

## 6. Memory Visualization with id
### Address Tracing Demo
```python
a = 256
b = 256
print(id(a) == id(b))  # True (small int caching)

x = 257
y = 257
print(id(x) == id(y))  # False (non-cached)

list1 = [1,2]
list2 = [1,2]
print(id(list1) == id(list2))  # Always False
```

---


# Section 3. Python Operator System


---
## Today's Learning Objectives
1. Master 6 types of operators in Python
2. Understand operator precedence rules
3. Learn practical coding techniques
4. Develop error-avoidance strategies

---
## 1. Arithmetic Operators

### Core Operators Table
| Operator | Description          | Example       | Result  |
|----------|----------------------|---------------|---------|
| `+`      | Addition             | `5 + 3`       | 8       |
| `-`      | Subtraction          | `7 - 2`       | 5       |
| `*`      | Multiplication       | `3 * 4`       | 12      |
| `/`      | True Division        | `10 / 3`      | 3.333...|
| `//`     | Floor Division       | `10 // 3`     | 3       |
| `%`      | Modulus              | `10 % 3`      | 1       |
| `**`     | Exponentiation       | `2 ** 3`      | 8       |


---
## 2. Comparison Operators

### Numeric Comparisons
```python
a = 7
b = 5
print(a > b)   # True
print(a == b+2)# True
```

### String Comparison Rules
1. Compare character by character (ASCII values)
2. Shorter strings are considered smaller
3. Case-sensitive comparison

```python
print('Apple' < 'Banana')  # True (A(65) < B(66))
print('cat' > 'CAT')       # True (lowercase > uppercase)
print('10' < '2')          # True (character '1'(49) vs '2'(50))
```

---
## 3. Logical Operators

### Truth Table
| X     | Y     | X and Y | X or Y | not X |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

### Short-Circuiting Demo
```python
def check():
    print("Called!")
    return False

print(True or check())  # Short-circuit, no output
print(False and check())# Short-circuit, no output
```

### Precedence Table

You need to know:

"()" parentheses are not operators but have the highest priority 

| Priority | Operators                     |
|----------|-------------------------------|
| 1        | `**`  Exponentiation          |
| 2        | `+x`, `-x`                    |
| 3        | `*`, `/`, `//`, `%`           |
| 4        | `+`, `-`                      |
| 5        | Comparisons (`<`, `>`, etc)   |
| 6        | `not`                         |
| 7        | `and`                         |
| 8        | `or`                          |

Full list:

| Priority | Operators                     |
|----------|-------------------------------|
| 1        | `**`                          |
| 2        | `+x`, `-x`, `~x`              |
| 3        | `*`, `/`, `//`, `%`           |
| 4        | `+`, `-`                      |
| 5        | `<<`, `>>`                    |
| 6        | `&`                           |
| 7        | `^`                           |
| 8        | `|`                           |
| 9        | Comparisons (`in`, `<`, `>`, etc)|
| 10       | `not`                         |
| 11       | `and`                         |
| 12       | `or`                          |


---
## 4. Assignment Operators

### Chained Assignment
```python
x = y = z = 0  # All variables point to same 0
print(id(x), id(y))  # Same memory address
```

### Compound Operators
```python
counter = 5
counter += 3    # Equivalent to counter = counter + 3
counter **= 2   # 8^2 = 64
```

### Mutable Object Pitfall
```python
list1 = list2 = []
list1.append(5)
print(list2)  # [5] (both reference same list)
```


---
## 5. Precedence Practice

### Challenge Exercise
```python
result = 5 + 3 * 2 ** 2 // (4 % 3) - 1
# Step-by-step evaluation:
# 1. 4%3 = 1
# 2. 2**2 = 4
# 3. 3*4 = 12
# 4. 12//1 = 12
# 5. 5+12 = 17
# 6. 17-1 = 16
```


### AI-Assisted Learning
"Ask Kimi/ChatGPT to explain why `0.1 + 0.2 != 0.3` in Python and how to properly compare floats."

---





# Section 4. Advanced String Operations


---

### 1. String Interning Mechanism 
- **What**: Python's memory optimization for identical strings
- **How it works**:
  ```python
  a = "python"
  b = "python"
  print(a is b)  # Output: True (when string meets interning conditions)
  print(id(a))
  print(id(b))
  a = "a"*10000
  b = "a"*10000
  print(id(a))
  print(id(b))
  ```
- **Rules**:
  - Automatically interns:
    - Empty strings
    - Identifier-like strings
    - Short Strings

---

### 2. Indexing & Slicing
#### Index Types
- Positive Index: `0` to `len(str)-1`
- Negative Index: `-1` (last char) to `-len(str)`

#### Slice Syntax
```python
text = "programming"
print(text[3:7])    # 'gram'
print(text[::-1])   # 'gnimmargorp' (reverse)
print(text[::2])    # 'pormig' (step=2)
```

#### Key Patterns
- `str[start:end]` (end not included)
- `str[start:]`    # till end
- `str[:end]`      # from beginning
- `str[::step]`    # step control

---

### 3. String Methods Library
#### Split & Join
```python
csv = "apple,banana,cherry"
items = csv.split(",")  # ['apple', 'banana', 'cherry']
new_str = "-".join(items)  # "apple-banana-cherry"
```

#### Stripping Methods
```python
s = "   hello world  \t\n"
print(s.strip())    # "hello world"
print(s.lstrip())   # "hello world  \t\n" "\n": line break; "\t": tab
print(s.rstrip())   # "   hello world"
```

#### Search Methods
```python
s = "Python Programming"
print(s.find('thon'))     # 2 (returns -1 if not found)
print(s.index('thon'))   # 2 (raises ValueError if not found)
```

#### Case Conversion
```python
print("Hello".lower())    # 'hello'
print("world".upper())    # 'WORLD'
print("title case".title()) # 'Title Case'
```

---

### 4. Formatting Methods
#### %-formatting
```python
name = "Alice"
print("Hello, %s! You have %d messages." % (name, 5))
```

#### str.format()
```python
print("{} + {} = {}".format(2, 3, 2+3))
print("{1} appears before {0}".format("apple", "banana"))
```

#### f-strings (Python 3.6+)
```python
price = 19.99
print(f"Total: ${price * 1.1:.2f}")
print(f"Binary: {42:b}")  # '101010'
```

#### Comparison Table
| Method       | Readability | Performance | Features            |
|--------------|-------------|-------------|---------------------|
| %-formatting | Low         | Medium      | Basic types only    |
| str.format   | Medium      | Medium      | Positional/Keyword  |
| f-strings    | High        | Best        | Expressions, inline |


#### My suggestion for beginner

```python
name = 'John'
number = 5
print("Hello, "+name+"! You have "+ str(number) +" messages.")
```

---

### 5. Escape Characters & Raw Strings
#### Common Escapes
- `\n` Newline
- `\t` Tab
- `\\` Backslash
- `\"` Double quote

#### Raw Strings
```python

r"" is raw string.

path = r"C:\new_folder\test.txt"
regex = r"\d+\.\d+"
print(path)  # Shows literal backslashes
print(regex)
```

---

### 6. Multi-line Strings
#### Triple-quoted Strings
```python
long_text = """First line
Second line
Third line"""
```




