#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''
Given a sorted array, every number is allowed at most 2 duplicates. Remove all other extra duplicates and return the new modified array length.

    Inp: [1, 1, 1, 2, 2, 3]
    Out: 5 (The 3rd one is removed)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        # If less than 3 numbers, no duplicates need to be discarded
        if len(nums)<=2:
            return len(nums)
        # The 1st 2 characters will be retained no matter what
        distincts = 2
        for i in xrange(2, len(nums)):
            # If number is same as the last 2 distinct numbers, then it's a duplicate that needs to be discarded
            if nums[i] == nums[distincts-1] and nums[i] == nums[distincts-2]:
                continue
            # Else, we push the number to the next available valid position
            nums[distincts] = nums[i]
            distincts += 1
        return distincts
s = Solution()
inp = [1,1,1,2,2,2,3,3]
print s.removeDuplicates(inp)
print s.removeDuplicates([1, 1, 1, 2, 2, 3])
