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

    def backTrack(self, nums, start, remaining, comb):
        # If our sum has exceeded target, then the remaining amount will be -ve. Hence we just return
        if remaining<0:
            return
        # If we have reached target, remaining will reach zero. We count this is as 1 extra combination
        if remaining==0:
            comb[0]+=1
            return
        # We go through all numbers, backTrack on the remaining sum
        for i in xrange(0, len(nums)):
            # If the number > remaining, we break since all forthcoming numbers will also > remaining (ascending sorted)
            if nums[i]>remaining:
                break
            self.backTrack(nums, i, remaining-nums[i], comb)

    def combinationSum4BT(self, nums, target):
        ''' In another standard BT solution, we try to reach target using nums'''
        nums.sort()
        comb = [0]
        self.backTrack(nums, 0, target, comb)
        return comb[0]

s = Solution()
print s.combinationSum4([1, 3, 2], 4)
print s.combinationSum4BT([1, 3, 2], 4)
print s.combinationSum4BT([1, 2, 4], 14)
print s.combinationSum4([1, 2, 4], 14)
print s.combinationSum4([1, 2, 4], 32)
print s.combinationSum4BT([1, 2, 4], 32)
