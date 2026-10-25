def wears_jacket(temp, raining):
    """ 
    signature: number, boolean --> boolean
    explanation: wears_jacket takes in values temp and raining and only returns true if the temp < 60 or it is raining and returns false otherwise
    doctests:
    >>> wears_jacket(70, True)
    True
    >>> wears_jacket(70, False)
    False
    >>> wears_jacket(50, False)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False





