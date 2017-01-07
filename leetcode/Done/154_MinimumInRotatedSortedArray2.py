#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
''' Given a rotated sorted array, find the minimum of the array. This array may contain duplicates.

    Inp: [4, 5, 6, 7, 0, 0, 0, 1, 1, 2]
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
            elif nums[mid] < nums[left]: # If nums[mid] < nums[right], mid is after the pivot. Moving left to mid+1, will move mid further away from pivot. Hence, we move right to mid
                right = mid
            else: #If mid is not different from left and right, then we have no information to proceed. But we know for sure that we can eliminate right
                #Note: We can't eliminate left because of input cases like [1, 3]. The underlying fact is that left and mid can overlap, whereas if mid and right overlap the loop breaks (mid and right overlap means left == right)
                right -=1
        return nums[right] #We return nums[left] or nums[right] since left==right when the loop breaks
s = Solution()
print s.findMin([4, 5, 6, 1, 2, 3])
print s.findMin(range(-1, 8))
print s.findMin(range(8, -9, -1))
