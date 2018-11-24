"""
Given a rectangular 2D array, write a function that prints the elements in a clockwise
spiral order, starting at the upper left corner and ending at the center of the array.

For example:

1  2  3  4
5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
9  10 11 12
"""

import numpy as np

def array_spiral(arr):
    """
    Given a rectangular 2D array, yields the elements in a clockwise spiral order,
    starting at the upper left corner and ending at the center of the array.

    For example:

    1  2  3  4
    5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
    9  10 11 12
    """

    #Orient the array like a matrix, so the 1st index is the row
    #and the 2nd index is the column.
    #That is, arr[i][j] is the element in the ith row and jth column.

    #Initialize variables to keep track of the current top and bottom rows
    #and the current left and right columns. These will be updated as we
    #spiral inward in the array.
    #Note that these are the actual indices (as opposed to, e.g. bottom
    #being the bottom index plus 1 as is typical with array indexing),
    #so the number of rows will be bottom-top+1 and the number of columns
    #will be right-left+1.
    #If the first row of the array is empty, we will have top=0, bottom=#rows-1,
    #left=0, right=-1.

    top = 0 #index of top row
    bottom =len(arr)-1 #index of bottom row
    left = 0 #index of left column
    right = len(arr[0])-1 #index of right column

    #Our spiral pattern will be symmetric with respect to the four directions:
    #For each row or column in a single spiral, start at the corner, and move
    #until you hit the index just BEFORE the next corner.
    #In the example above, the first iteration would be:
    #  top=0, bottom=2, left=0, right=3
    #  top: [1,2,3], right: [4,8], bottom: [12,11,10], left: [9,5]
    #After the first iteration, we will have:
    #  top=1, bottom=1, left=1, right=2,
    #and the spiraling loop will exit since top==bottom.
    #This leaves the final single row [6,7] to be handled after the loop.

    #Spiral until there is either one row or one column remaining (or both).
    #There will be exactly one row remaining once top == bottom.
    #There will be exactly one column remaining once left == right.
    #If both occur simultaneously, then there is excatly one entry remaining,
    #which could be considered as either one row or one column.
    while top < bottom and left < right:
        #Top row: (top,left) right to (top,right-1)
        for j in range(left, right):
            yield arr[top][j]
        #Right column: (top,right) down to (bottom-1,right)
        for i in range(top, bottom):
            yield arr[i][right]
        #Bottom row: (bottom,right) left to (bottom,left+1)
        for j in range(right, left, -1):
            yield arr[bottom][j]
        #Left column: (bottom,left) up to (top+1,left)
        for i in range(bottom, top, -1):
            yield arr[i][left]

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    #Once we're down to one row or one column, we don't want to spiral.
    #Instead just iterate through the single row or column.
    #Note that if both top==bottom and left==right, we have exactly
    #one element left in the array, so we only want to iterate through
    #either one row or one column, but not both. Thus we use elif.
    #If we have top>bottom or left>right, then the array is empty, so
    #we don't want to yield anything.

    if top == bottom:
        #Array is a single row; return the entry in each column
        for entry in arr[top][left:right+1]: yield entry
    elif left == right:
        #Array is a single column; return the first entry of each row
        for row in arr[top:bottom+1]: yield row[left]

    #Check one final case of a single square in the middle,
    #which occurs with a square nxn array of odd size n:
    #
    #If the top met the bottom and the left met the right
    #at the same time, then in the final iteration of the while
    #loop, ALL of the for loops would have been skipped, so we
    #failed to yield the final central element. Since the bounds
    #would have been incremented, we revert them to get the
    #correct indices.
    #
    #Didn't work - also executed for even square matrices.
    # if top > bottom and left > right:
    #     yield arr[top-1][left-1]
    #
    # #If array is square and n is odd, yield the central element.
    # if len(arr[0])==len(arr) and len(arr)%2:
    #     yield arr[len(arr)//2][len(arr[0])//2]

def array_spiral1(arr):
    """
    Given a rectangular 2D array, yields the elements in a clockwise spiral order,
    starting at the upper left corner and ending at the center of the array.

    For example:

    1  2  3  4
    5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
    9  10 11 12
    """

    #Orient the array like a matrix, so the 1st index is the row
    #and the 2nd index is the column.
    #That is, arr[i][j] is the element in the ith row and jth column.
    top = 0
    bottom =len(arr)-1
    left = 0
    right = len(arr[0])-1

    #Deal separately with the case when the array is a single row or column,
    #because in this case we only need to make a single pass, whereas the
    #while loop below would make both a forward and backward pass, or
    #no passes at all if the array is 1x1.
    if top == bottom:
        #Array is a single row; return the entry in each column
        for entry in arr[0]: yield entry
    elif left == right:
        #Array is a single column; return the first entry of each row
        for row in arr: yield row[0]
    else:
        #Array has at least two rows and two columns.
        #When either the top meets the bottom or the left
        #meets the right, we are done spiraling.
        while top <= bottom and left <= right:
            for j in range(left, right):
                yield arr[top][j]
            for i in range(top, bottom):
                yield arr[i][right]
            #if bottom != top:
            for j in range(right, left, -1):
                yield arr[bottom][j]
            #if left != right:
            for i in range(bottom, top, -1):
                yield arr[i][left]

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        #Check one final case of a single square in the middle,
        #which occurs with a square nxn array of odd size n:
        #
        #If the top met the bottom and the left met the right
        #at the same time, then in the final iteration of the while
        #loop, ALL of the for loops would have been skipped, so we
        #failed to yield the final central element. Since the bounds
        #would have been incremented, we revert them to get the
        #correct indices.
        #
        #Didn't work - also executed for even square matrices.
        # if top > bottom and left > right:
        #     yield arr[top-1][left-1]
        #
        #If array is square and n is odd, yield the central element.
        if len(arr[0])==len(arr) and len(arr)%2:
            yield arr[len(arr)//2][len(arr[0])//2]

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

    #Orient the array like a matrix, so the 1st index is the row
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

def array_spiral_orig_fixed(arr):
    """
    Fixed(?) version of the original I came up with.
    (Not fixed yet)

    Given a rectangular 2D array, yields the elements in a clockwise spiral order,
    starting at the upper left corner and ending at the center of the array.

    For example:

    1  2  3  4
    5  6  7  8   -->  1 2 3 4 8 12 11 10 9 5 6 7
    9  10 11 12
    """

    #Orient the array like a matrix, so the 1st index is the row
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

def test_spiral():
    spiral = array_spiral

    a = np.arange(12).reshape(3,4) + 1
    assert list(spiral(a)) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    a = np.arange(2*3).reshape(2,3)+1
    assert list(spiral(a)) == [1, 2, 3, 6, 5, 4]

    assert list(spiral([[]])) == []

    assert list(spiral([[], [], []])) == []

    assert list(spiral([[45]])) == [45]

    assert list(spiral([[1,2]])) == [1,2]

    assert list(spiral([[1,2,3]])) == [1,2,3]

    assert list(spiral([[1],[2]])) == [1,2]

    assert list(spiral([[1],[2],[3]])) == [1,2,3]

    a = np.arange(5).reshape(1,5) + 1
    assert list(spiral(a)) == [1,2,3,4,5]

    a = np.arange(7).reshape(7,1) + 1
    assert list(spiral(a)) == [1,2,3,4,5,6,7]

    a = np.arange(9*6).reshape(9,6)
    assert list(spiral(a)) == [0, 1, 2, 3, 4, 5, 11, 17, 23, 29, 35, 41, 47, 53, 52, 51, 50, 49, 48, 42, 36, 30, 24, 18, 12, 6, 7, 8, 9, 10, 16, 22, 28, 34, 40, 46, 45, 44, 43, 37, 31, 25, 19, 13, 14, 15, 21, 27, 33, 39, 38, 32, 26, 20]

    a = [[1,2],[3,4]]
    assert list(spiral(a)) == [1,2,4,3]

    a = [[1,2,3], [4,5,6], [7,8,9]]
    assert list(spiral(a)) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    a = np.arange(4*4).reshape(4,4)+1
    assert list(spiral(a)) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    a = np.arange(5*5).reshape(5,5)+1
    assert list(spiral(a)) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]

    a = np.arange(3*5).reshape(3,5) + 1
    assert list(spiral(a)) == [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9]

def test_spiral2():
    spiral = array_spiral

    a = np.arange(3*5).reshape(5,3) + 1
    assert list(spiral(a)) == [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]

    a = np.arange(4*6).reshape(4,6) + 1
    assert list(spiral(a)) == [1, 2, 3, 4, 5, 6, 12, 18, 24, 23, 22, 21, 20, 19, 13, 7, 8, 9, 10, 11, 17, 16, 15, 14]



if __name__=="__main__":
    arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print(list(array_spiral(arr))) #Output should be [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
