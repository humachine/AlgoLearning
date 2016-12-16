#https://leetcode.com/problems/single-number/

# Assuming that "Every number appears twice except for one" means "Every number appears EXACTLY twice except for one"
"""Test cases
    Inp: [3, 8, 3, 7, 8, 4, 4]
    Out: 7 (only number that does not appear twice)
"""
class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

s = Solution()
print s.singleNumber([3, 8, 3, 7, 8, 4, 4])
