# Linux and Command Line Basics

# Linux 与命令行基础

---

<br>

## Section 1: GUI vs. CLI and the Terminal / 第一章：图形界面、命令行与终端

Before we dive into Linux, it is important to understand how humans interact with computers. There are two primary interfaces:
在深入学习 Linux 之前，了解人类如何与计算机交互非常重要。主要有两种交互界面：

*   **GUI (Graphical User Interface / 图形用户界面)**: This is what you use every day on Windows or macOS. You interact with visual elements like windows, icons, and buttons using a mouse.
    **GUI（图形用户界面）**：这是你在 Windows 或 macOS 上每天使用的界面。你使用鼠标与窗口、图标和按钮等视觉元素进行交互。
*   **CLI (Command Line Interface / 命令行界面)**: An interface where you interact with the computer exclusively by typing text commands.
    **CLI（命令行界面）**：一种完全通过输入文本命令与计算机进行交互的界面。

### What is a Terminal? / 什么是终端？

A **terminal** is a text-based tool that lets you control a computer or server by typing commands instead of clicking icons. It is a typical example of a CLI. In professional software development and server management, the terminal is an indispensable tool.
**终端 (Terminal)** 是一种基于文本的工具，它允许你通过输入命令而不是点击图标来控制计算机或服务器。它是 CLI 的典型代表。在专业的软件开发和服务器管理中，终端是不可或缺的工具。

> **Q: What's your intuitive guess about the advantages and disadvantages of GUI and CLI?**
> **问：凭直觉猜测，GUI 和 CLI 的优缺点分别是什么？**
> 
> *   **GUI**: Easy to learn, highly visual, but can be slow and tedious for repetitive or complex work. (易于学习，直观，但对于重复性或复杂的工作来说可能很慢且繁琐。)
> *   **CLI**: Extremely fast, powerful, and easily automatable, but has a steep learning curve and is hard for beginners. (速度极快，功能强大且易于自动化，但学习曲线陡峭，对初学者有一定难度。)

---

<br>

## Section 2: Connecting to Remote Servers / 第二章：连接远程服务器

Most of the time, Linux runs on remote servers rather than your personal laptop. To control these servers, we use specific applications and protocols.
大多数情况下，Linux 运行在远程服务器上，而不是你的个人笔记本电脑上。为了控制这些服务器，我们使用特定的应用程序和协议。

### The Tool: Termius / 工具：Termius

**Termius** is a popular, cross-platform terminal application. It is the tool we use to connect to and manage Linux servers seamlessly.
**Termius** 是一款流行的跨平台终端应用程序。它是我们用来无缝连接和管理 Linux 服务器的工具。

To create a new host connection in Termius (or any SSH client), you need four essential elements:
要在 Termius（或任何 SSH 客户端）中创建新的主机连接，您需要四个核心要素：
1.  **IP Address (IP 地址)**: The network address of the server.
2.  **Port (端口)**: The specific channel for the connection (default for SSH is usually 22).
3.  **Username (用户名)**: Your account name on the server.
4.  **Password (密码)**: Your secret key to authenticate.

### Network Protocols: SSH and SFTP / 网络协议：SSH 与 SFTP

*   **SSH (Secure Shell)**: An encrypted network protocol used to securely access, manage, and transfer files between computers over unsecured networks. It ensures your commands and data cannot be intercepted easily.
    **SSH (安全外壳协议)**：一种加密的网络协议，用于在不安全的网络上安全地访问、管理计算机并在计算机之间传输文件。它确保您的命令和数据不会轻易被拦截。
*   **SFTP (SSH File Transfer Protocol / Secure File Transfer Protocol)**: A secure version of File Transfer Protocol that runs over SSH. Termius offers a built-in SFTP feature for easy visual file management (uploading and downloading).
    **SFTP (SSH 文件传输协议 / 安全文件传输协议)**：基于 SSH 运行的安全版本的文件传输协议。Termius 提供内置的 SFTP 功能，方便进行可视化的文件管理（上传和下载）。

---

<br>

## Section 3: Understanding File Systems and Paths / 第三章：理解文件系统与路径

> **Q: What are the two software components closest to users in a computer?**
> **问：在计算机中，最贴近用户的两个软件组件是什么？**
> 
> 1.  **File systems (文件系统)**: Where your data lives. (你的数据存放的地方。)
> 2.  **Application systems (应用系统)**: The programs you run. (你运行的程序。)

> **Q: What are the important things when controlling a computer?**
> **问：控制计算机时，最重要的是什么？**
> 
> *   **Position**: "where you are" (Location in the file system)
>     **位置**：“你在哪里”（在文件系统中的位置）
> *   **Intention**: "what you want to do" (The command you want to execute)
>     **意图**：“你想做什么”（你想执行的命令）

### Absolute vs. Relative Paths / 绝对路径与相对路径

To define your "Position" or locate a file, we use paths.
为了定义你的“位置”或定位一个文件，我们使用路径。

**1. Absolute Path (绝对路径)**
The full, complete path starting from the root directory to a specific file or folder. It works no matter where you currently are in the system.
从根目录开始到特定文件或文件夹的完整路径。无论你当前在系统中的哪个位置，它都有效。
*   *Linux*: `/home/zhangfeng/download/test.txt`
*   *Windows*: `D:\download\test.txt`

**2. Relative Path (相对路径)**
The path from your *current working directory* to a file or folder.
从你*当前工作目录*到文件或文件夹的路径。
*   *Linux*: `../download/test.txt` (`..` means one directory up)
*   *Windows*: `..\test.txt`

> **Q: Why do we need "relative paths"?**
> **问：为什么我们需要“相对路径”？**
> 
> *   They are **shorter and faster** to type than absolute paths. (它们比绝对路径更短，输入更快。)
> *   They are **portable**. If you move or copy a whole folder, relative links inside it still work. They make teamwork and navigation easier without relying on fixed root locations. (它们具有**可移植性**。如果移动或复制整个文件夹，其内部的相对链接仍然有效。它们使团队合作和导航变得更容易，而无需依赖固定的根目录位置。)

---

<br>

## Section 4: Essential Linux Commands / 第四章：Linux 基础命令

Now let's translate our "intentions" into actual Linux CLI commands.
现在让我们将“意图”转化为实际的 Linux CLI 命令。

### 1. Navigating and Viewing / 导航与查看

*   `pwd`: **P**rint **W**orking **D**irectory. Tells you your exact absolute path (where you are).
    **打印工作目录**。告诉你确切的绝对路径（你在哪里）。
*   `ls`: **L**i**s**t files and folders in the current directory.
    **列出**当前目录中的文件和文件夹。
*   `cd <path>`: **C**hange **D**irectories. Moves you to a new location.
    **切换目录**。将你移动到一个新位置。
    *   `cd ..`: Change to the parent directory (move up one level). / 切换到父目录（向上一级）。
    *   `cd ~`: Change to your user's home directory. / 切换到用户的主目录。

### 2. Creating and Viewing Files / 创建与查看文件

*   `mkdir <folder_name>`: **M**a**k**e **dir**ectory. Creates a new folder.
    **创建目录**。创建一个新文件夹。
*   `touch new_file.txt`: Creates a new, empty file named `new_file.txt`.
    创建一个名为 `new_file.txt` 的空文件。
*   `cat new_file.txt`: Con**cat**enate and print. Prints out *all* contents of the file to the terminal at once.
    打印。一次性将文件的**所有**内容打印到终端上。
*   `less new_file.txt`: Allows you to view the contents of a file page by page (useful for large files).
    分页查看文件内容（对于大文件非常有用）。

### 3. Modifying and Deleting / 修改与删除

*   `cp`: **C**o**p**y files or directories. / **复制**文件或目录。
    *   `cp original_file.txt copy_file.txt` (Copy a file / 复制文件)
    *   `cp -r original_folder copy_folder` (Copy a folder and all its contents **r**ecursively / **递归地**复制文件夹及其所有内容)
*   `mv`: **M**o**v**e files or directories. Also used to rename them! / **移动**文件或目录。也常用于重命名！
    *   `mv copy_file.txt move_file.txt` (Rename/Move a file / 重命名或移动文件)
    *   `mv copy_folder move_folder` (Rename/Move a folder / 重命名或移动文件夹)
*   `rm`: **R**e**m**ove files. / **删除**文件。
    *   `rm tmp.txt` (Remove a single file / 删除单个文件)
    *   `rm -r tmp_folder` (Remove a folder and all its contents recursively. *Use with caution!* / 递归删除文件夹及其所有内容。*谨慎使用！*)

> **Q: What differences do you feel between using Windows GUI and Linux CLI?**
> **问：在使用 Windows GUI 和 Linux CLI 之间，你感觉有什么不同？**
> *(Think about speed, visibility, and control! / 思考一下关于速度、可见性和控制力方面的差异！)*

---

<br>

## Section 5: Text Editing and Terminal Tips / 第五章：文本编辑与终端技巧

### Text Editing with `nano` / 使用 `nano` 编辑文本

While GUI systems have Notepad or Word, Linux terminals have text-based editors. **nano** is one of the most user-friendly terminal text editors.
虽然 GUI 系统有记事本 (Notepad) 或 Word，但 Linux 终端有基于文本的编辑器。**nano** 是对用户最友好的终端文本编辑器之一。

*   To open or create a file to edit: `nano filename.txt`
    打开或创建一个文件进行编辑：`nano filename.txt`
*   **Save your work**: Press `Ctrl + O` (Write Out), then press `Enter` to confirm the file name.
    **保存工作**：按 `Ctrl + O`，然后按 `Enter` 键确认文件名。
*   **Exit nano**: Press `Ctrl + X`.
    **退出 nano**：按 `Ctrl + X`。

### Terminal Superpowers (Tips) / 终端进阶技巧

Mastering these two features will make you much faster in the CLI:
掌握这两个功能会让你在 CLI 中的操作速度大幅提升：

1.  **The `Tab` Key (Auto-complete) / `Tab` 键（自动补全）**:
    If you type the first few letters of a file name or command and press the `Tab` key, Linux will automatically complete the rest for you. If there are multiple options, pressing `Tab` twice will list them.
    如果你输入文件名或命令的前几个字母，然后按下 `Tab` 键，Linux 会自动为你补全剩余部分。如果有多个选项，按两次 `Tab` 会列出所有可能。
2.  **The `history` Command / `history` 命令 (历史记录)**:
    Type `history` and press Enter to see a numbered list of all the commands you have run before. You can also press the **Up** and **Down** arrow keys on your keyboard to scroll through your previous commands.
    输入 `history` 并按回车键，可以查看你之前运行过的所有命令的编号列表。你也可以通过键盘上的**上**、**下**方向键来快速滚动查找之前的命令。
