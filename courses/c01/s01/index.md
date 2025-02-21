[home](https://www.bioinfo-lab.com)

# Programming 1

## Lesson 1

---

### Slide 1: Course Objectives
**Content:**  
- By the end of these 18 lessons, you’ll have learned the basics of Python programming.  
- You’ll be able to write your own programs, understand existing code, and use Python to solve real-world problems.  
- Python is versatile, easy to learn, and widely used across many industries.

---

### Slide 2: Course Structure
**Content:**  
- Step-by-step through core programming concepts  
- Start with basics: interacting with a computer, using Python, writing simple programs  
- Progress to advanced topics: object-oriented programming, data handling, files, and libraries  

---

### Slide 3: Learning to Learn
**Content:**  
- Become an independent learner  
- Utilize tools like large language models (e.g., ChatGPT)  
- Debug code, explain concepts, and get hints when stuck  

---

### Slide 4: Importance of Practice
**Content:**  
- Programming skill improves with experience  
- Try things on your own outside of class  
- Experiment more to get comfortable with Python  

---

### Slide 5: No Stupid Questions
**Content:**  
- If you’re confused, ask  
- We’re here to learn together  
- There’s no such thing as a stupid question  

---

### Slide 6: Learning Pace
**Content:**  
- Learning to program is not a race  
- Everyone learns at their own pace  
- It’s okay if you don’t understand everything right away  

---

### Slide 7: Overcoming Challenges
**Content:**  
- Programming is about solving problems  
- Running into challenges is normal  
- Each challenge you face and overcome makes you better and more confident  

---

### Slide 8: Course Summary
**Content:**  
- Cover Python fundamentals in a structured way  
- Use hands-on practice and theoretical learning  
- Get familiar with Python syntax, tools, and concepts  

---

### Slide 9: Practical Examples
**Content:**  
- Introduce you to the world of programming  
- Use practical examples to illustrate concepts  
- Help you see how different pieces of code fit together  

---

### Slide 10: Becoming Independent Learners
**Content:**  
- By the end of this course, you’ll be able to continue learning and growing on your own  
- Equip you with the skills to tackle new challenges independently  
- Foster a lifelong learning mindset  

---


---

### Slide 11: Introduction to Linux
**Content:**  
- Linux is an operating system like Windows or macOS.  
- It is open-source, free to use, modify, and distribute.  
- Widely used for servers, powering many of the world's most important servers.

---

### Slide 12: Why Linux is Popular
**Content:**  
- Highly customizable, secure, and stable.  
- Efficient even on large-scale systems.  
- Great for learning how servers work.

---

### Slide 13: CentOS 7
**Content:**  
- We will use CentOS 7 in this course.  
- Based on Red Hat Linux, reliable and easy to use.  
- Commonly used in production environments.

---

### Slide 14: Why Use Linux for Programming
**Content:**  
- Many programming projects are developed and run on Linux.  
- Common platform for hosting websites, managing databases, and running code.  
- Tools like Python are optimized for Linux environments.

---

### Slide 15: Learning About the Inner Workings
**Content:**  
- Linux encourages a hands-on learning experience.  
- Gain a deeper understanding of how code interacts with the system.  
- Invaluable for your growth as a programmer.

---

### Slide 16: What Are Servers
**Content:**  
- Servers provide services or resources to clients over a network.  
- Host applications, databases, websites, or files.  
- Example: Visiting a website involves a server delivering information to your browser.

---

### Slide 17: Using a CentOS 7 Server
**Content:**  
- We will use a CentOS 7 server to practice coding.  
- Access the server through a terminal interface.  
- Powerful for coding projects in a Linux environment.

---

### Slide 18: Why a Server Environment
**Content:**  
- Real-world developers often write and test code on remote servers.  
- Access to powerful computing resources.  
- Learn important concepts like remote file management and system administration.

---

### Slide 19: Course Overview
**Content:**  
- Learn to connect to the server and navigate the file system.  
- Use tools to manage and edit code.  
- Understand how servers interact with programming languages like Python.

---

### Slide 20: Summary
**Content:**  
- Linux is a powerful and versatile operating system.  
- CentOS 7 is the version we will use.  
- Working with a remote server provides real-world experience.  
- Gain key programming concepts and system management skills.  

---


---

### Slide 21: Introduction to Server Login
**Content:**  
- Now, we’ll cover how to log into the Linux server we’ll use throughout this course.  
- Don’t worry, I’ll guide you through each step.

---

### Slide 22: Understanding Server Access
**Content:**  
- When you access a server, you’re connecting to a computer running elsewhere.  
- This could be in a data center, at your university, or in the cloud.  
- Such computers are often referred to as remote servers.

---

### Slide 23: Introducing Termius
**Content:**  
- Termius is a tool that allows you to connect to remote servers using SSH (Secure Shell).  
- SSH is a secure way to communicate with remote computers over the internet.  
- Termius provides a user-friendly interface to manage these connections.

---

### Slide 24: Setting Up Termius
**Content:**  
- Download and install Termius from the official website or app store.  
- Open the application and create a new host.  
- Enter the following details:  
  - Host: IP address of the CentOS 7 server.  
  - Port: Default is 22.  
  - Username: Provided to you.  
  - Password: Provided to you.

---

### Slide 25: Logging In to the Server
**Content:**  
- Select the server from your saved connections in Termius.  
- Termius will attempt to establish a connection using SSH.  
- Verify the server’s identity if prompted, then enter your password.

---

### Slide 26: Interacting with the Server
**Content:**  
- Once logged in, you’ll see a command prompt.  
- This is where you can start entering commands to interact with the server.  
- Example prompt: `user@centos7:~$`

---

### Slide 27: Basic Command Line Commands
**Content:**  
- `ls`: List files in the current directory.  
- `cd`: Change directories.  
- `mkdir`: Create directories.  
- These commands help you navigate and manage files on the server.

---

### Slide 28: Key Concepts of the Terminal
**Content:**  
- **Terminal vs. Command Line**: The terminal is the program, the command line is the text interface.  
- **Directories**: Navigate through directories using `cd` and list contents with `ls`.  
- **Permissions**: Depending on your user role, you may need administrative access for certain actions.

---

### Slide 29: Importance of Server Interaction
**Content:**  
- Logging into servers and using the command line is essential for programmers.  
- Many programming environments rely on remote servers for data processing and application deployment.  
- Being comfortable with these skills will make you more efficient in real-world programming.

---

### Slide 30: Summary
**Content:**  
- Termius is the tool we’ll use to connect to the CentOS 7 server.  
- Once connected, you’ll interact with the server through the command line.  
- Basic commands like `cd`, `ls`, and `mkdir` will help you navigate the file system.  
- Understanding permissions and the terminal will be key as you work with the server.

---


---

### Slide 31: Introduction to Remote File Management
**Content:**   
- Now, we’ll explore remote file management using SFTP and Termius.  
- Understanding these tools is crucial for managing files on remote servers.

---

### Slide 32: What is SFTP?
**Content:**  
- SFTP stands for Secure File Transfer Protocol.  
- It allows secure file transfers between computers over a network.  
- Encrypts data during transfer, ensuring security.

---

### Slide 33: Why Use SFTP?
**Content:**  
- Unlike local file management, servers require specific tools.  
- SFTP enables uploading, downloading, and modifying files on remote servers.  
- Essential for managing sensitive information and private projects.

---

### Slide 34: Using Termius for File Management
**Content:**  
- Termius connects you to the CentOS 7 server and offers SFTP capabilities.  
- Switch between terminal and SFTP interfaces easily.  
- Manage files directly from the Termius interface.

---

### Slide 35: Steps to Manage Files with Termius
**Content:**  
1. Connect to the server using SSH.  
2. Navigate the file system in the graphical interface.  
3. Upload files by dragging them into the server’s folder.  
4. Download files by dragging them to your local folder.

---

### Slide 36: Advanced File Management with Termius
**Content:**  
- Rename and delete files using right-click options.  
- Edit files directly in your local editor and save changes back to the server.  
- Efficient and convenient for managing server files.

---

### Slide 37: Benefits of SFTP and Remote File Management
**Content:**  
- Efficiency: Quick and easy file management.  
- Organization: Keep files structured and accessible.  
- Security: Protect data during transfer.  
- Remote Access: Manage files from anywhere securely.

---

### Slide 38: Real-World Use Case: Web Development
**Content:**  
- Example: Uploading website files to a server.  
- Upload HTML, CSS, JavaScript, and Python scripts.  
- Maintain and update the site using SFTP.

---

### Slide 39: Tips for Efficient File Management
**Content:**  
- Keep Organized: Use separate folders for different file types.  
- Use Version Control: Track changes with tools like Git.  
- Backup Your Files: Always keep copies of important files.

---

### Slide 40: Wrapping Up
**Content:**  
- SFTP is a secure method for managing remote server files.  
- Termius provides a user-friendly interface for SFTP.  
- Essential for web development, application management, and data handling.

---


---

### Slide 41: Introduction to Nano
**Content:**  
- Nano is a text editor that works in the terminal.  
- It's great for creating, editing, and saving files on Linux servers.  
- Nano is beginner-friendly and doesn't require a graphical interface.

---

### Slide 42: Why Use Nano?
**Content:**  
- Ideal for remote server work via SSH.  
- No need for a graphical environment.  
- Fast and efficient, with minimal system resource usage.

---

### Slide 43: Opening Nano
**Content:**  
- Start nano by typing `nano` followed by the file name.  
- Example: `nano example.txt`  
- Nano will create the file if it doesn't exist.

---

### Slide 44: Navigating in Nano
**Content:**  
- Editing area at the top.  
- Command shortcuts at the bottom.  
- Use arrow keys to move the cursor.

---

### Slide 45: Basic Commands
**Content:**  
- **Ctrl + O**: Save the file.  
- **Ctrl + X**: Exit nano.  
- **Ctrl + K**: Cut the current line or selected text.  
- **Ctrl + U**: Paste the text.  
- **Ctrl + W**: Search for text.  
- **Ctrl + C**: Show cursor position.

---

### Slide 46: Editing Files in Nano
**Content:**  
- Type directly to add or edit text.  
- Use Ctrl + K and Ctrl + U for cutting and pasting.  
- Search for text with Ctrl + W.

---

### Slide 47: Real-World Use of Nano
**Content:**  
- Modify a Python script directly on the server.  
- Open, edit, and save the script without needing to download it.  
- Example: Change a variable in your script.

---

### Slide 48: Tips for Using Nano
**Content:**  
- Learn the basic commands.  
- Use keyboard shortcuts.  
- Save your work often.  
- Create backups before making changes.

---

### Slide 49: Saving and Exiting
**Content:**  
- Save your work with **Ctrl + O**.  
- Exit nano with **Ctrl + X**.  
- Nano will prompt you to save if changes are unsaved.

---

### Slide 50: Summary
**Content:**  
- Nano is a simple, terminal-based text editor.  
- Essential commands: **Ctrl + O** (save) and **Ctrl + X** (exit).  
- Editing, cutting, pasting, and searching are easy.  
- Save your work frequently and use keyboard shortcuts for efficiency.

---


---

### Slide 51: Why Install Python?
**Content:**  
- Write and run Python code locally  
- Debug and experiment freely  
- Python is versatile and runs on multiple platforms

---

### Slide 52: Step 1: Downloading Python
**Content:**  
- Official Python website: https://www.python.org/downloads/  
- Ensure you download Python 3.7.10  
- Download links for Windows, macOS, and Linux

---

### Slide 53: Installing Python on Windows
**Content:**  
1. Go to the official Python website  
2. Download Python 3.7.10  
3. Open the installer and check "Add Python to PATH"  
4. Click "Install Now" and follow instructions

---

### Slide 54: Installing Python on macOS
**Content:**  
1. Visit the official Python website  
2. Download the installer for Python 3 (no macOS installer for 3.7.10)  
3. Open the .pkg file and follow installation steps  
4. Verify installation with `python3 --version`

---

### Slide 55: Installing Python on Linux (CentOS 7)
**Content:**  
1. Update your system with `sudo yum update`  
2. Install Python 3.7 using `sudo yum install python37`  
3. Verify installation with `python3 --version`

---

### Slide 56: Step 2: Verifying the Installation
**Content:**  
- Windows: Open Command Prompt and type `python --version`  
- macOS: Open Terminal and type `python3 --version`  
- Linux: Open Terminal and type `python3 --version`

---

### Slide 57: Step 3: Installing pip
**Content:**  
- pip is included with Python 3.7.10  
- Windows: Check pip with `pip --version`  
- macOS/Linux: Check pip with `pip3 --version`

---

### Slide 58: Step 4: Testing the Installation
**Content:**  
1. Create a file named `test.py` with `print("Hello, Python!")`  
2. Run the script with `python3 test.py` (or `python test.py` on Windows)  
3. Expected output: `Hello, Python!`

---

### Slide 59: Troubleshooting Common Issues
**Content:**  
- Python not recognized: Reinstall and check "Add Python to PATH"  
- Version mismatch: Ensure you install Python 3.7.10  
- Permission errors: Use `sudo` for Linux/macOS installations

---

### Slide 60: Wrapping Up
**Content:**  
- Downloaded and installed Python 3.7.10  
- Verified Python installation  
- Checked pip installation  
- Ran a simple Python script successfully

---


---

### Slide 61: Introduction to Python
**Content:**  
- Python is a high-level, interpreted programming language.  
- It is designed to be easy to read and write.  
- Python code is executed line by line by an interpreter.

---

### Slide 62: Python's Popularity
**Content:**  
- Python is one of the most popular programming languages globally.  
- Known for its simplicity, readability, and versatility.  
- Excellent choice for beginners.

---

### Slide 63: Basic Concepts in Python
**Content:**  
- Variables  
- Data Types  
- Operators

---

### Slide 64: Variables in Python
**Content:**  
- Variables are like containers for storing data.  
- Example:  
  ```python
  message = "Hello, World!"
  print(message)
  ```

---

### Slide 65: Data Types
**Content:**  
- Strings: Text data enclosed in quotation marks.  
  ```python
  name = "John"
  ```  
- Integers: Whole numbers.  
  ```python
  age = 25
  ```  
- Floats: Decimal numbers.  
  ```python
  price = 19.99
  ```  
- Booleans: True or False values.  
  ```python
  is_student = True
  ```

---

### Slide 66: Operators in Python
**Content:**  
- Arithmetic operators: +, -, *, /  
  ```python
  x = 10
  y = 5
  sum_result = x + y  # 15
  difference = x - y  # 5
  product = x * y     # 50
  quotient = x / y    # 2.0
  ```  
- Comparison operators: ==, >  
  ```python
  is_equal = x == y   # False
  is_greater = x > y  # True
  ```

---

### Slide 67: Indentation in Python
**Content:**  
- Python uses indentation to define blocks of code.  
- Example:  
  ```python
  age = 18
  if age >= 18:
      print("You are an adult.")
  else:
      print("You are a minor.")
  ```

---

### Slide 68: Why Choose Python?
**Content:**  
- Readable and Simple Syntax  
- Cross-platform Compatibility  
- Large Standard Library  
- Strong Community Support

---

### Slide 69: Summary
**Content:**  
- Python is a high-level programming language.  
- Variables store data.  
- Data types include strings, integers, floats, and booleans.  
- Operators perform operations on values.  
- Indentation structures the code.

---

### Slide 70: Conclusion
**Content:**  
- Python is versatile and easy to learn.  
- It is widely used across many industries.  
- By the end of this course, you’ll be able to write your own programs and solve real-world problems.

---


---

### Slide 71: Introduction to Python REPL
**Content:**    
- Now, we'll explore the Python interactive command line, also known as the Python REPL.  
- It's a powerful tool for learning Python with ‌immediate‌ feedback.

---

### Slide 72: What is REPL?
**Content:**  
- REPL stands for Read-Eval-Print Loop.  
- **Read:** The REPL reads the code you type.  
- **Eval:** It evaluates the code.  
- **Print:** It shows the result.  
- **Loop:** It keeps running, waiting for more code.

---

### Slide 73: Starting the Python REPL
**Content:**  
- **Linux/macOS:** Open terminal, type `python3`, press Enter.  
- **Windows:** Open Command Prompt or PowerShell, type `python`, press Enter.  
- You'll see a prompt like:  
  ```
  Python 3.7.10 (default, May  3 2021, 08:25:12)
  [GCC 8.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```

---

### Slide 74: Using the REPL
**Content:**  
- Type Python commands directly into the REPL.  
- Example:  
  ```
  >>> print("Hello, World!")
  Hello, World!
  ```
- Try simple math:  
  ```
  >>> 5 + 3
  8
  >>> 10 * 4
  40
  >>> 9 / 3
  3.0
  ```

---

### Slide 75: Variables in the REPL
**Content:**  
- Variables hold values.  
- Example:  
  ```
  >>> x = 5
  >>> x
  5
  >>> y = 10
  >>> x + y
  15
  ```
- Reassign values:  
  ```
  >>> x = 20
  >>> x
  20
  ```

---

### Slide 76: Functions and the REPL
**Content:**  
- Use built-in functions:  
  ```
  >>> len("Python")
  6
  ```
- Define your own functions:  
  ```
  >>> def add_numbers(a, b):
  ...     return a + b
  ...
  >>> add_numbers(3, 4)
  7
  ```

---

### Slide 77: Debugging with the REPL
**Content:**  
- The REPL helps find and fix errors.  
- Example of an error:  
  ```
  >>> print("Hello, World!)
  SyntaxError: EOL while scanning string literal
  ```
- Immediate feedback helps catch errors early.

---

### Slide 78: Exiting the REPL
**Content:**  
- Type `exit()` to leave the REPL.  
- Or press:  
  - **Ctrl + Z** on Windows  
  - **Ctrl + D** on Linux/macOS

---

### Slide 79: Why Use the REPL?
**Content:**  
- Great for beginners.  
- Allows experimentation and immediate feedback.  
- Like a "scratchpad" for testing ideas and learning syntax.

---

### Slide 80: Conclusion
**Content:**  
- The Python REPL is a powerful learning tool.  
- Use it to:  
  - Test simple commands and expressions.  
  - Practice with variables and functions.  
  - Debug code with instant results and error messages.

---


---

### Slide 81: Introduction to Programming 1
**Content:**
- In this section, we'll write our first Python program.
- Starting simple with the classic "Hello, World!" program.

---

### Slide 82: What is “Hello, World!”?
**Content:**
- "Hello, World!" is the first program beginners write.
- It prints "Hello, World!" to the screen.
- Introduces basic Python concepts:
  - Syntax
  - Running programs
  - Using output

---

### Slide 83: Writing the Program
**Content:**
- Open the Python REPL (Read-Eval-Print Loop).
- Type the following code:
  ```python
  >>> print("Hello, World!")
  ```
- Press Enter to see the output:
  ```
  Hello, World!
  ```

---

### Slide 84: Understanding the Code
**Content:**
- `print()` is a function that displays text.
- "Hello, World!" is a string enclosed in quotes.
- Parentheses `()` enclose the function's argument.
- Quotation marks define the string.

---

### Slide 85: Running the Program in a File
**Content:**
- Create a Python file named `hello_world.py`.
- Type the following code in the file:
  ```python
  print("Hello, World!")
  ```
- Save and close the file.

---

### Slide 86: Running the Python File
**Content:**
- Open your terminal or command line.
- Run the command:
  ```
  python3 hello_world.py
  ```
- See the output:
  ```
  Hello, World!
  ```

---

### Slide 87: What Just Happened?
**Content:**
- Python executed the code in `hello_world.py`.
- The `print()` function displayed the text.
- Basic flow:
  - Write code in a `.py` file.
  - Run it using `python3 filename.py`.
  - Python executes and prints the output.

---

### Slide 88: Next Steps
**Content:**
- Experiment with variations:
  ```python
  print("Welcome to Programming 1!")
  print(5 + 3)
  print("The answer is:", 5 + 3)
  ```
- Try different messages and simple math.

---

### Slide 89: Why is “Hello, World!” Important?
**Content:**
- It's about understanding the basics:
  - Writing code
  - Running programs
  - Seeing output
  - Using built-in functions like `print()`
- It's the first step toward mastering Python.

---

### Slide 90: Summary
**Content:**
- We wrote the "Hello, World!" program.
- Learned to use the REPL for testing code.
- Explored creating and running Python files.
- Started our journey in Python programming.

---


---

### Slide 91: Introduction to Python Interpreter and Script Mode
**Content:**
- Now, we’ll explore Python’s interpreter and script mode.
- Understand how Python code is executed and run effectively.

---

### Slide 92: Recap of Python REPL
**Content:**
- We’ve used the Python REPL for quick experiments.
- REPL is great for small pieces of code.
- As programs grow, we need a more organized approach.

---

### Slide 93: What is Python’s Interpreter?
**Content:**
- The Python interpreter reads, processes, and executes your code.
- It acts as a translator for your Python instructions.
- Here’s how it works:
  1. You type Python code.
  2. The interpreter reads the code, one line at a time.
  3. It executes the code immediately and shows the results.

---

### Slide 94: Using Python in Script Mode
**Content:**
- Script mode is ideal for writing more complex programs.
- Write your code in a .py file and run it with the interpreter.
- Typical workflow:
  1. Write code in a text file (e.g., my_program.py).
  2. Run the file using the command `python3 my_program.py`.

---

### Slide 95: How to Use Script Mode
**Content:**
- Create a Python file:
  - Open nano text editor.
  - Type code into a new file:
    ```python
    # my_program.py
    print("Hello, from script mode!")
    ```
  - Save and exit the editor.
- Run the Python file:
  - In the terminal, type:
    ```
    python3 my_program.py
    ```
  - Output: `Hello, from script mode!`

---

### Slide 96: Why Use Script Mode?
**Content:**
- Organizing Code: Better for larger programs.
- Reusability: Run and share your code easily.
- Debugging: Easier to edit, add comments, and structure your program.

---

### Slide 97: Differences Between REPL and Script Mode
**Content:**
- **REPL:**
  - Ideal for quick testing.
  - Executes code line-by-line.
  - Limited to short scripts and simple tests.
- **Script Mode:**
  - Ideal for complete programs.
  - Write code in a .py file and run it all at once.
  - Code can be organized into functions, classes, and modules.

---

### Slide 98: Running Python Files in Other Editors
**Content:**
- Many prefer using other text editors or IDEs:
  - Visual Studio Code
  - PyCharm
  - Sublime Text
- These tools support Python and can run scripts using the same command:
  ```
  python3 my_program.py
  ```

---

### Slide 99: Using Python Scripts with Arguments
**Content:**
- Modify your script to accept arguments:
  ```python
  import sys

  if len(sys.argv) > 1:
      print("Hello, " + sys.argv[1] + "!")
  else:
      print("Hello, World!")
  ```
- Run the program with an argument:
  ```
  python3 my_program.py Alice
  ```
- Output: `Hello, Alice!`

---

### Slide 100: Conclusion
**Content:**
- Today, we covered the basics of Python’s interpreter and script mode.
- You learned how to write and run Python programs using script mode.
- Script mode helps create organized, reusable, and maintainable code.
- This knowledge is crucial for your future learning.

---


---

### Slide 101: Introduction to Python Documentation
**Content:**  
- Now, we’ll explore how to find and read Python documentation.  
- Python’s documentation is a valuable resource for learning and troubleshooting.

---

### Slide 102: Why Python Documentation is Important
**Content:**  
- Documentation acts as a manual for understanding Python.  
- It helps you:  
  - Understand built-in features.  
  - Use libraries and modules effectively.  
  - Troubleshoot code issues.  
  - Gain deeper knowledge of Python’s syntax and structure.

---

### Slide 103: Python’s Official Documentation
**Content:**  
- Hosted on the Python website: https://docs.python.org/3/  
- Contains comprehensive information from basic syntax to advanced topics.  
- Key sections:  
  - Tutorial  
  - Library Reference  
  - Language Reference  
  - Python HOWTOs  
  - Index

---

### Slide 104: How to Search the Documentation
**Content:**  
- Use the search bar at the top to find specific functions or modules.  
- Example: Type "print()" to find its documentation.  
- Browse using the table of contents on the left side.  
  - Tutorials  
  - Standard library  
  - Language reference

---

### Slide 105: Practice Searching the Documentation
**Content:**  
- Example: Searching for "for loop"  
  - Type "for loop" in the search bar.  
  - Review the results for syntax, examples, and explanations.  
- This hands-on approach helps you become familiar with the documentation.

---

### Slide 106: Using the Documentation Effectively
**Content:**  
- Search for specific functions:  
  - Example: len(), sorted()  
- Read the examples provided.  
- Check the syntax and parameters.  
- Example: print() function’s sep parameter.

---

### Slide 107: Example: Looking Up a Built-in Function
**Content:**  
- Search for "len" in the search bar.  
- Description: Returns the number of items in an object.  
- Syntax: len(object)  
- Example code: len("hello") returns 5.  
- Exceptions: TypeError if the object has no length.

---

### Slide 108: Using the Help Function in Python
**Content:**  
- Access documentation directly from the Python interpreter.  
- Type help() and press Enter.  
- Example: help(len) or help(math)  
- This displays function or module documentation in the terminal.

---

### Slide 109: Third-Party Documentation
**Content:**  
- Many third-party libraries extend Python’s capabilities.  
- Examples: numpy, requests, matplotlib.  
- Find documentation on their official websites or platforms like Read the Docs.  
- Reading these is crucial for using these libraries correctly.

---

### Slide 110: Conclusion
**Content:**  
- We’ve covered how to use Python’s official documentation.  
- Whether you’re searching for built-in functions or third-party libraries, the documentation is your best resource.  
- Use it to learn, troubleshoot, and deepen your understanding of Python.

---


---

### Slide 111: Final Segment
**Content:**  
Welcome to the final segment of today’s lesson in Programming 1. We’ve covered a lot of ground so far, and now, we’re going to wrap up today’s class with a summary and Q&A session.  

---

### Slide 112: Quick Recap of What We Covered Today
**Content:**  
Today, we started with an introduction to the course. You learned about the overall structure of the lessons and what you can expect to achieve by the end of the course. Our main focus today was on the foundational concepts of Python programming and getting comfortable with the Linux environment.  

---

### Slide 113: Course Overview
**Content:**  
- We discussed how this course will guide you through Python programming from scratch, with the help of resources like ChatGPT and other language models.  
- We also emphasized the importance of self-learning and using tools like documentation and online resources to enhance your programming skills.  

---

### Slide 114: Introduction to Linux
**Content:**  
- We talked about the Linux operating system, specifically CentOS 7, and why it’s an essential part of modern software development.  
- We explored how to connect to a Linux server using Termius and understood the importance of command-line tools in Linux.  

---

### Slide 115: Remote File Management
**Content:**  
- You learned how to use SFTP for remote file management through Termius. This is important when you start working on projects that require accessing and editing files on a server.  

---

### Slide 116: Using Nano for Text Editing
**Content:**  
- We also introduced nano, a simple text editor, and demonstrated how to create and edit Python scripts on the server using nano.  

---

### Slide 117: Installing Python Locally
**Content:**  
- You saw how to install Python 3.7.10 on different operating systems like Windows, macOS, and Linux, setting up your local environment for Python development.  

---

### Slide 118: Understanding Python Basics
**Content:**  
- We discussed the basic concepts of Python, including its role as a programming language and how it compares to other languages.  
- You learned how to use the Python interactive shell (REPL) and how to run simple Python commands.  

---

### Slide 119: Writing Your First Python Program
**Content:**  
- Together, we wrote and ran the “Hello, World!” program. This small program is a crucial first step in any programming journey.  
- You learned the difference between using the Python interactive shell and running Python programs as .py files.  

---

### Slide 120: Getting Help with Python Documentation
**Content:**  
- We discussed how to use Python’s official documentation to look up functions, syntax, and examples, making it easier to find solutions as you write code.  

---



    
