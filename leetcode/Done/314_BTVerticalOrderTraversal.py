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

from collections import defaultdict
from Queue import Queue
class Solution():
    def verticalOrder(self, root):
        if not root:    return []
        levelMap = defaultdict(list)

        # Set up Queue for BFS
        queue = [(root, 0)]
        for node, level in queue:
            if node:
                # Add each node to appropriate level
                levelMap[level].append(node.val)
                queue.append((node.left, level-1))
                queue.append((node.right, level+1))
                
        minLevel, maxLevel = min(levelMap.keys()), max(levelMap.keys())
        return [levelMap[level] for level in xrange(minLevel, maxLevel+1)]


    def verticalOrderQ(self, root):
        ''' Same function as above. Implemented with Python Queue.Queue'''
        if not root:    return []
        levelMap = defaultdict(list)

        queue = Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, level = queue.get()
            if node:
                levelMap[level].append(node.val)
                queue.put((node.left, level-1))
                queue.put((node.right, level+1))
        minLevel, maxLevel = min(levelMap.keys()), max(levelMap.keys())
        return [levelMap[level] for level in xrange(minLevel, maxLevel+1)]

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print s.verticalOrderQ(root)
