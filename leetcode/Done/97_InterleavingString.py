#https://leetcode.com/problems/interleaving-string/
'''Given 2 strings s1 and s2, return if string s3 can be formed by interleaving
strings s1 and s2.

Inp: s1 = "aabcc", s2 = "dbbca"
Out: s3 = "aadbbcbcac", True

Inp: s1 = "aabcc", s2 = "dbbca"
Out: s3 = "aadbbbaccc", False
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        if m > n:
            return self.isInterleave(s2, s1, s3)
        if not s1:
            return s2==s3
        # Similar to the below recursive solution, here we have an iterative
        # DP table. 
        # dp[i][j] = True if s3[:i+j] is an interleaving of s1[:i] and s2[:j]

        dp = [[False]*(n+1) for i in xrange(m+1)]
        dp[0][0] = True
        for j in xrange(1,n+1):
            # dp[0][j] is true if s3 and s2's respective characters match and
            # if dp[0][j-1] is true. This implies that the moment dp[0][j] becomes
            # false dp[0][j+1...] = False automatically
            # dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]
            dp[0][j] = s2[j-1] == s3[j-1]
            if not dp[0][j]:
                break
        for i in xrange(1,m+1):
            # dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]
            dp[i][0] = s1[i-1] == s3[i-1]
            if not dp[i][0]:
                break

        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                # if s1 & s3's characters match, dp value is the dp value for the
                # previous value of i
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                # if s2 & s3's characters match, dp value is the dp value for the
                # previous value of j
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        return dp[-1][-1]

    def interleave(self, s1, i1, s2, i2, s3, i3):
        # i1, i2, i3 represent the indices for the next character on s1, s2 & s3
        # i1 & i2 determine the state of each search since i1+i2=i3
        # If the result for this state has been precomputed, we reuse the result.
        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]
        # If we have exhausted s3, then we return True
        if i3 == len(s3):
            return True
        # If we exhaust either string, then remaining part of s3 must be the
        # same as remaining part of the other string
        if i2 == len(s2):
            return s3[i3:] == s1[i1:]
        if i1 == len(s1):
            return s3[i3:] == s2[i2:]

        res = False
        # If s3's character = s1's character, recurse forward
        if s3[i3] == s1[i1]:
            res = self.interleave(s1, i1+1, s2, i2, s3, i3+1)
        # Also if s3's character = s2's character, recurse forward
        if not res and s3[i3] == s2[i2]:
            res = self.interleave(s1, i1, s2, i2+1, s3, i3+1)
        # Save the results in the cache
        self.cache[(i1, i2)] = res
        return res

    def isInterleave(self, s1, s2, s3):
        # This is a simple recursive search of both strings looking to see
        # if s1 & s2 interleave to form s3
        m, n = len(s1), len(s2)
        self.cache = {}
        # If len(s3) doesn't add up with s1 & s2's lengths, then it's not an interleaving
        if len(s3) != m+n:
            return False
        return self.interleave(s1, 0, s2, 0, s3, 0)

s = Solution()
print s.isInterleave('a', '', 'a')
print s.isInterleave('abc', 'def', 'abcdef')
print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
print
print s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
print s.isInterleave('db', 'b', 'cbb')
