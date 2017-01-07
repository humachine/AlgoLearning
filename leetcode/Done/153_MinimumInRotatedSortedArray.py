#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
''' Given a rotated sorted array, find the minimum of the array.

    Inp: [4, 5, 6, 7, 0, 1, 2]
    Out: 0
'''
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            # mid essentially oscillates around the pivot before converging on to the pivot element
            mid = (left + right) / 2
            if nums[mid] > nums[right]:  #If nums[mid] > nums[right], then mid is before pivot. We hence move left to mid+1 so as to move mid closer and closer to pivot
                left = mid+1
            else: # If nums[mid] < nums[right], mid is after the pivot. Moving left to mid+1, will move mid further away from pivot. Hence, we move right to mid
                right = mid
        # We can observe that left moves to mid+1 everytime we are in the wrong zone. 
        # Left stops moving rightwards, if it is the pivot element.
        # Only when mid is left of pivot, does left move rightwards
        # The loop breaks when left == right. This happnes only if mid was before pivot and right was at pivot.
        return nums[right] #We return nums[left] or nums[right] since left==right when the loop breaks
s = Solution()
print s.findMin([4, 5, 6, 1, 2, 3])
print s.findMin(range(-1, 8))
print s.findMin(range(8, -9, -1))
