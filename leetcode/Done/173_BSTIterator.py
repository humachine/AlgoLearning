#https://leetcode.com/problems/binary-search-tree-iterator/
'''
Implement an iterator over a binary search tree (BST). Iterator is initialized with the root of the tree.
Calling next() will return the next smallest number in the BST.
next() and hasNext() - O(1) time and O(treeHeight) memory
'''
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator(object):
    def __init__(self, root):
        ''' We initialize the BSTIterator with root and recursively all left nodes of root.
        In this problem, we are required to return numbers in increasing order. This corresponds to the in-order traversal of the tree.
        Hence, we load up a stack with all left nodes. We pop the left nodes one by one.
        If a popped node has a right subtree, we add all the left nodes of the right subtree to the stack.

        Each node gets added ONCE during the constructor phase or the next() phase in unit time. Each node is also processed exactly once in unit time.
        This adds up to O(n) total time for n nodes = O(1) amortized complexity

        hasNext() - O(1) worst-case complexity too since it just makes sure stack is not empty
        '''
        self.root = root
        self.nodeStack = []
        while root:
            self.nodeStack.append(root)
            root = root.left
        
    def hasNext(self):
        # Return true if there are left children nodes to be processed
        return len(self.nodeStack)>0
        
    def next(self):
        nodeStack = self.nodeStack
        # if len(nodeStack)==0:
            # raise IndexError
        # We pop the top node of the stack and return its value
        node = nodeStack.pop()
        retVal = node.val
        # If popped node has a right subtree, append all the left children of poppedNode.right recursively
        node = node.right
        while node:
            nodeStack.append(node)
            node = node.left
        return retVal
        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

