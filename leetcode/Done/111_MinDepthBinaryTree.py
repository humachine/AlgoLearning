#https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
          3
    4            7
  8  -3        4
11
Out: 3 (3->7->4 or 3->4->-3)
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lDepth = self.minDepth(root.left)
        rDepth = self.minDepth(root.right)
        if 0 in [lDepth, rDepth]:
            return lDepth+rDepth+1
        return min(lDepth, rDepth)+1
