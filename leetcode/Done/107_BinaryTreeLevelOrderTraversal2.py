#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
Inp:
    3
   / \
  9  20
    /  \
   15   7
Out:
[
  [15,7],
  [9,20],
  [3]
]
'''
class Solution(object):
    def bottomTraversal(self, root, level):
        # Find regular level order traversal
        if not root:
            return
        if len(self.result)==level:
            self.result.append([])
        self.result[level].append(root.val)
        self.bottomTraversal(root.left, level+1)
        self.bottomTraversal(root.right, level+1)

    def levelOrderBottom(self, root):
        self.result = []
        self.bottomTraversal(root, 0)
        # Reverse the results of regular level order traversal.
        return self.result[::-1]
