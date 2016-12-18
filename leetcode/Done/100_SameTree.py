#https://leetcode.com/problems/same-tree/
import Queue
"""
    Two BTs are the same if they are structurally identical & have the same values
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p==q
    def isSameTreeIter(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            que = Queue.Queue()
            q.put((p, q))
            while not que.empty():
                p, q = que.get()
                if p.val != q.val:
                    return False
                if [p.left, q.left].count(None) == 1 or [p.right, q.right].count(None)==1:
                    return false
                if p.left:
                    que.put((p.left, q.left))
                if p.right:
                    que.put((p.right, q.right))
            return True
        return p==q
