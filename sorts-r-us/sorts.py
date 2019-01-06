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
    """Generates Sedgewick's increments for Shellsort"""
    # if n < 0 or upper_bound < 1:
    #     return #Stops the generator - this will return an empty generator

    i = 0
    counter=0
    #yields values alternaing between seq1 and seq2. These satisfy
    #seq1[i] < seq2[i] < seq1[i+1] for all i, so the gaps are increasing.
    while counter <= num_terms:
        #seq1[i] = 9*4**i - 9*2**i + 1
        term = (9<<(i<<1)) - (9<<i) + 1
        counter += 1
        if term > upper_bound or counter > num_terms:
            break
        else:
            yield term

        #seq2[i] = 4**(i+2) - 3*2**(i+2) + 1
        term = (1<<(i+2<<1)) - (3<<i+2) + 1
        counter += 1
        if term > upper_bound or counter > num_terms:
            break
        else:
            yield term

        i += 1
