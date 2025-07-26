# python collection
# Python Collections
# Python has several built-in collection types, which are used to store multiple items in a single variable.
# The main built-in collection types in Python are:
# 1. List: An ordered collection of items that can be changed (mutable).
# 2. Tuple: An ordered collection of items that cannot be changed (immutable).
# 3. Set: An unordered collection of unique items.
# 4. Dictionary: A collection of key-value pairs.
# List Example
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple Example
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set Example
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionary Example
my_dict = {"name": "Alice", "age": 30}
print("Dictionary:", my_dict)
# Accessing Elements in Collections
# You can access elements in collections using indexing or keys.
# Accessing List Elements
print("First element in list:", my_list[0])
# Accessing Tuple Elements
print("First element in tuple:", my_tuple[0])
# Accessing Set Elements
# Sets do not support indexing, but you can iterate through them.
for item in my_set:
    print("Set item:", item)
# Accessing Dictionary Elements
print("Name in dictionary:", my_dict["name"])
# Modifying Collections
# Lists can be modified by adding, removing, or changing elements.
my_list.append(6)  # Adding an element
print("Modified list:", my_list)
my_list.remove(2)  # Removing an element
print("List after removal:", my_list)
# Tuples cannot be modified, but you can create a new tuple.
my_new_tuple = my_tuple + (6,)  # Creating a new tuple
print("New tuple:", my_new_tuple)
# Sets can be modified by adding or removing elements.
my_set.add(6)  # Adding an element
print("Modified set:", my_set)