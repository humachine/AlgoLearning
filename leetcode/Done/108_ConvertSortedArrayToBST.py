#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
class Solution(object):
    def arrayToBST(self, nums, start, end):
        if start == end:
            return None
        mid = (start+end)/2
        # We put the middle element of the array as the root. 
        root = TreeNode(nums[mid])
        # Left child of root is the root for the subarray from start to mid
        root.left = self.arrayToBST(nums, start, mid)
        root.right = self.arrayToBST(nums, mid+1, end)
        return root

    def sortedArrayToBST(self, nums):
        return self.arrayToBST(nums, 0, len(nums))

s = Solution()
import TreeLib
head = s.sortedArrayToBST([1, 3, 4, 5, 7])
TreeLib.printTreeContents(head)
