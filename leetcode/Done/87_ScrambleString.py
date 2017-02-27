#https://leetcode.com/problems/scramble-string/
'''Given a string S1, we split it into 2 non-empty substrings recursively to get
a binary tree for the string. 

In this string, at any move we may swap two children of a node to rearrange the
characters of the string. 

Given a string S2, return if S2 is a scrambled version of S1.

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

Swapping the children of 'gr' above
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

Swapping the children of 'eat' and then 'at' above
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
'''
class Solution(object):
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True

        # If the 2 strings differ in length, S2 definitely can't be scramble
        # of S1
        n = len(s1)
        if len(s2) != n:
            return False

        counts = [0]*26
        for i in xrange(n):
            counts[ord(s1[i])-ord('a')]+=1
            counts[ord(s2[i])-ord('a')]-=1

        # If the character counts of the 2 strings differ, then S2 can
        # definitely NOT be a scramble of S1
        if max(counts)>0:
            return False

        for i in xrange(1, n):
            # We try each splitting point of the string. For each split of 
            # S1 into AB and S2 into CD, either A, C should be scrambles and
            # B, D scrambles. OR A, D and B, C should be scrambles.
            # if none of this holds true, then S2 is not a scramble of S1
            if (self.isScramble(s1[:i], s2[:i]) and
                    self.isScramble(s1[i:], s2[i:])):
                return True
            if (self.isScramble(s1[:i], s2[-i:]) and
                    self.isScramble(s1[i:], s2[:-i])):
                return True
        return False
s = Solution()
print s.isScramble('great', 'rgtae')
