#https://leetcode.com/problems/wildcard-matching/
''' Return if a wildcard pattern matches a string.
    Inp: 'aa', 'a'
    Out: False
    Inp: 'aaa', 'a*'
    Out: True (* matches any sequence of characters including the empty sequence)
    Inp: 'abc', 'a*'
    Out: True
'''
class Solution(object):
    def isMatchDP(self, s, p):
        '''Here we set up a DP[m][n] to solve the wildcard pattern matching. 
        Similar to Reg Exp matching, DP[i][j] = True if s[0..i] matches p[0..j]
        '''
        m, n = len(s), len(p)
        M = [[False]*(n+1) for _ in xrange(m+1)]
        M[0][0] = True
        for i in xrange(m+1):
            for j in xrange(1, n+1):
                # If current character is a *
                if p[j-1] == '*':
                    # M[i-1][j-1] If we match the * with the currentChar, then we check if pattern upto the * matches the string upto currentChar 
                    # M[i][j-1] If we wish to ignore the * (i.e * matches the empty sequence), we check if pattern upto to * matches the string including currentChar
                    # M[i-1][j] If the * has already made one match, then we check if string upto currentChar matches with the pattern (including *)
                    M[i][j] = (i>0 and (M[i-1][j-1] or M[i-1][j])) or M[i][j-1]
                # M[i-1][j-1] Or, if the currentChar is the current patternChar (or patternChar is '?'), then we check if pattern upto patternChar matches string upto currentChar
                elif i>0 and p[j-1] in [s[i-1], '?']:
                        M[i][j] = M[i-1][j-1]
        return M[m][n]
    def isMatchSpaceEfficient(self, s, p):
        '''Here we set up a DP[m][n] to solve the wildcard pattern matching. 
        Similar to Reg Exp matching, DP[i][j] = True if s[0..i] matches p[0..j]
        '''
        m, n = len(s), len(p)
        top = [False] + [False]*n
        bottom = [True] + [False]*n
        for i in xrange(m+1):
            for j in xrange(1, n+1):
                if p[j-1] == '*':
                    bottom[j] = (i>0 and (top[j-1] or top[j])) or bottom[j-1]
                elif i>0 and p[j-1] in [s[i-1], '?']:
                    bottom[j] = top[j-1]
                if j>1: #As we get done using values from top, we assign them to False, so that we can assign bottom to top, later
                    top[j-2] = False
            top[-2:] = [False]*2
            top, bottom = bottom, top
        return top[-1]

    def isMatch(self, s, p):
        # def isMatchZeroSpace(self, s, p):
        ''' This is an O(m*n) worst-case algorithm which requires Zero space. 
        This is a backtracking DFS solution. lastStarMatch & starPos are used to store the states, backtrack to them, change and retry.
        '''
        m, n = len(s), len(p)
        lastStarMatch, starPos = -1, -1
        i = j = 0
        while i < m:
            # If stringChar matches patternChar, then we move both pointers ahead
            if j<n and p[j] in [s[i], '?']:
                i, j = i+1, j+1
            # If we encounter a star, we make a note of both patternChar & stringChar's positions. This is useful for later backtracking
            elif j<n and p[j] == '*':
                lastStarMatch, starPos = i, j
                j+=1 # We only increase j to account for an empty match. (we now try to see if s including stringChar matches with p after the *)

            elif starPos > -1: # If there's a *, we use up one more character from the *
                # we go back to the last character that the previous star consumed. We now consume the character after that
                lastStarMatch += 1
                i, j = lastStarMatch, starPos + 1
            else:
                return False
        while j < n and p[j] == '*':
            j+=1
        return j==n
                
s = Solution()
print s.isMatch('aa', 'a')
print s.isMatch('abde', 'a*c*')
print s.isMatch('aab', 'c*a*b*')
print s.isMatch("bbbaab", "a**?***")
print
print s.isMatch('abc', 'abc')
print s.isMatch('aaa', 'a*')
print s.isMatch('abcde', 'a*')
print s.isMatch('abcde', 'a*c*')
print s.isMatch('abcde', 'a*c**')
print s.isMatch('ab', 'a?')
print s.isMatch('ab', '?*')
