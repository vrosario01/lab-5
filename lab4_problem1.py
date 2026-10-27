
import numpy as np
def flatten(arr):
  """
  signature: multidimensional array -> 1D array
  explanation: This function takes in a multidimensional array and returns a flattened version.
  doctests:
  >>> flatten(np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]))
  array([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  >>> flatten(np.array([[9, 10, 19], [6, 2, 0]]))
  array([ 9, 10, 19,  6,  2,  0])
  >>> flatten(np.array([[[1, 8], [9, 0]], [[8, 3], [4, 7]]]))
  array([1, 8, 9, 0, 8, 3, 4, 7])
  """
  all_numbers_in_arr = np.prod(arr.shape)
  return arr.reshape(all_numbers_in_arr)