#https://leetcode.com/problems/n-queens-ii/
'''Given an integer n, return the number of borad configurations for this  puzzle.

Inp: 4
Out: 2 (
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
])
'''
class Solution(object):
    def findBoards(self, cols, diags, row_num):
        # If we have filled up all the rows, we increment the total count
        # if this is a unique arrangement.
        if row_num == self.n:
            col_tuples = tuple(cols)
            if col_tuples not in self.boards:
                self.res += 1
                self.boards.add(col_tuples)
            return

        col_set = set(cols)
        for col_num in xrange(self.n):
            # If adding a queen at this position would cause a Q-Q attack, we skip this location.
            if (col_num in col_set or row_num+col_num in diags[0]
                    or row_num-col_num in diags[1]):
                continue

            cols.append(col_num)
            diags[0].add(row_num+col_num)
            diags[1].add(row_num-col_num)

            self.findBoards(cols, diags, row_num+1)

            # After recursing on this location, we backtrack
            cols.pop()
            diags[0].remove(row_num+col_num)
            diags[1].remove(row_num-col_num)

    def totalNQueens(self, n):
        # In a standard backtracking solution, in each row, we try placing queens
        # at all possible locations. At each location, we try to recurse on the
        # later rows, assuming that placing this queen doesn't result in a Q-Q attack.
        if not n:
            return []
        # cols is a list of all the cols on which we've had queens
        # Since cols is a list, the ordering & values of cols in total define 
        # a single arrangement of the queens on a board.
        # diags[0] is a set of all the SW->NE diagonals on which we have queens
        # diags[1] is a set of all the NW->SE diagonals. 
        cols, diags = [], [set(), set()]
        self.res, self.n, self.boards = 0, n, set()
        self.findBoards(cols, diags, 0)
        return self.res

s = Solution()
print s.totalNQueens(1)
print s.totalNQueens(2)
print s.totalNQueens(3)
print s.totalNQueens(4)
print s.totalNQueens(5)
print s.totalNQueens(6)
