[Back](https://www.bioinfo-lab.com/courses/Programming_I/w07_Data_Structure/)

<br>

<a id="all"></a>

### Content:

[Section 1. Lists](#s1.0)

[Section 2. Tuples](#s2.0)

[Section 3. Dictionaries](#s3.0)

[Section 4. Sets](#s4.0)

[Section 5. Data Structures in Action](#s5.0)

<br>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.0"></a>
# Section 1. Lists

<div align="left">
  <a href="#all">← Prev </a> | <a href="#all"> Home </a> | <a href="#s1.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.1"></a>

---

## 1.1. What is a List?

Like a shopping list that can hold multiple items

```python
# Shopping list example
groceries = ["apples", "milk", "eggs", "bread"]
print("My shopping list:" + str(groceries))
```

---

<div align="left">
  <a href="#s1.0">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s1.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.2"></a>

---

## 1.2. Four Ways to Create Lists

1. Square brackets `[]`

```python
colors = ["red", "green", "blue"]
```

2. `list()` constructor

```python
numbers = list((1, 2, 3))  # Converts tuple to list
```

---

<div align="left">
  <a href="#s1.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.3"></a>

---

## 1.3. More Creation Methods

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

<div align="left">
  <a href="#s1.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.4"></a>

---

## 1.4. Accessing Elements

Positive indexing:

```python
games = ["Mario", "Zelda", "Pokémon"]
print(games[0])  # Mario
print(games[-1]) # Pokémon (negative index)
```

---

<div align="left">
  <a href="#s1.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.5"></a>

---

## 1.5. Slicing Lists

Get sub-lists with `[start:end]`

```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
print(months[1:3])  # ['Feb', 'Mar']
print(months[:2])   # First two: ['Jan', 'Feb']
print(months[3:])   # Last two: ['Apr', 'May']
```

---

<div align="left">
  <a href="#s1.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.6"></a>

---

## 1.6. Adding Items

`append()` and `insert()`

```python
todo = ["wake up"]
todo.append("brush teeth")  # Add to end
todo.insert(1, "make bed")  # Insert at position 1
print(todo)  # ['wake up', 'make bed', 'brush teeth']
```

<br>

### Q: todo.insert(0,'start') ? todo.insert(len(todo),'end1') ? todo.insert(-1,'end2') ?

<br>

---

<div align="left">
  <a href="#s1.5">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.7"></a>

---

## 1.7. Removing Items

`remove()` and `pop()`

```python
pets = ["cat", "dog", "hamster"]
pets.remove("dog")  # Remove by value
last = pets.pop()   # Remove last item
print(pets)         # ['cat']
print(last)         # 'hamster'
```

<br>

### Q: pets=["dog", "bird", "dog", 'cat',"dog"]; pets.remove("dog") ?

<br>

### Q: pets.index('dog')?

<br>

---

<div align="left">
  <a href="#s1.6">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.8"></a>

---

## 1.8. Sorting Lists

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

<div align="left">
  <a href="#s1.7">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.9"></a>

---

## 1.9. Practice: Student Grades System

Store multiple students' scores

```python
students = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]
```

---

<div align="left">
  <a href="#s1.8">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.10"></a>

---

## 1.10. Calculate Average

```python
total = sum(scores)
average = total / len(scores)
print("Class average: " + str(average))
# Output: Class average: 85.0
```

<br>

### Q: how to convert the "+" to a f-string format (f"")?

<br>

---

<div align="left">
  <a href="#s1.9">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s1.11"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s1.11"></a>

---

## 1.11. Sort Scores

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
    print(str(one[1]) + ": " + str(one[0]))
```

<br>

### Q: sort in reverse order?

<br>

---

<div align="left">
  <a href="#s1.10">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s2.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.0"></a>

# Section 2. Tuples

<div align="left">
  <a href="#s1.11">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.1"></a>

---

## 2.1. Tuples vs Lists: Immutability Demo

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

<div align="left">
  <a href="#s2.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.2"></a>

---

## 2.2. Why Immutability Matters?

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

<div align="left">
  <a href="#s2.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.3"></a>

---

## 2.3. Tuple Unpacking

Basic unpacking:

```python
dimensions = (1920, 1080)
width, height = dimensions
print("Screen: " + str(width) + "x" + str(height))
```

Swapping variables:

```python
a = 5
b = 10
a, b = b, a
```

---

<div align="left">
  <a href="#s2.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.4"></a>

---

## 2.4. Advanced Unpacking Tricks

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

<br>

### Q: what is the content of "middle" ?

<br>

---

<div align="left">
  <a href="#s2.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.5"></a>

---

## 2.5. Single-element Tuple Trap

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

<br>

### Q: proper_tuple[0] ? proper_tuple[1] ?

<br>

---

<div align="left">
  <a href="#s2.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.6"></a>

---

## 2.6. Returning Multiple Values

Simple example:

```python
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return (area, circumference)

results = circle_calc(5)
print("Area: " + str(results[0]) + ", Circumference: " + str(results[1]))
```

Better usage with unpacking:

```python
area, circ = circle_calc(7)
print("Area is " + str(area) + " units")
```

---

<div align="left">
  <a href="#s2.5">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.7"></a>

---

## 2.7. When to Use Tuples?

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

<div align="left">
  <a href="#s2.6">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s2.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s2.8"></a>

---

## 2.8. Tuple Operations Summary

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

<div align="left">
  <a href="#s2.7">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s3.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.0"></a>

# Section 3. Dictionaries

<div align="left">
  <a href="#s2.8">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.1"></a>

---

## 3.1. Phone Book Analogy 📞

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

<div align="left">
  <a href="#s3.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.2"></a>

---

## 3.2. Three Ways to Create Dictionaries

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

<div align="left">
  <a href="#s3.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.3"></a>

---

## 3.3. Adding & Changing Entries

```python
animal_sounds = {}
animal_sounds["dog"] = "Woof!"  # Add new entry
animal_sounds["cat"] = "Mew"    # Add another
animal_sounds["cat"] = "Meow"   # Update existing
print(animal_sounds)  # {'dog': 'Woof!', 'cat': 'Meow'}
```

---

<div align="left">
  <a href="#s3.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.4"></a>

---

## 3.4. Removing Entries

```python
del animal_sounds["dog"]        # Delete entry
removed = animal_sounds.pop("cat")
print(removed)  # "Meow"
print(animal_sounds)  # Empty now
```

---

<div align="left">
  <a href="#s3.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.5"></a>

---

## 3.5. Safe Value Access with get()

```python
grades = {"Math": 90, "Science": 85}
print(grades.get("History", "Subject not found"))
# Outputs: Subject not found
```

---

<div align="left">
  <a href="#s3.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.6"></a>

---

## 3.6. Building a Simple Translator

nano translator.py

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

---

<div align="left">
  <a href="#s3.5">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.7"></a>

---

## 3.7. Handling Unknown Words

```python
if translation == "Translation not available":
    print("Please check spelling!")
    print("Current dictionary words:" + str(list(translator.keys())))
```

---

<div align="left">
  <a href="#s3.6">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.8"></a>

---

## 3.8. Dictionary Methods Summary

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())    # dict_keys(['a', 'b'])
print(my_dict.values())  # dict_values([1, 2])
print(my_dict.items())   # dict_items([('a', 1), ('b', 2)])
```

---

<div align="left">
  <a href="#s3.7">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.9"></a>

---

## 3.9. Real-World Example: Movie Ratings

nano movie_rating.py

```python
movies = {
    "Moana": 7.5,
    "Toy Story": 8.6,
    "Frozen": 8.5
}

movie = input("Enter movie title: ")
print("Rating: " + str(movies.get(movie, "Not in database")) + "/10")
```

---

<div align="left">
  <a href="#s3.8">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s3.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s3.10"></a>

---

## 3.10. Dictionary Power Tips 💡

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

---

<div align="left">
  <a href="#s3.9">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s4.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.0"></a>

# Section 4. Sets

<div align="left">
  <a href="#s3.10">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.1"></a>

---

## 4.1. What Makes Sets Special?

- **Unique Elements**: Automatically removes duplicates
- **Unordered**: No index-based access
- **Mutable**: Can add/remove elements
- **Math Operations**: Built-in set operations

---

<div align="left">
  <a href="#s4.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.2"></a>

---

## 4.2. Automatic Deduplication Demo

```python
# List vs Set comparison
fruits_list = ['apple', 'banana', 'apple', 'orange']
fruits_set = {'apple', 'banana', 'apple', 'orange'}

print("List: " + str(fruits_list))  # Keeps duplicates
print("Set: " + str(fruits_set))    # Auto-removes duplicates
```

---

<div align="left">
  <a href="#s4.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.3"></a>

---

## 4.3. Real-World Deduplication Example

```python
# Removing duplicate votes
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_voters = set(votes)

print("Total votes: " + str(len(votes)))
print("Unique voters: " + str(len(unique_voters)))
```

---

<div align="left">
  <a href="#s4.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.4"></a>

---

## 4.4. Set Operations: Intersection

```python
# Common elements in both sets
art_students = {'Tom', 'Alice', 'Bob', 'Eve'}
music_students = {'Alice', 'Eve', 'John'}

both = art_students & music_students
print("Students in both clubs: " + str(both))
```

---

<div align="left">
  <a href="#s4.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.5"></a>

---

## 4.5. Set Operations: Union

```python
# Combine sets (no duplicates)
week1_customers = {'Alice', 'Bob'}
week2_customers = {'Bob', 'Charlie'}

all_customers = week1_customers | week2_customers
print("All customers: " + str(all_customers))
```

---

<div align="left">
  <a href="#s4.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.6"></a>

---

## 4.6. Set Operations: Difference

```python
# Elements in first set not in second
available_colors = {'red', 'blue', 'green'}
used_colors = {'blue', 'yellow'}

remaining = available_colors - used_colors
print("Remaining colors: " + str(remaining))
```

---

<div align="left">
  <a href="#s4.5">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.7"></a>

---

## 4.7. Voting System Case Study

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
print("Candidates: " + ', '.join(unique_votes))
```

<br>

### Q: how can we get the number of votes? hint: use dict

<br>

---

<div align="left">
  <a href="#s4.6">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.8"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.8"></a>

---

## 4.8. Friend Finder System

```python
# Finding common friends
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Charlie', 'Diana', 'Eve'}

common = alice_friends & bob_friends
print("Common friends: " + str(common))

# Adding new friend
alice_friends.add('Eve')
print("Updated friends: " + str(alice_friends))
```

---

<div align="left">
  <a href="#s4.7">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.9"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.9"></a>

---

## 4.9. Set Methods Cheat Sheet

| Method      | Example                     | Description                 |
|-------------|-----------------------------|-----------------------------|
| `add()`     | `s.add('x')`                | Add element                 |
| `remove()`  | `s.remove('x')`             | Remove element              |
| `clear()`   | `s.clear()`                 | Empty the set               |
| `copy()`    | `new_set = s.copy()`        | Create duplicate            |

## List also has "clear()" and "copy()"

---

<div align="left">
  <a href="#s4.8">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s4.10"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s4.10"></a>

---

## 4.10. Why Use Sets?

1. **Fast membership testing**: `'a' in set`
2. **Mathematical operations**: Easy intersections/unions
3. **Data cleaning**: Quick duplicate removal
4. **Relationship modeling**: Social networks, groups

<br>

### Q: write a program to get all unique letters in your name?

<br>

---

<div align="left">
  <a href="#s4.9">← Prev </a> | <a href="#all"> Home </a> |  <a href="#s5.0"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.0"></a>

# Section 5. Data Structures in Action

<div align="left">
  <a href="#s4.10">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.1"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.1"></a>

---

## 5.1. Student Information System Demo

### 0. A demo

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
    print(a)

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

<br>

### Q: What happended here ?
### mutable variable: list, dict, set

### Variable "assignment" and "modifying its contents" (mutable) are two different things!
### Assignment = replacing the box → requires global
### Modifying contents = changing what’s inside the box → no global needed



<br>

---

<div align="left">
  <a href="#s5.0">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.2"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.2"></a>

---

## 5.2. Storing Students

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

<div align="left">
  <a href="#s5.1">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.3"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.3"></a>

---

## 5.3. Adding Students

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

<div align="left">
  <a href="#s5.2">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.4"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.4"></a>

---

## 5.4. Sorting Students

<br>

### Q: add two students, order students by age ?

<br>

---

<div align="left">
  <a href="#s5.3">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.5"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.5"></a>

---

## 5.5. Word Frequency Analyzer

### 1. Splitting Text

```python
text = "apple banana orange apple pear orange apple ok yes yes ok no no want"
words = text.lower().split()

print(words)
```

---

<div align="left">
  <a href="#s5.4">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.6"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.6"></a>

---

## 5.6. Counting Words

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

<div align="left">
  <a href="#s5.5">← Prev </a> |  <a href="#all"> Home </a> | <a href="#s5.7"> Next →</a>
</div>

<div style="height: 1000px;">&nbsp;</div>

<a id="s5.7"></a>

---

## 5.7. Finding TOP5 Words

<br>

### Q: How can we get top5 words?

<br>

---

<div align="left">
  <a href="#s5.6">← Prev </a> |  <a href="#all"> Home </a> 
</div>

<br>

End
