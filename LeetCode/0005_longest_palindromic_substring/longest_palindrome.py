"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Test cases:
aaabaaaa
fklkffa
affklkffffaaaffaffffaaafff -> "fffaaaffaffffaaaf" (should be fffaaafff)

For initial palindrome:
fffaaaffaffffaaafff -> fffaaaffaffffaaaf (should be fff)
ffaaaffaffffaaafff -> ffaaaffaffffaaa (should be ffaaaff)
"""

def longest_initial_palindrome(s: str) -> str:
    """Returns the longest palindrome starting at the beginning of s"""

    # The first two while loops stip of leading and trailing characters equal to s[0].
    # Without this step, the method fails for, e.g.
    # 'abaa', 'aaaabaaaaaaaaaa', 'aaabbcbbaaaaa',
    # where the number of trailing a's is greater than the number of leading a's.
    # while start < end and s[start] == s[0] and s[end] == s[0]:
    #     start += 1
    #     end -= 1
    # while start < end and s[end] == s[0]:
    #     end -= 1

    # Walk backwards through string:
    # 1. If current last letter equals the beginning letter,
    #    we might have a palindrome, so advance the start
    #    pointer to keep checking.
    # 2. If start and end don't match, the current end letter
    #    can't be in the longest palindrome, so reset start to 0.
    # 3. Decrement the end pointer in either case to continue
    #    walking backwards through string.
    # 4. We've found a palindrome when the pointers meet
    #    in the middle.

    start = 0
    end = len(s)-1
    end_of_initial_run = 0

    while start < end:
        # While the first and last letters match, move start and end
        # pointers simultaneously towards middle.
        if s[start] == s[end]:
            start += 1
            # If we haven't finished the initial run of the first letter,
            # advance the pointer in concert with start. Otherwise, leave
            # it pointing at the end of the initial run.
            if start-1 == end_of_initial_run and s[start] == s[0]:
                end_of_initial_run = start
        # If the first and last letters don't match, reset start...
        # UNLESS we just finished the initial run of the first letter
        # and the end letter is equal to the first. In this case,
        # we want to keep the start pointer in place and continue
        # moving the end pointer towards the middle until it reaches
        # a letter that is not equal to s[0].
        elif not (start-1 == end_of_initial_run and s[end] == s[0]):
            start = end_of_initial_run = 0
        # In all cases, we decrement the end pointer.
        end -= 1

    # Suppose the longest palindrome has length k.
    # When the loop exits, either
    # (1) start == end at the middle index when k is odd, or
    # (2) start == end + 1 when k is even, with end being
    # the last index of the first half of the string, and
    # start being the first index of the second half.
    return s[:start+end+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            pal = longest_initial_palindrome(s[i:])
            if len(pal) > len(longest):
                longest = pal
            if len(longest) >= len(s)-i-1: # No remaining substrings can be longer
                break
        return longest


def main():
    # Note: My second solution passed 100/103 tests, and failed on the following:
    s1 = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"

    output1 = "riir"
    expected1 = "fklkf"

    s2 = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"

    output2 = "23210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232"

    expected2 = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123"
