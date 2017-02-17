#https://leetcode.com/problems/target-sum/
''' Given a series of integers, in how many ways can you get to a target sum
by placing +/- between the integers.

    Inp: [1, 1, 1, 1, 1], Target=3
    Out: 5
        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3
'''
class Solution(object):
    def findWays(self, nums, target, start):
        # If this computation has already been made, we just retrieve it from the memo cache
        # For instance, if we have found that there are 5 ways to reach 15 from
        # nums[8] onwards, cache[(8, 15)] = 5
        if (start, target) in self.cache:
            return self.cache[(start, target)]

        # If we have used all the numbers, we check if we have reached the end target sum
        if start == self.n:
            if target==0:
                return 1
            return 0

        # ways_neg and ways_pos represent the number of ways to reach target
        # by placing a negative/positive sign at the current position in the computation.
        ways_neg = self.findWays(nums, target+nums[start], start+1)
        ways_pos = self.findWays(nums, target-nums[start], start+1)
        num_ways = ways_neg + ways_pos

        self.cache[(start, target)] = num_ways
        return num_ways

    def findTargetSumWays(self, nums, S):
        # cache stores all the ways in which nums[start:] can add upto $target
        self.n = len(nums)
        self.cache = {}
        return self.findWays(nums, S, 0)

s = Solution()
# print s.findTargetSumWays([1, 1, 1, 1, 1], 3)
# print s.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)
print s.findTargetSumWays([2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38],48)
