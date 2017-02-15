#https://leetcode.com/problems/binary-tree-vertical-order-traversal/
'''
        3
    9       20
     10   15    7
       2

    Out: [[9], [3, 10, 15], [20, 2], [7]]
    
    Note: If two nodes are on the same vertical level, the node that is closer to root comes earlier in the result list
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution():
    def verticalOrder(self, root):
        if not root:
            return []
        # We form a queue of nodes to traverse the tree in a BFS manner.
        # At each point, we maintain the vertical level/column of the node
        # We have a dictionary which holds the levels of the tree
        levels = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, col = queue.popleft()
            levels[col].append(node.val)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
        # Finally, we calculate the range of columns that we have to traverse through
        # We traverse through all columns and add them all into the list

        # This same problem could alternatively be performed WITHOUT a hashtable
        # We maintain two lists: 1) Containing nodes with columns >= 0
        # 2) Containing nodes on columns < 0
        # list2.reverse() + list1 is the list of all levels.
        min_col, max_col = min(levels.keys()), max(levels.keys())
        return [levels[col] for col in xrange(min_col, max_col+1)]

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print s.verticalOrderQ(root)
print s.verticalOrder(root)
