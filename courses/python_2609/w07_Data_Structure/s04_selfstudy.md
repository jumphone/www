# Python Data Structures

# Python 数据结构

Welcome to another essential milestone in your programming journey! Whenever you need to manage multiple pieces of data—like a list of users, a collection of unique tags, or a phone book of contacts—you will need **Data Structures**. In this chapter, we will learn how to store, organize, and manipulate data using **Lists**, **Tuples**, **Dictionaries**, and **Sets**.

欢迎来到你编程之旅中另一个不可或缺的里程碑！每当你需要管理多条数据时——比如用户列表、唯一标签的集合，或者联系人电话簿——你都会用到**数据结构（Data Structures）**。在本章中，我们将学习如何使用**列表（Lists）**、**元组（Tuples）**、字典（Dictionaries）**和**集合（Sets）来存储、组织和操作数据。

<br>

---

## Section 1. Lists

## 第 1 节：列表 (Lists)

### 1.1. What is a List? / 什么是列表？

Think of a list like a shopping list that can hold multiple items. In Python, a list is an ordered, changeable collection of data.

把列表想象成一个可以容纳多个物品的购物清单。在 Python 中，列表是一个有序且可更改的数据集合。

```python
# Shopping list example / 购物清单示例
groceries = ["apples", "milk", "eggs", "bread"]
print("My shopping list:" + str(groceries))

```

<br>


### 1.2. Four Ways to Create Lists / 创建列表的四种方法

**1. Square brackets `[]` / 方括号 `[]**`

```python
colors = ["red", "green", "blue"]

```

<br>


**2. `list()` constructor / `list()` 构造函数**

```python
numbers = list((1, 2, 3))  # Converts tuple to list / 将元组转换为列表

```

<br>


### 1.3. More Creation Methods / 更多创建方法

**3. List comprehension / 列表推导式**

```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

```
<br>


**4. Convert from string / 从字符串转换**

```python
word = list("hello")
# ['h', 'e', 'l', 'l', 'o']

```

<br>


### 1.4. Accessing Elements / 访问元素

You can access items using positive indexing (from the start) or negative indexing (from the end).

你可以使用正向索引（从头开始）或负向索引（从尾开始）来访问元素。

```python
games = ["Mario", "Zelda", "Pokémon"]
print(games[0])  # Mario
print(games[-1]) # Pokémon (negative index / 负向索引)

```

<br>


### 1.5. Slicing Lists / 列表切片

Get sub-lists with `[start:end]`.

使用 `[start:end]` 获取子列表。

```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
print(months[1:3])  # ['Feb', 'Mar']
print(months[:2])   # First two / 前两个: ['Jan', 'Feb']
print(months[3:])   # Last two / 后两个: ['Apr', 'May']

```

<br>


### 1.6. Adding Items / 添加元素

Use `append()` to add to the end, and `insert()` to add at a specific position.

使用 `append()`（追加）添加到末尾，使用 `insert()`（插入）添加到特定位置。

```python
todo = ["wake up"]
todo.append("brush teeth")  # Add to end / 添加到末尾
todo.insert(1, "make bed")  # Insert at position 1 / 在位置 1 插入
print(todo)  # ['wake up', 'make bed', 'brush teeth']

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: What happens if we run `todo.insert(0,'start')` ? `todo.insert(len(todo),'end1')` ? `todo.insert(-1,'end2')` ? / 问题：如果我们运行这些插入语句会怎样？**
> * *Solution (答案):*
> * `todo.insert(0, 'start')`: Inserts 'start' at the very beginning. (在最开头插入 'start'。)
> * `todo.insert(len(todo), 'end1')`: Inserts 'end1' at the very end, effectively the same as `append()`. (在最末尾插入 'end1'，效果等同于 `append()`。)
> * `todo.insert(-1, 'end2')`: Inserts 'end2' right *before* the current last item. (在当前的最后一个元素**之前**插入 'end2'。)
> 
> 

<br>


### 1.7. Removing Items / 移除元素

Use `remove()` to delete by value, and `pop()` to remove by index (or the last item).

使用 `remove()` 按值删除，使用 `pop()` 按索引删除（默认删除最后一个）。

```python
pets = ["cat", "dog", "hamster"]
pets.remove("dog")  # Remove by value / 按值删除
last = pets.pop()   # Remove last item / 移除最后一个元素
print(pets)         # ['cat']
print(last)         # 'hamster'

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question 1: If `pets=["dog", "bird", "dog", 'cat', "dog"]`, what happens after `pets.remove("dog")` ? / 问题 1：移除 "dog" 后的结果是什么？**
> * *Solution (答案):* `remove()` only deletes the *first* matching value. The list becomes `["bird", "dog", "cat", "dog"]`. (`remove()` 只会删除**第一个**匹配的值。列表将变成 `["bird", "dog", "cat", "dog"]`。)
> * **Question 2: What does `pets.index('dog')` return? / 问题 2：查找 "dog" 的索引会返回什么？**
> * *Solution (答案):* `index()` returns the position of the *first* occurrence. Using the original list, it will return `0`. (`index()` 返回**首次**出现的位置。在原列表中，它会返回 `0`。)
> 
> 

<br>


### 1.8. Sorting Lists / 列表排序

Use the `sort()` method to arrange items in order.

使用 `sort()` 方法将元素按顺序排列。

```python
scores = [88, 92, 75, 100]
scores.sort()
print(scores)  # [75, 88, 92, 100]

# Reverse sort / 降序排列
scores.sort(reverse=True)
print(scores)  # [100, 92, 88, 75]

```

<br>


### 1.9. Practice: Student Grades System / 实践：学生成绩系统

Store multiple students' scores in separate lists:

将多名学生的分数存储在不同的列表中：

```python
students = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

```

<br>


### 1.10. Calculate Average / 计算平均分

```python
total = sum(scores)
average = total / len(scores)
print("Class average: " + str(average))
# Output: Class average: 85.0

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: How to convert the "+" string concatenation to an f-string format (`f""`)? / 问题：如何把 "+" 的字符串拼接转换成 f-string 格式（`f""`）？**
> * *Solution (答案):* `print(f"Class average: {average}")`
> 
> 

<br>


### 1.11. Sort Scores / 分数排序

Combine data to sort students by their scores:

组合数据以按分数对学生进行排序：

```python
combined = []
i = 0
while i < len(scores):
    combined.append([scores[i], students[i]])
    i = i + 1

combined.sort()

print("Ranking:")
for one in combined:
    print(str(one[1]) + ": " + str(one[0]))

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: How to sort in reverse order (highest to lowest)? / 问题：如何倒序（从高到低）排序？**
> * *Solution (答案):* Change the sort line to `combined.sort(reverse=True)`. (将排序的代码行修改为 `combined.sort(reverse=True)`。)
> 
> 

---

<br>


## Section 2. Tuples

## 第 2 节：元组 (Tuples)

### 2.1. Tuples vs Lists: Immutability Demo / 元组与列表：不可变性演示

```python
# Lists are mutable (changeable) / 列表是可变的
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"
print(fruits)  # Changes successfully / 成功修改

# Tuples are immutable (unchangeable) / 元组是不可变的
colors = ("red", "green", "blue")

colors[0] = "pink"
# report error / 会报错

```

**Key difference (核心区别):**
📌 Tuples use `()` while lists use `[]` / 元组使用 `()` 而列表使用 `[]`
📌 Tuple elements cannot be changed after creation / 元组元素在创建后无法被修改

<br>


### 2.2. Why Immutability Matters? / 为什么不可变性很重要？

Real-life examples of unchangeable data:

现实生活中不可变数据的例子：

* Geographic coordinates (latitude, longitude) / 地理坐标（经度、纬度）
* RGB color codes / RGB 颜色代码
* Date components (year, month, day) / 日期组成（年、月、日）

```python
# Valid tuple usage / 元组的合理用法
black = (0, 0, 0)
current_position = (37.7749, -122.4194)

```

<br>


### 2.3. Tuple Unpacking / 元组解包

Basic unpacking / 基础解包：

```python
dimensions = (1920, 1080)
width, height = dimensions
print("Screen: " + str(width) + "x" + str(height))

```

Swapping variables / 交换变量：

```python
a = 5
b = 10
a, b = b, a

```

<br>


### 2.4. Advanced Unpacking Tricks / 进阶解包技巧

Ignoring values / 忽略某些值：

```python
coordinates = (45, -73, 100)
lat, lon, _ = coordinates

```

Multiple assignment / 多重赋值：

```python
# Get first and last items / 获取第一个和最后一个元素
numbers = (3, 1, 4, 1, 5, 9)
first, *middle, last = numbers

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: What is the content of "middle" ? / 问题："middle" 的内容是什么？**
> * *Solution (答案):* The `*` collects the remaining items into a list. `middle` will be `[1, 4, 1, 5]`. (`*` 会把剩余的元素收集到一个列表中。`middle` 会是 `[1, 4, 1, 5]`。)
> 
> 

<br>


### 2.5. Single-element Tuple Trap / 单元素元组陷阱

Common mistake / 常见错误：

```python
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

```

Correct way / 正确方式：

```python
proper_tuple = (42,)
print(type(proper_tuple))  # <class 'tuple'>

```

**Visual reminder (视觉提示):**
❗ Always add comma for single items ❗ / ❗ 单个元素时永远记得加上逗号 ❗

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: What is `proper_tuple[0]` ? `proper_tuple[1]` ? / 问题：`proper_tuple[0]` 和 `proper_tuple[1]` 分别是什么？**
> * *Solution (答案):* `proper_tuple[0]` is `42`. `proper_tuple[1]` will throw an `IndexError` because there is no second element! (`proper_tuple[0]` 是 `42`。`proper_tuple[1]` 会抛出索引越界错误 `IndexError`，因为没有第二个元素！)
> 
> 

<br>


### 2.6. Returning Multiple Values / 返回多个值

Simple example / 简单示例：

```python
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return (area, circumference)

results = circle_calc(5)
print("Area: " + str(results[0]) + ", Circumference: " + str(results[1]))

```

Better usage with unpacking / 使用解包的更好用法：

```python
area, circ = circle_calc(7)
print("Area is " + str(area) + " units")

```

<br>


### 2.7. When to Use Tuples? / 什么时候使用元组？

Perfect for / 非常适合：

1. Data that shouldn't change (constants) / 不应被更改的数据（常量）
2. Dictionary keys (unlike lists!) / 作为字典的键（列表可不行！）
3. Function return values / 函数返回值
4. Protecting important data / 保护重要数据

```python
# Valid dictionary key / 有效的字典键
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

```

<br>


### 2.8. Tuple Operations Summary / 元组操作总结

Essential methods / 核心方法：

```python
my_tuple = (1, 2, 3)

print(len(my_tuple))      # 3
print(2 in my_tuple)      # True
print(my_tuple.index(2))  # 1
print(my_tuple.count(2))  # 1

```

**Remember:** No append/remove/pop methods!
**请记住：** 没有任何 append/remove/pop 方法！

---

<br>


## Section 3. Dictionaries

## 第 3 节：字典 (Dictionaries)

### 3.1. Phone Book Analogy 📞 / 电话簿类比 📞

```python
# Think of dictionaries like phone contacts:
# 把字典想象成电话联系人：
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print(phone_book["Alice"])  # Outputs / 输出: 555-1234

```

<br>


### 3.2. Three Ways to Create Dictionaries / 创建字典的三种方法

**Method 1: Curly Braces `{}` / 方法 1：花括号 `{}**`

```python
student = {"name": "Emma", "age": 20, "major": "CS"}

```

**Method 2: `dict()` Constructor / 方法 2：`dict()` 构造函数**

```python
colors = dict(red="#FF0000", green="#00FF00")

```

**Method 3: List of Tuples / 方法 3：元组列表**

```python
weekdays = dict([(1, "Mon"), (2, "Tue"), (3, "Wed")])

```


<br>


### 3.3. Adding & Changing Entries / 添加与修改条目

```python
animal_sounds = {}
animal_sounds["dog"] = "Woof!"  # Add new entry / 添加新条目
animal_sounds["cat"] = "Mew"    # Add another / 添加另一个
animal_sounds["cat"] = "Meow"   # Update existing / 更新现有条目
print(animal_sounds)  # {'dog': 'Woof!', 'cat': 'Meow'}

```

<br>


### 3.4. Removing Entries / 移除条目

```python
del animal_sounds["dog"]        # Delete entry / 删除条目
removed = animal_sounds.pop("cat")
print(removed)  # "Meow"
print(animal_sounds)  # Empty now / 现在为空

```

<br>


### 3.5. Safe Value Access with get() / 使用 get() 安全访问值

```python
grades = {"Math": 90, "Science": 85}
print(grades.get("History", "Subject not found"))
# Outputs / 输出: Subject not found

```

<br>


### 3.6. Building a Simple Translator / 构建一个简单的翻译器

*File: `translator.py*`

```python
translator = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}

word = input("Enter English word: ").lower()
translation = translator.get(word, "Translation not available")
print("Spanish: " + str(translation))

```


<br>

### 3.7. Handling Unknown Words / 处理未知单词

```python
if translation == "Translation not available":
    print("Please check spelling!")
    print("Current dictionary words:" + str(list(translator.keys())))

```

<br>


### 3.8. Dictionary Methods Summary / 字典方法总结

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())    # dict_keys(['a', 'b'])
print(my_dict.values())  # dict_values([1, 2])
print(my_dict.items())   # dict_items([('a', 1), ('b', 2)])

```

<br>


### 3.9. Real-World Example: Movie Ratings / 现实世界案例：电影评分

*File: `movie_rating.py*`

```python
movies = {
    "Moana": 7.5,
    "Toy Story": 8.6,
    "Frozen": 8.5
}

movie = input("Enter movie title: ")
print("Rating: " + str(movies.get(movie, "Not in database")) + "/10")

```

<br>


### 3.10. Dictionary Power Tips 💡 / 字典高阶技巧 💡

1. Keys can be numbers/strings/tuples / 键可以是数字、字符串或元组
2. Values can be ANY data type / 值可以是**任何**数据类型
3. Fast lookup speed / 查找速度极快
4. Great for organizing related data / 非常适合组织相关联的数据

```python
mixed_example = {
    1: "Number key",
    (2,3): "Tuple key",
    "list": ["can", "be", "value"]
}

```

---

<br>


## Section 4. Sets

## 第 4 节：集合 (Sets)

### 4.1. What Makes Sets Special? / 集合有什么特别之处？

* **Unique Elements (唯一性)**: Automatically removes duplicates (自动移除重复项)
* **Unordered (无序性)**: No index-based access (没有基于索引的访问)
* **Mutable (可变性)**: Can add/remove elements (可以添加或删除元素)
* **Math Operations (数学运算)**: Built-in set operations (内置集合运算)

<br>


### 4.2. Automatic Deduplication Demo / 自动去重演示

```python
# List vs Set comparison / 列表与集合对比
fruits_list = ['apple', 'banana', 'apple', 'orange']
fruits_set = {'apple', 'banana', 'apple', 'orange'}

print("List: " + str(fruits_list))  # Keeps duplicates / 保留重复项
print("Set: " + str(fruits_set))    # Auto-removes duplicates / 自动移除重复项

```

<br>


### 4.3. Real-World Deduplication Example / 现实世界的去重案例

```python
# Removing duplicate votes / 移除重复选票
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_voters = set(votes)

print("Total votes: " + str(len(votes)))
print("Unique voters: " + str(len(unique_voters)))

```

<br>


### 4.4. Set Operations: Intersection / 集合操作：交集

```python
# Common elements in both sets / 两个集合共有的元素
art_students = {'Tom', 'Alice', 'Bob', 'Eve'}
music_students = {'Alice', 'Eve', 'John'}

both = art_students & music_students
print("Students in both clubs: " + str(both))

```

<br>


### 4.5. Set Operations: Union / 集合操作：并集

```python
# Combine sets (no duplicates) / 合并集合（无重复项）
week1_customers = {'Alice', 'Bob'}
week2_customers = {'Bob', 'Charlie'}

all_customers = week1_customers | week2_customers
print("All customers: " + str(all_customers))

```

<br>


### 4.6. Set Operations: Difference / 集合操作：差集

```python
# Elements in first set not in second / 存在于第一个集合但不在第二个集合中的元素
available_colors = {'red', 'blue', 'green'}
used_colors = {'blue', 'yellow'}

remaining = available_colors - used_colors
print("Remaining colors: " + str(remaining))

```

<br>


### 4.7. Voting System Case Study / 投票系统案例研究

*File: `vote.py*`

```python
# Counting unique votes / 统计唯一的选票
votes = []
while True:
    vote = input("Enter candidate name (or 'done'): ")
    if vote.lower() == 'done':
        break
    votes.append(vote)

unique_votes = set(votes)
print("Candidates: " + ', '.join(unique_votes))

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: How can we get the number of votes for each candidate? Hint: use dict / 问题：我们如何获取每位候选人的得票数？提示：使用字典。**
> * *Solution (答案):*
> 
> 
> ```python
> vote_counts = {}
> for v in votes:
>     vote_counts[v] = vote_counts.get(v, 0) + 1
> print(vote_counts)
> 
> ```
> 
> 

<br>


### 4.8. Friend Finder System / 寻找好友系统

```python
# Finding common friends / 寻找共同好友
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Charlie', 'Diana', 'Eve'}

common = alice_friends & bob_friends
print("Common friends: " + str(common))

# Adding new friend / 添加新好友
alice_friends.add('Eve')
print("Updated friends: " + str(alice_friends))

```

<br>


### 4.9. Set Methods Cheat Sheet / 集合方法速查表

| Method / 方法 | Example / 示例 | Description / 描述 |
| --- | --- | --- |
| `add()` | `s.add('x')` | Add element / 添加元素 |
| `remove()` | `s.remove('x')` | Remove element / 删除元素 |
| `clear()` | `s.clear()` | Empty the set / 清空集合 |
| `copy()` | `new_set = s.copy()` | Create duplicate / 创建副本 |

*Note: Lists also have `clear()` and `copy()`!*
*注：列表（List）同样也有 `clear()` 和 `copy()` 方法！*

<br>


### 4.10. Why Use Sets? / 为什么使用集合？

1. **Fast membership testing**: `'a' in set` / **快速成员测试**：`'a' in set`
2. **Mathematical operations**: Easy intersections/unions / **数学运算**：轻松求交集/并集
3. **Data cleaning**: Quick duplicate removal / **数据清洗**：快速去重
4. **Relationship modeling**: Social networks, groups / **关系建模**：社交网络、群组

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: Write a program to get all unique letters in your name? / 问题：编写一段程序来获取你名字中所有不重复的字母？**
> * *Solution (答案):*
> 
> 
> ```python
> my_name = "Alexandria"
> unique_letters = set(my_name.lower())
> print(unique_letters)
> 
> ```
> 
> 

---

<br>


## Section 5. Data Structures in Action

## 第 5 节：数据结构实战

### 5.1. Student Information System Demo / 学生信息系统演示

Let's look at how variables behave with functions.

让我们看看变量在函数中是如何表现的。

```python
a = []
def add():
    a.append(1)

add()
print(a)  # [1]

```

```python
a = set()
def add():
    a.add(1)

add()
print(a)  # {1}

```

```python
a = {}
def add():
    a[1]=1

add()
print(a)  # {1: 1}

```

```python
a = 0
def add():
    # Will print 0 / 会打印 0
    print(a)

add()
print(a)  # 0

```

```python
a = 0
def add():
    a = a + 1 # UnboundLocalError! (Without global keyword) / 报错！(缺少 global 关键字)

add()
print(a)

```

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: What happened here? Mutable vs Immutable variables. / 问题：这里发生了什么？可变变量与不可变变量。**
> * *Explanation (解析):* Variable "assignment" and "modifying its contents" (for mutable types like list, dict, set) are two completely different things!
> Assignment (e.g., `a = a + 1`) means replacing the entire box. To do this inside a function, Python requires the `global` keyword.
> Modifying contents (e.g., `a.append(1)`) means changing what’s inside the box. Since the box itself isn't replaced, no `global` keyword is needed.
> （变量的“赋值”和“修改其内容”（针对如列表、字典、集合等可变类型）是两码事！
> 赋值（如 `a = a + 1`）意味着替换掉整个盒子。如果在函数内部执行此操作，Python 需要 `global` 全局关键字。
> 修改内容（如 `a.append(1)`）意味着仅仅改变盒子内部的东西。由于盒子本身并没有被替换，因此不需要 `global` 关键字。）
> 
> 

<br>


### 5.2. Storing Students / 存储学生信息

```python
# Create empty list / 创建空列表
students = []

# Create student dictionary / 创建学生字典
student1 = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
students.append(student1)

```

<br>


### 5.3. Adding Students / 添加学生

```python
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")
    
    new_student = {
        "name": name,
        "age": age,
        "major": major
    }
    students.append(new_student)
    print("Student added!")

```

<br>


### 5.4. Sorting Students / 学生排序

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: How to add two students, and then order the students by age? / 问题：如何添加两名学生，然后按年龄对学生进行排序？**
> * *Solution (答案):*
> 
> 
> ```python
> add_student()
> add_student()
> # Using a lambda function as the sort key / 使用 lambda 函数作为排序键
> students.sort(key=lambda s: s["age"])
> print(students)
> 
> ```
> 
> 


<br>

### 5.5. Word Frequency Analyzer / 词频分析器

**1. Splitting Text / 分割文本**

```python
text = "apple banana orange apple pear orange apple ok yes yes ok no no want"
words = text.lower().split()

print(words)

```

<br>


### 5.6. Counting Words / 统计单词

```python
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

```

<br>


### 5.7. Finding TOP5 Words / 找出出现频率前五的单词

> **🧠 Interactive Exercises & Explanations / 互动练习与解析:**
> * **Question: How can we get the top 5 words? / 问题：我们如何获取前 5 个高频词？**
> * *Solution (答案):*
> We can convert the dictionary to a list of tuples, sort it by frequency in descending order, and slice the first 5 elements.
> （我们可以将字典转换为元组列表，按频率降序排序，然后切片获取前 5 个元素。）
> 
> 
> ```python
> # Convert dictionary items to a list of lists/tuples: [[count, word], ...]
> # 将字典项转换为列表/元组的列表：[[频率, 单词], ...]
> count_list = []
> for word, count in word_counts.items():
>     count_list.append([count, word])
> 
> # Sort in reverse (highest counts first) / 降序排序（高频词在前）
> count_list.sort(reverse=True)
> 
> print("Top 5 words:", count_list[:5])
> 
> ```
> 
> 

---

<br>


**Congratulations! / 恭喜你！** You have successfully learned how to store and manipulate complex data in Python using Data Structures. These tools (Lists, Tuples, Dictionaries, and Sets) are the foundation of all advanced programming concepts!

你已经成功学会了如何使用数据结构在 Python 中存储和操作复杂的数据。这些工具（列表、元组、字典和集合）是所有进阶编程概念的基石！
