#https://leetcode.com/problems/path-sum-iii/
'''
Given a BT, find the number of paths that sum up to a target value. (each path must begin at a node and only proceed downwards towards the leaf)

Inp: target=8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Out: 3 (5->3, 5->2->1, -3->11)
'''
from collections import defaultdict
class Solution(object):
    def countPathSums(self, root, currSum, prevSums, numPaths):
        if not root:    return
        currSum += root.val 
        if currSum == self.target: #If currSum is the target wholly, then add 1 + number of paths that sum up to zero. The 1 is for the 0-length path before root.
            numPaths[0] += prevSums[0] + 1
        elif currSum-self.target in prevSums: #For all other sums, add the number of ways to get to currSum-target
            #Eg: For target 8 in example above, currSum=18 at Node 11. currSum-target=10 and hence we add one more to numPaths
            numPaths[0] += prevSums[currSum-self.target]
        prevSums[currSum] += 1

        self.countPathSums(root.left, currSum, prevSums, numPaths)
        self.countPathSums(root.right, currSum, prevSums, numPaths)
        prevSums[currSum] -= 1 #Backtrack step


    def pathSum(self, root, sum):
        if not root:    return 0
        # prevSums is a dictionary that holds the number of nodes in the current subtree 
        self.target, prevSums, numPaths = sum, defaultdict(int), [0]
        self.countPathSums(root, 0, prevSums, numPaths)
        return numPaths[0]
