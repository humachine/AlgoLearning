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
class Solution(object):
    def dfs(self, board, i, j):
        m, n = len(board), len(board[0])
        board[i][j] = 'o'

        if i<m-1 and board[i+1][j]=='O': self.dfs(board, i+1, j)
        if i>0 and board[i-1][j]=='O':   self.dfs(board, i-1, j)
        if j>0 and board[i][j-1]=='O':   self.dfs(board, i, j-1)
        if j<n-1 and board[i][j+1]=='O': self.dfs(board, i, j+1)

    def printBoard(self, board):
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                print board[i][j], 
            print

    def solve(self, board):
        if not board:   return
        m, n = len(board), len(board[0])

        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    print i, j
                    self.dfs(board, i, j)
        for j in [0, n-1]:
            for i in xrange(m):
                if board[i][j] == 'O':
                    print i, j
                    self.dfs(board, i, j)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'o':
                    board[i][j] = 'O'
        self.printBoard(board)

board = ['X X X X'.split(), 'X O O X'.split(), 'X X O X'.split(), 'X O X X'.split()]
s = Solution()
s.solve(board)
