#https://leetcode.com/problems/elimination-game/
'''In a list of numbers of 1 through N, first remove every other number starting
from the left. Next, remove every other number starting from the right most 
of the remaining numbers. Return the number that survives to the very end.

Inp: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Out: 6 (123456789 -> 2468 -> 26 -> 6)
'''

class Solution(object):
    def lastRemaining(self, n):
        # If n is 1, it's the last survivor trivially
        if n==1:
            return 1

        # Since every game begins with L->R all the odd numbers get eliminated
        # first. We then find the survivor of the remaining numbers beginning
        # from the right. And multiply that survivor by 2.
        # Eg: 123456789->2*(1234). Since 3 is the surivor of 1234 starting backwards
        # the elimination winner is 2*3 = 6

        # Calculating the winner from right is the same as calculating winner
        # from left and removing the value from n+1
        return 2*((n/2)+1-self.lastRemaining(n/2))

s = Solution()
print s.lastRemaining(9)
for i in xrange(1, 10):
    print i, s.lastRemaining(i)
