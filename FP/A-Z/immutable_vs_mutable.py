def immutable_vs_mutable():
    """
    Demonstrates the difference between immutable and mutable data structures in Python.
    """
    # Immutable data structure: tuple
    immutable_tuple = (1, 2, 3)
    print("Immutable Tuple:", immutable_tuple)

    # Attempting to modify an immutable tuple will raise an error
    try:
        immutable_tuple[0] = 10
    except TypeError as e:
        print("Error:", e)

    # Mutable data structure: list
    mutable_list = [1, 2, 3]
    print("Mutable List before modification:", mutable_list)

    # Modifying a mutable list is allowed
    mutable_list[0] = 10
    print("Mutable List after modification:", mutable_list)
    
if __name__ == "__main__":
    immutable_vs_mutable()    