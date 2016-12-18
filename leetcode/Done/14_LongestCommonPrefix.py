#https://leetcode.com/problems/longest-common-prefix/
"""
Inp: ['abc', 'abcdef', 'abcxxx', 'abcdjieowijfg', 'xabc']
Out: ""

Inp: ['abc', 'abcdef', 'abcxxx', 'abcdjieowijfg', 'abc']
Out: 'abc'
"""
# Method 1: Pick first string as prefix. Consecutively find longest common prefix between prefix and the next string
# Method 2: Pick the first string as prefix. Traverse through the chars of prefix and check if each character can be added to answer by comparing against corresponding characters of ALL other strings

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:    return ""
        prefix = strs[0]
        for i in xrange(len(prefix)):
            for j in xrange(len(strs)):
                if i==len(strs[j]) or strs[j][i] != prefix[i]:
                    return prefix[:i]
        return prefix
s = Solution()
inp = ['abc', 'abcdef', 'abcxxx', 'abcdjieowijfg', 'abc']
print s.longestCommonPrefix(inp)
