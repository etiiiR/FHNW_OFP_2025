# higher_order_functions.py

def apply_function(func, value):
    """Applies a given function to a value."""
    return func(value)

def square(x):
    """Returns the square of a number."""
    return x * x

def double(x):
    """Returns double the value of a number."""
    return x * 2

def higher_order_example():
    """Demonstrates the use of higher-order functions."""
    # Using apply_function with square
    result_square = apply_function(square, 5)
    print(f"Square of 5: {result_square}")

    # Using apply_function with double
    result_double = apply_function(double, 5)
    print(f"Double of 5: {result_double}")

def create_multiplier(factor):
    """Returns a function that multiplies its input by a given factor."""
    def multiplier(x):
        return x * factor
    return multiplier

def higher_order_closure_example():
    """Demonstrates closures with higher-order functions."""
    triple = create_multiplier(3)
    quadruple = create_multiplier(4)

    print(f"Triple of 5: {triple(5)}")
    print(f"Quadruple of 5: {quadruple(5)}")

if __name__ == "__main__":
    higher_order_example()
    higher_order_closure_example()