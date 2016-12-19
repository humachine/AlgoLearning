#https://leetcode.com/problems/battleships-in-a-board/
'''
Inp:
    X..X
    ...X
    ...X
Out: 2

Battleships will always have a cell separating them. A battleship is any 
'''
class Solution():
    def countBattleShips(self, board):
        if not board:   return 0
        ships = 0
        m, n = len(board), len(board[0])
        ''' Here we go over the board and try to locate the top/left edges of each ship. 
        This will be denoted by an X which has no Xs to its left or top. In this manner, for each ship, we count only the top/left tip of it.
        '''
        for x in xrange(m):
            for y in xrange(n):
                if board[x][y] == 'X' and (x==0 or board[x-1][y]=='.') and (y==0 or board[x][y-1]=='.'):
                        ships+=1
        return ships
s = Solution()
board = ['X..X', '...X', '...X']
print s.countBattleShips(board)
