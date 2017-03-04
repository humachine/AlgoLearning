#https://leetcode.com/problems/n-queens/
'''Given an integer n, return all distinct solutions to the n-queens puzzle.

Inp: 4
Out:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution(object):
    def findBoards(self, board, cols, diags, row_num):
        # If we have filled up all the rows, we add the board to the result.
        if row_num == self.n:
            ans = [''.join(x) for x in board]
            self.res.append(ans)
            return

        for col_num in xrange(self.n):
            # If adding a queen at this position would cause a Q-Q attack, we skip this location.
            if (col_num in cols or row_num+col_num in diags[0]
                    or row_num-col_num in diags[1]):
                continue

            # Adding a queen at board[row_num][col_num] and recursing
            board[row_num][col_num] = 'Q'
            cols.add(col_num)
            diags[0].add(row_num+col_num)
            diags[1].add(row_num-col_num)

            self.findBoards(board, cols, diags, row_num+1)

            # After recursing on this location, we backtrack
            board[row_num][col_num] = '.'
            cols.remove(col_num)
            diags[0].remove(row_num+col_num)
            diags[1].remove(row_num-col_num)

    def solveNQueens(self, n):
        # In a standard backtracking solution, in each row, we try placing queens
        # at all possible locations. At each location, we try to recurse on the
        # later rows, assuming that placing this queen doesn't result in a Q-Q attack.
        if not n:
            return []
        board = [['.']*n for i in xrange(n)]
        # cols is a set of all the cols on which we've had queens
        # diags[0] is a set of all the SW->NE diagonals on which we have queens
        # diags[1] is a set of all the NW->SE diagonals. 
        cols, diags = set(), [set(), set()]
        self.res, self.n = [], n
        self.findBoards(board, cols, diags, 0)
        return self.res

s = Solution()
print s.solveNQueens(1)
print s.solveNQueens(2)
print s.solveNQueens(3)
print s.solveNQueens(4)
print s.solveNQueens(5)
print s.solveNQueens(6)
