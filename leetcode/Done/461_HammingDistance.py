#https://leetcode.com/problems/hamming-distance/
'''  Given two numbers x and y, the hamminig distance between x and y is the
number of bits that differ between the 2 numbers.

    Inp: 4, 3
    Out: 2
'''
class Solution(object):
    def hammingDistance(self, x, y):
        # Hamming Distance is the number of bits that differ between x & y
        # In other words, it is the number of set bits you find in x^y
        n, dist = x^y, 0
        while n:
            n &= n-1
            dist += 1
        return dist
        return bin(x^y).count('1')
