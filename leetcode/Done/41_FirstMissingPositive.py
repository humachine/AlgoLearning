#https://leetcode.com/problems/first-missing-positive/
''' Given an unsorted integer array, find the first missing positive integer.

    Inp: [1, 2, 0]
    Out: 3

    Inp: [-2, 84, -3, 7, 5]
    Out: 1

    Inp: [-1,4,2,1,9,10]
    Out: 3
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in xrange(n):
            # For each i, if nums[i] is a positive number, we try to put it in its appropriate location.
            # While nums[i] is not at its position, we swap it with the number at its position.
            # After each swap, we check again if the new swapped value is at its right position. If not, we swap again.
            # At each instance, a swap ensures that ONE number goes to its rightful location (or there's a copy of this number at the rightful location).
            # Since there are n, numbers we can perform at most O(n) swaps
            while 0 < nums[i] < n and (nums[nums[i]-1] != nums[i]):
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i, num in enumerate(nums):
            if num!=i+1: #If any number does not match its index+1, then we return the missing index
                return i+1
        return n+1 #If all numbers are present, then we return n+1

s = Solution()
print s.firstMissingPositive([1, 2, 0])
print s.firstMissingPositive([-2, 84, -3, 7, 5])
print s.firstMissingPositive([-1, 4, 2, 1,  9, 10])
