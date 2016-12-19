#https://leetcode.com/problems/sum-of-left-leaves/
"""
            3
        9       20
              15  7

    Out: 24 (9+15)
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        lSum = rSum = 0

        if root.left:
            #If left child is a leaf, return leaf's value
            if not root.left.left and not root.left.right:
                lSum = root.left.val
            #If left child is not a leaf, trigger recursion on left child
            else:
                lSum = self.sumOfLeftLeaves(root.left)
        if root.right:
            rSum = self.sumOfLeftLeaves(root.right)
        return lSum + rSum

