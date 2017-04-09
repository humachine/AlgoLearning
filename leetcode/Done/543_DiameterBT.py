#https://leetcode.com/problems/diameter-of-binary-tree/
'''Given a binary, return the diameter of the binary tree.

Inp:
          1
         / \
        2   3
       / \     
      4   5 
Out: 4 (4213 or 5213)
'''
class Solution(object):
    def findDiameter(self, root):
        if not root:
            return 0
        # Find the longest path ending at each child
        l_diam = self.findDiameter(root.left)
        r_diam = self.findDiameter(root.right)

        self.diameter = max(self.diameter, l_diam+1+r_diam)
        # Return the longest path possible that ends at root.
        return 1+max(l_diam, r_diam)
        
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.diameter = 0
        self.findDiameter(root)
        # return diameter-1 since the diameter is the number of edges in the longest
        # path between any 2 nodes of the tree
        return self.diameter-1
