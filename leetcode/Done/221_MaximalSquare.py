#https://leetcode.com/problems/maximal-square/
'''
Given a grid, what is the size of the largest square that can be formed from this grid
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Out: 4
'''
class Solution(object):
    def maximalSquare(self, matrix):
        '''
        We set up a 2-D DP
        DP[i][j] = the side of the largest square that can be formed for whom the bottom-right corner is (i, j)
        DP[i][j] = 1 + min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
        '''
        if not len(matrix) or not len(matrix[0]):   return 0
        m, n = len(matrix), len(matrix[0])
        grid = [ [0 for x in xrange(n+1)] for y in xrange(m+1)]
        maxSide = 0

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    grid[i+1][j+1] = 1 + min(grid[i][j+1], grid[i+1][j], grid[i][j])
                    maxSide = max(maxSide, grid[i+1][j+1])
        return maxSide**2 #Returning area of the maximal square that can be formed
