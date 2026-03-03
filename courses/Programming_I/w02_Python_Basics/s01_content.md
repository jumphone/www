[Back](https://www.bioinfo-lab.com/courses/Programming_I/w02_Python_Basics/)

Q: How many of you have written Python code before?

Q: How many of you have run a Python script before?

---

"Interactive Mode" is a command-line interface where you type and execute Python code line by line.

"Script Mode" is used to execute entire Python programs saved in files.

Python interpreter: A program that reads and executes Python code. It works in both interactive and script modes.

IDLE is a simple integrated development environment for Python.

---

Q: What's your intuitive guess about the advantages and disadvantages of interactive mode and script mode?

---

`exit()` is the command used to exit Python interactive mode.

`python3 script.py` is used to run a Python script in script mode.

Python syntax emphasizes indentation, typically using 4 spaces as the standard.

`#` is used for single-line comments in Python.

Reserved keywords (such as `if`, `else`, `while`) cannot be used as variable names or function names.

---

Q: What are the important things when writing Python code?

Q: What are the two most common types of errors in Python?

---

Variable Naming Rules: Cannot start with a number, can only contain letters, numbers, and underscores.

Python is a dynamically typed language, allowing variables to be rebound to objects of different types at runtime.

Core data types: Integers (`int`), floating-point numbers (`float`), and strings (`str`).

`type()` function is used to check the type of a variable.

Type conversion functions: `int()`, `float()`, `str()`.

---

Q: Why do we need different data types in Python?

---

Six types of operators in Python:

1. Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
2. Comparison operators: `>`, `<`, `==`, `!=`, `>=`, `<=`
3. Logical operators: `and`, `or`, `not`
4. Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`
5. Identity operators: `is`, `is not`
6. Membership operators: `in`, `not in`

Operator precedence determines evaluation order; parentheses can change precedence.

---

"aaa" + "bbb" results in "aaabbb"

Escape characters: `\n` (newline), `\t` (tab)

---

Q: What differences do you feel between writing Python code and using Linux commands?

---

Strings support indexing and slicing operations.

String index starts from 0.

Common string methods:
- `split()`: Split a string into a list
- `join()`: Concatenate strings in a list
- `strip()`: Remove leading and trailing whitespace
- `find()`: Search for substrings, returns index or -1
- `index()`: Search for substrings, raises exception if not found
- `lower()`: Convert to lowercase
- `upper()`: Convert to uppercase
- `title()`: Capitalize first letter of each word

---

`tab` type the first few letters of a variable name or function, then press the Tab key. Python will suggest completions.

`history` In interactive mode, you can use the up arrow key to see previously entered commands.

---

End
