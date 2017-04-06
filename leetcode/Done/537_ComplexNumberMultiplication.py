#https://leetcode.com/problems/complex-number-multiplication/
'''Given two strings representing complex numbers, return the product of them.

Inp: '1+1i', '1+1i'
Out: '0+2i'

Inp: '1+-1i', '1+-1i'
Out: '0+-2i'
'''
class Solution(object):
    def complexNumberMultiply(self, a, b):
        # Split the complex number into real and imaginary parts
        x1, y1 = a.split('+')
        x2, y2 = b.split('+')
        x1, y1, x2, y2 = int(x1), int(y1[:-1]), int(x2), int(y2[:-1])

        # Find the real and imaginary parts of the product
        ans1, ans2 = x1*x2 - (y1*y2), y1*x2 + y2*x1
        return str(ans1) + '+' + str(ans2) + 'i'

s = Solution()
print s.complexNumberMultiply('1+1i', '1+1i')
print s.complexNumberMultiply('1+-1i', '1+-1i')
