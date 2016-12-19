#https://leetcode.com/problems/sum-of-two-integers/
#Java algorithm fails in Python because of the way numbers are represented in Python
"""
    Perform the addition without using mathematical operators
    Inp: 3, 4
    Out: 7
"""
class Solution(object):
    def getSum(self, a, b):
        if a==0:    return b
        if b==0:    return a

        """
        If we add two bits x1 and x2, result is x1^x2 prefixed by carry if any.
        Similary, a+b = a^b if there is never any carry

        Hence, we compute the carry to be 1s at any two bits of the numbers which are equally 1
        Eg: 1000101, 10101 -> carry will be 1s at bit 0 and bit 2
        """

        while b!=0:
            carry = a & b
            # We add b to a using the XOR operator
            a = a ^ b
            # Since b has already been consumed, we push carry forward by a bit and set b = carry
            b = carry << 1
        return a
s = Solution()
print s.getSum(-1, 1)

