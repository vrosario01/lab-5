
### create a randomly generated comma-separated string of values
###this creates a string of 400 randomly generated integer values between 0 and 10 with commas separating the numbers.
import numpy as np
rng = np.random.default_rng(10)
random_integers = rng.integers(0, 11, size = 400)
ran_int_string = random_integers.astype(str)
csv_string = ""
for x in ran_int_string:
    csv_string += str(x) + ","
def csv_string_to_array(csv_string):
    """
    signature: string -> 2d array
    explanation: this function converts a comma-separated string of integers into a 2D NumPy integer array with 4 values in each row.
    >>> csv_string_to_array("1,2,3,4,5,6,7,8")
    array([[1, 2, 3, 4],
           [5, 6, 7, 8]])
    >>> csv_string_to_array("10,20,30,40,50,60,70,80")
    array([[10, 20, 30, 40],
           [50, 60, 70, 80]])
    >>> csv_string_to_array("2,4,6,8,10,11,12,13")
    array([[ 2,  4,  6,  8],
           [10, 11, 12, 13]])
    """
    ### changed cleaned_list = csv_string[:-1].split(",") to csv_string.rstrip(",").split(",") to remove any commas not just any character at the end
    cleaned_list = csv_string.rstrip(",").split(",")
    ### changed np.array(cleaned_list, dtype=str).reshape(100, 4) to return np.array(cleaned_list, dtype=int)
    ### -1 lets NumPy figure out how many rows are needed when there are 4 values in each row.
    return np.array(cleaned_list, dtype=int).reshape(-1, 4)
result = csv_string_to_array(csv_string)
print(result)
