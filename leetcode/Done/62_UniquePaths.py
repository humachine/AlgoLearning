#https://leetcode.com/problems/unique-paths/
'''Given that you can only move bottom or right, what is the number of ways
you can reach the bottom-right of a grid, starting with the top-left.

    Inp: 2x2
    Out: 2
'''
class Solution(object):
    def uniquePaths(self, m, n):
        if not m or not n:
            return max(m, n)

        # Ways represents a row of the number_of_ways matrix
        # We initialize ways with 1s, since every cell of the first row has exactly one way of being reached
        ways = [1]*n
        for i in xrange(1, m):
            # Every cell of the first column also has 1 way of being reached
            ways[0] = 1
            for j in xrange(1, n):
                # Number of ways to reach a cell = #ways from top + #ways from left
                # ways[j] = number of ways from the top (until it's overwritten)
                # ways[j-1] = number of ways to reach the cell at its left
                ways[j] = ways[j] + ways[j-1]
        return ways[-1]
