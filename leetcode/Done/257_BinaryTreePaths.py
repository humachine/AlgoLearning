#https://leetcode.com/problems/binary-tree-paths/
'''
Return all root->leaf paths of a binary tree
   1
 /   \
2     3
 \
  5
Out: ["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findPaths(self, root, res, currPath):
        '''
        For each path, add root.val to currPath.
        If we are currently at a leaf node, add result to paths
        Else, recurse on left and right children
        '''
        currPath.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(currPath))
            currPath.pop()
            return

        if root.left:
            self.findPaths(root.left, res, currPath)
        if root.right:
            self.findPaths(root.right, res, currPath)
        currPath.pop()

    def binaryTreePaths(self, root):
        if not root:    return []
        currPath, paths = [], []
        self.findPaths(root, paths, currPath)
        return paths


root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.right = TreeNode(5)
s = Solution()
print s.binaryTreePaths(root)
