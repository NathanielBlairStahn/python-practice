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
    start = 0
    end = len(s)-1

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
    end_of_initial_run = 0
    while start < end:
        if s[start] == s[end]:
            start += 1
            if start-1 == end_of_initial_run and s[start] == s[0]:
                end_of_initial_run = start
        elif not (start-1 == end_of_initial_run and s[end] == s[0]):
            start = end_of_initial_run = 0
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
    s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"

    output = "riir"
    expected = "fklkf"
