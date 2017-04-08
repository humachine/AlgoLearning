#https://leetcode.com/problems/most-frequent-subtree-sum/
'''Given a BT, find the most frequent subtree sum (Return all subtree sums if there's a tie).

Inp:
  5
 /  \
2   -3
Out: [2, -3, 4]

Inp:
  5
 /  \
2   -5
Out: [2] (2 occurs twice as 5+2-5 and 2) 
'''
import collections
class Solution(object):
    def findSubsums(self, root, freqs):
        if not root:
            return 0
        # Subtree sum = root value + subtree sum of left & right children
        l_sum, r_sum = self.findSubsums(root.left, freqs), self.findSubsums(root.right, freqs)
        sub_sum = l_sum + r_sum + root.val
        freqs[sub_sum] += 1
        # Update max frequency encountered if required
        self.max_freq = max(self.max_freq, freqs[sub_sum])
        return sub_sum

    def findFrequentTreeSum(self, root):
        if not root:
            return []
        # freqs contains the frequency of each subsum encountered in the tree
        freqs = collections.defaultdict(int)
        # max_freq is the highest subsum frequency encountered
        self.max_freq = -1
        self.findSubsums(root, freqs)

        result = []
        # Add all subsums that have max_frequency into the result
        for key, val in freqs.iteritems():
            if val == self.max_freq:
                result.append(key)
        return result
