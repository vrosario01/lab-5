
def sum_id(n):
    """ 
    signature: number -> factorial(number) or sum
    explanation: sum_id(n) takes in a positive number n and returns the sum from 1 to n: 1+2+3+...+n 
    doctests:
    >>> sum_id(2)
    3
    >>> sum_id(3)
    6
    >>> sum_id(4)
    10
    """
    if not isinstance(n, int) or n <= 0:
        return None
    if n == 1:
        return 1
    else:
        return n + sum_id(n-1)



def sum_squares(n):
    """ 
    signature: number --> number**2
    explanation:sum_squares takes in a positive number n and if n = 1 returns 1 otherwise it returns the sum of the square of the numbers from 1 to n: 1^2+2^2+3^2+...+n^2.
    doctests:
    >>> sum_squares(2)
    5
    >>> sum_squares(3)
    14
    >>> sum_squares(4)
    30
    """
    if n == 1:
        return 1
    else:
        return n*n + sum_squares(n-1)

### changed from the original that just returned n so I can differentiate between the two functions better. 
def f(n):
    return n+1

def sum(n, f):
    """
    signature: number, function -> number 
    explanation: sum(n, f) takes in a number n and a function f and returns the sum of f applied to the numbers from 1 to n. ( number, function -> number + f)
    doctests:
     >>> sum(2, f)
     6
     >>> sum(1, f)
     2
     >>> sum(3, f)
     9
     """
    if n == 0:
        return 0
    return f(n) + sum(n - 1, f)

def product(n, f):
    """ 
    signature: number, function -> number 
    explanation: product(n, f) takes in a number n and a function f and returns the product of f applied to the numbers from 1 to n. (number, function -> number x f)
    doctests:
    >>> product(1, f)
    2
    >>> product(2, f)
    6
    >>> product(3, f)
    24
    """
    if n == 0:
        return 1
    return f(n) * product(n - 1, f)


def combine_sequence(n, f, combine=lambda a, b: a + b):
    """ 
    signature: number, function, function -> number
    explanation: combine_sequence  takes in a number n and two functions, one called combine and one called f, where f is the function as before and combine now controls the manner in which terms are combined.
    If not otherwise specified, combine_sequence sums the values of the function applied to the numbers from 1 to n.
    doctests:
    >>> combine_sequence(3, f)
    9
    >>> combine_sequence(4, f)
    14
    >>> combine_sequence(3, f, combine=lambda a, b: a * b)
    24
    """
    if n == 1:
        return f(1)
    return combine(f(n), combine_sequence(n - 1, f, combine))