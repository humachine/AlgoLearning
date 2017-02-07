#https://leetcode.com/problems/valid-sudoku/
''' Given a sudoku board, return if it's a valid sudoku.

Note: The sudoku board need not be solvable. You just need to return whether
this board COULD have a solution. 
i.e Return False, if the input board DEFINITELY cannot have a solution.
'''
class Solution(object):
    def isValidSudoku(self, board):
        # Contrary to the name of the question, we actually only have to
        # ascertain if the sudoku is invalid or not. Return True if not invalid, 
        # else False

        # We maintain separate sets for each row and each column. If any of the
        # numbers we encounter has already been seen in the set for its column/
        # row/grid, then we return False

        # Note: We are assuming that each cell of the grid either contains a 
        # digit or a '.'
        rows = [set() for i in xrange(9)]
        cols = [set() for i in xrange(9)]
        boxes = [set() for i in xrange(9)]

        for i in xrange(9):
            for j in xrange(9):
                char = board[i][j]
                if char != '.':
                    # Determine grid number
                    box_num = 3*(j/3) + (i/3)
                    # Check if character has already been seen in current
                    # row/column/grid box
                    if char in rows[i] or char in cols[j] or char in boxes[box_num]:
                        return False
                    rows[i].add(char)
                    cols[j].add(char)
                    boxes[box_num].add(char)
        return True
