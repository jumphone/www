
[EN](https://www.bioinfo-lab.com/courses/python_2609/preview.md#en)
[CN](https://www.bioinfo-lab.com/courses/python_2609/preview.md#cn)

# EN

# PR1 Course Preview: What Kind of Programming Foundation This Course Builds for You

If this is your first time learning to program, you have probably wondered more than once as you go through the syllabus: why does an “introductory programming” course not start with writing Python, but with Linux, the terminal, and SSH remote servers? Why use the seemingly “primitive” nano instead of a polished graphical editor? Why cover functions, lists, and dictionaries at such length, yet never mention classes or object-oriented programming?

These are perfectly reasonable questions. If you look up Python tutorials online, most of them open with “install PyCharm, click the run button, and print Hello World.” PR1 takes a different path — one that may feel slower at first, but lays a far more solid foundation. It does not rush you into building a flashy little game. Instead, it wants to first help you truly understand *where* your code runs, *where* your files live, and *what* error messages actually mean.

We are fully aware that PR1 is not the end of your programming journey. It is only the first step in a full sequence. PR2 will follow, introducing you to local IDEs, object-oriented programming, and more powerful tools like NumPy, pandas, and Pygame. The entire purpose of PR1 is to make sure that by the time you reach PR2, you stand on firm ground — that you will not stumble your way through because of shaky fundamentals about environments, file paths, or basic concepts.

---

## Why We Start with Linux and the Terminal

One of the biggest misconceptions beginners have is that “programming = writing code in an editor.” Many students write code smoothly on their local IDE, yet the moment they face a real working environment — running scripts on a lab server, troubleshooting file path errors, debugging on a headless machine — they feel completely lost.

That is why PR1 opens with Linux.

In the real world today, the vast majority of servers, research computing platforms, and industrial control systems run on Linux. Whether you go into bioinformatics, data analysis, or backend development, your code will almost always end up running on a remote Linux machine. If you only learn to program by clicking buttons on your local computer, you will not even know where you are, where your files are, or how to run a script once you log into a real server.

So the first step in this course is to teach you to connect to a remote server with Termius and get to know the file system through the command line. You will learn what absolute and relative paths are; how `pwd` tells you your current location, how `ls` shows you what is around you, how `cd` moves you around, and how `mkdir` and `touch` create folders and files. These commands may look plain, but they are the universal language you will use to work with any server in the future.

You might ask: can’t all of this be done with buttons in an IDE later? Yes, much of it can. But if you never navigate paths manually in the terminal, you will never truly understand what “current working directory” actually means. And without that understanding, you will waste countless hours later on “module not found” and “file not found” errors.

PR1 does not want you to become an “IDE button-pusher” who only knows how to click run. It wants you to see the operating system underneath your code — to see how files are stored, how scripts are executed, and how data flows. That layer of understanding is better built early than late.

---

## Why We Stick to nano in PR1, and Save Local IDEs for PR2

You may already have heard that PR2 will formally teach local IDEs like VS Code, along with breakpoints, syntax highlighting, and auto-completion — all very useful features. So why not start with IDEs right away in PR1?

The answer is simple: the more powerful a tool is, the more it can hide the underlying logic from you.

If you open VS Code on day one, it will automatically select your interpreter, complete your code for you, flag errors with red squiggles, and even offer one-click fixes. It feels very convenient — but you may also never figure out which rules belong to the Python language itself, and which things the IDE is doing for you behind the scenes. Take the IDE away, and you feel like you have lost your crutches.

PR1 deliberately starts with nano, the simplest terminal editor, and takes those crutches away on purpose.

In nano, there is no auto-completion and no on-the-fly error checking. You have to type every command correctly, remember the 4-space indentation rule, and work through errors line by line by reading the traceback. The process may feel slow at first, even a little clumsy, but it forces you to focus on the code itself — on syntax, on logic, on reading error messages.

More importantly, when you pick up IDEs again in PR2, they will no longer feel like magic. You will understand that auto-completion just saves you typing time, and that breakpoint debugging is just a more efficient version of print debugging. None of them change the fundamental fact that code runs on top of an operating system. You will be in control of your tools, not dependent on them.

Think of it as learning to drive on a manual transmission first. It is not because manual cars are nicer to drive, but because they teach you how the clutch, gears, and throttle actually work. Once you understand the mechanics, you can drive an automatic confidently and competently.

---

## Why Object-Oriented Programming Belongs in PR2, Not PR1

Many introductory courses throw `class`, `self`, and inheritance at students very early, as if you have not truly learned Python without OOP. PR1 does not do this. It leaves full object-oriented programming entirely for PR2.

This is not a shortcut. It is a deliberate choice that respects the cognitive load of absolute beginners.

Object-oriented programming is a highly abstract concept. To truly grasp what classes and instances are for, you first need to understand what functions are, how parameters are passed, and how return values work. You need experience storing data in dictionaries and processing it with functions. You need to feel first-hand the inconvenience of keeping data and operations separate — only then, when OOP arrives, will you see it as a solution to a real problem, instead of just another syntax template to memorize.

Look at the learning path in PR1:
- First you learn variables and data types, so you know how to store individual pieces of data.
- Then you learn lists, tuples, dictionaries, and sets, so you know how to store data in batches.
- Then you learn functions, so you know how to wrap repeated operations for reuse.
- Then you learn modules, so you know how to split code across files and organize it.

By the end of this arc, you can already write complete small scripts using “functions + data structures” — password generators, log analyzers, grade management systems, file backup utilities. And by then, you will naturally start to feel some pain points: for example, storing a student’s information in a dictionary gets messy when there are many fields; related functions scattered around are hard to manage.

When you enter PR2 with those pain points and learn object-oriented programming, everything falls into place. You will immediately see that a class is simply a box that packages “data and the functions that operate on that data” together; that `self` is just a reference to the instance itself; that inheritance exists not to show off, but to reuse code.

That is how programming should be learned: experience the problem first, then learn the solution. Not the other way around — dumping syntax on you first and saying “you’ll need this later.”

---

## How the Topics in PR1 Build on Each Other

If PR1 were building a house, it would not start by showing you the roof decorations. It would start with the foundation, then the walls, then the doors and windows.

The deepest foundation is the Linux environment and file system. This layer does not teach you Python — it teaches you *where code runs*. You will learn what a path is, what a file is, how to run a script in the terminal. This is the common-sense groundwork for all programming.

One layer up is basic Python syntax: variables, data types, operators, and strings. These are the “words and phrases” of programming. You will learn what numbers, strings, and booleans are, how to operate on them, how to concatenate them, and how to slice them. The course pays special attention to pitfalls that trip up beginners — floating-point precision, ASCII-based string comparison, the difference between dynamic and static typing. Many crash courses skip these details, but they determine whether you will write subtle bugs later.

Above that sits control flow: conditionals, loops, `break` and `continue`. This is the “logical skeleton” of programming. Using relatable examples — traffic lights, vending machines, number-guessing games, grade rating systems — the course shows you how programs make different decisions in different situations. Special emphasis is placed on avoiding infinite loops and writing termination conditions first. This is not nitpicking; it is the muscle memory of a professional programmer.

Higher still are functions and modules. This is where “modular thinking” enters. Using analogies like microwave presets and sandwich-making, the course helps you grasp the essence of functions: wrap a named block of code so you can call it again and again. From parameterless functions to parameterized ones, from return values to multiple return values, from scope to module imports, it step by step lifts your code from “flat sequence” to “layered organization.”

Then come the four core data structures: lists, tuples, dictionaries, and sets. These are your “storage toolbox.” The course does not just teach you APIs — it explains clearly what problem each structure solves: lists for ordered sequences, tuples for immutable data, dictionaries for key-value lookups, sets for deduplication and set operations. By the time you reach real-world examples like word frequency analysis and student information systems, you will feel firsthand how choosing the right data structure simplifies your code.

The top layer covers file operations, exception handling, and standard/third-party libraries. This is how programming connects to the real world. You will learn to read and write files, handle encoding issues, use try-except to make programs more robust, and install libraries written by others with pip. By this point, you can write genuinely useful small tools — not just toy code that only works in exercises.

If you trace the whole path, you will see that PR1 does not chase sheer quantity of topics. It chases solidity at every step. Everything earlier is the foundation for what comes later. No chapter stands alone.

---

## The Designs That “Feel Like Extra Work” Are Actually Careful Choices

Many students find weekly reports tedious at first: screenshot every step, put them in a PowerPoint, export to PDF, and submit. Why not just turn in the code?

Because the biggest enemy of learning to program is “having watched it all but retaining nothing.”

Many people watch video tutorials, feel they understand everything, then close the video and can do nothing. The reason is simple: you never walked through the full process yourself, and you left no record of your own work. The point of weekly reports is to force you to go through the entire chain — log into the server, create a file, write code, run it, check the output, fix errors — and leave evidence of every step.

Years from now you may forget the exact commands. But you will remember: I ran these scripts on a server with my own hands, and I know what the full workflow looks like. That hands-on intuition is worth more than any list of memorized facts.

Another small but important detail is the thought questions scattered throughout the material: “What are the pros and cons of GUI vs CLI?” “Why do we need relative paths?” “Why the 4-space indentation rule?”

There are no perfect answers to these questions, but they push you to think about *why things are designed this way*. Programming is not about memorizing instructions — it is about understanding the trade-offs behind design decisions. Once you work through those “why” questions, what you take away is not a scattered list of commands, but a whole way of thinking.

---

## How PR1 and PR2 Fit Together

By now, you can probably see how the two courses connect.

PR1 gives you the low-level understanding and the fundamentals:
- You know Linux and the command line, so when you learn remote IDE development in PR2, it clicks immediately.
- You understand file paths and working directories, so “module not found” and other environment issues will not stop you in PR2.
- You know functions, dictionaries, and data structures, so object-oriented programming will feel like a natural next step, not something out of nowhere.
- You can read error messages and debug with print statements, so breakpoint debugging in PR2 is just a more efficient tool, not a whole new world.
- You know pip and third-party libraries, so installing and importing NumPy, pandas, and Pygame will not be a hurdle at all.

PR2 gives you upgraded tools and expanded capabilities:
- A local IDE makes you faster at writing code and more effective at debugging.
- Object-oriented programming lets you organize larger codebases and build more complex projects.
- NumPy and pandas open the door to real data processing.
- Pygame lets you build complete small games and put everything you have learned to use.

Put simply: PR1 is for “building a strong stance,” PR2 is for “putting together combinations.”
A solid stance keeps your combinations from falling apart. You *could* skip PR1 and go straight to PR2, and you would still learn things and write code — but your foundation would be hollow. Hit any environment issue or edge case, and you would easily get stuck.

---

## A Few Words for Each of You

**If you are a student choosing this course:**
Please do not dismiss the Linux and command-line sections as “something I’ll never need because I’ll use an IDE later.” The time you spend working in the terminal now will pay you back many times over. Take every hands-on exercise seriously. Take your weekly reports seriously. Do not copy answers. In programming, there is no faking whether your hands know the work. This course will not turn you into an expert overnight, but it will help you avoid almost every pitfall that normally trips up beginners.

**If you are an instructor teaching this course:**
The value of this curriculum goes beyond its topic list. It conveys a teaching philosophy: systems first, language second; procedural programming first, object-oriented second. As you teach, look one step ahead — remind students that the path knowledge they learn today will reappear with IDEs later; that the dictionaries they learn today will meet classes again later. When students see that their current effort has clear future payoff, they stay more motivated.

**If you are a self-learner:**
You can absolutely use this material on your own. Go at your own pace. If you do not have access to a server yet, you can follow along with a local virtual machine or WSL. Do not rush to finish a chapter in one day. The key is to type every command and every line of code yourself, and see the output with your own eyes. When you hit an error, do not immediately search for the solution — try to read the error message first. The ability to read tracebacks is the single most important skill for a self-taught programmer. Once you work through PR1 thoroughly, moving on to OOP and libraries in PR2 will be much faster than if you had jumped ahead.

---

## In Closing

PR1 is not a “learn Python in seven days” course. It does not want to give you the illusion that you “already know how to code.”

What it wants to give you is something more reliable: the confidence of knowing where your code runs, where your files live, what error messages mean, and why every line is written the way it is. What you hold in your hands is not a handful of memorized templates — it is a foundation that can keep growing.

When you finish PR1 and step into PR2, you will not be starting from zero. You will be building a taller building on top of a foundation you have already poured solid.

It may not be the fastest path. But it is the steadiest one. And on the road of programming, steady almost always takes you farther than fast.

<br><br>


# CN

# PR1 课程前瞻：这门课，想给你打下什么样的编程底子
如果你是第一次接触编程，打开这份大纲的时候，大概率会有一个疑问：
为什么一门叫“编程入门”的课，一上来不先教写 Python，反而先讲 Linux、终端、SSH 远程服务器？为什么不用漂亮的图形化编辑器，反而要用看起来很“原始”的 nano？为什么讲了这么久的函数、列表、字典，却全程没提“类”和面向对象？

这些疑问非常正常。如果你去网上搜 Python 入门，大部分课程的第一页都是“安装 PyCharm，点运行按钮，打印 Hello World”。但 PR1 走的是另一条路——一条看起来慢一点、但地基更稳的路。它不急于让你立刻做出一个炫酷的小游戏，而是想先帮你把“代码到底跑在哪、文件到底存在哪、报错到底是什么意思”这件事讲透。

因为我们很清楚：PR1 不是编程学习的终点，它只是整个序列的第一站。后面还有 PR2，会带你走进本地 IDE、面向对象编程，还有 numpy、pandas、pygame 这些更有趣、更强大的工具。而 PR1 存在的全部意义，就是让你在进入 PR2 之前，脚下是实的，不会因为环境、路径、基础概念模糊而一路磕磕绊绊。

## 一、为什么第一课，我们先从 Linux 和终端讲起
很多人学编程的第一个误区，是把“编程”等同于“在编辑器里写代码”。他们会在本地 IDE 里写得很顺，可一旦碰到真实的工作场景——比如要把脚本传到实验室的服务器上运行，要处理文件路径报错，要在没有图形界面的机器上调试——立刻就手足无措。

这就是 PR1 开篇先讲 Linux 的原因。

今天的真实世界里，绝大多数服务器、科研计算平台、工业控制系统，跑的都是 Linux。你学生物信息、做数据分析、搞后端开发，最终代码几乎都要跑在远程 Linux 机器上。如果只学过本地点按钮的编程方式，你到了真实环境里会连“我在哪、文件在哪、怎么运行”都搞不清楚。

所以这门课的第一步，是教你用 Termius 连上一台远程服务器，用命令行认识文件系统：什么是绝对路径，什么是相对路径；`pwd` 告诉你在哪，`ls` 告诉你周围有什么，`cd` 带你移动，`mkdir` 和 `touch` 帮你创建文件和文件夹。这些命令看起来朴素，却是你未来和任何一台服务器打交道的通用语言。

你可能会问：这些东西以后用 IDE 不都能点按钮完成吗？是的，很多可以。但如果你没在命令行里亲手走过一遍路径，你永远不会真正理解“当前工作目录”是什么意思。而理解不了这件事，未来你会在“模块导入失败”“文件找不到”这类问题上，浪费无数个小时。

PR1 不想让你成为只会点运行按钮的“IDE 操作员”。它想让你先看见代码底下的操作系统——看见文件是怎么存放的，脚本是怎么被调用的，数据是怎么流动的。这层认知，早建立比晚建立好。

## 二、为什么 PR1 全程用 nano，不急着上本地 IDE
你可能已经听说了，PR2 会正式教本地 IDE，比如 VS Code，会教断点调试、语法高亮、自动补全这些非常好用的功能。那为什么 PR1 不直接从 IDE 开始呢？

答案很简单：工具越强大，越容易藏住底层逻辑。

如果你第一天就打开 VS Code，它会自动帮你选解释器，自动补全代码，出错了给你标红波浪线，甚至一键修复。你会觉得很方便，但你也很可能搞不清楚：到底哪部分是 Python 语言本身的规则，哪部分是 IDE 帮你做的。一旦换了一台没有 IDE 的机器，你就像被抽走了拐杖。

PR1 选择先用 nano 这种最朴素的终端编辑器，就是故意先把拐杖拿走。

在 nano 里，没有自动补全，没有语法纠错，你必须老老实实地敲对每一个命令，记住缩进是 4 个空格，自己对着报错信息一行一行找问题。这个过程刚开始会有点慢，甚至有点笨拙，但它会逼你把注意力放回代码本身——放回语法、放回逻辑、放回错误信息的阅读上。

更重要的是，当你在 PR2 重新拿起 IDE 这把“利器”的时候，你不会再觉得它是魔法。你会明白：自动补全只是帮你省时间，断点调试只是比 print 调试更高效，它们本质上都没有改变“代码运行在操作系统上”这件事。你是在驾驭工具，而不是依赖工具。

这就像学车先学手动挡，不是因为手动挡更好开，而是因为它能让你明白变速箱、离合、油门之间到底是什么关系。等你理解了底层逻辑，再开自动挡，你开得明白，也开得稳。

## 三、为什么面向对象（OOP）要放到 PR2，PR1 只讲过程式
很多入门课会早早地把 `class`、`self`、继承塞给学生，好像不讲面向对象就不算学过 Python。但 PR1 没有这么做。它把完整的面向对象编程，全部留给了 PR2。

这不是偷懒，这是对零基础学习者认知负荷的尊重。

面向对象是一个抽象度非常高的概念。要真正理解“类”和“实例”的意义，你得先明白函数是什么、参数怎么传、返回值怎么用；得先有用字典存数据、用函数处理数据的经历；得亲身体验过“数据和操作分开写”带来的麻烦——只有这样，当 OOP 出现的时候，你才会明白它是用来解决什么问题的，而不是死记硬背语法模板。

你可以回想一下 PR1 的知识路径：
先学变量和数据类型，知道怎么存单个数据；
再学列表、元组、字典、集合，知道怎么成批地存数据；
再学函数，知道怎么把重复的操作打包起来重复用；
再学模块，知道怎么把代码拆分到不同文件里组织管理。

走完这一圈，你已经能用“函数 + 数据结构”写出完整的小脚本了——比如密码生成器、日志统计、学生成绩管理、文件备份工具。这时候你也自然会碰到一些痛点：比如用字典存一个学生的信息，字段多了容易写错；相关的函数散落在各处，管理起来很乱。

带着这些痛点进入 PR2，再去学面向对象，一切就顺理成章了。你会一眼看懂：原来类就是把“数据和操作数据的函数”打包在一起的盒子；原来 `self` 就是实例自己的引用；原来继承不是为了炫技，是为了复用代码。

这才是学习编程该有的节奏：先体验问题，再学习解法。而不是反过来，先塞给你一堆语法，却告诉你“以后会用到的”。

## 四、PR1 的知识点，是怎么一步步串起来的
如果把 PR1 比作盖房子，它不是先给你看屋顶的装饰，而是从打地基、砌墙、装门窗一步步来的。

最底层的地基，是 Linux 环境与文件系统。这一层教你的不是 Python，而是“代码运行的地方”。你会明白什么是路径，什么是文件，怎么在终端里运行一个脚本。这是所有编程的底层常识。

往上一层，是 Python 基础语法：变量、数据类型、运算符、字符串。这是编程的“单词和词组”。你会知道数字、字符串、布尔值分别是什么，怎么运算，怎么拼接，怎么切片。这里课程特别强调了一些新手最容易踩的坑——比如浮点数精度问题，比如字符串比较的 ASCII 规则，比如动态类型和静态类型的区别。这些细节很多速成课会跳过，但它们决定了你以后会不会写出隐蔽的 bug。

再往上，是控制流：条件判断、循环、break 和 continue。这是编程的“逻辑骨架”。从交通灯到自动售货机，从猜数字游戏到成绩评级，课程用一个个生活化的例子，让你明白“程序是怎么根据不同情况做不同事的”。这里尤其强调了避免死循环、先写终止条件的习惯——这不是小题大做，是职业程序员的肌肉记忆。

再往上，是函数与模块。这是编程的“模块化思维”。课程用微波炉预设按钮、三明治制作这样的比喻，让你理解函数的本质：把一段有名字的代码包起来，重复调用。从无参函数到带参函数，从返回值到多返回值，从作用域到模块导入，一步一步把代码从“平铺直叙”变成“分层组织”。

再往上，是四大数据结构：列表、元组、字典、集合。这是编程的“收纳工具箱”。课程不只是教你 API，而是讲清楚每种结构适合解决什么问题：列表适合有序队列，元组适合不可变的数据，字典适合键值查找，集合适合去重和集合运算。到了词频统计、学生系统这些实战例子里，你会真实感受到选对数据结构，代码能简洁多少。

最上面一层，是文件操作、异常处理、标准库与第三方库。这是编程和真实世界对接的接口。你会学会怎么读写文件，怎么处理编码问题，怎么用 try-except 让程序不轻易崩溃，怎么用 pip 安装别人写好的库。到这里，你已经能写出真正有用的小工具了——而不是只能在练习题里运行的玩具代码。

整条路径看下来你会发现：PR1 没有追求“知识点多”，它追求的是“每一步都踩实”。前面的知识，永远是后面的基础。没有哪一章是孤立的。

## 五、那些看起来“麻烦”的设计，其实都是用心
很多学生一开始会觉得周报很麻烦：每一步操作都要截图，放进 PPT，导出 PDF 提交。为什么不能直接交代码？

因为编程学习最大的敌人，是“学过了但没留下痕迹”。

很多人看视频教程，感觉都听懂了，一关视频什么都不会。原因很简单：你没有亲手走过完整流程，没有留下自己的操作记录。周报的意义，就是逼你把“登录服务器 → 创建文件 → 写代码 → 运行 → 看结果 → 排错”这个完整链条走一遍，并且留下证据。

多年以后你可能会忘了具体的命令，但你会记得：我当年亲手在服务器上跑通过这些脚本，我知道完整的流程是什么样的。这份体感，比背多少知识点都重要。

还有一个设计细节：课程里到处都是思考题。比如“GUI 和 CLI 各有什么优缺点？”“为什么我们需要相对路径？”“为什么要有 4 空格缩进原则？”

这些问题没有标准答案，但它们在逼你思考“为什么这么设计”。编程不是背指令，是理解设计背后的权衡。想通了这些为什么，你学到的就不是一堆零散的命令，而是一整套思维方式。

## 六、PR1 和 PR2 是怎么接在一起的
说到这里，你应该已经能隐约看到两门课的衔接关系了。

PR1 给你的，是底层认知和基本功：
- 你懂 Linux 和命令行，到了 PR2 学 IDE 远程开发，一接就通；
- 你懂文件路径和工作目录，到了 PR2 就不会被“模块找不到”这类环境问题卡住；
- 你懂函数、字典和数据结构，到了 PR2 学面向对象，会觉得顺理成章，而不是凭空出现；
- 你会读报错、会用 print 调试，到了 PR2 学断点调试，只是多了一件更高效的工具；
- 你懂 pip 和第三方库，到了 PR2 学 numpy、pandas、pygame，安装和导入对你来说根本不是问题。

PR2 给你的，是工具升级和能力扩容：
- 本地 IDE 让你写代码更高效，调试更方便；
- 面向对象让你能组织更大规模的代码，做更复杂的项目；
- numpy 和 pandas 让你真正进入数据处理的世界；
- pygame 让你能做出完整的小游戏，把之前学的所有知识用起来。

简单说：PR1 负责“扎马步”，PR2 负责“打连招”。
马步扎得稳，连招才不会散。如果跳过 PR1 直接去 PR2，你也能学，也能写出东西，但底层是空的。稍微遇到一点环境问题、边界问题，就容易卡壳。

## 七、写给不同的你
如果你是选课的学生：
请不要轻视 Linux 和命令行那部分，不要觉得“我以后用 IDE 就够了”。现在多花一点时间在终端里摸爬滚打，未来你会感谢现在的自己。认真做每一次实操，认真写周报，不要抄答案。编程这东西，手熟和不熟，骗不了人。这门课不会让你学完立刻变成大神，但它会帮你避开绝大多数新手必经的坑。

如果你是授课的老师：
这套课程的价值，不止于知识点。它传递的是一种“先系统、后语言，先过程、后对象”的教学思路。教学中可以多向前瞻一眼：告诉学生今天学的路径知识，以后用 IDE 会碰到；今天学的字典，以后学类的时候会再见面。让学生知道现在的付出有明确的后续价值，他们会更有动力。

如果你是自学者：
你完全可以用这套材料自学。节奏可以自己调，Linux 部分如果暂时没有服务器，也可以先在本地装个虚拟机或者 WSL 跟着练。不用强求一天学完一章，重点是每一个命令、每一段代码都亲手敲一遍，看到运行结果。遇到报错不要立刻搜答案，先试着自己读错误信息。读报错的能力，是自学者最重要的能力之一。等你把 PR1 扎扎实实走完，再去学 PR2 的 OOP 和各种库，进度会比直接跳过去快得多。

## 最后
PR1 不是一门“让你七天速成 Python”的课。它不想给你一种“我学会了”的幻觉。
它想给你的，是一种更踏实的东西：你知道代码跑在哪，知道文件存在哪，知道报错是什么意思，知道每一行代码为什么这么写。你手里攥的不是几个背下来的模板，而是一套可以继续生长的基础。

当你走完 PR1，再走进 PR2 的时候，你不会是从零开始。你是带着一整个扎实的地基，去盖更高的楼。
这可能不是最快的路，但这是最稳的路。而编程这条路，走得稳，往往比走得快，能走得更远。

