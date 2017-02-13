#https://leetcode.com/problems/base-7/
'''Given an integer, return its Base-7 representation
'''
class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'

        negative = num < 0
        num, res = abs(num), []

        while num:
            # Keep adding the remainder when num is divided by 7
            res.append(num%7)
            num/=7

        if negative:
            res.append('-')

        # Reverse the list and convert to string
        return ''.join([str(x) for x in res[::-1]])

s = Solution()
for i in xrange(-100, 100):
    if int(s.convertTo7(i), 7) != i:
        print i
