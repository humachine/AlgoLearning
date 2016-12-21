#https://leetcode.com/problems/longest-palindromic-substring/
"""
    Inp: 'babad'
    Out: 'bab'

    Inp: 'cbbd'
    Out: 'bb'
"""
class Solution(object):
    def buildPalindrome(self, s, start, end):
        '''Given start and end, palindromes are grown leftwards of start and rightwards of end to the maximum extent possible'''
        left, right = start, end

        while left>=0 and right< len(s) and s[left]==s[right]:
            left, right = left-1, right+1
        return left+1, right-1
        
    def longestPalindrome(self, s):
        if not s:   return s
        maxLen, n = 1, len(s)
        head = tail = 0
        '''Pick a starting point. Pick a starting point at each character and try to grow the longest possible palindrome on both sides
        Next pick all starting points BETWEEN two characters and try to grow more palindromes.
        '''
        for i in xrange(len(s)-1):
            # Checking for palindromes which have a character as center
            left, right = self.buildPalindrome(s, i, i)
            if right-left+1 >= maxLen:
                maxLen = right-left+1
                head, tail = left, right

            # Checking for palindromes which have space between two characters as the centre
            left, right = self.buildPalindrome(s, i, i+1)
            if right-left+1 >= maxLen:
                maxLen = right-left+1
                head, tail = left, right
        return s[head:tail+1]

s = Solution()
print s.longestPalindrome('abbabad')
print s.longestPalindrome('babad')
print s.longestPalindrome('cbbd')
