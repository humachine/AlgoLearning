#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
    Inp: [1, 1, 2]
    Out: [1, 2] return 2 since there are 2 distinct elements in the array
'''
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:    return 0
        prev, distincts = nums[0]-1, -1
        for i in xrange(len(nums)):
            if nums[i] != prev:
                distincts+=1
                nums[distincts] = prev = nums[i]
        return distincts+1
s = Solution()
print s.removeDuplicates([1, 1, 2])
