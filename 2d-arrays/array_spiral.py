"""
Given a rectangular 2D array, write a function that prints the elements in a clockwise
spiral order, starting at the upper left corner and ending at the center of the array.

For example:

1  2  3  4
5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
9  10 11 12
"""

def array_spiral(arr):
    """
    Given a rectangular 2D array, yields the elements in a clockwise spiral order,
    starting at the upper left corner and ending at the center of the array.

    For example:

    1  2  3  4
    5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
    9  10 11 12
    """

    #Orient the array in like a matrix, so the 1st index is the row
    #and the 2nd index is the column.
    #That is, arr[i][j] is the element in the ith row and jth column.
    top = 0
    bottom =len(arr)-1
    left = 0
    right = len(arr[0])-1

    while top <= bottom and left <= right:
        for j in range(left, right):
            yield arr[top][j]
        for i in range(top, bottom):
            yield arr[i][right]
        for j in range(right, left, -1):
            yield arr[bottom][j]
        for i in range(bottom, top, -1):
            yield arr[i][left]

        top += 1
        bottom -= 1
        left += 1
        right -= 1

def array_spiral_orig(arr):
    """
    Original version I came up with (has a bug).

    Given a rectangular 2D array, yields the elements in a clockwise spiral order,
    starting at the upper left corner and ending at the center of the array.

    For example:

    1  2  3  4
    5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
    9  10 11 12
    """

    #Orient the array in like a matrix, so the 1st index is the row
    #and the 2nd index is the column.
    #That is, arr[i][j] is the element in the ith row and jth column.
    top = 0
    bottom =len(arr)
    left = 0
    right = len(arr[0])

    while top < bottom and left < right:
        for j in range(left, right):
            yield arr[top][j]
        for i in range(top+1, bottom):
            yield arr[i][right-1]
        for j in range(right-2, left-1, -1):
            yield arr[bottom-1][j]
        for i in range(bottom-2, top, -1):
            yield arr[i][left]

        top += 1
        bottom -= 1
        left += 1
        right -= 1


if __name__=="__main__":
    arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print(list(array_spiral(arr))) #Output should be [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
