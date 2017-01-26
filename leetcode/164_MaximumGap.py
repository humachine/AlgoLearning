#https://leetcode.com/problems/maximum-gap
'''
Given an unsorted array, find the maximum gap between consecutive elements in the sorted version of the array

Inp: [3, 1, -4, 5, 8]
Out: 5 (-4 to 1)
'''
class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2: return 0

        minimum, maximum, n = min(nums), max(nums), len(nums)
        average = sum(nums)/n
        numberMap = {nums[i]:i for i in xrange(n)}
        if minimum == maximum:
            return 0
        maxGap = 1  
        start = minimum
        while start < maximum:
            nextElem = 
            # Find next elem, update maxGap
