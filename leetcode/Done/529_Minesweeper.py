#https://leetcode.com/problems/minesweeper/
'''You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

    1) If a mine ('M') is revealed, then the game is over - change it to 'X'.
    2) If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    3) If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    4) Return the board when no more squares will be revealed.
'''
import collections
class Solution(object):
    def updateBoard(self, board, click):
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = collections.deque()
        queue.append((click[0], click[1]))
        valid_neighbours = lambda (i, j): 0<=i<m and 0<=j<n

        while queue:
            # queue.pop makes it DFS. queue.popleft() makes it BFS 
            # Here we can observe that BFS is very slow for large inputs. BFS
            # processes all nodes of a level before moving on to the next level. 
            # In this manner, there are nodes that are added multiple times
            # to the queue from their various neighbours and are hence processed
            # multiple times.
            x, y = queue.pop()
            if board[x][y] == 'M':
                board[x][y] = 'X'
            else:
                # Filter out the valid neighbours
                neighbours = filter(valid_neighbours, [(x-1, y), (x+1, y), 
                    (x, y-1), (x, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)])
                # Count the number of mines amongst the neighbours
                mine_count = sum([board[i][j]=='M' for i, j in neighbours])
                # If at least one neighbour is a potential mine, store the mine count.
                if mine_count > 0:
                    board[x][y] = str(mine_count)
                # If no neighbour is a mine, then add all unvisited neighbours
                # to the queue for future processing
                else:
                    board[x][y] = 'B'
                    queue.extend([(i, j) for (i, j) in neighbours if board[i][j]=='E'])
        return board
s = Solution()
inp = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
print s.updateBoard(inp, [3, 0])
print s.updateBoard(inp, [1, 2])
