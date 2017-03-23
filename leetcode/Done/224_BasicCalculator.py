#https://leetcode.com/problems/basic-calculator/
'''Given a valid expression containing ()+-, spaces and digit evaluate it

Inp: "1 + 1"
Out: 2

Inp: ' 2-1 + 2 '
Out: 3

Inp: '(1-(4+5)-3)  + (6+8)'
Out: 3
'''
class Solution(object):
    def calculate(self, s):
        # st is a stack that we use for storing various levels of expressions
        # plus = True, if the most recent sign was a plus sign (i.e if we have
        # to add the next number to the answer, rather than subtract it)
        st, plus = [], True
        curr = i = 0
        n = len(s)
        while i<n:
            char = s[i]
            # If char is (, we add it the current sum and the sign to the stack
            if char == '(':
                st.append((curr, plus))
                # Resetting current value & the sign
                curr, plus = 0, True
            # If end of a paren, we add/subtract the curr value to the value 
            # that we had pushed on to the stack
            # st[-1][1] represents the sign that we pushed on to the stack
            # Since st[-1][1] is boolean, 2*st[-1][1] will either be +/-1.
            elif char == ')':
                curr = st[-1][0] + (2*st[-1][1]-1)*curr
                # Once we have added our current value to the value on the stack,
                # we pop it.
                st.pop()
            elif char in '+-':
                plus = char=='+'
            elif char.isdigit():
                j = i
                while j<n and s[j] in '0123456789':
                    j+=1
                num = int(s[i:j])
                # We pick the next number and add/subtract it to/from the curr
                # value according to the sign.
                curr = curr + (2*plus-1)*num
                # setting i to j-1, so that after the i+=1 line below, i=j at
                # the start of the next iteration.
                i=j-1
            i+=1
        return curr

s = Solution()
print s.calculate('1 + 1')
print s.calculate('  2-1 + 2 ')
print s.calculate('(1-(4+5)-3)  + (6+8)')
print s.calculate("2147483647")
print s.calculate('')
