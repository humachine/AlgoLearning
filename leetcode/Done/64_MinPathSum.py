#https://leetcode.com/problems/minimum-path-sum
'''Given that you can only move bottom or right, what is the minimum path sum
to the bottom-right of a grid, starting with the top-left.

    Inp: [[1, 3],
        [2, 4]]
    Out: 7 (1->2->4)
'''
class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        # $path_sums represents the current row of the minPathSum solution matrix
        path_sums = list(grid[0])
        # We initialize $path_sums with cumSums of the first row of the grid
        for j in xrange(1, n):
            path_sums[j] += path_sums[j-1]

        for i in xrange(1, m):
            # Since there's only one way to reach grid[i][0] for any i, we just
            # add the previous pathSum to the current grid value
            path_sums[0] += grid[i][0]
            for j in xrange(1, n):
                # We pick the minimum path sum of the paths to reach the top
                # cell and the left cell; and add the current grid value to it.
                path_sums[j] = min(path_sums[j], path_sums[j-1]) + grid[i][j]
        return path_sums[-1]
