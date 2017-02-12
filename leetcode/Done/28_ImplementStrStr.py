#https://leetcode.com/problems/implement-strstr/
''' Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  

Inp: ABCDE, BCD
Out: 1
'''
class Solution(object):
    def strStr(self, haystack, needle):
        ind = -1
        # Pick each possible starting point for the needle, and look for it
        for i in xrange(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                ind = i
                break
        # If no possible starting points found, return -1
        return ind
s = Solution()
print s.strStr('ABCDE', 'BCD')
print s.strStr('ABCDE', 'XYP')
