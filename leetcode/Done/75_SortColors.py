#https://leetcode.com/problems/sort-colors/
'''
Dutch National Flag problem
    Inp: [0, 1, 2, 2, 1, 0, 1]
    Out: [0, 0, 1, 1, 1, 2, 2]
'''
class Solution(object):
    def sortColors(self, nums):
        if len(nums)<=1:    return

        '''
        We split the array into 3 one sided intervals: [0...low), [low...mid), mid..high [high..end)
        0..low contains only 0s
        low..mid contains only 1s
        high..end contains only 2s

        We constantly look at the element array[mid] and try to assign it to one of the 3 sections of the array.
        '''
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            # If arr[mid] is 0, we swap it with array[low]. Thus arr[low] is now 0 and arr[mid] is now quite possibly 1
            # Note: in the case that there have so far been no 1s, mid = low. In which case swapping arr[mid] with arr[low] is a self-swap which performs nothing
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low, mid = low+1, mid+1
            # If arr[mid] is 1, we just absorb it into the low..mid section and thus increment mid by 1
            elif nums[mid] == 1:
                mid+=1
            # If arr[mid] is 2, we just swap arr[high] with arr[mid]. Arr[high] is now 2, which implies we can decrement hi. We then process arr[mid] once again.
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1

s = Solution()
print s.sortColors([0, 1, 2, 2, 1, 0, 1])
print s.sortColors([1, 0])
