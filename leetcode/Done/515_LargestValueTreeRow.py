#https://leetcode.com/problems/find-largest-value-in-each-tree-row/
'''Given a binary tree, return the largest value in each level of the tree.
Inp:
          1
         / \
        3   2
       / \   \  
      5   3   9 
Out: [1, 2, 3]
'''
import collections
class Solution(object):
    def largestValues(self, root):
        result = []
        if root:
            nodes = collections.deque()
            nodes.append(root)
            # Perform BFS/level-order traversal of the nodes
            while nodes:
                n = len(nodes)
                max_val = float('-inf')
                # Scroll through all the nodes of a particular level and obtain
                # the max value of the nodes
                for i in xrange(n):
                    node = nodes.popleft()
                    max_val = max(max_val, node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                # Add children of nodes to be processed in the next level
                result.append(max_val)
        return result
