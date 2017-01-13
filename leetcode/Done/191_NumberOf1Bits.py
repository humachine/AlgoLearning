#https://leetcode.com/problems/number-of-1-bits/
'''Given an unsigned integer, return the number of set bits in it. (aka Hamming Weight)

    Inp: 6 (i.e 110)
    Out: 2
'''
class Solution(object):
    def hammingWeight(self, n):
        # Keep ANDing n with n-1, until n becomes zero.
        # each iteration of n&n-1 will remove the rightmost 1
        weight = 0
        while n:
            n &= n-1
            weight += 1
        return weight
