#https://leetcode.com/problems/jump-game/
'''
From arr[i], you can jump arr[i] places. Return if you can reach the last index of the array.
    Inp: [2,3,1,1,4]
    Out: True
    Inp: [3, 2, 1, 0, 4]
    Out: False
'''
class Solution(object):
    def canJump(self, nums):
        if not nums: return True
        canReach = 0
        # At each step, we calculate the maximum index that can be reached by just array values upto the current value
        # When we are at a particular index, if index > maxReachableValue, then we return False
        for i, jump in enumerate(nums):
            if i > canReach:
                return False
            canReach = max(canReach, i+jump)
        return True
s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])
