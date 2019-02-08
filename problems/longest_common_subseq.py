"""
Given two strings, find their longest common subsequence.
"""

def lcs_recursive(s1, s2):
    """
    Given two strings s1 and s2, find their longest common subsequence (lcs).

    Basic idea of algorithm is to split on whether the first characters of
    the two strings match, and use recursion.

    Time complexity:
    If n1 = len(s1) and n2 = len(s2), the runtime is O(2^(n1+n2)).
    The depth of the recursion is at most n1+n2, by alternately
    removing the first letter of s1, then s2, then s1, and so on.
    One function call makes at most two subsequent recursive calls,
    so the total number of calls is at most 2^(recursion depth),
    or 2^(n1+n2).
    This bound is also the time complexity of the brute force approach
    of enumerating all 2^n1 subsequences of s1 and all 2^n2 subsequences
    of s2, and comparing all (2^n1)*(2^n2) pairs.

    Space complexity:
    As noted above, the recursion depth is at most n1+n2, which is
    achieved in the worst case of an empty lcs, so the space complexity
    is Omega(n1+n2).
    """
    if len(s1)==0 or len(s2) == 0:
        return ""

    if s1[0] == s2[0]:
        #If 1st character is the same, it is part of the
        #longest common subsequence.
        return s1[0] + lcs_recursive(s1[1:],s2[1:])

    #If 1st characters are different, need to consider two cases
    seq1 = lcs_recursive(s1, s2[1:])
    seq2 = lcs_recursive(s1[1:], s2)

    #Return whichever sequence is longer
    return seq1 if len(seq1) > len(seq2) else seq2

def lcs(s1, s2):
    """
    Given two strings s1 and s2, find their longest common subsequence (lcs).

    Time complexity:
    O(n1*n2), because there are n1 suffixes of n1 and n2 suffixes of s2, hence
    at most n1*n2 pairs that get stored in the cache. Note that we have reduced
    the problem from looking at all possible pairs of subsequences to looking
    only at pairs of suffixes.

    Space complexity:
    O(n1^2 * n2^2), because the space needed to store all the pairs of suffixes
    is (n1 + n1-1 + ... + 1)(n2 + n2-1 + ... + 1) = n1(n1+1)*n2(n2+1)/4.
    This is an upper bound, assuming the strings have no common subsequence;
    if the initial letters of the substrings are ever the same, the number of
    pairs will be fewer because the call within the if statement will be
    executed instead, and the pairs of suffixes there are a subset of the
    pairs in the else block.
    The space needed to store the longest common subsequence for a given pair
    is only O(min(n1,n2)), hence negligible compared to the bi-quadratic term.

    Ahh, but what if instead of storing the actual pairs of substrings, we
    just stored a pair of indices instead?
    """

    cache = {}

    def lcs_memoized(s1, s2, cache):
        if (s1,s2) in cache:
            return cache[(s1,s2)]

        if s1[0] == s2[0]:
            cache[(s1,s2)] = s1[0] + lcs_memoized(s1[1:], s2[1:], cache)
        else:
            seq1 = lcs_memoized(s1, s2[1:], cache)
            seq2 = lcs_memoized(s1[1:], s2, cache)
            cache[(s1,s2)] = seq1 if len(seq1) > len(seq2) else seq2

        return cache[(s1,s2)]

    return lcs_memoized(s1, s2, cache)
