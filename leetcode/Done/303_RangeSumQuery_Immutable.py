#https://leetcode.com/problems/range-sum-query-immutable/
'''
Given an array of numbers and i, j find the sum of numbers between the indices i, j (both inclusive)

    Inp: [-2, 0, 3, -5, 2, -1], (0, 2)
    Out: [1]

    Inp: [-2, 0, 3, -5, 2, -1], (2, 5)
    Out: [-1]
'''
class NumArray(object):
    def __init__(self, nums):
        self.arr = nums
        self.sums = [0]
        # Compute continuous sums such that sums[i] = sum of arr[:i]
        for i in xrange(len(nums)):
            self.sums.append(self.sums[i]+nums[i])
        
    def sumRange(self, i, j):
        return self.sums[j+1] - self.sums[i] # To compute sum of all numbers including j (i.e sum arr[:j+1], we use sums[j+1]. We finally remove the sum of all numbers before i (sums[i])
        
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
