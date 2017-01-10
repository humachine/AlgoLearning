#https://leetcode.com/problems/number-complement/
''' Given a number, return the 1s complement (invert all bits) of it.

    Inp: 5 (101)
    Out: 2 (010)
'''
class Solution(object):
    def findComplement(self, num):
        bits = str(bin(num))[2:] #Finding all bits
        comp = ['0' if x=='1' else '1' for x in bits] #Inverting all bits
        return int('0b'+''.join(comp), 2) #Converting them back to an integer
