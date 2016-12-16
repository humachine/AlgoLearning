#https://leetcode.com/problems/move-zeroes/
"""
Inp: [0, 1, 0, 3, 12]
Out: [1, 3, 12, 0, 0]
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        #Keep track of number of zeros seen
        #For every non zero number, swap num[i], num[i-numZeros]
        for i in xrange(len(nums)):
            if nums[i] == 0:
                num_zeroes += 1
            else:
                nums[i-num_zeroes], nums[i] = nums[i], nums[i-num_zeroes]

s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print nums
