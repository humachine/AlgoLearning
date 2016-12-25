#https://leetcode.com/problems/valid-parentheses/
'''
Given a string of '(){}][' return if its valid.
    Inp: '()[]{}'
    Out: True

    Inp: '([)]'
    Out: False
'''
class Solution(object):
    def isValid(self, s):
        # We use a list as a stack. If we have a closing bracket that does not match the top of the stack, then we return False. 
        # We finally return whether the stack is empty or not
        if not s:   return True
        st = []
        matching = {'(':')', '{':'}', '[':']'}
        for i, char in enumerate(s):
            if char in '({[':
                st.append(char)
            else:
                if len(st) == 0 or char != matching[st.pop()]:
                    return False
        return len(st) == 0
s = Solution()
print s.isValid('()[]{}')
print s.isValid('([)]')
