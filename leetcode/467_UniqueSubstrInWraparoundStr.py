#https://leetcode.com/problems/unique-substrings-in-wraparound-string/
"""
    s = abcd...zabcd...zabcd...
    Inp: 'a'
    Out: 1 ('a' appears once in s)

    Inp: 'cac'
    Out: 2 ('c' and 'a' appear in s)

    Inp: 'zab'
    Out: 6 ('z', 'a', 'b', 'za', 'ab', 'zab')

    Inp: 'abcd'
    Out: 10 ('abcd', 'abc', 'ab', 'bc', 'a', 'b', 'c', 'bcd', 'cd', 'd')
"""
class Solution(object):
    def findSubstringInWraproundString(self, p):
        if len(p) < 1:  return len(p)

        seq = {}
        n = len(p)
        start = 0
        startChar = p[0]
        nextChar = lambda x: chr(97 + (ord(x)+1)%26)
        for i in xrange(1, len(p)):
            if nextChar(startChar) == p[i]:
                pass
            else:
