#https://leetcode.com/problems/validate-binary-search-tree/
'''
    2
   / \
  1   3
Out: True

    1
   / \
  2   3
Out: False
'''

# The common mistake is when the following condition is not adhrered to:
# - All elements of the left subtree are < than root's value

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _isValidBST(self, root, prev):
        if not root:    
            return True
        if prev is None or prev < root.val:
            lRes = self._isValidBST(root.left, 
    def isValidBST(self, root):
        if not root:    return True
        prev = None
s = Solution()
head = TreeNode(1)
head.left, head.right = TreeNode(2), TreeNode(3)
print s.isValidBST(head)
