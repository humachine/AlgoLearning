#https://leetcode.com/problems/regular-expression-matching/
''' Given a string s and a pattern p, return if pattern p FULLY matches string s.

    Inp: 'aa', 'a'
    Out: False ('a' does not consume 'aa')

    Inp: 'aa', 'a*'
    Out: True ('*' matches ZERO or more of the preceding element)

    Inp: 'ab', '.*'
    Out: True

    Inp: 'aab', 'c*a*b'
    Out: True (c* matches nothing. a* matches aa and 'b' matches 'b')
'''
class Solution(object):
    def isMatch(self, s, p):
        ''' We build a DP[m][n] where DP[i][j] represents whether s[0..i] can be consumed by p[0..j]
        We initialize DP[0][0] to True since the empty string can beb consumed by the empty pattern.
        '''
        m, n = len(s), len(p)
        M = [[False]*(n+1) for i in xrange(m+1)]
        M[0][0] = True
        for i in xrange(m+1):
            for j in xrange(1, n+1):
                if p[j-1] == '*': #If current pattern char is a *
                    if i>0 and p[j-2] in [s[i-1], '.']: # If the character before the star matches with the current character. (Either equal to that character or is a '.')
                        M[i][j] = M[i][j-2] or M[i-1][j] # M[i][j-2] represents the results when the current <char><*> consumes zero charactesr of the string. M[i-1][j] represents the case where <char><*> uses up 1 or more copies of <char>. Hence we just retain the result from the previous usage of <char><star>
                    else:
                # For <char><*>, if char doesn't match the currentChar of s, then the only possibility is if we use up zero copies of <char> during the * operation.
                        M[i][j] = M[i][j-2]
                elif i>0 and p[j-1] in [s[i-1], '.']:
                    # If the current char matches with pattern's current char (or is a '.'), then patternChar & stringCurrentChar have made no difference to the matches. We just propagate the previous result of the search without patternChar, stringCurrentChar
                    M[i][j] = M[i-1][j-1]
        return M[m][n] #Returning M[m][n]

    def isMatchSpaceEfficient(self, s, p):
        ''' If we look at isMatch() above, we observe that only M[i][j] only needs the rows M[i-1] and M[i]. Hence, we have just 2 arrays and reuse them.
        '''
        m, n = len(s), len(p)
        top = [False] + [False]*n
        bottom = [True] + [False]*n
        for i in xrange(m+1):
            for j in xrange(1, n+1):
                if p[j-1] == '*':
                    bottom[j] = bottom[j-2]
                    if i>0 and p[j-2] in [s[i-1], '.']:
                        bottom[j] = bottom[j] or top[j]
                elif i>0 and p[j-1] in [s[i-1], '.']:
                    bottom[j] = top[j-1]
                if j>=2: #We set top[j-2] to zero continuously. 
                    top[j-2] = False
            top[-2:] = [False, False]
            top, bottom = bottom, top #At the end of an iteration, bottom becomes top. And bottom is now top (which is an array filled with False)
        return top[-1]


s = Solution()
print s.isMatch('aa', 'aa')
print s.isMatch('aa', 'a*')
print s.isMatch('aaa', 'a*')
print s.isMatch('abb', 'ab*')
print s.isMatch('aab', 'c*a*b')
print s.isMatch('ab', '.*')
print s.isMatch('', '.*')

print
print s.isMatch('ab', 'a*')
print s.isMatch('aa', 'a')
print s.isMatch('', '.')
