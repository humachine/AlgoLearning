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
        ans = 0
        for i in xrange(1, n+1):
