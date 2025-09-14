
<br>
<br>
<br>

## Open Question: What's the "previous" evolutionary direction of programming languages ? 

<br>
<br>
<br>
<br>
<br>
<br>

## Question: What's the difference between "variable" in programming language and the "object" (e.g. a bird) in the real world ?

<br>
<br>
<br>
<br>
<br>
<br>


## Section 01. Procedural Programming VS. Object-Oriented Programming

### Programming Styles

**Procedural Programming**:
```python
# Step-by-step instructions
def calculate_area(width, height):
    return width * height

print(calculate_area(5, 3))
```

**Object-Oriented Programming**:
```python
# Create objects with properties and abilities
class Rectangle:
    def __init__(self, width, height):   ## Initialization Method/Function (or Constructor)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

my_rect = Rectangle(5, 3)
print(my_rect.area())
```

## Question: What's the difference between them two?

<br>
<br>


---
### Real-World Objects Example
Your phone:
- **Attributes** (what it *is*):
  - color = "Space Gray"
  - brand = "Apple"
- **Methods** (what it *can do*):
  - make_call()
  - take_photo()

---
### Classes are Blueprints
```python
# Phone 
class Phone:
    def __init__(self, color, brand):   
        self.color = color  # Attribute
        self.brand = brand  # Attribute
    
    def ring(self):  # Method
        return self.color+' '+self.brand+' Phone: '+ "Ring ring!"


my_phone = Phone('Red', 'Apple')
print(my_phone.ring())

```

---
### Objects are Real Things
```python
# Create actual phones
my_phone = Phone("Black", "Samsung")
friends_phone = Phone("Rose Gold", "iPhone")

print(my_phone.brand)  
print(friends_phone.ring())   
```

---
### Attributes in Action
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Dog("Buddy", 2)
print(f"{my_pet.name} is {my_pet.age} years old")
# Output: Buddy is 2 years old
```

---
### Methods Make Things Happen
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof! Woof!")
    
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! Now {self.age} years old")

my_pet = Dog("Buddy", 2)
print(my_pet.age)
my_pet.bark()      # Output: Woof! Woof!
my_pet.birthday()  # Output: Happy Birthday! Now 3 years old

```

<br>
<br>

## Question: what's the output of "print(my_pet.age)" after "my_pet.birthday()"?

<br>
<br>

---
### Let's Make a Car!
```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0
    
    def accelerate(self):
        self.speed += 10
        print(f"Vroom! Speed: {self.speed}km/h")
    
    def brake(self):
        self.speed = 0
        print("Screeech! Stopped!")

my_car = Car("Model S", "Red")
my_car.accelerate()  # Output: Vroom! Speed: 10km/h
```

---

<br>
<br>

## Question: Why Use Object-oriented programming?

<br>
<br>

---

<br>
<br>

## Section 02. Revisit details of Object-Oriented Programming
## Creating Class and Object

---

### What is a Class?
A **class** is like a blueprint for creating objects  
Example blueprints:  
- Student blueprint: `name`, `age`  
- Car blueprint: `color`, `model`

---

### Creating a Simple Class
Basic class definition syntax:
```python
class Student:
    # Special initialization method
    def __init__(self, name, age):
        self.name = name  # Create name attribute
        self.age = age    # Create age attribute
```
- `self`: Reference to the instance/object itself  
- `__init__`: Constructor that runs when object is created

---

### Let's Make a Student Object!
Creating instances (objects) from class:
```python
# Creating student objects
stu1 = Student("Xiao Ming", 18)
stu2 = Student("Li Hua", 17)

print(stu1.name)  # Output: Xiao Ming
print(stu2.age)   # Output: 17
```

---
<br>
<br>

## Question: What's Happening in __init__?

<br>
<br>
---

### Let's Add Some Personality!
Customizing object display with `__str__`:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

stu = Student("Anna", 19)

```
<br>
<br>

## Question: What will happen when enter "str(stu)" and "print(stu)" ?

<br>
<br>

---

### GameCharacter
Let's create a game character class:
```python
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def __str__(self):
        return f"{self.name} (❤{self.health})"

player1 = GameCharacter("Warrior", 100)
print(player1)  
```


---

## Question: What's wrong here?

```python
class Cat:
    def __init__(name, color):
        name = color

my_cat = Cat("Whiskers", "orange")
```

## Question: What's the correct version?

---

<br>
<br>


## Section 03. Class Members

---

## Two types of properties:
  - Instance Attributes
  - Class Attributes
## Three types of methods:
  - Instance Methods
  - Static Methods
  - Class Methods

---

### Instance Attributes
Attributes unique to each object
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

# Create two dogs
buddy = Dog("Buddy")
max = Dog("Max")

print(buddy.name)  # Output: Buddy
print(max.name)    # Output: Max
```

---

### Class Attributes 
Shared by all instances of the class
```python
class Dog:
    species = "Mammal"  # Class attribute
    
    def __init__(self, name):
        self.name = name

buddy = Dog("Buddy")
max = Dog("Max")

print(Dog.species)        # Output: Mammal
print(buddy.species)      # Output: Mammal
print(max.species)        # Output: Mammal
```

---

### Changing Class Attributes
```python
Dog.species = "Doggy"

```

<br>

## Question: What's the output of "print(buddy.species)"?

<br>
<br>

---

### Instance Methods 
Work with instance attributes
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):  # Instance method
        print(f"{self.name} says: Woof!")

buddy = Dog("Buddy", 3)
buddy.bark()  # Output: Buddy says: Woof!
```

---

### Static Methods 
Utility methods that don't need object data
```python
import random
class Dog:
    @staticmethod
    def random_name():
        names = ["Buddy", "Max", "Charlie"]
        return random.choice(names)


# No need to create object!
print(Dog.random_name())  # Output: Random name
```

---

### Class Methods 
Work with class-level attributes
```python
class Dog:
    species = "Mammal"
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

Dog.change_species("Doggy")
print(Dog.species)  
```

---

### Method Type Comparison
|               | Instance Method | Static Method | Class Method |
|---------------|------------------|---------------|--------------|
| Parameter     | `self`          | None          | `cls`        |
| Can modify... | Instance data   | Nothing       | Class data   |
| Called via... | Object          | Class/Object  | Class/Object |

---
<br>
<br>

## Question: Who can use simple words to describe the differences among them three?

<br>
<br>




### Let's Make a Robot! 
```python
class Robot:
    population = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name
        Robot.population += 1
    
    @classmethod
    def count_robots(cls):
        print(f"There are {cls.population} robots")
    
    @staticmethod
    def robot_law():
        print("1. A robot may not harm humanity")

r2d2 = Robot("R2-D2")
c3po = Robot("C-3PO")


```
<br>
<br>

## Question: What's the output of "Robot.count_robots()"? Why?

<br>
<br>
---

### Why Different Methods?
- **Instance methods**: Work with object-specific data
- **Class methods**: Manage class-wide settings
- **Static methods**: For utility functions related to class




<br>
<br>

---

## Section 04. Inheritance


### Inheritance: Like Family Traits 
```python
class Animal:
    def eat(self):
        print("Nom nom nom!")

class Cat(Animal):  # Inherits from Animal
    def meow(self):
        print("Meow! I'm a special cat")

# Let's create our first family
kitty = Cat()
kitty.eat()  # From Animal parent
kitty.meow() # From Cat child
```

---

### Benefits:
- Reuse existing code
- Create logical relationships
- Extend functionality

---

### Puppies 
```python
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Test our puppy
buddy = Dog()
buddy.eat()  # Inherited method
buddy.bark() # New method
```

---

### Method Overriding: Customizing Behavior
```python
class PickyCat(Cat):
    def eat(self):  # Override parent method
        print("I only eat tuna!")

# Test our picky cat
princess = PickyCat()
princess.eat()  # Uses overridden method
princess.meow() # Inherited from Cat
```

<br>
<br>

## Question: Why do we need "Method Overriding" ?

<br>
<br>

---

### Super() in Action 
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Rabbit(Animal):
    def __init__(self, name, ear_length):
        super().__init__(name)  # Call parent's __init__
        self.ear_length = ear_length

# Create a fluffy friend
bugs = Rabbit("Bugs", 10)
print(f"{bugs.name} has {bugs.ear_length}cm ears")
```

<br>
<br>

## Question: What's happening here?

<br>
<br>



---

### Real-world Example: Game Characters 
```python
class GameCharacter:
    def move(self):
        print("Moving forward")

class Mario(GameCharacter):
    def jump(self):
        print("Jumping high!")

class SuperMario(Mario):
    def move(self):  # Override with new ability
        print("Flying while moving!")
        super().move()  

# Test our hero
sm = SuperMario()

```

<br>
<br>

## Question: What will happen after typing "sm.move()"?

<br>
<br>


---



---

### Question: Who can help me to create a helicopter class?
```python
class Vehicle:
    def transport(self):
        print("Moving something")

# Create a Helicopter class that:
# 1. Inherits from Vehicle
# 2. Adds rotate() method
# 3. Overrides transport() to print "Flying"

# Type your solution here...
```

<br>
<br>
<br>
<br>
<br>
<br>

### Solution Check 
```python
class Helicopter(Vehicle):
    def rotate(self):
        print("Rotating blades")
    
    def transport(self):
        print("Flying through air")

# Test it
chopper = Helicopter()
chopper.transport()
chopper.rotate()
```

---

## Section 05. Polymorphism in Python

---

## What is Polymorphism? 
- **Greek roots**: "poly" (many) + "morph" (form)
- One method name, multiple reactions.
- Two main types:
  - Inheritance-based (using parent classes)
  - method name matching (duck typing)

---

## Inheritance Review
```python
class Animal:
    def speak(self):
        return "ok"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

---

## Example
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return 3.14 * self.r ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
```

---

## Using the Shape Classes
```python
shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 78.5
# Area: 16
```
- Different objects responding to same method call
- Uniform interface despite different implementations

---

## Duck Typing basics
- "If it walks like a duck and quacks like a duck..."
- Focus on **behavior** not type
- Example with file-like objects:

```python
class FileReader:
    def read(self):
        return "File content"

class NetworkStream:
    def read(self):
        return "Network data"
```

---

## Duck Typing basics
```python
def read_data(source):
    print(source.read())

file = FileReader()
stream = NetworkStream()

read_data(file)    # Output: File content
read_data(stream)  # Output: Network data
```
- Both classes have `read()` method
- No need for common parent class

---

## Real-World Example: Game Characters
```python
class Archer:
    def attack(self):
        return "Shoots arrow"

class Knight:
    def attack(self):
        return "Sword slash"

class Wizard:
    def attack(self):
        return "Casts fireball"

characters = [Archer(), Knight(), Wizard()]
for char in characters:
    print(char.attack())
```

<br>
<br>

## Question: What is Polymorphism? Why is it important?

<br>
<br>

---

## Section 06. More Cases
### **Case 1: Bank Account System**
```python
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
    
    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")

# Create account
my_account = BankAccount("123-456")
my_account.deposit(100.50)
my_account.withdraw(25.75)
my_account.check_balance()

```

<br>

## Question: Who can explian the usage of this class?

<br>
<br>

---

### **Case 2: Game Character Basics**
```python
class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
    
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}!")

# Create base characters
warrior = GameCharacter("Alice")
wizard = GameCharacter("Bob")
wizard.attack(warrior)
```

<br>
<br>

## Question: what's the output of "warrior.health" ? 

<br>
<br>

---

### **Warrior Subclass**
```python
class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150  # Warriors have more health
    
    def shield_bash(self, target):
        target.health -= 20
        print(f"{self.name} uses shield bash!")

tank = Warrior("Hercules")
```

---

### **Mage Subclass**
```python
class Wizard(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 5  # Mages have weaker physical attacks
    
    def fireball(self, target):
        target.health -= 40
        print(f"{self.name} casts fireball!")

gandalf = Wizard("Gandalf")
```

---

### **Character Battle Demo**
```python
tank.shield_bash(gandalf)
gandalf.fireball(tank)

print(f"{tank.name} health: {tank.health}")
print(f"{gandalf.name} health: {gandalf.health}")

```

<br>
<br>

## Question: What are the outputs?

<br>
<br>
<br>

## Open Question: What's the "future" evolutionary direction of programming languages ? 

<br>
<br>
<br>


## Self-learning: Abstract Class
