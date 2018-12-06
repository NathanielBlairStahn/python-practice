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
    n = len(arr[0]) #not len(arr), because if arr = [[]], len(arr) would return 1, not 0
    if n==0: return [[]] #Need special case because the below code would return [], not [[]]
    return [[arr[n-j-1][i] for j in range(n)] for i in range(n)]

def rotate_square_array_inplace(arr):
    """
    Given a square array, rotates the array 90 degrees clockwise in place.
    """

    n = len(arr)

    # for m in range(n//2):
    #     length = n-2*m
    #     for i in range(length):
    #         temp = arr[m][i]
    #         arr[m][i] = arr[m][]

    top = 0
    bottom = n-1

    while top < bottom:
        left = top
        right = bottom
        for i in range(right-left):
            temp = arr[top][left+i]
            arr[top][left+i] = arr[bottom-i][left]
            arr[bottom-i][left] = arr[bottom][right-i]
            arr[bottom][right-i] = arr[top+i][right]
            arr[top+i][right] = temp

        top += 1
        bottom -=1
