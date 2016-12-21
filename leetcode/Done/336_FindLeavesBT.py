#https://leetcode.com/problems/find-leaves-of-binary-tree/
'''
         1
         / \
        2   3
       / \     
      4   5   
    Out: [4, 5, 3], [2], [1]
'''
from collections import defaultdict
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _findLeaves(self, root, res):
        # For each node, find how far it is from a leaf (return 0) if itself is a leaf
        if not root:
            return -1
        lSum = self._findLeaves(root.left, res)
        rSum = self._findLeaves(root.right, res)
        currLevel = max(lSum, rSum)+1

        # If there have been no nodes at currentLevel, add an empty list to res
        if currLevel == len(res):
            res.append([])
        res[currLevel].append(root.val)
        return currLevel

    def findLeaves(self, root):
        if not root:    return []
        res = []
        self._findLeaves(root, res)
        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print s.findLeaves(root)
