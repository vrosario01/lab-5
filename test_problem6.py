from problem6 import add_without_add

def test_add_without_add_normal():
    assert add_without_add(30, 4) == 34
    assert add_without_add(0, 0) == 0
    assert add_without_add(100, 10) == 110

def test_add_without_add_with_negative_numbers():
    assert add_without_add(-1, 0) == None
    assert add_without_add(3, -1) == None
    assert add_without_add(-2, -2) == None