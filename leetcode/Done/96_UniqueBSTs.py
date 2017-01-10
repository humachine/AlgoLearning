#https://leetcode.com/problems/unique-binary-search-trees/
'''
Given a number of nodes, what is the number of unique BSTs that can be formed.

    Inp: n=3
    Out:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
class Solution(object):
    def numTrees(self, n):
        ''' Say the N numbers of the BST are from 1-n
        We place each number as root and count the number of possible BSTs we can make out of this.
        With n=5 and root as 3, we know that we have 2 nodes in the left sub-tree and 2-nodes in the right subtree. There are 2 ways of having a subtree with 2 nodes.
        This totals up to 2*2 ways of having 2 subtrees each with 2 nodes.
        '''
        if not n:   return 0
        # ans[i] stores the number of ways in which we can have a BST/BS subtree with i nodes
        ans = [1] + [0]*(n) #There is 1 way of having 0 nodes in a BST
        for i in xrange(1, n+1):
            for left in xrange(i): #Number of nodes in left subtree = 0...i-1
                right = i-1-left  # Number of nodes in right subtree = total-left-1(for root)
                ans[i] += ans[left]*ans[right]
        return ans[n]
s = Solution()
print s.numTrees(3)
