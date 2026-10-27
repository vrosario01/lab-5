import numpy as np 
from lab4_problem2 import merge

def test_merge_if_array_is_alphebetically_sorted_string():
    assert (merge(np.array(["app", "cat", "eel"]), np.array(["blue", "dog","fish"])) == np.array(["app", "blue", "cat", "dog", "eel", "fish"])).all()
    assert (merge(np.array(["a", "b", "c"]), np.array(["d", "e", "f"])) == np.array(["a", "b", "c", "d", "e", "f"])).all()

def test_merge_if_array_sorted_array_has_duplicates():
    assert (merge(np.array([1, 2, 3]), np.array([1, 2, 3])) == np.array([1, 1, 2, 2, 3, 3])).all()
    assert (merge(np.array([5, 7, 7]), np.array([5, 6, 6])) == np.array([5, 5, 6, 6, 7, 7])).all()
