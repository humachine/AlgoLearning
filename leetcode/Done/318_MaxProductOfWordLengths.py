#https://leetcode.com/problems/maximum-product-of-word-lengths/
'''Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Inp: ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Out: 16 ('abcw' and 'xtfn')

Inp: ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Out: 4 ('ab' and 'cd')

Inp: ["a", "aa", "aaa", "aaaa"]
Out: 0 (No such pair of words)
'''
class Solution(object):
    def wordToNumber(self, word):
        # Create a bit string (and hence an integer) for each word. 
        # Every bit of a word is 0 or 1 depending on whether that letter is
        # present in the word.
        number = 0
        for char in word:
            char_index = ord(char)-ord('a')
            number |= 1 << char_index
        return number

    def maxProduct(self, words):
        word_val = []
        max_prod = 0
        for i in xrange(len(words)):
            # Add the bit string for each word to a list
            word_val.append(self.wordToNumber(words[i]))
            for j in xrange(i):
                # Compare the bit string of the current word with all previous words
                if not (word_val[i] & word_val[j]):
                    max_prod = max(max_prod, len(words[i])*len(words[j]))
        return max_prod

s = Solution()
print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
print s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
print s.maxProduct(["a", "aa", "aaa", "aaaa"])
