#https://leetcode.com/problems/wiggle-sort/
''' Given an unsorted array, reorder it in-place in such a manner that nums[0] <= nums[1] >= nums[2] <= nums[3] ...

    Inp: [3, 5, 2, 1, 6, 4]
    Out: [1, 6, 2, 5, 3, 4] is a possible solution
'''
class Solution(object):
    def wiggleSort(self, nums):
        ''' At any a[i], if i is odd, we make sure that a[i] >= a[i+1]. If not, we swap a[i] with a[i+1].
        For every i, we have an invariant - which is that all numbers upto arr[i] are wiggle-sorted.
        At each i, we just make sure that arr[i] & arr[i+1] adhere to the wiggle sort.
        '''
        for i in xrange(len(nums)-1):
            # Odd Index (hump number which is greater than both its neighbours)
            if i & 0b1 and nums[i] < nums[i+1]:
                # If number < nextNumber, swap them
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif not i&0b1 and nums[i] > nums[i+1]:
                # If number > nextNumber, swap them
                nums[i], nums[i+1] = nums[i+1], nums[i]
