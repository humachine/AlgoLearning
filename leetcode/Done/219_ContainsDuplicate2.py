#https://leetcode.com/problems/contains-duplicate-ii/
"""test cases
    Inp: [2, 3, 4, 1, 5, 8, 3], 3
    Out: False
    Inp: [2, 3, 4, 1, 5, 8, 3], 5
    Out: True
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k==0:
            return False
        numSet = set()

        '''To check if duplicate lies in the last k numbers, we maintain a set of the last k numbers seen. 
        At each occasion, we remove the k+1th recent element and check if duplicate exists. 
        '''
        for i in xrange(len(nums)):
            if i>k:
                numSet.remove(nums[i-k-1])
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False
