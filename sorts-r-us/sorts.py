"""Module implementing sort algorithms"""

def insertion_sort(arr, inplace=True):
    """Sorts an array in place using insertion sort."""

    a = arr if inplace else arr.copy()
    for i in range(1,len(a)):
        element = a[i]
        j=i
        #Move left, shifting each element to the right
        #until we find the place where the current
        #element belongs.
        while j>0 and element < a[j-1]:
            a[j] = a[j-1]
            j -= 1

        a[j] = element

    return a
