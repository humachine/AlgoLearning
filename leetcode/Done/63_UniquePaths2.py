#https://leetcode.com/problems/unique-paths/
'''Given that you can only move bottom or right, what is the number of ways
you can reach the bottom-right of a grid, starting with the top-left.

    Inp: 2x2
    Out: 2
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0]*n
        for j in xrange(n):
            # On the first row, all cells that are to the right-side of any obstacle
            # have no paths to them
            if obstacleGrid[0][j]:
                break
            ways[j] = 1

        # Ways represents a row of the number_of_ways matrix
        # We initialize $ways with the first row of the num_paths solution matrix
        for i in xrange(1, m):
            # A cell on the first column has a way to be reached ONLY if its cell
            # does not have an obstacle and there was a path to the cell above it
            ways[0] = (1-obstacleGrid[i][0]) & ways[0]
            for j in xrange(1, n):
                # Number of ways to reach a cell = #ways from top + #ways from left
                # ways[j] = number of ways from the top (until it's overwritten)
                # ways[j-1] = number of ways to reach the cell at its left
                # If there's an obstacle in a cell, there's no way to reach this cell
                if obstacleGrid[i][j]:
                    ways[j] = 0
                else:
                    ways[j] = ways[j] + ways[j-1]
        return ways[-1]

s = Solution()
grid = [[0], [0]]
print s.uniquePathsWithObstacles(grid)
