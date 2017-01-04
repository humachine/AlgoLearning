#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
''' Given a BT, populate the next right pointers for each node.

Inp: 
         1
       /  \
      2    3
     / \  / \
    4  5  6  7

Out:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def rightConnect(self, left, right):
        '''This function receives two nodes: left and right. It performs the connection from left->right. And it spawns off to recurse on the rest of the tree.
        '''
        left.next = right
        if left.left: #If there's no left child, then this is the last level of the tree (Since it's a perfect BT)
            self.rightConnect(left.left, left.right) # We need to connect left's left to left's right.
            self.rightConnect(left.right, right.left if right else None) # We now try to connect rightchild's right -> right's left

    def connect(self, root):
        ''' If there exists a left-child, then this is not the last level of the tree. (since it is a perfect binary tree - i.e a BT which has 2^h-1 nodes)
        '''
        if root and root.left:
            self.rightConnect(root.left, root.right)
            self.rightConnect(root.right, None)

head = TreeLinkNode(0)
head.left = TreeLinkNode(1)
head.right = TreeLinkNode(2)
head.left.left = TreeLinkNode(3)
head.left.right = TreeLinkNode(4)
head.right.left = TreeLinkNode(5)
head.right.right = TreeLinkNode(6)

s = Solution()
head = s.connect(head)
def traverse(head):
    if not head:    return
    print head.val, head.next.val if head.next else None
    traverse(head.left)
    traverse(head.right)
traverse(head)
