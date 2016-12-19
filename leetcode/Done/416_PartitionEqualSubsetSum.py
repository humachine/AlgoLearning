#https://leetcode.com/problems/partition-equal-subset-sum/

# There also exists a bitset solution which uses O(max possible sum of all numbers) space and O(N) time

"""
    Inp: [1, 5, 11, 5]
    Out: True (can be partitioned into 11 and the rest)

    Inp: [1, 2, 3, 5]
    Out: False (no equal partition of the array possible)

    Inp: [1, 2, 3, 4, 5, 6, 7, 8]
    Out: True (1, 8, 3, 6 and the rest is an equal partition)
"""
from bisect import bisect_left
class Solution(object):
    def canPartition(self, nums):
        if not nums:
            return True
        if len(nums) == 1:
            return False

        arraySum = sum(nums)
        if arraySum & 1 == 1:
            return False
        # If we have to partition the array, we have to find a subset of the array that adds up to arraySum/2

        nums = sorted(nums)
        target = arraySum/2
        n = len(nums)

        # li1 is a set which contains all the unique sums obtained until now
        # At each step, we take all the possible sums and add the current element to it and update li1
        li1 = {0}
        li2 = []
        for i in xrange(1, n):
            li2 = [nums[i] + x for x in li1]
            li1.update(li2)
        # If arraySum/2 exists in li1, then there exists SOME subset of nums which can split the array
        return target in li1


    def canPartitionDP(self, nums):
        if not nums:    return True
        if len(nums) == 1:  return False

        arraySum = sum(nums)
        target = arraySum/2
        if arraySum & 1:
            return False

        nums = sorted(nums)
        #DP represents a list which contains whether a particular sum can be achieved using a subset of nums
        dp = [False]*(target+1)
        dp[0] = True

        """
        For each number x, we begin from sum and loop down until x
        For each number we loop across, we check if number-x is True. If so, we assign that number to be True too.

        nums = [2, 3, 5]
        Eg: 0 is True
        While looping down, 2 is set to True (2-2=0 is True)
        While looping down, 5, 3 is set to True (5-3=2 is True & 3-3=0 is True)

        Note:
        Had we looped up from x until sum, we would have had incorrect answers
        nums = [1, 2, 5]
        First iteration, 1 is set to True (Since 1-1=0 is True). Then 2 is set to True (2-1=1 is True) and so on ...
        """

        for i in xrange(len(nums)):
            for j in xrange(target, nums[i]-1, -1):
                dp[j] |= dp[j-nums[i]]
        return dp[target]

s = Solution()
print s.canPartitionDP([1, 5, 11, 5])
print s.canPartitionDP([1, 2, 3, 5])
print s.canPartitionDP([1, 2, 5])
print s.canPartition(range(8))
