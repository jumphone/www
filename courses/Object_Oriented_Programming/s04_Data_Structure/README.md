
---
# Section 1. List

### 1.1 What is a List?
Like a shopping list that can hold multiple items  
```python
# Shopping list example
groceries = ["apples", "milk", "eggs", "bread"]
print("My shopping list:", groceries)
```

---
### 1.2 Four Ways to Create Lists
1. Square brackets `[]`  
```python
colors = ["red", "green", "blue"]
```

2. `list()` constructor  
```python
numbers = list((1, 2, 3))  # Converts tuple to list
```

---
### 1.3 More Creation Methods
3. List comprehension  
```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

4. Convert from string  
```python
word = list("hello")
# ['h', 'e', 'l', 'l', 'o']
```

---
### 2.1 Accessing Elements
Positive indexing:  
```python
games = ["Mario", "Zelda", "Pokémon"]
print(games[0])  # Mario
print(games[-1]) # Pokémon (negative index)
```

---
### 2.2 Slicing Lists
Get sub-lists with `[start:end]`  
```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
print(months[1:3])  # ['Feb', 'Mar']
print(months[:2])   # First two: ['Jan', 'Feb']
print(months[3:])   # Last two: ['Apr', 'May']
```

---
### 3.1 Adding Items
`append()` and `insert()`  
```python
todo = ["wake up"]
todo.append("brush teeth")  # Add to end
todo.insert(1, "make bed")  # Insert at position 1
print(todo)  # ['wake up', 'make bed', 'brush teeth']
```

## Question: todo.insert(0,'start') ? todo.insert(len(todo),'end1') ?  todo.insert(-1,'end2') ? 

---
### 3.2 Removing Items
`remove()` and `pop()`  
```python
pets = ["cat", "dog", "hamster"]
pets.remove("dog")  # Remove by value
last = pets.pop()   # Remove last item
print(pets)         # ['cat']
print(last)         # 'hamster'
```

## Question: pets=["dog", "bird", "dog", 'cat',"dog"]; pets.remove("dog") ?
## Question: pets.index('dog')?

---
### 3.3 Sorting Lists
`sort()` method  
```python
scores = [88, 92, 75, 100]
scores.sort()
print(scores)  # [75, 88, 92, 100]

# Reverse sort
scores.sort(reverse=True)
print(scores)  # [100, 92, 88, 75]
```

---
### 4.1 Practise: Student Grades System
Store multiple students' scores  
```python
students = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]
```

---
### 4.2 Calculate Average
```python
total = sum(scores)
average = total / len(scores)
print(f"Class average: {average}")
# Output: Class average: 85.0
```
## Question: how to convert the f-string format to "+" format?

---
### 4.3 Sort Scores
Combine data with `zip()`  
```python
combined = []
i=0
while i<len(scores):
    combined.append( [scores[i], students[i]] )
    i=i+1

combined.sort()

print("Ranking:")
for one in combined:
    print(f"{one[1]}: {one[0]}")
```

## Question: sort in reverse order?

---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 2. Tuple

## 1 Tuples vs Lists: Immutability Demo

```python
# Lists are mutable
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"
print(fruits)  # Changes successfully

# Tuples are immutable (unchangeable)
colors = ("red", "green", "blue")


colors[0] = "pink"

# report error

```

Key difference:  
📌 Tuples use () while lists use []  
📌 Tuple elements cannot be changed after creation

---

## Why Immutability Matters?

Real-life examples of unchangeable data:
- Geographic coordinates (latitude, longitude)
- RGB color codes
- Date components (year, month, day)

```python
# Valid tuple usage
black = (0, 0, 0)
current_position = (37.7749, -122.4194)
```

---

## 2 Tuple Unpacking

Basic unpacking:
```python
dimensions = (1920, 1080)
width, height = dimensions
print(f"Screen: {width}x{height}") 
```

Swapping variables:
```python
a = 5
b = 10
a, b = b, a  
```

---

## Advanced Unpacking Tricks

Ignoring values:
```python
coordinates = (45, -73, 100)
lat, lon, _ = coordinates
```

Multiple assignment:
```python
# Get first and last items
numbers = (3, 1, 4, 1, 5, 9)
first, *middle, last = numbers
```
## Question: what is the content of "middle" ? 

---

## 3 Single-element Tuple Trap

Common mistake:
```python
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>
```

Correct way:
```python
proper_tuple = (42,)
print(type(proper_tuple))  # <class 'tuple'>
```
Visual reminder:  
❗ Always add comma for single items ❗


## Question: proper_tuple[0] ? proper_tuple[1] ? 

---

## 4 Returning Multiple Values

Simple example:
```python
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return (area, circumference)

results = circle_calc(5)
print(f"Area: {results[0]}, Circumference: {results[1]}")
```

Better usage with unpacking:
```python
area, circ = circle_calc(7)
print(f"Area is {area} units")
```

---

## When to Use Tuples?

Perfect for:
1. Data that shouldn't change (constants)
2. Dictionary keys (unlike lists!)
3. Function return values
4. Protecting important data

```python
# Valid dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

---

## Tuple Operations Summary

Essential methods:
```python
my_tuple = (1, 2, 3)

print(len(my_tuple))      # 3
print(2 in my_tuple)      # True
print(my_tuple.index(2))  # 1
print(my_tuple.count(2))  # 1
```

### Remember:  
### No append/remove/pop methods!

---



<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 3. Dictionaries in Python

## 1. Phone Book Analogy 📞
```python
# Think of dictionaries like phone contacts:
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print(phone_book["Alice"])  # Outputs: 555-1234
```

---

## 2. Three Ways to Create Dictionaries 

### Method 1: Curly Braces {}
```python
student = {"name": "Emma", "age": 20, "major": "CS"}
```

### Method 2: dict() Constructor
```python
colors = dict(red="#FF0000", green="#00FF00")
```

### Method 3: List of Tuples
```python
weekdays = dict([(1, "Mon"), (2, "Tue"), (3, "Wed")])
```

---

## 3. Adding & Changing Entries
```python
animal_sounds = {}
animal_sounds["dog"] = "Woof!"  # Add new entry
animal_sounds["cat"] = "Mew"    # Add another
animal_sounds["cat"] = "Meow"   # Update existing
print(animal_sounds)  # {'dog': 'Woof!', 'cat': 'Meow'}
```

---

## 4. Removing Entries
```python
del animal_sounds["dog"]        # Delete entry
removed = animal_sounds.pop("cat") 
print(removed)  # "Meow"
print(animal_sounds)  # Empty now
```

---

## 5. Safe Value Access with get()
```python
grades = {"Math": 90, "Science": 85}
print(grades.get("History", "Subject not found")) 
# Outputs: Subject not found
```

---

## 6. Building a Simple Translator

nano translator.py

```python
translator = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}

word = input("Enter English word: ").lower()
translation = translator.get(word, "Translation not available")
print(f"Spanish: {translation}")
```

---

## 7. Building a Simple Translator
```shell

python3 translator.py

# input: hello

```

---

## 8. Handling Unknown Words
```python
if translation == "Translation not available":
    print("Please check spelling!")
    print("Current dictionary words:", list(translator.keys()))
```

---

## 9. Dictionary Methods Summary
```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())    # dict_keys(['a', 'b'])
print(my_dict.values())  # dict_values([1, 2])
print(my_dict.items())   # dict_items([('a', 1), ('b', 2)])
```

---

## 10. Real-World Example: Movie Ratings

nano movie_rating.py

```python
movies = {
    "Moana": 7.5,
    "Toy Story": 8.6,
    "Frozen": 8.5
}

movie = input("Enter movie title: ")
print(f"Rating: {movies.get(movie, 'Not in database')}/10")
```

---

## 11. Dictionary Power Tips 💡
1. Keys can be numbers/strings/tuples
2. Values can be ANY data type
3. Fast lookup speed
4. Great for organizing related data
```python
mixed_example = {
    1: "Number key",
    (2,3): "Tuple key",
    "list": ["can", "be", "value"]
}
```


<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 4. Sets in Python: Special Features

---

## What Makes Sets Special?
- **Unique Elements**: Automatically removes duplicates
- **Unordered**: No index-based access
- **Mutable**: Can add/remove elements
- **Math Operations**: Built-in set operations

---

## 1 Automatic Deduplication Demo
```python
# List vs Set comparison
fruits_list = ['apple', 'banana', 'apple', 'orange']
fruits_set = {'apple', 'banana', 'apple', 'orange'}

print(f"List: {fruits_list}")  # Keeps duplicates
print(f"Set: {fruits_set}")    # Auto-removes duplicates
```

---

## Real-World Deduplication Example
```python
# Removing duplicate votes
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_voters = set(votes)

print(f"Total votes: {len(votes)}")
print(f"Unique voters: {len(unique_voters)}")
```

---

## 2 Set Operations: Intersection
```python
# Common elements in both sets
art_students = {'Tom', 'Alice', 'Bob', 'Eve'}
music_students = {'Alice', 'Eve', 'John'}

both = art_students & music_students
print(f"Students in both clubs: {both}")
```

---

## Set Operations: Union
```python
# Combine sets (no duplicates)
week1_customers = {'Alice', 'Bob'}
week2_customers = {'Bob', 'Charlie'}

all_customers = week1_customers | week2_customers
print(f"All customers: {all_customers}")
```

---

## Set Operations: Difference
```python
# Elements in first set not in second
available_colors = {'red', 'blue', 'green'}
used_colors = {'blue', 'yellow'}

remaining = available_colors - used_colors
print(f"Remaining colors: {remaining}")
```

---

## 3 Voting System Case Study

nano vote.py
```python
# Counting unique votes
votes = []
while True:
    vote = input("Enter candidate name (or 'done'): ")
    if vote.lower() == 'done':
        break
    votes.append(vote)

unique_votes = set(votes)
print(f"Candidates: {', '.join(unique_votes)}")
```

## Question: how can we get the number of votes? hint: use dict


---

## 4 Friend Finder System
```python
# Finding common friends
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Charlie', 'Diana', 'Eve'}

common = alice_friends & bob_friends
print(f"Common friends: {common}")

# Adding new friend
alice_friends.add('Eve')
print(f"Updated friends: {alice_friends}")
```

---

## Set Methods Cheat Sheet
| Method      | Example                     | Description                 |
|-------------|-----------------------------|-----------------------------|
| `add()`     | `s.add('x')`                | Add element                 |
| `remove()`  | `s.remove('x')`             | Remove element              |
| `clear()`   | `s.clear()`                 | Empty the set               |
| `copy()`    | `new_set = s.copy()`        | Create duplicate            |

---

## Why Use Sets?
1. **Fast membership testing**: `'a' in set`
2. **Mathematical operations**: Easy intersections/unions
3. **Data cleaning**: Quick duplicate removal
4. **Relationship modeling**: Social networks, groups

---


## Question: write a program to get all unique letters in your name?

---

<img src="https://fzhang.bioinfo-lab.com/img/white.png" height="50">

# Section 5. Data Structures in Action

## Student Information System Demo

### 0 A demo

```python
a = []
def add():
    a.append(1)

add()
print(a)
```

```python
a = set()
def add():
    a.add(1)

add()
print(a)
```

```python
a = {}
def add():
    a[1]=1

add()
print(a)
```

```python
a=0
def add():
    a=a+1

add()
print(a)

```
## Question: What happended here ?
## mutable variable: list, dict, set


### 1 Storing Students

```python
# Create empty list
students = []

# Create student dictionary
student1 = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
students.append(student1)
```



---
### 2 Adding Students
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

---
### 3 Sorting Students

## Question: add two students, order students by age ?

---
## Word Frequency Analyzer

### 1 Splitting Text
```python
text = "apple banana orange apple pear orange apple ok yes yes ok no no want"
words = text.lower().split()

print(words)

```

---
### 2 Counting Words
```python
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

```

---
### 3 Finding TOP5 Words

## Question: How can we get top5 words?

