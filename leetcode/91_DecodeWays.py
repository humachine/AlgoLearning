#https://leetcode.com/problems/decode-ways/
'''
    Inp: 12
    Out: 2 (AB or L)

    Inp: 45
    Out: 1 (DE)
'''
class Solution(object):
    def numDecodings(self, s):
        if not s:   return 0
        i = 0
        n = len(s)
        numWays = 1
        while i < n:
            if s[i] == '1' and i+1 < n:
                numWays += 1 if s[i+1] in '123456789' else 0
            elif s[i] == '2':
                if i+1 < n:
                    numWays += 1 if s[i+1] in '123456' else 0
                    i+=1
                i+=1
            elif s[i] == '0':
                return 0
            i+=1
        return numWays

s = Solution()
print s.numDecodings('12')
print s.numDecodings('45')
