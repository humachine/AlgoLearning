#https://leetcode.com/problems/one-edit-distance/
'''
Given two strings S and T, determine if they are one edit distance apart.
    Inp: 'abc', 'ac'
    Out: True
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        # If difference in lengths is > 1, then at least 2 edits are required
        if abs(len(s)-len(t)) > 1:
            return False
        # We always shift the smaller string to s
        if len(s) > len(t):
            s, t = t, s
        n = len(t)
        for i in xrange(len(s)):
            # If some characters don't match, the only possibilities are:
            # Replacement (replacing s[i] with t[i]) => check if s[i+1:n]==t[i+1:n]
            # Deletion: (since len(s)<=len(t), we can only delete from t. Deleting t[i] would leave us to check s[i:n] with t[i+1:n]
            # Insertion: (Similarly, we can only insert in s. We insert t[i] at s[i]. Hence we have to check if s[i:n] == t[i+1:n]
            if s[i] != t[i]:
                return s[i+1:n] == t[i+1:n] or t[i+1:n] == s[i:n]
        # If no differing characters have been found, we check if there's an extra character in the bigger string
        return len(t)-len(s) == 1
s = Solution()
print s.isOneEditDistance('abc', 'ac')
print s.isOneEditDistance('abc', 'ab')
print s.isOneEditDistance('abc', 'abcd')
print s.isOneEditDistance('abc', 'abc')
print s.isOneEditDistance('ab', 'cab')
