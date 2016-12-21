#https://leetcode.com/problems/surrounded-regions/
'''
Any region of zeros surrounded by Xs is captured and made Xs
X X X X
X O O X
X X O X
X O X X

Out:
X X X X
X X X X
X X X X
X O X X
'''
from Queue import Queue
class Solution(object):
    def printBoard(self, board):
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                print board[i][j], 
            print

    def floodBoard(self, i, j, board):
        m, n = len(board), len(board[0])
        cells = Queue()
        cells.put((i, j))
        while not cells.empty():
            x, y = cells.get()
            board[x][y] = 'o'
            if x>0 and board[x-1][y]=='O': cells.put((x-1, y))
            if x<m-1 and board[x+1][y]=='O': cells.put((x+1, y))
            if y>0 and board[x][y-1]=='O': cells.put((x, y-1))
            if y<n-1 and board[x][y+1]=='O': cells.put((x, y+1))

    def solve(self, board):
        if not board:   return
        m, n = len(board), len(board[0])
        if m<=2 or n<=2:    return

        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    self.floodBoard(i, j, board)
        for i in xrange(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    self.floodBoard(i, j, board)

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = 'XO'[board[i][j]=='o']
        self.printBoard(board)

board = ['X X X X'.split(), 'X O O X'.split(), 'X X O X'.split(), 'X O X X'.split()]
s = Solution()
s.solve(board)

