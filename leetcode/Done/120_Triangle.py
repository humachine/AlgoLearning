#https://leetcode.com/problems/triangle/
'''
Given a triangle of numbers, find the minimum path sum from top to the bottom row. 
At each step, one may only move to the adjacent elements on the row below. 

Inp:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

Out: 11 (2+3+5+1)
'''
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n_rows, max_cols = len(triangle), len(triangle[-1])
        MAX_INT = float('inf')
        
        # Prev[j] represents the min path sum to reach element j on the row above
        # from the top-left element
        prev = [float('inf')]*max_cols
        prev[0] = triangle[0][0]
        
        curr = [MAX_INT]*max_cols
        for row in xrange(1, n_rows):
            for j in xrange(row+1):
                curr[j] = triangle[row][j] + min(prev[j], prev[j-1] if j>0 else MAX_INT)
                if j>=2:
                    prev[j-2] = MAX_INT
            # Setting previous with MAX_INT so that it can be swapped with curr later
            prev[-2:] = [MAX_INT]*2
            curr, prev = prev, curr
        return min(prev)

    def minimumTotal(self, triangle):
        # In this bottom-up approach, we find the minimum of all paths from the
        # bottom row to the top element.
        #
        # At each row, the shortest path from the bottom row to that element is
        # the sum of that element with the minimum of its 2 adjacent elements in
        # the row below.
        if not triangle:
            return 0
        # Initializing path sums with the last row of the triangle
        path_sums = list(triangle[-1])
        num_rows = len(triangle)

        for row in xrange(num_rows-2, -1, -1):
            for col in xrange(row+1):
                path_sums[col] = triangle[row][col] + min(path_sums[col], path_sums[col+1])
        return path_sums[0]

s = Solution()
inp = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print s.minimumTotal(inp)
inp = [[-1],[-2,-3]]
print s.minimumTotal(inp)
