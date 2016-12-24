#https://leetcode.com/problems/word-break/
'''
Given a string and a dictionary of words, return if the word can be broken down into baby word(s), each belonging to the dictionary

    Inp: ['leet', 'code'], 'leetcode'
    Out: True ('leetcode' = 'leet' + 'code' who are both in the dictionary of words)
'''
class Solution(object):
    def _wordBreak(self, s, start, wordSet, wordBreak):
        if start==len(s):
            return True
        # Return result if already has been visited and computed
        if wordBreak[start] > -1:
            return wordBreak[start]

        res = False
        # Scroll from start to length of string, check if start:i is a valid word.
        # If yes, check if i:end is a valid word break string
        # Also, continue checking to find other such possible i

        # Eg: butterflyeffect with 3 words butter, butterfly and effect
        # If we stop at butter and look for flyeffect, we return False, since the word fly does not exist
        # If we also continue, we'll find butterfly as a word and then find effect to return True
        # This is also used to check for cases where the entire string is a single word
        for i in xrange(start+1, len(s)+1):
            if s[start:i] in wordSet:
                res = res or self._wordBreak(s, i, wordSet, wordBreak)
        wordBreak[start] = int(res)
        return wordBreak[start]

    def wordBreak(self, s, wordDict):
        if not s:   return True
        if not wordDict:    return False

        n, numWords = len(s), len(wordDict)
        wordSet = set(wordDict)
        wordBreak = [-1]*n
        # Return result of DP
        return bool(self._wordBreak(s, 0, wordSet, wordBreak))


    def wordBreakIterative(self, s, wordDict):
        if not s:   return True
        if not wordDict:    return False
        n = len(s)
        if n==1:
            return s in wordSet

        wordSet = set(wordDict)
        validWordString = [True] + [False]*n

        '''
        Iterative version which requires no stack space.

        validWordString[x] = True if s[0:x-1] can be broken down successfully using just dictionary words
        For each i, we try to find a j before it such that validWordString[j] is True and s[j:i] is a valid word.
        If we can find one such j, then validWordString[i] = True

        This is because, if validWordString[j] is True, then s[:j-1] can be built using just dictionary words. Now, if s[j:i] is also in the dictionary, s[:i-1] can now be built using dictionary words
        '''
        for i in xrange(1, len(s)+1):
            for j in xrange(i-1, -1, -1):
                if validWordString[j] and s[j:i] in wordSet:
                    validWordString[i] = True
                    break

        return validWordString[-1]

s = Solution()
print s.wordBreakIterative('leetcode', ['leet', 'code'])
print s.wordBreakIterative('butterflyeffect', ['butter', 'effect', 'butterfly'])
print s.wordBreakIterative('abcd', ['a', 'bcd', 'butterfly'])
print s.wordBreakIterative('abcd', ['abcd'])
