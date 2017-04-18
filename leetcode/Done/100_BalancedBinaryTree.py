#https://leetcode.com/problems/balanced-binary-tree/
'''Return if a binary tree is height-balanced.

Inp:
    3
   / \
  1   18
 /
-4

Out: False (left subtree has > height than right subtree)
'''
class Solution(object):
    def isBalanced(self, root):
        return self.checkBalance(root) > -1

    def checkBalance(self, root):
        if not root:
            return 0
        # Find the height of the left subtree
        l_height = self.checkBalance(root.left)
        # if left subtree is balanced, find height of right subtree
        if l_height > -1:
            r_height = self.checkBalance(root.right)
            # If right height and left height differ by <= 1, return max(l_height, r_height)
            if r_height > -1 and abs(l_height - r_height) <= 1:
                    return max(l_height, r_height)+1
        return -1
