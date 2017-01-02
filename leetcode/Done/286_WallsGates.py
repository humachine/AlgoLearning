#https://leetcode.com/problems/walls-and-gates/
'''Given a 2D grid with 0 as gates, -1 as wall/obstacles and INF(=2147483647) as empty room.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Inp: 
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF

Out:
      3  -1   0   1
      2   2   1  -1
      1  -1   2  -1
      0  -1   3   4
'''
from Queue import Queue
class Solution(object):
    def wallsAndGates(self, rooms):
        ''' This can be solved by a variety of methods (BFS, Multi-end BFS and DFS).

        This is the multi-end BFS solution, especially fast for boards which have multiple gates. 
        Here, we first just add all the gates to a queue. (Note: Contrasting to the BFS approach below, here we process all the gates and their neighbours first).
        Once the gates are processed, their first level neighbours go into the queue. Only after all the first-level neighbours are visited, do second-level neighbours get visited. 
        In this manner, if a room is visited, it is only visited ONCE and ONLY by the neighbour that is closest to a gate. 
        '''
        if not rooms:   return
        m, n, INF, q = len(rooms), len(rooms[0]), 2147483647, Queue()
        # Check if neighbor is valid in the grid
        isValidNeighbor = lambda (x, y): 0<=x<m and 0<=y<n and rooms[x][y] == INF

        # Pick the gates from the grid
        gates = [(i, j) for i in xrange(m) for j in xrange(n) if rooms[i][j]==0]
        map(q.put, gates)

        while not q.empty():
            i, j = q.get()
            # Filter out only the neighbors that are valid and useful (rooms[x][y] == INF) to us
            neighbours = filter(isValidNeighbor, [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            for x, y in neighbours:
                rooms[x][y] = rooms[i][j]+1
                q.put((x, y))

    # ------------------------------------------------------------
    ''' We run a standard BFS from each gate (0). To all its neighbours whose scores could better by propagation of the current cell's value, we propagate.
    So, starting at each 0, we propagate ahead until we run out of neighbours to keep spreading. 

    This Naive-BFS solution times to roughly O(n^3) and is faster than DFS mostly because of the lack of recursion depth.

    The problem here is again the same. Say, we had a large board with lots of rooms (say O(n*n)). When we process Gate 1, we explore ahead and assign values to the O(n*n) rooms based on the first gate. 
    After the second gate is visited, a good portion of the rooms may be overwritten if they are closer to gate 1 than gate 0.

    This overwriting essentially denotes repetitive runs over some of the rooms.
    '''
    def wallsAndGatesBFS(self, rooms):
        if not rooms:   return
        m, n, INF = len(rooms), len(rooms[0]), 2147483647
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)

    def bfs(self, rooms, x, y):
        m, n, INF, q = len(rooms), len(rooms[0]), 2147483647, Queue()
        q.put((x, y))

        while not q.empty():
            x, y = q.get()
            # We only consider a neighbour that is valid on the grid and would be served by propagating the current cell (x,y)'s score
            isValidNeighbor = lambda (a, b): 0<=a<m and 0<=b<n and rooms[a][b] > rooms[x][y]+1
            neighbours = filter(isValidNeighbor, [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
            for i, j in neighbours:
                rooms[i][j] = rooms[x][y]+1 #Propagating the current cell(x,y)'s score to its validNeighbors
                q.put((i, j))


    # ------------------------------------------------------------
    ''' The solution below is based on a DFS search. We search through the array for 0s and run a dfs search from each of them. For every 0, the dfs performs a search across the board, possibly updating any and every neighbour that can be updated.
    If there's a cell that has neighbours which are greater than 1+cell, then the cell's value propagates to that particular neighbor. In this manner, we begin at every 0 and propagate the scores until we run out of neighbours to propagate.

    In the worst case, we could have O(n*n) gates. And O(n*n) empty rooms (INF), possibly even in a single component. For each of the 0s, there's a DFS that runs potentially across the entire set of empty rooms. This could potentially be a O(n^4) complexity solution.
    '''
    def wallsAndGatesDFS(self, rooms):
        if not rooms:   return
        m, n, INF = len(rooms), len(rooms[0]), 2147483647
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j)

    def dfs(self, rooms, x, y):
        m, n, INF = len(rooms), len(rooms[0]), 2147483647
        isValidNeighbor = lambda (i, j): 0<=i<m and 0<=j<n and rooms[i][j] > rooms[x][y]+1
        neighbours = filter(isValidNeighbor, [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
        for i, j in neighbours:
            rooms[i][j] = rooms[x][y] + 1
            self.dfs(rooms, i, j)

s = Solution()


INF = 2147483647
grid = [ [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]]
s.wallsAndGatesBFS(grid)
