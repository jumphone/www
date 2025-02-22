[home](https://www.bioinfo-lab.com)

# Data Analysis and Intro to ML

## Lesson 1


---

### Slide 1: Course Introduction
**Content:**  
- This course aims to teach you the basics of R programming.  
- In 13 sessions, you’ll be comfortable with R and ready to tackle data analysis and machine learning tasks.  
- No prior experience needed. Ideal for beginners.

---

### Slide 2: Why Learn R?
**Content:**  
- R is powerful for data manipulation, statistical analysis, and visualization.  
- Widely used in data science, bioinformatics, and research.  
- Learn from basic syntax to advanced topics like machine learning and RNA sequencing.

---

### Slide 3: Course Structure
**Content:**  
- Concepts introduced gradually to build your skills over time.  
- Use large language models like ChatGPT for learning and problem-solving.  
- Emphasis on practical application and continuous learning.

---

### Slide 4: Linux Environment
**Content:**  
- We’ll use a Linux-based server for our work.  
- Learn basic Linux commands and file management.  
- Linux is powerful, flexible, and secure, making it ideal for data analysis.

---

### Slide 5: First Session Overview
**Content:**  
- Introduction to Linux and logging into the CentOS 7 server.  
- Basic file management using the command line.  
- Installing R locally on your machine for practice.

---

### Slide 6: R as a Tool
**Content:**  
- R is a tool, not a language to memorize.  
- Extensive community and documentation available.  
- Interactive environment for immediate feedback and experimentation.

---

### Slide 7: Session Goals
**Content:**  
- Comfortably log into the server and manage files.  
- Install R on your personal computer.  
- Run basic commands in R’s interactive environment.

---

### Slide 8: Terminal Skills
**Content:**  
- Learn essential terminal skills for text editing and file management.  
- These skills are crucial for any programming or data project.  
- Practice using the command line for various tasks.

---

### Slide 9: Self-Learning Importance
**Content:**  
- Programming improves with practice and persistence.  
- Experiment, make mistakes, and learn from them.  
- Use large language models for troubleshooting and additional resources.

---

### Slide 10: Course Summary
**Content:**  
- By the end of this course, you’ll be proficient in R programming.  
- You’ll understand how to use Linux and the command line.  
- You’ll have the skills to tackle real-world data analysis and machine learning tasks.

---


---

### Slide 11: Introduction to Linux
**Content:**  
Let’s start with the Linux operating system, a cornerstone of this course. You’ll discover what Linux is and why it’s crucial in data analysis, machine learning, and scientific research. We’ll also overview CentOS 7, the Linux version we’ll use on our server.

---

### Slide 12: Linux: The Open-Source Advantage
**Content:**  
Linux is an open-source OS, free to use, modify, and share. Known for stability, security, and flexibility, it’s preferred for servers and high-performance computing. Almost all the world’s most powerful supercomputers run on Linux due to its superior performance, scalability, and customization.

---

### Slide 13: Why Linux Over Windows or macOS?
**Content:**  
For data analysis and machine learning, Linux offers key advantages. Most tools and libraries, like R and machine learning frameworks, are optimized for Linux. It’s lightweight and efficient, ideal for complex computations, and its commands are tailored for data scientists and researchers.

---

### Slide 14: CentOS 7: Our Linux Distribution
**Content:**  
CentOS, short for Community ENTerprise Operating System, is a popular Linux distribution based on Red Hat Enterprise Linux. It provides a stable, reliable environment, especially for servers, and is widely used in academic and research institutions due to its cost-effectiveness.

---

### Slide 15: Interacting with Linux via the Command Line
**Content:**  
To work with Linux, you’ll often use the terminal or command-line interface (CLI). Unlike a GUI, the terminal lets you interact with the system by typing commands. This method is powerful and efficient for tasks like managing files, running programs, and setting up environments.

---

### Slide 16: Essential Linux Commands
**Content:**  
As part of this course, you’ll learn basic Linux commands like `ls` to list files, `cd` to change directories, and `cp` to copy files. These commands form the foundation for your interactions with the Linux system and will become essential tools in your work.

---

### Slide 17: Understanding the Linux File System
**Content:**  
Linux organizes everything into a hierarchical structure with the root directory (/) at the top. Key directories include `/home` for user files, `/etc` for configuration files, and `/usr` for software and libraries. Navigating this structure using the terminal is crucial for managing files and running programs.

---

### Slide 18: User Permissions in Linux
**Content:**  
Linux is built with security in mind. Each file or directory has permissions that dictate who can read, write, or execute it. You’ll learn commands like `chmod` and `chown` to manage these permissions, which are essential for tasks like editing documents or executing scripts.

---

### Slide 19: Remote Access with Termius
**Content:**  
Since we’ll be working with a server, you’ll need to know how to connect remotely. Termius is a terminal emulator that allows you to connect to your CentOS 7 server from your local machine. This tool gives you access to the system as if you were sitting in front of it.

---

### Slide 20: Secure File Transfer with SFTP
**Content:**  
To manage files on the server, you’ll use SFTP (Secure File Transfer Protocol). SFTP lets you transfer files between your local computer and the server securely. During the course, you’ll learn how to use SFTP through Termius to move files seamlessly.

---


---

### Slide 21: Logging into CentOS 7 Server
**Content:**  
- Today, we will learn how to log into a CentOS 7 server using the terminal.  
- This skill is crucial for this course as we will be using the server extensively.  
- We will use Termius, a tool that allows secure remote access to the server.

---

### Slide 22: Understanding the Terminal
**Content:**  
- The terminal is a text-based interface for interacting with your system.  
- Unlike graphical interfaces, it requires typing commands.  
- It is powerful and efficient for managing servers and large data systems.

---

### Slide 23: Using SSH with Termius
**Content:**  
- SSH (Secure Shell) enables secure connections to remote servers.  
- Termius uses SSH to connect to the CentOS 7 server.  
- It provides a user-friendly interface for managing connections.

---

### Slide 24: Installing Termius
**Content:**  
- Download Termius from its website.  
- Install it on your local machine (Windows, macOS, Linux).  
- Open the application after installation.

---

### Slide 25: Creating a New Connection
**Content:**  
- Click “New Host” in Termius.  
- Enter the server’s IP address and your login credentials.  
- Save the connection settings.

---

### Slide 26: Connecting to the Server
**Content:**  
- Double-click the saved server connection.  
- Termius will connect to the server using SSH.  
- You will see a command prompt ready for input.

---

### Slide 27: Basic Terminal Commands
**Content:**  
- **pwd**: Shows your current directory.  
- **ls**: Lists the contents of the current directory.  
- **cd**: Changes to a different directory.

---

### Slide 28: More Basic Commands
**Content:**  
- **mkdir**: Creates a new directory.  
- **rm**: Deletes a file.  
- **touch**: Creates a new empty file.

---

### Slide 29: Using nano Text Editor
**Content:**  
- **nano**: Opens a text editor within the terminal.  
- Use it to create and edit text files.  
- Example: `$ nano myfile.txt`

---

### Slide 30: Logging Out
**Content:**  
- When done, type `exit` to log out.  
- Termius will disconnect you from the server.  
- Proper logout ensures security and resource management.

---


---

### Slide 31: Introduction to Remote File Management
**Content:**  
In this session, we’ll explore remote file management using SFTP within Termius to manage files on a CentOS 7 server. Efficient file management is crucial for storing and organizing data, scripts, and outputs.

---

### Slide 32: What is SFTP?
**Content:**  
SFTP, or Secure File Transfer Protocol, is a secure version of FTP. It encrypts both commands and data, ensuring secure file transfers over a network. Unlike FTP, SFTP keeps your information protected.

---

### Slide 33: Why Use SFTP?
**Content:**  
SFTP simplifies file management between your local machine and remote servers. It allows you to securely upload, download, and manage files, making it essential for tasks like transferring R scripts and managing program outputs.

---

### Slide 34: Setting Up Termius
**Content:**  
1. Open Termius on your local machine.  
2. Create a connection to your CentOS 7 server by entering the server’s IP address and your login credentials.  
3. Click on the server connection to log in and open a terminal window.

---

### Slide 35: Entering SFTP Mode
**Content:**  
To start managing files using SFTP in Termius:  
- Type `sftp username@hostname` (replace `username` and `hostname` with your details).  
- You’ll see an SFTP prompt (`sftp>`), indicating you’re connected securely.

---

### Slide 36: Basic SFTP Commands
**Content:**  
- **Listing Files:** Use `ls` to display files and directories in the current directory.  
- **Navigating Directories:** Use `cd` to change directories (e.g., `cd projects`). Confirm your location with `pwd`.

---

### Slide 37: Downloading and Uploading Files
**Content:**  
- **Downloading Files:** Use `get filename` to download files from the server (e.g., `get data.csv`). Specify a local path if needed.  
- **Uploading Files:** Use `put filename` to upload files to the server (e.g., `put script.R`).

---

### Slide 38: Managing Files
**Content:**  
- **Deleting Files:** Use `rm filename` to remove files. Be cautious, as this action is permanent.  
- **Deleting Directories:** Use `rmdir directoryname` to remove empty directories.

---

### Slide 39: Exiting SFTP Mode
**Content:**  
When you’re done, type `exit` to leave SFTP mode and return to the normal terminal window in Termius. Continue running commands or disconnect from the server as needed.

---

### Slide 40: Benefits and Future Use
**Content:**  
SFTP provides a secure and efficient way to manage files remotely, essential for sensitive data and remote work. As you progress, file management will become even more critical. Tools like SFTP will help you stay organized across different systems.

---


---

### Slide 41: Introduction to Nano Text Editor
**Content:**  
- Nano is a command-line text editor used for creating, editing, and saving text files directly within the terminal.  
- It is simple, easy to use, and highly effective for tasks like writing scripts or editing configuration files, especially on server environments like CentOS 7.

---

### Slide 42: Command Line Interface (CLI)
**Content:**  
- Many tasks in Linux systems are done through the CLI.  
- Nano is commonly used because it is lightweight, doesn’t require a graphical user interface, and can be easily accessed from within the terminal.

---

### Slide 43: Opening Nano and Creating a New File
**Content:**  
- To start using nano, open a terminal window and type:  
  `nano filename.txt`  
- If the file doesn’t exist, nano will create a new one. If it exists, nano will open it for editing.

---

### Slide 44: Navigating and Editing in Nano
**Content:**  
- Arrow Keys: Move the cursor within the file.  
- Backspace: Delete characters to the left of the cursor.  
- Delete: Remove characters to the right of the cursor.  
- Ctrl + K: Cut the current line.  
- Ctrl + U: Paste the text back.  
- Ctrl + W: Find a specific word or section of text.  
- Ctrl + C: Cancel the current action.

---

### Slide 45: Saving and Exiting Nano
**Content:**  
- To save your file, press Ctrl + O, confirm the file name, and press Enter.  
- To exit nano, press Ctrl + X. If you haven’t saved your changes, nano will prompt you to save before exiting.

---

### Slide 46: Opening and Editing an Existing File
**Content:**  
- To open an existing file, type:  
  `nano existing_file.txt`  
- Make changes as needed and save using the same steps.

---

### Slide 47: Common Uses of Nano in this Course
**Content:**  
- Writing R scripts with a .R extension.  
- Creating text files for data storage.  
- Editing configuration files for the server.  
- Running R scripts in the R console.

---

### Slide 48: Additional Nano Tips
**Content:**  
- Undo: Use Ctrl + Z to undo the last operation.  
- Copy and Paste: Use Ctrl + ^ to set a starting point, move the cursor, and press Ctrl + K to cut, then Ctrl + U to paste.  
- Help Menu: Press Ctrl + G to bring up the help menu.

---

### Slide 49: Why Nano?
**Content:**  
- Nano is lightweight and doesn’t require a graphical interface.  
- It is perfect for remote servers and easy to learn and use in a terminal environment.  
- Nano will be a valuable tool for your R scripts and beyond.

---

### Slide 50: Conclusion
**Content:**  
- Nano is a powerful tool for editing text files on Linux systems.  
- It is essential for tasks in this course, including writing and editing scripts and configuration files.  
- Familiarize yourself with nano to enhance your efficiency in a server environment.

---


---

### Slide 51: Introduction to R Installation
**Content:**  
In this section, we will guide you through the installation of R 4.2.0 on your local machine. R is essential for data analysis and machine learning in this course. Proper setup is crucial for your learning experience.

---

### Slide 52: Installing R on Windows - Step 1
**Content:**  
1. **Download the R Installer:**  
   - Open your web browser and go to the official CRAN website: https://cran.r-project.org/.  
   - Click “Download R for Windows,” then “base,” and download the installer for R 4.2.0.

---

### Slide 53: Installing R on Windows - Step 2
**Content:**  
2. **Run the Installer:**  
   - Locate the downloaded installer in your Downloads folder and double-click it.  
   - Follow the prompts, using default settings. The default installation path is C:\Program Files\R\R-4.2.0.

---

### Slide 54: Installing R on Windows - Step 3
**Content:**  
3. **Verifying the Installation:**  
   - After installation, search for “R” in the Start menu.  
   - Open “R x64 4.2.0” to verify the installation.

---

### Slide 55: Installing R on Windows - Optional Step
**Content:**  
4. **Optional Step: Installing RStudio:**  
   - Go to https://posit.co/download/rstudio-desktop/ and download the free version for Windows.  
   - Run the installer and follow the prompts. RStudio will detect your R installation.

---

### Slide 56: Installing R on macOS - Step 1
**Content:**  
1. **Download the R Installer:**  
   - Open Safari or your preferred browser and go to https://cran.r-project.org/.  
   - Click “Download R for macOS” and download the R-4.2.0.pkg installer.

---

### Slide 57: Installing R on macOS - Step 2
**Content:**  
2. **Run the Installer:**  
   - Open the downloaded .pkg file.  
   - Follow the prompts, accepting the default settings to install R in the /Applications folder.

---

### Slide 58: Installing R on macOS - Step 3
**Content:**  
3. **Verifying the Installation:**  
   - Open the Applications folder and double-click the R icon.  
   - Alternatively, open Terminal and type `R` to start the R console.

---

### Slide 59: Installing R on macOS - Optional Step
**Content:**  
4. **Optional Step: Installing RStudio:**  
   - Download the macOS version of RStudio from https://posit.co/download/rstudio-desktop/.  
   - Open the .dmg file and drag the RStudio icon into your Applications folder.

---

### Slide 60: Verifying and Updating R
**Content:**  
- **Verifying Installation:** Open the terminal or RStudio and type `R`. Run `print("Hello, R!")` to test.  
- **Updating R:** On Windows and macOS, download the latest version from the R website. On Linux, use `sudo yum update R`.

---


---

### Slide 61: Introduction to R
**Content:**  
- R is a powerful, open-source language for data analysis, statistics, and machine learning.  
- It is widely used in data science, academic research, and various industries.  
- R’s flexibility and ease of use make it an excellent choice for beginners.

---

### Slide 62: Why Use R?
**Content:**  
- Strong support for statistics and data visualization.  
- Designed for statisticians and data scientists.  
- Extensive ecosystem with thousands of packages for various tasks.

---

### Slide 63: R Environment
**Content:**  
- The R console is an interactive environment where you can type and execute commands.  
- Useful for running simple commands and testing code snippets.  
- For more complex analysis, R scripts (text files with a .R extension) can be written and executed.

---

### Slide 64: R Data Types and Objects
**Content:**  
- R is object-oriented: everything is an object.  
- Basic data types include numeric, character, logical, integer, and complex.  
- More complex structures include vectors, lists, data frames, and matrices.

---

### Slide 65: Assigning Values in R
**Content:**  
- Use the assignment operator <- to assign values to variables.  
- Example: `x <- 10` assigns the value 10 to the variable x.  
- Variables can be used in subsequent calculations or commands.

---

### Slide 66: Basic Arithmetic and Operations
**Content:**  
- R supports basic arithmetic operations: +, -, *, /, and ^.  
- Example: `2^3` returns 8.  
- Functions for advanced operations: `sqrt(16)` returns 4.

---

### Slide 67: R Functions and Syntax
**Content:**  
- Functions perform specific tasks and are essential in R.  
- Example: `sum(1, 2, 3)` returns 6.  
- Syntax: `function_name(argument1, argument2, ...)`

---

### Slide 68: Vectors in R
**Content:**  
- Vectors are collections of values of the same type.  
- Create vectors using the `c()` function: `my_vector <- c(1, 2, 3, 4, 5)`.  
- Access elements using square brackets: `my_vector[1]` returns 1.

---

### Slide 69: Summary of Key Points
**Content:**  
- R is powerful for statistical computing and data analysis.  
- It is object-oriented and supports basic arithmetic and functions.  
- Functions work with data structures like vectors, matrices, and data frames.  
- The interactive R console is great for learning and experimenting.

---

### Slide 70: Next Steps
**Content:**  
- Continue exploring R’s capabilities.  
- Practice using R for data manipulation and visualization.  
- Utilize R’s extensive package ecosystem to expand your skills.

---


---

### Slide 71: Introduction to the R REPL
**Content:**  
The R REPL (Read-Eval-Print Loop) is a core component of R, allowing direct interaction with the language. It's essential for beginners, offering an interactive, hands-on experience where you can experiment and get immediate feedback.

---

### Slide 72: Starting the R Interactive Session
**Content:**  
To start using R interactively, launch R from your terminal or command prompt.  
- **Windows:** Open Start menu, search for R, or use RStudio.  
- **macOS:** Open terminal and type `R`, or use RStudio.  
- **Linux:** Open terminal and type `R`.

---

### Slide 73: The R REPL Interface
**Content:**  
Once you type `R` and press Enter, you enter the R REPL. It looks like this:  
```
R version 4.2.0 (2022-04-22) -- "Innocent and Trusting"
Copyright (C) 2022 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

Type 'demo()' for some demos, 'help()' for on-line help, or 'q()' to quit.

>
```
The `>` symbol is the R prompt, indicating R is waiting for your input.

---

### Slide 74: Running Simple Commands
**Content:**  
Perform basic arithmetic calculations in the REPL:  
- Addition: `> 5 + 3`  
  Output: `[1] 8`  
- Multiplication: `> 4 * 7`  
  Output: `[1] 28`  
- Exponentiation: `> 2^3`  
  Output: `[1] 8`

---

### Slide 75: Using Variables in R
**Content:**  
Assign values to variables using the assignment operator `<-`:  
- Assign value: `> x <- 10`  
  Output: `[1] 10`  
- Perform calculations: `> y <- 5`  
  `> result <- x + y`  
  `> result`  
  Output: `[1] 15`

---

### Slide 76: Functions in the REPL
**Content:**  
Use built-in functions interactively:  
- Square root: `> sqrt(16)`  
  Output: `[1] 4`  
- Combine functions: `> sqrt(x^2 + y^2)`  
  Output: `[1] 11.18034`

---

### Slide 77: Working with Data
**Content:**  
Create and manipulate data structures like vectors:  
- Create vector: `> my_vector <- c(1, 2, 3, 4, 5)`  
  Output: `[1] 1 2 3 4 5`  
- Access elements: `> my_vector[3]`  
  Output: `[1] 3`

---

### Slide 78: Help and Documentation
**Content:**  
Access help for functions using `?` or `help()`:  
- Example: `> ?sqrt` or `> help(sqrt)`  
  Displays documentation explaining the function, usage, and arguments.

---

### Slide 79: Exiting the R REPL
**Content:**  
Exit the REPL by typing `> q()`. R will ask if you want to save your workspace image. Choose to save or not based on your preference.

---

### Slide 80: Summary
**Content:**  
The R interactive command line is a powerful tool for learning and experimenting with R code. It allows you to:  
- Run commands and see results immediately.  
- Assign values to variables for later use.  
- Use functions to perform calculations and manipulate data.  
- Work with different types of data, including vectors and data frames.  
- Access documentation for functions when needed.

---


---

### Slide 81: Introduction to R Programming
**Content:**  
- Today, we start our journey with R by writing and running your first program: Hello, World!  
- This simple program is the foundation for mastering R programming.

---

### Slide 82: Setting Up Your R Environment
**Content:**  
- Open your R environment:  
  - Use the interactive R terminal by typing `R` in your terminal or command line interface.  
  - Alternatively, open the R application on your local machine.  
- You will work within an interactive shell where you can type commands and get immediate feedback.

---

### Slide 83: Writing Your First R Command
**Content:**  
- The first line of code you will write is:  
  ```R
  print("Hello, World!")
  ```  
- This command uses the `print()` function to display the string "Hello, World!" on the screen.

---

### Slide 84: Understanding the Code
**Content:**  
- `print()` is a basic function in R that outputs whatever is inside the parentheses.  
- "Hello, World!" is a string—a sequence of characters surrounded by quotation marks.  
- When you run this command, you should see the output:  
  ```
  [1] "Hello, World!"
  ```  
- The `[1]` indicates the first element in the output.

---

### Slide 85: The Significance of Hello, World!
**Content:**  
- Running Hello, World! confirms that your R environment is set up correctly.  
- It demonstrates the importance of functions and syntax in programming.  
- This simple program sets the foundation for more complex tasks in data analysis and machine learning.

---

### Slide 86: Saving Your Script
**Content:**  
- Open a text editor like RStudio or any other text editor.  
- Type the command:  
  ```R
  print("Hello, World!")
  ```  
- Save the file as `hello_world.R` with the `.R` extension.

---

### Slide 87: Running Your Script
**Content:**  
- Go back to your R console and type:  
  ```R
  source("hello_world.R")
  ```  
- Hit Enter to run the script.  
- You should see the output:  
  ```
  [1] "Hello, World!"
  ```  
- This method allows you to save and run scripts for future use.

---

### Slide 88: Importance of Saving Scripts
**Content:**  
- Saving scripts helps organize your code, especially for larger projects.  
- It allows you to easily share your work with others or save it for later use.  
- This practice is crucial as you progress in your R programming journey.

---

### Slide 89: Recap of Your First Program
**Content:**  
- You used the `print()` function to display a string.  
- You executed code interactively and learned to save it in a script.  
- These skills are essential for future lessons in data manipulation, statistical analysis, and machine learning.

---

### Slide 90: Looking Ahead
**Content:**  
- As you continue, you’ll explore more advanced functions, data structures, and machine learning algorithms.  
- The ability to write and execute code confidently will provide a solid foundation for tackling more complex tasks.  
- Stay curious and keep practicing!

---


---

### Slide 91: Introduction to Scripting in R
**Content:**  
- Transition from interactive to script mode  
- Importance of script files in real-world programming  
- Overview of R interpreter and script mode  

---

### Slide 92: What is an Interpreter?
**Content:**  
- Definition: A program that reads and executes code line by line  
- R interpreter in command-line interface  
- Interactive vs. Script mode  

---

### Slide 93: R Script Mode
**Content:**  
- Writing programs in script mode  
- .R files for organizing and saving code  
- Adding comments for clarity  

---

### Slide 94: Creating an R Script File
**Content:**  
- Using a text editor (e.g., nano)  
- Command: `nano my_script.R`  
- Writing and saving the script  

---

### Slide 95: Writing Your First Script
**Content:**  
- Example script:
  ```
  # This is a simple R script
  print("Hello, World!")
  x <- 10
  print(x)
  ```
- Explanation of each line  

---

### Slide 96: Saving and Exiting Nano
**Content:**  
- Saving the file in nano: Ctrl + O, Enter, Ctrl + X  
- Importance of saving and exiting correctly  

---

### Slide 97: Running the Script
**Content:**  
- Using the `source()` function  
- Command: `source("my_script.R")`  
- Expected output:
  ```
  [1] "Hello, World!"
  [1] 10
  ```  

---

### Slide 98: Why Use Script Mode?
**Content:**  
- Organized code for complex programs  
- Reusability and efficiency  
- Easier debugging and collaboration  

---

### Slide 99: Script Workflow
**Content:**  
1. Write the code in a script file  
2. Test parts interactively  
3. Run the full script with `source()`  
4. Iterate and improve  

---

### Slide 100: Conclusion
**Content:**  
- Recap of script mode benefits  
- Encouragement to practice writing and running scripts  
- Next steps in learning R programming  

---


---

### Slide 101: Importance of Documentation in R
**Content:**  
- As you advance in R, understanding documentation is crucial.  
- It helps with complex functions, libraries, and packages.  
- Documentation provides detailed explanations and examples.

---

### Slide 102: Accessing Documentation in the Console
**Content:**  
- Use the `help()` function to access documentation.  
- Example: `help(mean)` opens the help page for the `mean()` function.  
- Documentation includes function description, arguments, return value, and examples.

---

### Slide 103: Using the ? Shortcut
**Content:**  
- A quicker way to access documentation is using the `?` shortcut.  
- Example: `?mean` does the same as `help(mean)`.  
- This is especially useful for interactive work in the R console.

---

### Slide 104: Documentation for Specific Packages
**Content:**  
- Access documentation for functions in specific packages using the `package::` prefix.  
- Example: `?ggplot2::ggplot` for the `ggplot()` function in the `ggplot2` package.  
- Use `help(package = "ggplot2")` to get an index of all functions in the package.

---

### Slide 105: Getting Help with Errors
**Content:**  
- Understanding error messages is crucial.  
- Use the `traceback()` function to see the sequence of function calls leading to an error.  
- The `debug()` function helps step through a function to identify issues.

---

### Slide 106: Using vignette() for Package Documentation
**Content:**  
- Vignettes are long-form guides that provide detailed tutorials and examples.  
- Access a vignette using the `vignette()` function.  
- Example: `vignette("ggplot2")` for detailed documentation on ggplot2.

---

### Slide 107: Reading R Documentation Online
**Content:**  
- Official R documentation is available on the R project’s website.  
- Websites like Stack Overflow, R-bloggers, and RStudio Community offer additional resources.  
- These sites provide examples, code snippets, and real-world use cases.

---

### Slide 108: Searching for Functions and Topics with RSiteSearch()
**Content:**  
- Use `RSiteSearch()` to search for terms across R’s online documentation.  
- Example: `RSiteSearch("lm")` returns resources related to the `lm()` function.  
- This helps find specific use cases and solutions.

---

### Slide 109: Combining Documentation and Learning Resources
**Content:**  
- Documentation is a valuable learning tool, not just for troubleshooting.  
- Experiment with functions, read usage details, and find examples.  
- Regularly referring to documentation enhances your understanding and confidence in R.

---

### Slide 110: Active Use of Documentation
**Content:**  
- Actively using documentation helps you become more independent in R.  
- Develop an intuitive understanding of R by regularly referring to documentation.  
- This will help you analyze data, build models, and solve real-world problems effectively.

---


---

### Slide 111: Recap and Moving Forward
**Content:**  
In this final segment, we’ll recap today’s session and discuss how to apply what you’ve learned. You’ve covered logging into the server, using the R console, managing files in Linux, and writing basic R programs. Let’s consolidate this knowledge and see how it fits together.

---

### Slide 112: Key Takeaways
**Content:**  
Today’s lesson laid the foundation for data analysis and machine learning in R. You learned to access and use a Linux server, work with files remotely, and start writing R programs. Understanding documentation and online resources is crucial for your continued learning.

---

### Slide 113: Linux Environment
**Content:**  
Operating in the Linux environment is essential. You learned to use Termius to log in and interact with servers, a skill vital for real-world data analysis. This ability to run computations on remote machines is very useful for accessing powerful tools.

---

### Slide 114: R’s Interactive Environment
**Content:**  
You gained a basic understanding of R’s REPL, allowing you to experiment with code and see results instantly. Writing and running R scripts is key to developing more complex programs as you progress in the course.

---

### Slide 115: R Documentation
**Content:**  
R’s documentation system is a valuable resource. Learning to read help files and vignettes will accelerate your transition from beginner to intermediate user. Use the help() function or ? shortcut to quickly look up functions and their documentation.

---

### Slide 116: Practical Steps
**Content:**  
Practice logging into the server and navigating using the command line. Access different directories, create and edit files with nano, and run basic R code. Familiarity with these environments will make complex tasks easier later.

---

### Slide 117: Using AI Models for Learning
**Content:**  
AI models like ChatGPT can assist in explaining confusing concepts, providing additional examples, and understanding error messages. They can also suggest useful resources for deeper learning.

---

### Slide 118: Embracing Practice
**Content:**  
Programming improves with practice. Experiment with writing short R scripts, working with variables, and performing basic arithmetic. The more time you spend in the R environment, the more confident you will become.

---

### Slide 119: The Next Steps
**Content:**  
Future lessons will delve deeper into R, covering functions, loops, conditional statements, data manipulation, and visualization. These skills are foundational for data analysis and machine learning. Continue practicing and reviewing material after each class.

---

### Slide 120: Conclusion
**Content:**  
Today’s session focused on building a strong foundation. By mastering the Linux server, R environment, and documentation, you’re set for success in the course. These initial skills will support your journey through advanced topics in data analysis and machine learning.

---

