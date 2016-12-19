#https://leetcode.com/problems/happy-number/
"""
Test case:
    Inp: 19
    Out: True, 19->82(1^2+9^2)->68->100-> 1

    Inp: 21
    Out: False, 21->5->25->29->85->89->....->21
"""
class Solution(object):
    def squareSum(self, n):
        Sum = 0
        for digit in map(int, str(n)):
            Sum += digit**2
        return Sum

    def isHappy(self, n):
        '''Pick a number and keep performing square sums until you hit 1 or repeat a number'''
        nums = set()
        while n not in nums:
            if n==1:
                return True
            nums.add(n)
            n = self.squareSum(n)
        return False

s = Solution()
print s.isHappy(19)
print s.isHappy(21)
