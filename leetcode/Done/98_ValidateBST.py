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
        # If left child exists, but left subtree is not a valid BST, then return False
        if root.left and not self._isValidBST(root.left, prev):
            return False
        # If you have a previously visited node and that previous is >= current root's value, then the sorted ordering fails
        if prev[0] is not None and prev[0] >= root.val:
            return False
        prev[0] = root.val
        # Change the previous value and recurse on right child, if it exists
        return self._isValidBST(root.right, prev) if root.right else True

    def isValidBST(self, root):
        if not root:    return True
        return self._isValidBST(root, [None])

s = Solution()
head = TreeNode(2)
head.left, head.right = TreeNode(1), TreeNode(3)
print s.isValidBST(head)

head = TreeNode(0)
head.right = TreeNode(-1)
print s.isValidBST(head)
