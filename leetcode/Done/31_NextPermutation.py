#https://leetcode.com/problems/next-permutation/
''' Given a permutation of digits, find the lexicographically next permutation.

    Inp: 123
    Out: 132

    Inp: 313
    Out: 331

    Inp: 321
    Out: 123
'''
class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return nums
        n = len(nums)
        left, right = n-2, n-1
        
        # First, we locate the rightmost point in the array at which nums[i] > nums[i+1]
        # i.e, we find the rightmost index at which the array decreases
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1

        # If there is no such index, then we have a completely descending sorted array
        # In this case, we cycle through and return the ascending sorted sequence
        if left < 0:
            nums.reverse()
        else:
            # Here, we try to find the max index at which arr[i] > arr[left]
            right = n-1
            while right>left:
                if nums[right] > nums[left]:
                    break
                right -=1
            # We swap arr[left] and arr[right] and reverse the rest of the list
            nums[left], nums[right] = nums[right], nums[left]
            nums[left+1:] = nums[left+1:][::-1]
        return nums

s = Solution()
print s.nextPermutation([1, 2, 3])
print s.nextPermutation([3, 1, 3])
print s.nextPermutation([3, 2, 1])
print s.nextPermutation([2, 3, 1])
