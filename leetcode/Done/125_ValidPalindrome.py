#https://leetcode.com/problems/valid-palindrome/
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    Inp: "A man, a plan, a canal: Panama"
    Out: True
'''
class Solution(object):
    def isPalindrome(self, s):
        if not s:   return True
        left, right, alphabet = 0, len(s)-1, 'abcdefghijklmnopqrstuvwxyz'
        VALID_CHARS = alphabet + '0123456789'
        while left < right:
            if s[left].lower() not in VALID_CHARS:
                left+=1
            elif s[right].lower() not in VALID_CHARS:
                right-=1
            elif s[left].lower()!=s[right].lower():
                return False
            else:
                left, right = left+1, right-1
        return True

    def isPalindromeConcise(self, s):
        if not s:   return True
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left, right = left+1, right-1
        return True
s = Solution()
Inp= "A man, a plan, a canal: Panama"
print s.isPalindromeConcise(Inp)
