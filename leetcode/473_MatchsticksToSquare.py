#https://leetcode.com/problems/matchsticks-to-square/
'''
    Inp: [1, 1, 2, 2, 2]
    Out: True (you can make a square of side 2 by using the 2 sticks of length 1 as a side)

    Inp: [3, 3, 3, 3, 4]
    Out: False (no possible placements of these stick lengths can generate a square)
'''
class Solution(object):
    def makesquare(self, nums):
        if len(nums) < 4:
            return False
        total = sum(nums)
        if total & 0b11 > 0 or max(sums) > total/4:
            return False
        return False
