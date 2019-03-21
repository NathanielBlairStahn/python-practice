"""
36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
class Solution:
    def isValidSudoku(self, board):
        # value_counter = {str(i): 0 for i in range(1,10)}

        # Check rows
        # for row in board:
        #     for num in row:
        #         if num != '.':
        #             value_counter[num] += 1
        #     if any(value_counter[num] > 1 for num in value_counter):
        #         return False
        #
        # # Reset counter
        # for num in value_counter:
        #     value_counter[num] = 0

        # board is itself a list of rows
        rows = board
        if not self.isValidCollectionOfGroups(rows): return False

        # Check columns
        # for c in range(9):
        #     for r in range(9):
        #         if board[r][c] != '.':
        #             value_counter[board[r][c]] += 1
        #
        # for col in zip(*board):
        #     for num in col:
        #         if num != '.':
        #             value_counter[num] += 1
        #     if any(value_counter[num] > 1 for num in value_counter):
        #         return False
        #
        # # Reset counter
        # for num in value_counter:
        #     value_counter[num] = 0

        # Transpose board using zip(*board) to get list of columns
        columns = zip(*board)
        if not self.isValidCollectionOfGroups(columns): return False

        # Check subsquares
        #
        subsquares = [[board[square//3 + i][square%3 + j] for i in range(3) for j in range(3)] for square in range(9)]
        if not self.isValidCollectionOfGroups(subsquares): return False

        return True

    def isValidCollectionOfGroups(self, collection):
        """A "group" can be a row, columm, or 3x3 subsquare.
        A collection of groups can be all rows, all columns, or all 3x3 subsquares.
        """
        value_counter = {str(i): 0 for i in range(1,10)}
        for group in collection:
            for num in group:
                if num != '.':
                    value_counter[num] += 1
            if any(value_counter[num] > 1 for num in value_counter):
                return False
            #Reset counter after each group
            for num in value_counter:
                value_counter[num] = 0

        return True

if __name__=="__main__":
    solution = Solution()

    board1 = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]

    print(solution.isValidSudoku(board1))

    board2 = [
       ["8","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]
    ]

    print(solution.isValidSudoku(board2))
