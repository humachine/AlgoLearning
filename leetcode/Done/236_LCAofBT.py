#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # If root matches any of the targets, then return target
        if root in [None, p, q]:
            return root

        '''
        left and right represent the highest (closest to root) location at which one of p or q is found
        Case 1: One of p,q is an ancestor of the other
        In which case, for one of root.left/root.right, we will be returning the ancestor node
        
        If only one of root's children return a non-NULL node, we return the non-NULL node since we know that it's the LCA of the 2 nodes

        Case 2: p and q are on separate subtrees of a node
        In this case, the left subtree will return (say p, WLOG) and the right subtree returns q.
        Since both subtrees returned non-NULL nodes, we know that the current root is the LCA

        '''
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if not right else right
