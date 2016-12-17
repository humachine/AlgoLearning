#https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
          3
    4            7
  8  -3        4
11
Out: 4 (3->4->8->11)
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
