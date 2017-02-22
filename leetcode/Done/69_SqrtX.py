#https://leetcode.com/problems/sqrtx/
'''Given an integer N, return int(sqrt(N))

Inp: 15
Out: 3
'''
class Solution(object):
    def mySqrt(self, x):
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = (left+right)/2
            # If mid*mid <= x, move the left end of the window by 1. 
            # Also, cache the most recently used window left-end
            if mid <= (x/mid):
                left = mid+1
                ans = mid
            # Also, if mid*mid >= x, we need to make the window smaller
            else:
                right = mid-1
        # We finally return ans - which is actually the greatest value of left 
        # that has left*left <= x
        return ans

s = Solution()
for i in xrange(0, 100):
    if s.mySqrt(i) != int(i**0.5):
        print i
