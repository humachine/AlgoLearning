#https://leetcode.com/problems/inorder-successor-in-bst/
'''
Given a node of a tree, return its in-order successor
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def _inorderSuccessor(self, root, p, parent):
        # If target's val is greater than root, then we pick the right subtree
        if root.val < p.val:
            return self._inorderSuccessor(root.right, p, parent)
        # If target's val is lesser than root, then we pick the left subtree. We also update the value of the parent
        if root.val > p.val:
            return self._inorderSuccessor(root.left, p, root)
        # If we have discovered the node
        if root == p:
            # If the node has a right child, the left-most (i.e smallest) node of the right subtree will be the inorder successor
            if root.right:
                root = root.right
                while root.left:
                    root = root.left
                return root
            # If there's no right child, then return the parent
            return parent

    def _inorderSuccessorIterative(self, root, p):
        successor = None
        while root:
            # If root's value > target's value, we move left after updating successor
            # Only nodes whose value > p's value can even be successor candidates
            if root.val > p.val:
                successor = root
                root = root.left
            # Here we essentially take a root->leaf path that encompasses the node p
            # If the node p is a leaf, then we return the previous successor we have (which is the same as the parent node in the _inorderSuccessor()
            # If p is not a leaf, then we proceed to its right.
            # Each time our root exceeds p's value, we try to push it back to the left and each time it goes <= target's value, we push it to the right
            else:
                root = root.right
        return successor

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        return self._inorderSuccessorIterative(root, p)
        return self._inorderSuccessor(root, p, None)

s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
head = s.inorderSuccessor(root, root.right.left)
print head.val
