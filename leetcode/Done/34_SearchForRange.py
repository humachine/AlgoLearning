#https://leetcode.com/problems/search-for-a-range/
'''Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Inp: [5, 7, 7, 8, 8, 10], 8
Out: [3, 4]

Inp: [5, 7, 7, 8, 8, 10], 9
Out: [-1, -1]
'''
import bisect
class Solution(object):
    def searchRange(self, nums, target):
        # In this problem, all we are required to perform is to find the left
        # and right limits of the target number in the input array.
        # We just return the values returned by bisect_left and bisect_right-1
        start = bisect.bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            start = end = -1
        else:
            end = bisect.bisect_right(nums, target)-1
        return [start, end]

    def bisect(self, nums, target, left_bisect=True):
        left, right = 0, len(nums)
        while left<right:
            mid = (left+right)/2
            # If nums[mid] > target, then we need to move mid leftward.
            # Hence we move right to mid
            # We perform the equality case only when left_bisect flag is enabled.
            if nums[mid] > target or (left_bisect and nums[mid]==target):
                right = mid
            else:
            # If nums[mid] < target, we need to push left rightwards
                left = mid+1
        return right

    def searchRange(self, nums, target):
        # Here, we write our own bisect_left and bisect_right function
        start = self.bisect(nums, target)
        # Start = len(nums) happens when target is greater than all numbers in
        # the array.
        # if nums[start]!=target, then target isn't present in the array. In this
        # case, $start just represents the location at which target can be inserted
        # to preserve sorting order
        if start == len(nums) or nums[start] != target:
            start = end = -1
        else:
            end = self.bisect(nums, target, False)-1
        return [start, end]

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 5)
print s.searchRange([5, 7, 7, 8, 8, 10], 8)
print s.searchRange([5, 7, 7, 8, 8, 10], 11)
print s.searchRange([], 0)
