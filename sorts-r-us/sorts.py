"""Module implementing sort algorithms"""

def insertion_sort(arr, inplace=True):
    """Sorts an array in place using insertion sort."""

    a = arr if inplace else arr.copy()
    for i in range(1,len(a)):
        element = a[i]
        j=i
        #Move left, shifting elements one space to the right
        #as we go, until we find the place where the current
        #element belongs.
        while j>0 and element < a[j-1]:
            a[j] = a[j-1]
            j -= 1

        a[j] = element

    return a


def sedgewick_shell_gaps(num_terms=float('inf'), upper_bound=float('inf')):
    """Generates Sedgewick's increments for Shellsort.

    The first 20 terms of the sequence are:
    [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929, 16001, 36289, 64769, 146305, 260609, 587521, 1045505, 2354689, 4188161, ...]

    The terms alternate between the sequences
    a_i = 9*4**i - 9*2**i + 1 (i >= 0) and
    b_j = 4**j - 3*2**j + 1 (j >= 2).

    That is, the sequence is
    [a_0, b_2, a_1, b_3, a_2, b_4, a_3, b_5, a_4, b_6, ...].
    The a and b sequences satisfy a_i < b_(i+2) < a_(i+1) for all i,
    so the combined sequence is strictly increasing.
    """

    i = 0
    #yields values alternaing between seq1 and seq2. These satisfy
    #seq1[i] < seq2[i] < seq1[i+1] for all i>=0, so the terms are increasing.
    while i<<1 < num_terms:
        #seq1[i] = 9*4**i - 9*2**i + 1
        term = (9<<(i<<1)) - (9<<i) + 1
        #number of terms is now 2*i+1, guaranteed to be <= num_terms
        if term > upper_bound:# or (i<<1)+1 > num_terms:
            break
        else:
            yield term

        #seq2[i] = 4**(i+2) - 3*2**(i+2) + 1
        term = (1<<(i+2<<1)) - (3<<i+2) + 1
        #number of terms is now 2*i+2, could be too many.
        if term > upper_bound or (i<<1)+2 > num_terms:
            break
        else:
            yield term

        i += 1

def tokuda_gap(i):
    """Returns the i^th Tokuda gap for Shellsort (starting with i=0).

    The first 20 terms of the sequence are:
    [1, 4, 9, 20, 46, 103, 233, 525, 1182, 2660, 5985, 13467, 30301, 68178, 153401, 345152, 776591, 1747331, 3931496, 8845866, ...]

    h_i = ceil( (9*(9/4)**i-4)/5 ) for i>=0.

    If 9*(9/4)**i-4)/5 is not an integer, I believe this is the same as
    h_i = ((9**(i+1)>>(i<<1))-4)//5 + 1,
    and I believe the above should be non-integer valued for all i>0.
    (We have to explicitly return 1 when i=0, as the above formula would return 2.)
    """
    return 1 if i==0 else ((9**(i+1)>>(i<<1))-4)//5 + 1

def shellsort(arr, inplace=True):
    """Sorts an array using Shellsort with Sedgewick's increments.

    With these increments, Shellsort operates in O(n^4/3) time worst case,
    and is conjectured to operate in O(n^7/6) time average case.
    """

    a = arr if inplace else arr.copy()
    #Storing the gaps in an array requires O(log(n)) extra space.
    #Order the gaps in descending order.
    gaps = list(sedgewick_shell_gaps(upper_bound=len(a)-1))[::-1]

    #Iterate through gaps h in descending order.
    for h in gaps:
        #Each pass performs an h-sort on the array using the insertion sort algorithm.
        for i in range(h,len(a)):
            element = a[i]
            j = i
            while j>=h and element < a[j-h]:
                a[j] = a[j-h]
                j -= h

            a[j] = element

    return a
