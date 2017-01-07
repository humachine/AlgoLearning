#https://leetcode.com/problems/majority-element/
''' Given an unsorted array of numbers, find the majority element in the array (appears more than int(n/2) times). Assume that majority element always exists.

    Inp: [2, 2, 3, 2, 3]
    Out: 2

    Inp: [2, 2, 2, 3, 3, 3, 3, 3, 2]
    Out: 3
'''
class Solution(object):
    def majorityElement(self, nums):
        cand, count = nums[0], 0
        # Boyer-Moore's Voting Algorithm
        # REMEMBER: If count of a candidate hits zero, you immediately change candidates.
        for num in nums:
            if num == cand: #Increase count for candidate if num==candidate
                count+=1
            elif count == 0: #If count is ZERO, we switch candidates
                cand, count = num, 1
            else:
                count-=1
        return cand

s = Solution()
print s.majorityElement([2, 2, 3, 2, 3, 2, 3])
print s.majorityElement([2, 2, 2, 3, 3, 3, 3, 3, 2])
