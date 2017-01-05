#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
'''
Given any BT(non-perfect BTs too), populate the next right pointers for every node.

Inp:
         1
       /  \
      2    3
     / \    \
    4   5    7

Out:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution: # @param root, a tree link node
    def rightConnect(self, curr, leftPredecessor):
        '''This function takes in a node (which represents the root of some subtree of the tree and a leftPredecessor which is the predecessor of the left most node on the level below curr (if any).
        The finalOutput looks something like:
                    1 -> NULL
                   /  \
     dummyHead->  2 -> 3 -> NULL
                 / \    \
    dummyHead-> 4-> 5 -> 7 -> NULL
        '''
        startOfLevel = None #startOfLevel is set to None always
        if not leftPredecessor: #If this is the first node on this level, then create a dummyHead
            leftPredecessor = TreeLinkNode(-1) #Creating a dummy haed for each level
            startOfLevel = leftPredecessor #startOfLevel changes from None only when it is the first node of a level of the tree (i.e when leftPredecessor is None)
        if curr.left: #If the previous root (i.e curr) has a left node, make the predecessor->curr.left connection and move predecessor to curr.left
            leftPredecessor.next = curr.left
            leftPredecessor = leftPredecessor.next
        if curr.right:
            leftPredecessor.next = curr.right
            leftPredecessor = leftPredecessor.next

        if curr.next: #If the previous root(i.e curr) had a next node, move curr to curr.next and recurse
            self.rightConnect(curr.next, leftPredecessor)
        if startOfLevel and startOfLevel.next: #If this was the start of a level, recurse on the lower level
            self.rightConnect(startOfLevel.next, None)

    def connect(self, root):
        if root:
            self.rightConnect(root, None)

    def connectIterative(self, root):
        '''This is the same algorithm as above, written in an iterative manner'''
        dummyHead = leftPredecessor = TreeLinkNode(-1)
        while root:
            leftPredecessor.next = root.left
            if leftPredecessor.next:
                leftPredecessor = leftPredecessor.next
            leftPredecessor.next = root.right
            if leftPredecessor.next:
                leftPredecessor = leftPredecessor.next
            root = root.next #Move root to root's next and iterate again
            if not root: #If not root, then we have reached the end of a level. We iterate now on a lower level.
                root, leftPredecessor = dummyHead.next, dummyHead #root becomes dummyHead.next
            
head = TreeLinkNode(1)
head.left = TreeLinkNode(2)
head.right = TreeLinkNode(3)
head.left.left = TreeLinkNode(4)
head.left.right = TreeLinkNode(5)
# head.right.left = TreeLinkNode(5)
head.right.right = TreeLinkNode(7)

s = Solution()
head = s.connect(head)
def traverse(head):
    if not head:    return
    print head.val, head.next.val if head.next else None
    traverse(head.left)
    traverse(head.right)
traverse(head)
