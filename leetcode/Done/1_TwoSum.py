#https://leetcode.com/problems/two-sum/
#Instead of creating the dictionary at the beginning, try creating it on the fly
#This gives better best case performance
"""Test cases
Inp: [2, 7, 11, 15], 9
Output: [0, 1]
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numDict = {}
        for i in xrange(len(nums)):
            diff = target - nums[i]
            if diff in numDict and numDict[diff] != i:
                return [numDict[diff], i]
            numDict[nums[i]] = i
s = Solution()
print s.twoSum([2, 7, 11, 15], 17)
