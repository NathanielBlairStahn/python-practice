"""
Given an array of numbers, check for duplicates. If there are
duplicates, increment the duplicates until there are no more.
Return the sum of the array.

Is there an O(n) solution?
Hmm, it seems possible you could use a union-find data structure...
e.g. one component would be a sequence of consecutive numbers
that are already in the array. If you see one of these numbers,
you have to find their maximum and add 1. How quickly can that
be done? Perhaps we can keep a hashtable tracking the maximum of
each component.
"""

def increment_duplicates(arr):
    """Increments duplicates in an array until there are no duplicates.

    Uses a hash set to keep track of which values have been seen in the array.
    Runs in O(n^2) time worst case (e.g. all elements are equal),
    O(n) time best case (elements are already unique).
    """
    seen = set()
    for i in range(len(arr)):
        while arr[i] in seen:
            arr[i] += 1
        seen.add(arr[i])
    return arr
