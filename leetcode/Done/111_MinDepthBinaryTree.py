#https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
          3
    4            7
  8  -3        4
11
Out: 3 (3->7->4 or 3->4->-3)
"""
# Definition for a binary tree node.
from Queue import Queue
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
    def minDepthIter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = Queue()
        q.put(root)
        level = 1
        while not q.empty():
            level += 1
            n = q.qsize()
            for x in xrange(n):
                root = q.get()
                if not root.left and not root.right:
                    return level
                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)
        return level
