#https://leetcode.com/problems/number-of-islands/
'''
Return number of islands found in grid. (4-connected)
11110
11010
11000
00000

Out: 1

11000
11000
00100
00011
Out: 3 (0,0 to 1,1, both inclusive) and unit island (2, 2) and (3, 3 to 4, 4)
'''
class Solution(object):
    def dfs(self, grid, x, y, islandLabel):
        nodes = [(x, y)]
        m, n = len(grid), len(grid[0])
        # Straightforward DFS into all valid neighbours and updating them
        for x, y in nodes:
            grid[x][y] = islandLabel
            if x>0 and grid[x-1][y]=='1':   self.dfs(grid, x-1, y, islandLabel)
            if x<m-1 and grid[x+1][y] == '1': self.dfs(grid, x+1, y, islandLabel)
            if y>0 and grid[x][y-1]=='1':    self.dfs(grid, x, y-1, islandLabel)
            if y<n-1 and grid[x][y+1] == '1': self.dfs(grid, x, y+1, islandLabel)

    def bfs(self, grid, x, y, islandLabel):
        nodes = [(x, y)]
        m, n = len(grid), len(grid[0])
        grid[x][y] = islandLabel
        # We use the list 'nodes' to simulate a queue (which we initialize with (x, y)).
        # For each valid neighbour, we add them to the queue after updating the gridvalue with the islandLabel
        for x, y in nodes:
            if x>0 and grid[x-1][y]=='1':  
                grid[x-1][y] = islandLabel
                nodes.append((x-1, y))
            if x<m-1 and grid[x+1][y] == '1':
                grid[x+1][y] = islandLabel
                nodes.append((x+1, y))
            if y>0 and grid[x][y-1]=='1':   
                grid[x][y-1] = islandLabel
                nodes.append((x, y-1))
            if y<n-1 and grid[x][y+1] == '1':   
                grid[x][y+1] = islandLabel
                nodes.append((x, y+1))
        return

    def numIslands(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        islandLabel = 2 #islandLabels begin at 2 so that there's no confusion with unvisited islands which still have '1' as their value. It also helps in recovering the original array
        # Iterate through the gird. Every teime you come across a 1, either trigger BFS or DFS
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == '1':
                    self.bfs(grid, x, y, islandLabel)
                    islandLabel+=1
        return islandLabel-2

s = Solution()
# grid = [ list('11110'), list('11010'), list('11000'), list('00000'),]
grid = [ list('11000'), list('11000'), list('00100'), list('00011')]
print s.numIslands(grid)
