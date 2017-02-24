class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printTreeContents(root):
    if not root:
        return
    if root.left:
        printTreeContents(root.left)
    print root.val,
    if root.right:
        printTreeContents(root.right)

sampleTreeHead = TreeNode(4)
sampleTreeHead.left = TreeNode(2)
sampleTreeHead.left.left = TreeNode(1)
sampleTreeHead.left.right = TreeNode(3)
sampleTreeHead.right = TreeNode(6)
sampleTreeHead.right.left = TreeNode(5)
sampleTreeHead.right.right = TreeNode(7)
