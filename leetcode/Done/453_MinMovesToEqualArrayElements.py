#https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""
Min moves to make array elements equal by incrementing n-1 elements of an array at a time
    Inp: [1, 2, 3]
    Out: 3 (123 -> 233 -> 343 -> 444)
"""
class Solution(object):
    def minMoves(self, nums):
        if not nums:    return 0
        return sum(nums) - min(nums)*len(nums)
