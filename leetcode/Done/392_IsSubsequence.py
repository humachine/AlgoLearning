#https://leetcode.com/problems/is-subsequence/
"""
    Inp: 'abc', 'ahgbdc'
    Out: True
    Inp: 'abc', 'def'
    Out: False
    Inp: 'axc', 'ahgbdc'
    Out: False
"""
from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def isSubsequence(self, s, t):
        if not t: return False

        m, n = len(s), len(t)

        left, right = 0, n
        for i in xrange(m):
            while left < right:
                left += 1
                if t[left-1] == s[i]:
                    break
            else:
                return False
        return True

    def createCharMap(self, t):
        charMap = defaultdict(list)
        for ind, char in enumerate(t):
            charMap[char].append(ind)
        return charMap

    def isSubsequencePreProcess(self, s, t):
        """If t is incredibly long compared to s.
        And if we have want to check several strings if they are subsequences of t, we perform some preprocessing
        """
        if not s: return True
        if not t:   return False

        # First, create a character map which has a list of indices where each character appears
        charMap = self.createCharMap(t)

        lowBound = 0 #lowBound represents the index of the least recently visited occurences of a character of s found in t
        for ind, char in enumerate(s):
            if char not in charMap:
                return False

            # Find the index for which charMap[char][index] > lowBound
            i = bisect_left(charMap[char], lowBound)

            # If there are no more occurences of char beyond lowBound
            if i == len(t):
                return False
            lowBound = charMap[char][i]+1
        return True


s = Solution()
print s.isSubsequencePreProcess('abc', 'ahgbdc')
print s.isSubsequencePreProcess('axc', 'ahgbdc')
