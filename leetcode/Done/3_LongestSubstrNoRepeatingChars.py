#https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
    Inp: 'abcabcbb'
    Out: 'abc'
    Inp: 'bbbbb'
    Out: 'b'
    Inp: 'pwwkew'
    Out: 'wke'
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        charPos = {}
        maxLen = start = 0
        # maxStart = maxEnd = 0

        for i in xrange(len(s)):
            if s[i] in charPos and charPos[s[i]]>=start:
                start = charPos[s[i]]+1

            charPos[s[i]] = i
            maxLen = max(maxLen, i-start+1)
            # if maxLen < (i-start+1):
                # maxLen = i-start+1
                # maxStart = start
                # maxEnd = i
        #maxString = s[maxStart:maxEnd+1]
        return maxLen

s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')
print s.lengthOfLongestSubstring('bbbb')
print s.lengthOfLongestSubstring('pwwkew')
print s.lengthOfLongestSubstring('abba')
