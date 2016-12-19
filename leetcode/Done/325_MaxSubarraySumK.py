#https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
"""test cases
    Inp: [1, -1, 5, -2, 3] k=3
    Out: 4 ([1, -1, 5, -2] adds up to 3)
    Inp: [-2, -1, 2, 1] k=1
    Out: 2 ([-1, 2] adds up to 1)
    Inp: [2, 3, 6] k=4
    Out: 0
"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:    return 0
        if len(nums)==1:    return int(nums[0]==k)

        n = len(nums)
        cumSum = {}
        cumSum[0] = -1
        Sum = maxLen = 0
        '''
        Compute running sums. For each sum, check if there exists a cumulative sum K lesser than this.
        Update cumSums only if you have a new key. 
        DO NOT UPDATE existing keys with new values. Since i is increasing, newer values always > older values
        For maxLen, we are looking for the least possible i for which cumSum upto i is a particular number
        '''
        for i in xrange(n):
            Sum += nums[i]
            if Sum-k in cumSum:
                maxLen = max(maxLen, i-cumSum[Sum-k])
            if Sum not in cumSum:
                cumSum[Sum] = i
        return maxLen

s = Solution()
print s.maxSubArrayLen([1, -1, 5, -2, 3], 3)
print s.maxSubArrayLen([2, -1, 2, 1], 1)
print s.maxSubArrayLen([2, 3, 6], 4)
