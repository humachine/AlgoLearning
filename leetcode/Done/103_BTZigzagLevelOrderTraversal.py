#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
  [20, 9],
  [15,7]
]
'''
import collections
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        # Put the nodes of each level into a queue
        queue, res = collections.deque(), []
        queue.append(root)
        L_R = True
        while queue:
            # At the beginning of each level, count the number of nodes in that level
            # and pop as many
            n, level = len(queue), []

            for i in xrange(n):
                # Depending on the level, popleft or popright
                # If popping left, append to the right and vice versa
                if L_R:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    level.append(node.val)
                else:
                    node = queue.pop()
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    level.append(node.val)
            L_R = not L_R
            res.append(level)
        return res

