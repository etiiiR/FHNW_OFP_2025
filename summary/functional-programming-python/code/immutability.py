# immutability.py

# This file illustrates the concept of immutability in functional programming, showcasing how to work with immutable data structures in Python.

# Example 1: Using Tuples
# Tuples are immutable sequences in Python. Once created, their elements cannot be changed.

def demonstrate_tuples():
    my_tuple = (1, 2, 3)
    print("Original tuple:", my_tuple)
    
    # Attempting to change an element will raise an error
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print("Error:", e)

# Example 2: Using frozensets
# frozensets are immutable sets in Python.

def demonstrate_frozensets():
    my_set = frozenset([1, 2, 3])
    print("Original frozenset:", my_set)
    
    # Attempting to add an element will raise an error
    try:
        my_set.add(4)
    except AttributeError as e:
        print("Error:", e)

# Example 3: Using Strings
# Strings in Python are immutable. Any operation that modifies a string will return a new string.

def demonstrate_strings():
    my_string = "Hello"
    print("Original string:", my_string)
    
    # Modifying the string
    new_string = my_string.replace("H", "J")
    print("Modified string:", new_string)
    print("Original string after modification attempt:", my_string)

# Example 4: Using Named Tuples
# Named tuples provide a way to create immutable objects with named fields.

from collections import namedtuple

def demonstrate_named_tuples():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print("Original named tuple:", p)
    
    # Attempting to change a field will raise an error
    try:
        p.x = 30
    except AttributeError as e:
        print("Error:", e)

# Main function to run all demonstrations
if __name__ == "__main__":
    print("Demonstrating immutability in Python:")
    demonstrate_tuples()
    demonstrate_frozensets()
    demonstrate_strings()
    demonstrate_named_tuples()