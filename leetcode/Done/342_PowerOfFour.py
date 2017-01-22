#https://leetcode.com/problems/power-of-four/
''' Given a number, return if it's a power of 4.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        # num & (num-1) will tell us if num is a power of 2
        # 0x555555 is a mask which has only bits corresponding to even powers of 2 set as 1
        return (num&(num-1)==0) and (num&0x555555555 > 0)
