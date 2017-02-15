#https://leetcode.com/problems/integer-to-roman/
'''Given an integer, return its roman representation.

Inp: 33
Out: XXXIII

Inp: 49
Out: XLIX

Inp: 3999
Out: MMMCMXCIX
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        key_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        key_roman = 'M CM D CD C XC L XL X IX V IV I'.split()

        res = []
        # The above tables are the key values of interest in any roman->integer conversion
        # All we do is greedily reduce as many of each consecutive value as possible.
        for i, val in enumerate(key_values):
            res.append(key_roman[i]*(num/val))
            num%=val

        return ''.join(res)

s = Solution()
print s.intToRoman(33)
print s.intToRoman(49)
print s.intToRoman(3999)
