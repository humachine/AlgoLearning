#https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Inp: "Let's take LeetCode contest"
Out: "s'teL ekat edoCteeL tsetnoc"
'''
class Solution(object):
    def reverseWords(self, s):
        i, n = 0, len(s)
        string = [' ']*n
        while i<n:
            # s[start:end+1] represents a word (white-space separated)
            start = i
            while i<n and not s[i].isspace():
                i+=1
            end = i-1
            # We now swap all the letters between start and end
            while start <= end:
                string[start], string[end] = s[end], s[start]
                start += 1
                end -= 1
            # Next, we add all the white space characters to the result string
            while i<n and s[i].isspace():
                string[i] = s[i]
                i+=1
        return ''.join(string)


s = Solution()
print s.reverseWords("Let's take LeetCode contest")
