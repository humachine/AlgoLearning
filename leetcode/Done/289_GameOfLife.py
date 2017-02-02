#https://leetcode.com/problems/game-of-life/
'''
The Game of Life is a cellular automaton which works such:
    - Each cell has a start state (1 or 0)
    - Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    - Any live cell with two or three live neighbors lives on to the next generation.
    - Any live cell with more than three live neighbors dies, as if by over-population..
    - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Given a board state, return the next state of the board.
'''
class Solution(object):
    def gameOfLife(self, board):
        if board and board[0]:
            m, n = len(board), len(board[0])
            validNeighbours = lambda (x, y): (x>=0 and y>=0 and x<m 
                    and y<n and board[x][y] in [ALIVE_TO_DEAD, ALIVE])

            # There are 4 possible transition states for a cell of the board:
                # Dead -> Alive, Alive->Dead, Dead->Dead, Alive->Alive

            # If the cell is originally alive, it can die only if it has <2 or >3 live neighbours
            # If the cell is originally dead, it can come to life only if it has exactly 3 live neighbours
            DEAD_TO_ALIVE, DEAD = 2, 0
            ALIVE_TO_DEAD, ALIVE = -1, 1

            for i in xrange(m):
                for j in xrange(n):
                    neighbours = [(i-1, j-1), (i, j-1), (i+1, j-1),
                            (i-1, j), (i+1, j),
                            (i-1, j+1), (i, j+1), (i+1, j+1)]
                    # Filtering out the valid neighbours on the board that are alive
                    live_neighbours = filter(validNeighbours, neighbours)

                    # If cell was previously alive, it can only die by over/under-population
                    if board[i][j] == ALIVE:
                        if len(live_neighbours) < 2 or len(live_neighbours) > 3:
                            board[i][j] = ALIVE_TO_DEAD
                    # If cell was previously dead, it can revive only if it has =3 live neighbours
                    elif len(live_neighbours) == 3:
                        board[i][j] = DEAD_TO_ALIVE
                    # If we are on row 2 and below, we start updating the i-2th row's values
                    if i>1:
                        board[i-2][j] = 1 if board[i-2][j] in [ALIVE, DEAD_TO_ALIVE] else 0

            for i in xrange(m-2, m):
                for j in xrange(n):
                    board[i][j] = 1 if board[i][j] in [ALIVE, DEAD_TO_ALIVE] else 0
        return board
s = Solution()
board = [[1, 1]]
board = [[0,0,0,0,0],[0,1,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
# board = [[0,0,0,0,0]
        # [0,1,1,0,0]
        # [0,1,0,1,0]
        # [0,0,1,0,0]
        # [0,0,0,0,0]]
print s.gameOfLife(board)
