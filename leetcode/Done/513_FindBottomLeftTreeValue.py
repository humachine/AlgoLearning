#https://leetcode.com/problems/find-bottom-left-tree-value
'''Given a binary tree, find the leftmost value in the last row of the tree.

Inp:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Out: 7
'''

import collections
class Solution(object):
    def findBottomLeftValue(self, root):
        # Perform a BFS of the tree. At each level, we update the leftmost value
        # found so far. We also add the children of each node to the queue
        queue = collections.deque()
        queue.append(root)
        ans = None
        while queue:
            # Determine the number of nodes in this level.
            n = len(queue)
            # Update answer with the value of the leftmost node on this level.
            node = queue.popleft()
            ans = node.val
            # Put the leftmost node back onto the queue for processing of its children
            queue.appendleft(node)
            for i in xrange(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    def findBottomLeftValue(self, root):
        # Alternatively, we just append the right child before the left child.
        # In this manner, the answer will be the last node ever visited.
        queue = collections.deque()
        queue.append(root)
        ans = None
        while queue:
            node = queue.popleft()
            # Append right node before the left node
            queue.extend(filter(None, [node.right, node.left]))
            # If no more nodes in the queue, then this is the leftmost value
            # in the bottom row.
            if not queue:
                ans = node.val
        return ans
