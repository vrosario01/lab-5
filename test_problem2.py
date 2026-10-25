from problem2 import is_triangle

def test_is_triangle_True():
    assert is_triangle(3,4,5) == True
    assert is_triangle(4,7,10) == True
    assert is_triangle(5,6,7) == True

def test_is_triangle_is_eqauilateral_triangle_True():
    assert is_triangle(1,1,1) == True
    assert is_triangle(2,2,2) == True 

def test_is_triangle_ineqaulities_are_greater_or_less_than_and_eqaul_to_False():
    assert is_triangle(1,2,3) == False
    assert is_triangle(3,2,1) == False
    assert is_triangle(1,3,2) == False


