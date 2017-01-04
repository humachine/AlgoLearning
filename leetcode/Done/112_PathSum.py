#https://leetcode.com/problems/path-sum/
'''
Given a BT, determine if there's a path from root->leaf which sums up to a target number.
Inp: target=22
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
Out: True (5, 4, 11, 2)
'''
class Solution(object):
    def findPathSum(self, root, currSum, target):
        # If current node is a leaf and it has reached the target, then return True
        if not root.left and not root.right and currSum == target:
            return True
        lRes = rRes = False
        if root.left:
            # If there's a left node, recurse on the left subtree after adding root.val to currSum
            lRes = self.findPathSum(root.left, currSum+root.left.val, target)
        if root.right:
            rRes = self.findPathSum(root.right, currSum+root.right.val, target)
        # Return True if either of the 2 subtrees had a matching path
        return lRes or rRes

    def hasPathSum(self, root, sum):
        if not root:    return False
        return self.findPathSum(root, root.val, sum)

    def hasPathSumConcise(self, root, sum):
        if not root:    return False
        if not any([root.left, root.right]) and root.val==sum:  return True #If root is a leaf and root's value is the remaining sum, then return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val) #Search for target-root.val on each subtree

