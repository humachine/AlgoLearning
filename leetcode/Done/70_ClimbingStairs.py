#https://leetcode.com/problems/climbing-stairs/
"""Test Cases
    2: 2
    1: 1
    3: 3 [1+2, 2+1, 1+1+1]
    4: 5 [1+2+1, 2+1+1, 1+1+2, 1+1+1+1, 2+2]
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            raise Exception

        #prev - number of ways to reach i-1
        #prev_prev - number of ways to reach i-2
        prev = prev_prev = 1

        for i in xrange(2, n+1):
            prev, prev_prev = prev + prev_prev, prev

        return prev

s = Solution()
print s.climbStairs(4)
