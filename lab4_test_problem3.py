import numpy as np
from lab4_problem3 import csv_string_to_array


def test_converts_csv_string_to_two_rows():
    assert (csv_string_to_array("1,2,3,4,5,6,7,8") == np.array([[1, 2, 3, 4], [5, 6, 7, 8]])).all()


def test_converts_string_with_trailing_comma():
    assert (csv_string_to_array("10,20,30,40,50,60,70,80,") == np.array([[10, 20, 30, 40], [50, 60, 70, 80]])).all()