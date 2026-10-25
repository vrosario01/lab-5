from problem7 import  sum_id, sum_squares, f, sum, product, combine_sequence
  


def test_sum_id_big_numbers():
    assert sum_id(20) == 210
    assert sum_id(100) == 5050
    assert sum_id(200) == 20100

def test_sum_id_zero_and_decimals_return_none():
    assert sum_id(0) is None
    assert sum_id(0.25) is None
    assert sum_id(2.7) is None
    assert sum_id(0.4) is None


def test_sum_squares_positive_numbers():
    assert sum_squares(1) == 1
    assert sum_squares(4) == 30
    assert sum_squares(10) == 385

def test_sum_with_different_functions_and_big_numbers():
    assert sum(10, f=lambda x: x+5) == 105
    assert sum(2, f=lambda x: x*100) == 300
    assert sum(200, f=lambda x: x) == 20100

def test_product_complex_numbers_and_functions_with_lambda():
    assert product(7, f) == 40320
    assert product(3, lambda x: x * x) == 36
    assert product(60, f) == 507580213877224798800856812176625227226004528988036003099405939480985600000000000000

def test_combine_sequences_specified_cases_that_are_not_default():
    assert combine_sequence(3, f, combine=lambda a, b: a // b) == 4
    assert combine_sequence(4, f, combine=lambda a, b: a - b) == 2
    assert combine_sequence(3, f, combine=lambda a, b: a * b) == 24
