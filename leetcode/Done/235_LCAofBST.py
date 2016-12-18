#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
""" Given two nodes, return LCA of the two nodes
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not p and not q:
            return root
        if not p or not q:
            return p if not q else q

        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right)
        return root

    def lowestCommonAncestorIter(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not p and not q:
            return root
        if not p or not q:
            return p if not q else q
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
