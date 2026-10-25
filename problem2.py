def is_triangle(a,b,c):
    """
    signature: number + number > number  --> Boolean
    explanation: the function takes in values a b c and returns true if the triangle ineqaulities are met otherwise it returns false
    dosctests:
    >>> is_triangle(3,4,5)
    True
    >>> is_triangle(4,7,10)
    True
    >>> is_triangle(5,3,10)
    False
    """
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
