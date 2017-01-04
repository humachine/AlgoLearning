#https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
Given a binary tree where each node represents a digit, return the sum of all numbers formed by each root-to-leaf path.

Inp:
    1
   / \
  2   3
   \
    8

Out: 141 (1->2->8 represents the number 128 and 1->3 represents 13, summing up to 141)
'''
class Solution(object):
    def sumPathNumbers(self, root, numSofar, result):
        '''sumPathNumbers represents the sum of all numbers that are present in the subtree of root'''
        if not root:
            return 0
        numSofar = numSofar*10 + root.val #We add the new digit at the end of the previous number
        if not root.left and not root.right: #We have found a leaf node
            return numSofar
        # Sum of numbers in root's subtree = sum of numbers in left subtree + right subtree
        return self.sumPathNumbers(root.left, numSofar) + self.sumPathNumbers(root.right, numSofar)

    def sumNumbers(self, root):
        return self.sumPathNumbers(root, 0)
