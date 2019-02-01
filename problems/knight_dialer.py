"""
From Medium post "Google Interview Questions Deconstructed: The Knight’s Dialer" by Alex Golec:
https://hackernoon.com/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029

Imagine you place a knight chess piece on a phone dial pad.
This chess piece moves in an uppercase “L” shape: two steps
horizontally followed by one vertically, or one step horizontally
then two vertically. For example, from the 1, the knight can move
to the 6 or the 8:

1* 2  3
4  5  6*
7  8* 9
   0

Suppose you dial keys on the keypad using only hops a knight can make.
Every time the knight lands on a key, we dial that key and make another hop.
The starting position counts as being dialed.

How many distinct numbers can you dial in N hops from a particular starting position?
"""

legal_moves = {1:[6,8], 2:[7,9], 3:[4,8],
               4:[3,9,0], 5:[], 6:[1,7,0],
               7:[2,6], 8:[1,3], 9:[2,4],
               0:[4,6]}

def knight_dialer_count_recursive(start, n):
    """
    Recursively counts the number of distinct numbers that can be dialed in n hops
    of a knight from a particular starting position.

    Complexity:
    Runtime is O(3^n) (and Omega(2^n) if start!=5) because for each move you
    recursively check 2 or 3 subsequent moves, and you do this n-1 times:
    3*3*3*...*3. This counts the total number of recursive calls, which gives
    the time complexity.
    The space complexity should be O(n) because the maximum depth of recursion is n.
    """
    if n <0: return 0
    if n==0: return 1
    if n==1: return len(legal_moves[start])

    return sum(knight_dialer_count_recursive(move, n-1) for move in legal_moves[start])

def knight_dialer_count_memoized(start, n, memo={}):
    """
    Recursively counts the number of distinct numbers that can be dialed in n hops
    of a knight from a particular starting position.

    Complexity:
    Now if start!=5, there are 9*n tuples:
    (1,n),(2,n),...,(0,n),(1,n-1),(2,n-1),...,(0,n-1),...,(1,1),(2,1),...,(0,1)
    This is the maximum possible size of the memo, so the space complexity is still O(n),
    though on the order of 10 times as large as the non-memoized version.

    Once the memo is filled in, it takes constant time to look up the 2 or 3 values
    needed to compute the sum for the final answer. So the time complexity is the time
    needed to fill in the memo, which is O(n) since that's its maximum size.

    Trace calls for (start,n) = (1,4):
    (1,4) -> [(6,3),(8,3)] -> [6:(1,2),(7,2),(0,2);8:(1,2),(3,2)]
    -> [1:(6,1)=3,(8,1)=2;7:(2,1)=2,(9,1)=2;0:(4,1)=3,@(6,1)=3;@(1,2)=5;3:@(4,1)=3,(8,1)=2]
    """
    if (start,n) in memo:
        pass #skip to the end and return memo[(start,n)]
    elif n<0: return 0
    elif n==0: return 1
    elif n==1:
        memo[(start,n)] = len(legal_moves[start])
    else:
        memo[(start,n)] = sum(knight_dialer_count_memoized(move, n-1) for move in legal_moves[start])

    return memo[(start,n)]
