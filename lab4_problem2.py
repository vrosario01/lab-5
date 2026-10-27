
import numpy as np
sorted_arr1 = np.array([1,2,3,9])
sorted_arr2 = np.array([5,6,7,8])
def merge(sorted_arr1, sorted_arr2):
    """
    signature: (1D array, 1D array) -> 1D array
    explanation: this function merges the two sorted arrays and then return a new array "merged" in ascending order
    doctests:
    >>> merge(np.array([1, 2, 3, 9]), np.array([5, 6, 7, 8]))
    array([1, 2, 3, 5, 6, 7, 8, 9])
    >>> merge(np.array([1, 10, 15]), np.array([2, 8]))
    array([ 1,  2,  8, 10, 15])
    >>> merge(np.array([5, 10, 15]), np.array([0, 20, 25]))
    array([ 0,  5, 10, 15, 20, 25])
     """
    merged = np.concatenate((sorted_arr1, sorted_arr2))
    return np.sort(merged)

print(merge(sorted_arr1, sorted_arr2))