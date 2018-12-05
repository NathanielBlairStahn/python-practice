"""
Given a square matrix, write a function that rotates the matrix 90 degrees clockwise.
For example:

1  2  3        7  4  1
4  5  6  --->  8  5  6
7  8  9        9  6  3

1  2  3  4         13 9  5  1
5  6  7  8   --->  14 10 6  2
9  10 11 12        15 11 7  3
13 14 15 16        16 12 8  4
"""

def rotate_square_array(arr):
    """
    Given a square array, rotates the array 90 degrees clockwise,
    outputting to a new array.
    """
    n = len(arr)
    return [[arr[n-j-1][i] for j in range(n)] for i in range(n)]
