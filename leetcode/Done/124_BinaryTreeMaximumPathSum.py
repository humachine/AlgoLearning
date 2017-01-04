#https://leetcode.com/problems/binary-tree-maximum-path-sum/
''' Given a Binary Tree, find the maximum path sum of any node->node path.
Inp: 
       1
      / \
     2   3
Out: 6
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def findMaxPathSum(self, root, result):
        ''' This function returns the value of the greatest sum path possible starting at root and going downwards. 
        This function also updates the value of result based on root->downwards paths AND root.left+root+root.right paths (/\ shaped paths)

        We only return the best root-downwards path because that's the only entity that can be built upon by the parent nodes of every root.
        '''
        if not root:    return 0

        # We perform a max with 0, so that any negative paths from either left/right child is discarded
        lSum = max(0, self.findMaxPathSum(root.left, result)) # Represents the best path possible from root.left downwards
        rSum = max(0, self.findMaxPathSum(root.right, result)) # Represents the best path possible from root.right downwards
        # At the end of the above 2 statements, lSum and rSum contain the best child-downwards paths (if any). Clearly lSum & rSum >= 0


        # Since lSum and rSum >=0, it's always in our interest to consider the /\ leftChild-downwards + root + right child downwards path
        result[0] = max(result[0], root.val + lSum + rSum) # We update result if required
        return root.val + max(lSum, rSum) # We finally only return the best sum of a root-downwards path
    def maxPathSum(self, root):
        result = [float('-inf')] #Result is the value of the maxPathSum of this tree
        self.findMaxPathSum(root, result)
        return result[0]

s = Solution()
head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

print s.maxPathSum(head)
