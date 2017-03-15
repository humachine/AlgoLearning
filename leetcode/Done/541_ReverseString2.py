#https://leetcode.com/problems/reverse-string-ii/
'''Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string. If there are less
than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and left
the other as original.

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''
class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)
        res = []
        # For each set of 2k characters, we reverse the first k and append the 
        # remaining characters unchanged.
        for left in xrange(0, n, 2*k):
            res.append(s[left:left+k][::-1] + s[left+k:left+2*k])
        return ''.join(res)

s = Solution()
print s.reverseStr('abcdefg', 2)
print s.reverseStr('abcdefg', 8)
