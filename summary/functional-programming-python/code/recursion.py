def factorial(n):
    """Calculate the factorial of n using recursion."""
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
print(factorial(5))  # Output: 120