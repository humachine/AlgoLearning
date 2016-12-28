#https://leetcode.com/problems/random-pick-index/
'''
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Inp: [1,2,3,3,3]
// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
'''
import random
from bisect import bisect_left
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pickSorting(self, target):
        '''This solution doesn't pass TLE'''
        nums = [(self.nums[i], i) for i in xrange(len(self.nums))]
        nums.sort(key = lambda x: x[0])
        l, r = bisect_left(nums, (target, 0)), bisect_left(nums, (target+1, 0))
        count = (r-l)
        return nums[l+random.randrange(count)][1]
        
    def pickReservoirSampling(self, target):
        ''' To randomly pick 1 element out of a list of size N is easy. (return list[randrange(n)])
        If we don't know N in advance and we STILL have to perform the same, we use reservoir sampling.

        We keep the first element in memory (say result).  We also keep a running count of number of numbers we've seen. 
        For all i>1: with probability (1/i) we replace the original element with nums[i]
        With probability (1-1/i), we retain the original result.

        For i=say n, Probability of picking ith element = 1/n
        Probability of picking one of the previous elements is (1-1/n) = (n-1)/n for (n-1) elements.
        Which is the same as 1/n for each and every element (can be proved by induction)
        '''
        count = 0
        nums = self.nums
        result = -1
        for i in xrange(len(nums)):
            if nums[i] == target:
                count += 1
                if random.randrange(count)==0:
                    result = i
        return result

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.pickReservoirSampling(target)

obj = Solution([1, 3, 2, 3, 3])
print obj.pick(3)
