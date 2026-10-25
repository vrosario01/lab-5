def successor(x):
    return x + 1


def add_without_add(a, b):
    """
    signature: number, number --> number + number (without actually using +)
    explanation: this function takes in 2 values a and b and returns the sum of a and b without using the + operator. or any other arithmetic operators. 
    doctests:
    >>> add_without_add(1, 4)
    5
    >>> add_without_add(6, 4)
    10
    >>> add_without_add(10, 10)
    20
    """
    ### cannot take in negative numbers because successor only works with nonnegative integers
    if a < 0 or b < 0:
        return None
    result = a
    for _ in range(b):
        result = successor(result)
    return result
