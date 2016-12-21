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
    def printBoard(self, board):
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                print board[i][j], 
            print

    def solve(self, board):
        ''' We clearly know that only Os that are not connected to any borders/edges get swallowed by their surrounding Xs.
        Hence we just pick a list of border Os and flood fill their components with a new letter (say 'o'). 
        Once we are done, we convert every 'o' back to 'O' and every 'O' to 'X'
        '''
        if not board:   return
        m, n = len(board), len(board[0])
        # Any board lesser than 3x3 cannot have any swallowed Os, since everything is touching a border (or two)
        if m<=2 or n<=2:    return

        cells = []
        # We first attempt to select and form a list of border Os. Here we use a list to simuluate a Queue
        for i in [0, m-1]:
            for j in xrange(n):
                if board[i][j] == 'O':
                    cells.append((i, j))
        for i in xrange(m):
            for j in [0, n-1]:
                if board[i][j] == 'O':
                    cells.append((i, j))

        # For each of the border Os, we try to bfs from its neighbours by using a queue (simulated using a list)
        for x, y in cells:
            board[x][y] = 'o'
            if x>0 and board[x-1][y]=='O': cells.append((x-1, y))
            if x<m-1 and board[x+1][y]=='O': cells.append((x+1, y))
            if y>0 and board[x][y-1]=='O': cells.append((x, y-1))
            if y<n-1 and board[x][y+1]=='O': cells.append((x, y+1))

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = 'XO'[board[i][j]=='o']
        # self.printBoard(board)

board = ['X X X X'.split(), 'X O O X'.split(), 'X X O X'.split(), 'X O X X'.split()]
s = Solution()
s.solve(board)
