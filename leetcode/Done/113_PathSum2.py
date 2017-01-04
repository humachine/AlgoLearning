#https://leetcode.com/problems/path-sum-ii/
'''
Given a BT, find all paths from root->leaf which sums up to a target number.
Inp: target=22
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
Out: [[5,4,11,2],
      [5,8,4,5]]
'''
class Solution(object):
    def findPathSums(self, root, target, currPath, res):
        if not root: return
        currPath += [root.val] # Add the root node to the current path

        # If root is a leaf and root.val == remaining target, then add currPath to the result.
        if not root.left and not root.right and target == root.val:
            res.append(list(currPath))
            currPath.pop() #removing root.val from the currPath so that other 
            return
        # Find the paths possible in the left subtree
        self.findPathSums(root.left, target-root.val, currPath, res)
        self.findPathSums(root.right, target-root.val, currPath, res)
        currPath.pop() #Remove root.val from the list (back-tracking step)

    def pathSum(self, root, sum):
        if not root:    return []
        res, path = [], []
        self.findPathSums(root, sum, path, res)
        return res
