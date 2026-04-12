[Back](https://www.bioinfo-lab.com/courses/Programming_I/w07_Data_Structure/)

<br>

---

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the <b>"Weekly Report Assignment"</b> on Moodle by 23:59 this Sunday. 

This is an important part of your "General Performance". Please ensure timely submission!!!

### Recommended: 2、3、4、5、6、8、14、15、18、22


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

### 2. Create and Run Your First List Script

```
# Create a new Python script file
cd ~
nano list_demo.py

# Type the following code in nano:
# Shopping list example
groceries = ["apples", "milk", "eggs", "bread"]
print("My shopping list:", groceries)

# Save: Ctrl + O
# Exit: Ctrl + X

# Run the script
python3 list_demo.py
```

<br>

---

### 3. Four Ways to Create Lists

```
# Create a new script file
cd ~
nano list_creation.py

# Type the following code:
# Method 1: Square brackets
colors = ["red", "green", "blue"]
print("Colors:", colors)

# Method 2: list() constructor
numbers = list((1, 2, 3))
print("Numbers:", numbers)

# Method 3: List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# Method 4: Convert from string
word = list("hello")
print("Word as list:", word)

# Save and exit nano
# Run the script
python3 list_creation.py
```

<br>

---

### 4. Accessing and Slicing List Elements

```
# Create a new script file
cd ~
nano list_access.py

# Type the following code:
games = ["Mario", "Zelda", "Pokémon"]
print("First game:", games[0])
print("Last game:", games[-1])

months = ["Jan", "Feb", "Mar", "Apr", "May"]
print("Months 1-3:", months[1:3])
print("First two:", months[:2])
print("Last two:", months[3:])

# Save and exit nano
# Run the script
python3 list_access.py
```

<br>

---

### 5. Modifying Lists - Adding Items

```
# Create a new script file
cd ~
nano list_add.py

# Type the following code:
todo = ["wake up"]
todo.append("brush teeth")
todo.insert(1, "make bed")
print("Todo list:", todo)

# Demonstrate insert positions
todo.insert(0, 'start')  # Add at beginning
print("After insert(0, 'start'):", todo)

todo.insert(len(todo), 'end1')  # Add at end (like append)
print("After insert(len(todo), 'end1'):", todo)

todo.insert(-1, 'end2')  # Insert before last element
print("After insert(-1, 'end2'):", todo)

# Save and exit nano
# Run the script
python3 list_add.py
```

<br>

---

### 6. Modifying Lists - Removing Items

```
# Create a new script file
cd ~
nano list_remove.py

# Type the following code:
pets = ["cat", "dog", "hamster"]
pets.remove("dog")
last = pets.pop()
print("Pets after removal:", pets)
print("Popped item:", last)

# Demonstrate remove with duplicates
pets = ["dog", "bird", "dog", "cat", "dog"]
pets.remove("dog")  # Only removes first occurrence
print("After removing first 'dog':", pets)

# Find index of an element
dog_index = pets.index('dog')
print("Index of 'dog':", dog_index)

# Save and exit nano
# Run the script
python3 list_remove.py
```

<br>

---

### 7. Sorting Lists

```
# Create a new script file
cd ~
nano list_sort.py

# Type the following code:
scores = [88, 92, 75, 100]
scores.sort()
print("Sorted scores:", scores)

scores.sort(reverse=True)
print("Reverse sorted:", scores)

# Save and exit nano
# Run the script
python3 list_sort.py
```

<br>

---

### 8. Student Grades System Practice

```
# Create a new script file
cd ~
nano student_grades.py

# Type the following code:
students = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

# Calculate average
total = sum(scores)
average = total / len(scores)
print(f"Class average: {average}")

# Alternative format using concatenation
print("Class average: " + str(average))

# Combine and sort by score
combined = []
i = 0
while i < len(scores):
    combined.append([scores[i], students[i]])
    i = i + 1

combined.sort()
print("Ranking (low to high):")
for one in combined:
    print(f"{one[1]}: {one[0]}")

# Sort in reverse order
combined.sort(reverse=True)
print("Ranking (high to low):")
for one in combined:
    print(f"{one[1]}: {one[0]}")

# Save and exit nano
# Run the script
python3 student_grades.py
```

<br>

---

### 9. Understanding Tuples - Immutability Demo

```
# Create a new script file
cd ~
nano tuple_demo.py

# Type the following code:
# Lists are mutable
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"
print("Modified list:", fruits)

# Tuples are immutable
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Attempting to modify will cause error
# colors[0] = "pink"  # Uncomment to see TypeError

# Valid tuple usage
black = (0, 0, 0)
current_position = (37.7749, -122.4194)
print("Color tuple:", black)
print("Position tuple:", current_position)

# Save and exit nano
# Run the script
python3 tuple_demo.py
```

<br>

---

### 10. Tuple Unpacking

```
# Create a new script file
cd ~
nano tuple_unpack.py

# Type the following code:
# Basic unpacking
dimensions = (1920, 1080)
width, height = dimensions
print(f"Screen: {width}x{height}")

# Swapping variables
a = 5
b = 10
a, b = b, a
print(f"Swapped: a={a}, b={b}")

# Ignoring values
coordinates = (45, -73, 100)
lat, lon, _ = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Multiple assignment with *middle
numbers = (3, 1, 4, 1, 5, 9)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Save and exit nano
# Run the script
python3 tuple_unpack.py
```

<br>

---

### 11. Single-element Tuple Trap

```
# Create a new script file
cd ~
nano tuple_single.py

# Type the following code:
# Common mistake
not_a_tuple = (42)
print("Type of (42):", type(not_a_tuple))

# Correct way
proper_tuple = (42,)
print("Type of (42,):", type(proper_tuple))

# Accessing elements
print("First element:", proper_tuple[0])
# print("Second element:", proper_tuple[1])  # Uncomment to see IndexError

# Save and exit nano
# Run the script
python3 tuple_single.py
```

<br>

---

### 12. Returning Multiple Values from Functions

```
# Create a new script file
cd ~
nano tuple_return.py

# Type the following code:
def circle_calc(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return (area, circumference)

# Using tuple return
results = circle_calc(5)
print(f"Area: {results[0]}, Circumference: {results[1]}")

# Better usage with unpacking
area, circ = circle_calc(7)
print(f"Area is {area} units")
print(f"Circumference is {circ} units")

# Save and exit nano
# Run the script
python3 tuple_return.py
```

<br>

---

### 13. When to Use Tuples and Tuple Operations

```
# Create a new script file
cd ~
nano tuple_usage.py

# Type the following code:
# Dictionary keys (tuples work, lists don't)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
print("Location lookup:", locations[(40.7128, -74.0060)])

# Tuple operations
my_tuple = (1, 2, 3, 2, 2)
print("Length:", len(my_tuple))
print("Count of 2:", my_tuple.count(2))
print("Index of 3:", my_tuple.index(3))
print("2 in tuple:", 2 in my_tuple)

# Remember: No append/remove/pop methods for tuples

# Save and exit nano
# Run the script
python3 tuple_usage.py
```

<br>

---

### 14. Creating Dictionaries

```
# Create a new script file
cd ~
nano dict_create.py

# Type the following code:
# Method 1: Curly braces
student = {"name": "Emma", "age": 20, "major": "CS"}
print("Student:", student)

# Method 2: dict() constructor
colors = dict(red="#FF0000", green="#00FF00")
print("Colors:", colors)

# Method 3: List of tuples
weekdays = dict([(1, "Mon"), (2, "Tue"), (3, "Wed")])
print("Weekdays:", weekdays)

# Phone book example
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
print("Alice's number:", phone_book["Alice"])

# Save and exit nano
# Run the script
python3 dict_create.py
```

<br>

---

### 15. Modifying Dictionaries

```
# Create a new script file
cd ~
nano dict_modify.py

# Type the following code:
animal_sounds = {}
animal_sounds["dog"] = "Woof!"
animal_sounds["cat"] = "Mew"
animal_sounds["cat"] = "Meow"  # Update existing
print("Animal sounds:", animal_sounds)

# Removing entries
del animal_sounds["dog"]
removed = animal_sounds.pop("cat")
print("Removed value:", removed)
print("After removals:", animal_sounds)

# Safe access with get()
grades = {"Math": 90, "Science": 85}
print("History grade:", grades.get("History", "Subject not found"))

# Save and exit nano
# Run the script
python3 dict_modify.py
```

<br>

---

### 16. Building a Simple Translator

```
# Create a new script file
cd ~
nano translator.py

# Type the following code:
translator = {
    "hello": "hola",
    "goodbye": "adiós",
    "thank you": "gracias"
}

word = input("Enter English word: ").lower()
translation = translator.get(word, "Translation not available")
print(f"Spanish: {translation}")

# Handle unknown words
if translation == "Translation not available":
    print("Please check spelling!")
    print("Current dictionary words:", list(translator.keys()))

# Save and exit nano
# Run the script
python3 translator.py
```

<br>

---

### 17. Dictionary Methods and Real-World Example

```
# Create a new script file
cd ~
nano dict_methods.py

# Type the following code:
my_dict = {"a": 1, "b": 2}
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))

# Movie ratings example
movies = {
    "Moana": 7.5,
    "Toy Story": 8.6,
    "Frozen": 8.5
}

movie = input("Enter movie title: ")
print(f"Rating: {movies.get(movie, 'Not in database')}/10")

# Mixed data types in dictionaries
mixed_example = {
    1: "Number key",
    (2,3): "Tuple key",
    "list": ["can", "be", "value"]
}
print("Mixed dictionary:", mixed_example)

# Save and exit nano
# Run the script
python3 dict_methods.py
```

<br>

---

### 18. Understanding Sets - Automatic Deduplication

```
# Create a new script file
cd ~
nano set_dedup.py

# Type the following code:
# List vs Set comparison
fruits_list = ['apple', 'banana', 'apple', 'orange']
fruits_set = {'apple', 'banana', 'apple', 'orange'}

print(f"List: {fruits_list}")
print(f"Set: {fruits_set}")

# Removing duplicate votes
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_voters = set(votes)
print(f"Total votes: {len(votes)}")
print(f"Unique voters: {len(unique_voters)}")

# Get unique letters in a name
name = "yourname"
unique_letters = set(name)
print(f"Unique letters in '{name}': {unique_letters}")

# Save and exit nano
# Run the script
python3 set_dedup.py
```

<br>

---

### 19. Set Operations

```
# Create a new script file
cd ~
nano set_operations.py

# Type the following code:
art_students = {'Tom', 'Alice', 'Bob', 'Eve'}
music_students = {'Alice', 'Eve', 'John'}

# Intersection (common elements)
both = art_students & music_students
print(f"Students in both clubs: {both}")

# Union (combine sets)
week1_customers = {'Alice', 'Bob'}
week2_customers = {'Bob', 'Charlie'}
all_customers = week1_customers | week2_customers
print(f"All customers: {all_customers}")

# Difference (elements in first but not second)
available_colors = {'red', 'blue', 'green'}
used_colors = {'blue', 'yellow'}
remaining = available_colors - used_colors
print(f"Remaining colors: {remaining}")

# Save and exit nano
# Run the script
python3 set_operations.py
```

<br>

---

### 20. Set Methods and Voting System

```
# Create a new script file
cd ~
nano set_voting.py

# Type the following code:
# Counting unique votes with vote frequency
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
unique_votes = set(votes)
print(f"Candidates: {', '.join(unique_votes)}")

# Get vote counts using dictionary
vote_counts = {}
for candidate in votes:
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1
print("Vote counts:", vote_counts)

# Friend finder system
alice_friends = {'Bob', 'Charlie', 'Diana'}
bob_friends = {'Charlie', 'Diana', 'Eve'}
common = alice_friends & bob_friends
print(f"Common friends: {common}")

alice_friends.add('Eve')
print(f"Updated Alice's friends: {alice_friends}")

# Set methods demo
s = {'a', 'b', 'c'}
s.add('x')
print("After add:", s)
s.remove('b')
print("After remove:", s)

# Save and exit nano
# Run the script
python3 set_voting.py
```

<br>

---

### 21. Data Structures in Action - Mutable vs Immutable

```
# Create a new script file
cd ~
nano data_structure_mutable.py

# Type the following code:
# List (mutable)
a = []
def add_list():
    a.append(1)
add_list()
print("List after function call:", a)

# Set (mutable)
a = set()
def add_set():
    a.add(1)
add_set()
print("Set after function call:", a)

# Dictionary (mutable)
a = {}
def add_dict():
    a[1] = 1
add_dict()
print("Dict after function call:", a)

# Integer (immutable)
a = 0
def add_int():
    # This would cause error: a = a + 1
    # Because 'a' is local to function
    pass
add_int()
print("Integer unchanged:", a)

# Save and exit nano
# Run the script
python3 data_structure_mutable.py
```

<br>

---

### 22. Student Information System

```
# Create a new script file
cd ~
nano student_system.py

# Type the following code:
students = []

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

# Add two students
add_student()
add_student()

# Sort students by age
students.sort(key=lambda x: x['age'])
print("\nStudents sorted by age:")
for s in students:
    print(f"{s['name']}: {s['age']} years, {s['major']}")

# Save and exit nano
# Run the script
python3 student_system.py
```

<br>

---

### 23. Word Frequency Analyzer

```
# Create a new script file
cd ~
nano word_frequency.py

# Type the following code:
text = "apple banana orange apple pear orange apple ok yes yes ok no no want"
words = text.lower().split()
print("Words:", words)

# Count word frequencies
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Word counts:", word_counts)

# Find top 5 words
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 words:")
for i in range(min(5, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{i+1}. {word}: {count}")

# Save and exit nano
# Run the script
python3 word_frequency.py
```

<br>

---

End
