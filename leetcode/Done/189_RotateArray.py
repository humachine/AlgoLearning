#https://leetcode.com/problems/rotate-array/
'''Given an array of N elements, rotate it (circular) by k.

    Inp: [1, 2, 3, 4, 5, 6, 7] with K=3
    Out: [5, 6, 7, 1, 2, 3, 4]
'''
class Solution(object):
    def rotate(self, nums, k):
        # We first simplify k to a range between 0 and N (=len(nums))
        k = k%len(nums) 
        # We then reverse the last k numbers
        nums[-k:] = reversed(nums[-k:])
        # We then reverse all the remaining numbers
        nums[:-k] = reversed(nums[:-k])
        # We now finally reverse the entire array
        nums.reverse()
s = Solution()
print s.rotate(range(1, 8), 3)
print s.rotate([1,2], 3)
