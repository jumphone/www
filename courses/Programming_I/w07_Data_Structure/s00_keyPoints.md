# List, Tuple, Dictionary, Set

* Two ways to Create Lists: 1. Using square brackets `[]`, like `colors = ["red", "green", "blue"]`. 2. Using the `list()` constructor, like `numbers = list((1, 2, 3))`.

* Accessing Elements: Access list elements using positive or negative indexing, such as `games[0]` and `games[-1]`.

* Slicing Lists: Get sub-lists using `[start:end]`, like `months[1:3]`, `months[:2]`, and `months[3:]`.

* Adding Items: Use `append()` to add an element to the end of the list, like `todo.append("brush teeth")`. Use `insert()` to insert an element at a specified position, like `todo.insert(1, "make bed")`.

* Removing Items: Use `remove()` to remove an element by its value, like `pets.remove("dog")`. Use `pop()` to remove the last element or an element at a specified position, like `last = pets.pop()`.

* Sorting Lists: Use the `sort()` method to sort the list, like `scores.sort()`. You can sort in descending order using the `reverse=True` parameter, like `scores.sort(reverse=True)`.

* Tuples vs Lists: Tuples are immutable, while lists are mutable. Tuples use parentheses `()`, and lists use square brackets `[]`.

* Two ways to Create Dictionaries: 1. Using curly braces `{}`, like `student = {"name": "Emma", "age": 20, "major": "CS"}`. 2. Using the `dict()` constructor, like `colors = dict(red="#FF0000", green="#00FF00")`.

* Adding & Changing Entries: Add or update values in the dictionary using keys, like `animal_sounds["dog"] = "Woof!"`.

* Removing Entries: Use `del` to delete entries in the dictionary, like `del animal_sounds["dog"]`.

* Safe Value Access with get(): Use the `get()` method to access values in the dictionary, and return a default value if the key does not exist.

* Dictionary Methods Summary: `my_dict.keys()`: Get all the keys in the dictionary. `my_dict.values()`: Get all the values in the dictionary. `my_dict.items()`: Get all the key-value pairs in the dictionary.

* Two ways to Create Sets: 1. Using curly braces `{}`, like `colors = {"red", "green", "blue"}`. 2. Using the `set()` constructor, like `numbers = set([1,2,3,3])`.

* Set intersection: Use `&` to get the intersection of two sets, like `both = art_students & music_students`.

* Set union: Use `|` to combine two sets, like `all_customers = week1_customers | week2_customers`.

* Set difference: Use `-` to get elements in one set that are not in another, like `remaining = available_colors - used_colors`.

* Set Methods: a`add()`: Add an element. `remove()`: Remove an element. 
