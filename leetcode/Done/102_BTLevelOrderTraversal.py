#https://leetcode.com/problems/binary-tree-level-order-traversal/
'''Given a BT, return the level order traversal of the tree.

Inp:
    3
   / \
  9  20
    /  \
   15   7

Out:
[
  [3],
  [9,20],
  [15,7]
]
'''
import collections
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        # Put the nodes of each level into a queue
        queue, res = collections.deque(), []
        queue.append(root)
        while queue:
            # At the beginning of each level, count the number of nodes in that level
            # and pop as many
            n, level = len(queue), []
            for i in xrange(n):
                node = queue.popleft()
                level.append(node.val)
                # If the node has any children, add them to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
