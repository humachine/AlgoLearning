#https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
    Inp: [4 5 6 7 0 1 2], 2
    Out: True
'''
from bisect import bisect_left
class Solution(object):
    def search(self, nums, target):
        ''' Note: This solution works regardless of whether a pivot point actually exists or not.
        Here, we do a typical binary search. 
        At each juncture, we have to pick between either left..mid or mid..right
        We know that in the rotate array, one of left..mid and mid..right will be completely ascending (the one that does not contain the pivot, to be precise)

        At each juncture, we check if target lies within the sorted portion. Else, we check the other half of the array.
        '''
        if not nums:    return -1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            # If nums[mid] == target, return mid
            if nums[mid] == target:
                return mid
            #if nums[left] <= nums[mid], then left..mid is an ascending sequence
            if nums[left] <= nums[mid]:
                # If target lies within this ascending sequence, we look exclusively in this sequence
                if nums[left] <= target < nums[mid]:
                    # loc = left + bisect_left(nums[left:mid], target)
                    # return loc if nums[loc] == target else -1
                    right=mid-1
                # Since target doesn't lie inside that sequence, we now look outside that sequence
                else:
                    left = mid+1
            # If left...mid wasn't an ascending sequence, then mid..right will definitely be one.
            elif nums[mid] <= nums[right]: 
                if nums[mid] < target <= nums[right]: # Similar to above, if target lies in this ascending sequence, search exclusively in this sequence
                    # loc = mid+1 + bisect_left(nums[mid+1:right], target)
                    # return loc if nums[loc] == target else -1
                    left = mid+1
                else: # Since target doesn't lie in mid..right, we now search in low..mid-1
                    right = mid-1
        return -1
s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2], 2)
print s.search([4, 5, 6, 7, 0, 1, 2], 4)
print s.search([4, 5, 6, 7, 0, 1, 2], 14)
print s.search([14, 15,16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
print s.search(range(10), 8)
