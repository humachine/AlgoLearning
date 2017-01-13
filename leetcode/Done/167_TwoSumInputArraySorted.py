#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

    Inp: [2, 7, 11, 15], 9
    Out: [1, 2] (indices are not zero-based)
'''
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        indices = []
        # We have two pointers pointing to numbers at left and right extremes of array
        while left <= right:
            # If the two numbers add to target, we set the result and break
            if numbers[left] + numbers[right] == target:
                indices = [left+1, right+1]
                break
            # If left number and right number > target, we reduce right. 
            # Reducing right makes right number smaller (since we have an ascending sorted array)
            elif numbers[left] + numbers[right] > target:
                right -= 1
            # If left number and right number < target, we push left pointer rightwards
            else:
                left += 1
        return indices
