#https://leetcode.com/problems/reverse-words-in-a-string/
"""
    Inp: "    the sky    is       blue    "
    Out: "blue is sky the"
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split()[::-1]
        return ' '.join(ans)
