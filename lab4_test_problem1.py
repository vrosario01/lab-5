import numpy as np
from lab4_problem1 import flatten

### have to use .all at the end of the assert statement because the assert checks for true or false for all elements seperately, so you have to compare the whole expected to the actual array
def test_flatten_if_1D_array():
    assert (flatten(np.array([12,10,8,6,4,7])) == np.array([12,10,8,6,4,7])).all()

def test_flatten_if_7D_array():
    assert (flatten(np.array([[[[[8,9],[11,14],[12,18],[18,19],[20,21],[22,23],[23,24],[15,16]]]]])) == np.array([8,9,11,14,12,18,18,19,20,21,22,23,23,24,15,16])).all()

def test_flatten_if_tuples_are_large():
    assert (flatten(np.array([[10,9,8,7,6,5,4,3,2,1,0],[0,1,2,3,4,5,6,7,8,9,10]])) == np.array([10,9,8,7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7,8,9,10])).all()

def test_flatten_if_array_inside_array():
    assert (flatten(np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])) == np.array([1,2,3,4,5,6,7,8,9,10,11,12])).all()
    assert (flatten(np.array([[[12,8,6,4],[1,2,3,4]],[[9,10,11,12],[13,14,15,16]],[[1,2,3,4],[1,2,5,6]]])) == np.array([12,8,6,4,1,2,3,4,9,10,11,12,13,14,15,16,1,2,3,4,1,2,5,6])).all()