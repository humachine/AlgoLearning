#https://leetcode.com/problems/contains-duplicate/
"""test cases
    Inp: [1, 2, 3, 4]
    Out: False (all numbers are distinct
    Inp: [1, 2, 3, 3]
    Out: True (3 is repeated)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        numDict = set()
        for num in nums:
            if num in numDict:
                return True
            numDict.add(num)
        return False
