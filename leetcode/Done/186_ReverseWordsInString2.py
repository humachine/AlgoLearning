#https://leetcode.com/problems/reverse-words-in-a-string-ii/
'''Given a string of words, reverse the words in the string in-place.

Inp: 'The sky is blue'
Out: 'blue is sky The'
'''
class Solution:
    def reverseWord(self, li, start, end):
        # Given a word, swap characters at both ends of the word
        while start<end:
            li[end], li[start] = li[start], li[end]
            start, end = start+1, end-1

    def reverseWords(self, s):
        # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
        # Reverse the whole string
        s.reverse()
        start=end=0
        n = len(s)

        # If there are trailing spaces in the input string
        # while start<n and s[start] == ' ':
            # start+=1
        while start < n:
            # Find a space-separated word and reverse it in place
            while end<n and s[end]!=' ':
                end+=1
            self.reverseWord(s, start, end-1)
            # If words could be separated by more than 1 space
            # while end<n and s[end]==' ':
                # end+=1
            end+=1
            start = end

s = Solution()
print s.reverseWords(list('the sky is blue'))
