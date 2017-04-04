#https://leetcode.com/problems/word-break-ii/
'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return ALL possible sentences.

Inp:
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

Out: ["cats and dog", "cat sand dog"].
'''
import collections
class Solution(object):
    def wordBreak(self, s, wordDict):
        sentences, wordDict = {}, set(wordDict)
        return self.breakWords(s, wordDict, sentences)

    def breakWords(self, s, wordDict, sentences):
        # If this substring has already been computed, reuse the result
        if s in sentences:
            return sentences[s]

        res = []
        for i in xrange(1, len(s)):
            # If the first substring is in the dictionary, then append all
            # the possibilities of the remaining string at the end of the 
            # first substring
            if s[:i] in wordDict:
                # new_words is all the possible word strings possibly by
                # breaking s[i:]
                new_words = self.breakWords(s[i:], wordDict, sentences)
                for new_word in new_words:
                    res.append(s[:i]+' '+new_word)
        # if the entire string s is a word, add it too
        if s in wordDict:
            res.append(s)
        # Update the memoized results for later usage
        sentences[s] = res
        return res


s = Solution()
ss = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]
print s.wordBreak(ss, dic)

print s.wordBreak("aaaaaaa", ["aaaa","aaa"])

ss = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print s.wordBreak(ss, dic)
