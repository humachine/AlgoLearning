#https://leetcode.com/problems/missing-number/
'''
Given N numbers from 0, 1, 2, ... n, find the missing number from them. 

    Inp: 3, 2, 0
    Out: 1
'''
class Solution(object):
    def missingNumberXOR(self, nums):
        # Here we XOR all the numbers with 0 to N. Only the missing number won't have a corresponding pairing with a number from the array.
        ans = 0
        for i in xrange(len(nums)):
            ans = ans ^ nums[i] ^ i
        ans ^= len(nums)
        return ans

    def missingNumber(self, nums):
        nums.sort()
        left, right = 0, len(nums)
        # The culprit number will be the first number which is at a position greater than itself. We perform a simple binary search to locate such a position.
        while left < right:
            mid = (left+right)/2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid+1
        return right
s = Solution()
print s.missingNumberXOR([3, 1, 0])
print s.missingNumberXOR([0])
