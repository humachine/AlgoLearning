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
        for num in nums:
            count += 1 if num==cand else -1 #Increase count for candidate if num==candidate
            if count < 0: #If candidate count is 0, change candidate
                cand, count = num, 1
        return cand
s = Solution()
print s.majorityElement([2, 2, 3, 2, 3, 2, 3])
print s.majorityElement([2, 2, 2, 3, 3, 3, 3, 3, 2])
