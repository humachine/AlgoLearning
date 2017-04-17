#https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
'''Find the longest consecutive parent-child sequence
in a binary tree.

Inp:
        1
       / \
      2   3
Out: 2 (12 or 21 are the longest sequences)

Inp:
        2
       / \
      1   3
Out: 3 
'''
class Solution(object):
    def findLongestSequence(self, root):
        '''Returns the length of the longest increasing sequences that begins at root.'''
        if not root:
            return 0
        curr_val = root.val
        # we set l_val & r_val to curr_val-2 so that they don't count as consecutive
        l_val = curr_val-2 if not root.left else root.left.val
        r_val = curr_val-2 if not root.right else root.right.val

        l_best = self.findLongestSequence(root.left)
        r_best = self.findLongestSequence(root.right)

        # Set max length sequence value starting at root, based on either subtree 
        max_len = 1
        if l_val-curr_val == 1:
            max_len = 1+l_best
        if r_val-curr_val == 1:
            max_len = max(max_len, 1+r_best)
        # Update max length found so far
        self.longest_seq = max(self.longest_seq, max_len)
        return max_len

    def longestConsecutive(self, root):
        self.longest_seq = 0
        self.findLongestSequence(root)
        return self.longest_seq
