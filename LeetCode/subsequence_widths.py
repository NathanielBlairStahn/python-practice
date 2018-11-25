# From Leetcode (8/24/2018):
#
# 891. Sum of Subsequence Widths
#
# Given an array of integers A, consider all non-empty subsequences of A.
#
# For any sequence S, let the width of S be the difference between the maximum
#  and minimum element of S.
#
# Return the sum of the widths of all subsequences of A.
#
# As the answer may be very large, return the answer modulo 10^9 + 7.

class Solution:
#     def sumSubseqWidths(self, a):
#         """
#         :type A: List[int]
#         :rtype: int
#         This solution runs in quadratic time, rather than the naive exponential time solution.
#         """
#         #The answer is the same if we rearrange the elements of a.
#         #Sorting the elements allows us to count the subsequences
#         #that have a particular pair of elements as its minimum
#         #and maximum - see comments below.
#         a = sorted(a)
#         n = len(a)
#         total = 0
#         modulus = 10**9 + 7

#         #Rather than the naive solution that iterates through all 2**n - 1 subsequences,
#         #we can compute the sum of the widths in quadratic time by grouping subsequences
#         #according to the minimum and maximum values.
#         for i in range(n):
#             for j in range(i+1, n):
#                 #There are exactly 2**(j-i-1) subsequences where
#                 #a[i] is the minimum and a[j] is the maximum (one for
#                 #each subset of the elements between indices i and j),
#                 #so the sum of the widths for all these subsequences
#                 #is (a[j]-a[i]) * 2**(j-i-1).
#                 total += (a[j]-a[i]) * (2**(j-i-1) % modulus)
#                 total %= modulus

#         return total


#     def sumSubseqWidths(self, a):
#         """
#         :type a: List[int]
#         :rtype: int
#         This solution runs in quadratic time, but 4 times faster than the one above.
#         """
#         #The answer is the same if we rearrange the elements of a.
#         #Sorting the elements allows us to count the subsequences
#         #that have a particular pair of elements as its minimum
#         #and maximum - see comments below.
#         a = sorted(a)
#         n = len(a)
#         total = 0
#         modulus = 10**9 + 7

#         #Rather than the naive solution that iterates through all 2**n - 1 subsequences,
#         #we can compute the sum of the widths in quadratic time by grouping subsequences
#         #according to the minimum and maximum values.
#         #There are exactly 2**(k-j-1) subsequences where
#         #a[j] is the minimum and a[k] is the maximum (one for
#         #each subset of the elements between indices j and k),
#         #so the sum of the widths for all these subsequences
#         #is (a[k]-a[j]) * 2**(k-j-1).
#         #Moreover, the sum of the widths for which k-j = i is the same as the sum of the
#         #widths for which k-j = n-i (this is not obvious until you compute some examples),
#         #so by grouping these terms together, we can cut the work by a factor of 4 ((n/2)^2 vs. n^2).
#         for i in range(1,(n+1)//2):
#             sum_diffs = 0
#             for j in range(i):
#                 sum_diffs += a[n-j-1] - a[j]
#             total += sum_diffs * ((2**(i-1) + 2**(n-i-1)) % modulus)
#             total %= modulus

#         #If n is even, the widths for k-j=n/2 are not paired, so compute this case separately
#         if n % 2 == 0:
#             sum_diffs = 0
#             for j in range(n//2):
#                 sum_diffs += a[n-j-1] - a[j]
#             total += sum_diffs * (2**(n//2-1) % modulus)
#             total %= modulus

#         return total


    def sumSubseqWidths(self, a):
        """
        :type a: List[int]
        :rtype: int
        This solution runs in O(n*log(n)) time overall:
        The total time is O(n*log(n)) for sorting the array, plus O(n) time
        for computing the sum of widths from the sorted array.
        """
        #The answer is the same if we rearrange the elements of a.
        #Sorting the elements allows us to count the subsequences
        #that have a particular pair of elements as its minimum
        #and maximum - see comments below.
        a = sorted(a)
        n = len(a)
        total = 0
        sum_diffs = 0
        modulus = 10**9 + 7

        #Rather than the naive solution that iterates through all 2**n - 1 subsequences,
        #we can compute the sum of the widths in quadratic time by grouping subsequences
        #according to the minimum and maximum values.
        #There are exactly 2**(k-j-1) subsequences where
        #a[j] is the minimum and a[k] is the maximum (one for
        #each subset of the elements between indices j and k),
        #so the sum of the widths for all these subsequences
        #is (a[k]-a[j]) * 2**(k-j-1).
        #Moreover, for i>0, the sum of the widths for which k-j = i is the same as the sum of the
        #widths for which k-j = n-i, and this common sum is precisely a[n-i] - a[i-1]
        #greater than the sum of the widths for which k-j = i-1. This occurs because the sum of
        #widths for which k-j is fixed is a telescoping sum (to see this, compute some examples).
        #This observation allows us to iterate exactly once through the sorted array in order to compute
        #the total sum of the widths, so the remainder of this function runs in linear time. Thus,
        #the overall runtime will be O(n log(n)) from the sorting above.

        for i in range(1,(n+1)//2):
            sum_diffs += a[n-i] - a[i-1]
            total += sum_diffs * ((2**(i-1) + 2**(n-i-1)) % modulus)
            if total >= modulus:
                total %= modulus

        #If n is even, the widths for k-j=n/2 are not paired (i.e. when i = n/2, then n-i = n/2 as well),
        #so compute this case separately.
        if n % 2 == 0:
            i = n//2
            sum_diffs += a[i] - a[i-1]
            total += sum_diffs * (2**(i-1) % modulus)
            if total >= modulus:
                total %= modulus

        return total


def counting_sort_integers(values, max_val=None, inplace=False):
    """
    Sorts an array of integers using counting_sort.
    Let n = len(values), k = max_val+1
    """
    if max_val is None:
        #Runs in O(n) time if max_val is None
        max_val = max(values)

    #Assume values are integers in the range 0,1,2,...,max_val
    #Runs in O(k) time
    counts = [0 for _ in range(max_val+1)]

    #Runs in O(n) time
    for value in values:
        counts[value] += 1

    #Overwrite values if inplace==True, otherwise create a new array for output.
    #Requires O(n) time if inplace is False.
    output = values if inplace else [0 for _ in range(len(values))]

    #Simultaneously iterate through output and counts arrays.
    #value will be the index of counts array - this is the value
    #we will be storing in the output array.
    value = 0

    #Iterate through output array, storing one value at a time.
    #The for loop has n iterations.
    #The inner while loop will have a total of k iterations.
    #So the runtime for this loop is O(n+k)
    for i in range(len(output)):
        #Find the next value with a nonzero count.
        while counts[value] == 0:
            value += 1
        #Store the value in the output array and decrease its count.
        output[i] = value
        counts[value] -= 1

    #Total runtime, in iterations, is 2k+2n if max_key is passed and inplace==True.
    #Another n is added if max_key is None or inplace is False, for a maximum
    #runtime of 2k+4n.

    return output

def counting_sort(items, key=None, max_key=None):
    """
    Sorts an array of items by their integer keys, using counting_sort.
    Implemented as a stable sort.

    This is a modified version of the code described on Wikipedia:
    https://en.wikipedia.org/wiki/Counting_sort

    Parameters
    ----------
    items: list of items
    key: function mapping each item to an integer key
    max_key: the maximum value of a key
    """
    #If no key functions is passed, assume items
    #are integers in the range 0,1,2,...,max_key
    if key is None:
        key = lambda x: x

    #If the maximum key wasn't specified, find it.
    if max_key is None:
        #(Takes time n if max_key was not specified)
        max_key = max(key(item) for item in items)

    #Initialize an array to count the occurrances of keys.
    #The index is the key, and counts[key] is the count of that key.
    #(Takes time K)
    counts = [0 for key in range(max_key+1)]

    #Iterate through items, to count how many times each key occurs
    #(Takes time n)
    for item in items:
        counts[key(item)] += 1

    #Rename the counts array because we will be overwriting it to store indices
    #of keys instead of counts of keys.
    index_of = counts

    #Create the index_of array as the cumulative sum of the counts array.
    #When the loop finishes, we will have
    #index_of[k] = counts[0] + counts[1] + ... + counts[k-1],
    #but we can do it in place, replacing count[k] with index_of[k].
    #
    #The value index_of[k] is the start index of the items with key(item) = k.
    #We will increment index_of[key] each time we place an item with key(item) = k.

    index=0 #Store the current index (cumulative sum of counts)
    #(Takes time K)
    for k, count in enumerate(counts):
        #k is the key, count is its count.
        index_of[k] = index #Note that index_of = counts
        index += count

    #Create a new array for output. This is necessary if we want a stable sort.
    #(Takes time n)
    output = [None for _ in range(len(items))]

    #Iterate through items, putting each item in the correct place in output.
    #The index for the first item with each key is stored in index_of[key]
    #(Takes time n)
    for item in items:
        #Put the item in the correct index for its key.
        output[index_of[key(item)]] = item
        #Increment the index for the next time we encounter the key.
        index_of[key(item)] += 1


    #Total runtime in iterations is 2k + 3n, plus another n if max_key is not passed.
    return output
