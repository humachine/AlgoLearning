#https://leetcode.com/problems/maximum-subarray/

"""Test Cases:
    Inp: [-2,1,-3,4,-1,2,1,-5,4]
    Out: 6 ([4, -1, 2, 1])
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currSum = nums[0]
        maxSum = nums[0]
        #CurrSum is usually new number unless when it goes to negative. 
        #if currSum<0 && newNum is positive, currSum will become equal to newNum
        #This represents resetting of the sequence once the sum dips below zero
        #This also ensures that even if all numbers are negative, it still picks the array max
        for num in nums[1:]:
            currSum = max(num, currSum+num)
            maxSum = max(maxSum, currSum)
        return maxSum
s = Solution()
print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print s.maxSubArray([-2, -3, -3, -832, -78, -1])
print s.maxSubArray([-2, -3, -8, -832, -78, -5])
