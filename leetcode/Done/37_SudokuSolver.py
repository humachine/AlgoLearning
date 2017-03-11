#https://leetcode.com/problems/sudoku-solver/
'''Given a Sudoku board, fill up the board to solve the sudoku. Assume that
there exists exactly one solution.

Inp: ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

Out: ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
'''
class Solution(object):
    def solveBoard(self, board, x, y, rows, cols, boxes):
        n, box_size = self.n, self.box_size
        # If we are beyond the end of the column, we try to start from the
        # beginning of the next row.
        if y==n:
            x, y = x+1, 0
        # If we are beyond the last row, then we have solved the entire board.
        if x==n:
            return True
        # If the cell != '.', then we already have a fixed value for this cell.
        # We recurse on the rest of the board.
        if board[x][y] != '.':
            return self.solveBoard(board, x, y+1, rows, cols, boxes)

        box_num = box_size*(x/box_size) + (y/box_size)
        for number in xrange(1, n+1):
            char = str(number)
            # If digit $char is already part of its row/col/box, we continue on 
            # to other choices
            if char in boxes[box_num] or char in rows[x] or char in cols[y]:
                continue
            # Since $char is not part of its row & col & box, we add it to its
            # row, col & box sets.
            board[x][y] = char
            boxes[box_num].add(char)
            rows[x].add(char)
            cols[y].add(char)
            # If the addition of this char to the board results in a consistent
            # solution of the board, we return True.
            if self.solveBoard(board, x, y+1, rows, cols, boxes):
                return True
            # Since the attempt has failed, we update the cell to a '.' and
            # remove it from box/col/row sets.
            boxes[box_num].remove(char)
            rows[x].remove(char)
            cols[y].remove(char)
            board[x][y] = '.'
        # If none of the 9 choices were suitable we return False
        return False

    def solveSudoku(self, board):
        # In this backtracking solution, we try out all 9 possible values
        # for each box. For every possible value, we move forward in the box,
        # seeing if this value holds consistent across the rest of the board.
        # If at any point, the board becomes inconsistent, we immediately backtrack
        # and try out a new value at every layer (from most recent to least recent)

        # For any layer (i.e cell) if none of the values can result in a consistent
        # board, there's no possible solution and we return False
        n = 9
        box_size = int(n**0.5)
        self.n, self.box_size = n, box_size

        # rows, cols & boxes represent the digits already used in that row/box/col
        rows = [set() for i in xrange(n)]
        cols = [set() for i in xrange(n)]
        boxes = [set() for i in xrange(n)]

        # We first load the existing values of the board into boxes/cols/rows  
        for i in xrange(n):
            for j in xrange(n):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_size*(i/box_size) + (j/box_size)].add(num)

        self.solveBoard(board, 0, 0, rows, cols, boxes)
        for row in board:
            print ' '.join([str(x) for x in row])

s = Solution()
board = [['.']*16 for i in xrange(16)]
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [list(x) for x in board]
s.solveSudoku(board)
