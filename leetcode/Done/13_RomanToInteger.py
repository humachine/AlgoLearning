#https://leetcode.com/problems/roman-to-integer/
'''Given a Roman numeral, convert it to its decimal equivalent.

Inp: XI
Out: 11

Inp: VL
Out: 45
'''
class Solution(object):
    def romanToInt(self, s):
        ans = 0
        roman_values = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in xrange(len(s)-1):
            # When the next character corresponds to a bigger value, then
            # this numeral is a prefix that needs to be deducted from
            # the rest of the number.
            if roman_values[s[i]] < roman_values[s[i+1]]:
                ans -= roman_values[s[i]]
            else:
                ans += roman_values[s[i]]
        # Adding the value of the last digit
        ans += roman_values[s[-1]]
        return ans
s = Solution()
print s.romanToInt('XI')
print s.romanToInt('VL')
