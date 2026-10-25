from problem4 import wears_jacket

def test_wears_jacket_temp_less_than_60_and_raining():
    assert wears_jacket(45, True) == True
    assert wears_jacket(50, True) == True

def test_wears_jacket_temp_less_than_60_and_not_raining():
    assert wears_jacket(45, False) == True
    assert wears_jacket(50, False) == True

def test_wears_jacket_true_temp_greater_than_60_and_raining():
    assert wears_jacket(65, True) == True
    assert wears_jacket(89, True) == True

def test_wears_jacket_temp_greater_than_60_and_not_raining():
    assert wears_jacket(70, False) == False
    assert wears_jacket(87, False) == False
