from math import factorial


def trailing_zeros(n):
    """ 
    signature: n --> # of trailing zeros in n 
    explanation: trailing_zeros(n) takes in a value n and if the remainder of n once divided by 10 is eqaul to 0 it returns the number of trailing zeros otherwise it returns 0 
    doctests:
    >>> trailing_zeros(4000)
    3
    >>> trailing_zeros(100)
    2
    >>> trailing_zeros(100000)
    5
    """
    if n % 10 == 0:
        return 1 + (trailing_zeros(n // 10))
    else:
        return 0
    
### changed the original 2 functions to just be one function that uses factors of 5 to check the number of trailing zeros and then uses trailing_zeros_in_factorial to execute again(recursion) to check the number of trailing zeros in answer to n divided by 5. 
### math: The number of trailing zeros in n! is equal to the number of factors of 5 in n! 
def trailing_zeros_in_factorial(n):
    """
    signature: n --> # of trailing zeros in n!
    explanation: trailing_zeros_in_factorial(n) takes in a value n and returns the number of trailing zeros in n!
    doctests:
    >>> trailing_zeros_in_factorial(10)
    2
    >>> trailing_zeros_in_factorial(15)
    3
    >>> trailing_zeros_in_factorial(25)
    6
    """
    if n < 0:
        return "undefined"
    if n < 5:
        return 0
    return n // 5 + trailing_zeros_in_factorial(n // 5)



