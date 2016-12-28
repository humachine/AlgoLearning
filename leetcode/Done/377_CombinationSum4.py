#https://leetcode.com/problems/combination-sum-iv/
'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

    Inp: [1, 2, 3], target = 4
    Out: (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 3) (2, 1, 1) (2, 2) (3, 1)
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        if not target:  return []
        nums.sort()
        n = len(nums)
        # numWays[x] represents the number of ways to reach the sum x using nums
        # numWays[x] = numWays[x-nums[0]] + numWays[x-nums[1]] + ... until x-nums[1] < 0
        # numWays[0] = 1 (just {0})
        numWays = [1] + [0]*target
        for i in xrange(1, target+1):
            for num in nums:
                # if num > current Target i, then we break. Every num henceforth will be > i (sorted ascending)
                if i < num:
                    break
                numWays[i] += numWays[i-num]
        return numWays[-1]
s = Solution()
print s.combinationSum4([1, 3, 2], 4)

