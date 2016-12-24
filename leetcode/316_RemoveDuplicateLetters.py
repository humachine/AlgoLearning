#https://leetcode.com/problems/remove-duplicate-letters/
'''
    Inp: 'bcabc'
    Out: 'abc'

    Inp: 'cbacdcbc'
    Out: 'acdb'

    Remove duplicate letters to give lexicographically smallest result
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        if len(s)<=1:   return s
        counts = [0]*26
        charIndex = lambda char: ord(char)-97
        for char in s:
            counts[charIndex(char)]+=1

        start, minimum = 0, s[0]
        for i in xrange(len(s)-1):
            if counts[charIndex(s[i])] == 1:
                start = i+1
                continue
            minimum = min(minimum, s[i])

s = Solution()
print s.removeDuplicateLetters('bcabc')
print s.removeDuplicateLetters('cbacdcbc')
