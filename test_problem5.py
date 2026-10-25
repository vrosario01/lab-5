from problem5 import trailing_zeros, trailing_zeros_in_factorial

def test_trailing_zeros_with_no_trailing_zeros():
    assert trailing_zeros(4) == 0

def test_trailing_zeros_normal():
    assert trailing_zeros(10000000) == 7

from problem5 import trailing_zeros_in_factorial

def test_trailing_zeros_in_factorial_normal_big_numbers(): 
    assert trailing_zeros_in_factorial(100) == 24
    assert trailing_zeros_in_factorial(2000) == 499
    assert trailing_zeros_in_factorial(10000) == 2499

def test_trailing_zeros_in_factorial_with_no_trailing_zeros():
    assert trailing_zeros_in_factorial(2) == 0
    assert trailing_zeros_in_factorial(7) == 1

def test_trailing_zeros_in_factorial_negative_numbers():
    assert trailing_zeros_in_factorial(-1) == "undefined"
    assert trailing_zeros_in_factorial(-100) == "undefined"   
    assert trailing_zeros_in_factorial(-1000) == "undefined"
