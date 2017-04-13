#https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
'''Find the longest consecutive child-parent-child or parent-child sequence
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
        '''Returns the length of the longest increasing and decreasing sequences
        that begin at root'''
        if not root:
            return (0, 0)
        l_best = self.findLongestSequence(root.left)
        r_best = self.findLongestSequence(root.right)

        max_inc = max_dec = 0
        curr_val = root.val
        # we set l_val & r_val to curr_val-2 so that they don't count as consecutive
        l_val = curr_val-2 if not root.left else root.left.val
        r_val = curr_val-2 if not root.right else root.right.val

        # Set max length descending & ascending sequence values if required
        if l_val-root.val == 1:
            max_dec = l_best[1]
        elif root.val - l_val == 1:
            max_inc = l_best[0]

        if r_val-root.val == 1:
            max_dec = max(max_dec, r_best[1])
        elif root.val - r_val == 1:
            max_inc = max(max_inc, r_best[1])
        # We increase both max_inc and max_dec by 1 to account for the extra root(current) node
        max_inc += 1
        max_dec += 1

        # If lChild, root, rChild form an increasing sequence, update accordingly
        if (l_val+1 == root.val == r_val-1) or (l_val-1 == root.val == r_val+1):
            self.longest_seq = max(self.longest_seq, max_dec+max_inc-1)
        # If not, apply just one of the increasing/decreasing sequences
        else:
            self.longest_seq = max(self.longest_seq, max(max_dec, max_inc))
        return (max_inc, max_dec)

    def longestConsecutive(self, root):
        self.longest_seq = 0
        self.findLongestSequence(root)
        return self.longest_seq

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

s = Solution()
node = TreeNode(2)
node.left = TreeNode(1)
node.right = TreeNode(3)
print s.longestConsecutive(node)
