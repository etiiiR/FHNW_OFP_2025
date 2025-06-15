# lambda_functions.py

# This file includes examples of lambda functions in Python, demonstrating how to create small anonymous functions for use in functional programming.

# Example 1: Basic Lambda Function
# A simple lambda function that adds two numbers
add = lambda x, y: x + y
print("Addition of 5 and 3:", add(5, 3))

# Example 2: Lambda Function with map
# Using lambda with map to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Example 3: Lambda Function with filter
# Using lambda with filter to get even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 4: Lambda Function with sorted
# Using lambda to sort a list of tuples by the second element
tuples = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted tuples by second element:", sorted_tuples)

# Example 5: Lambda Function as an Argument
# A higher-order function that takes a function as an argument
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * 10, 5)
print("Result of applying lambda function:", result)

# Example 6: Lambda Function with reduce
# Using lambda with reduce to calculate the product of a list of numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)