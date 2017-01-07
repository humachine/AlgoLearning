#https://leetcode.com/problems/excel-sheet-column-number/
''' Given a column title as it appears in Excel, return its column number.

    Inp: A
    Out: 1

    Inp: 28
    Out: AB
'''
class Solution(object):
    def titleToNumber(self, s):
        colNumber = 0
        for char in s:
            colNumber = colNumber*26 + (1+ord(char)-ord('A')) # Multiplying colNumber by 26 and adding the letter number for each character
        return colNumber
        return reduce(lambda x, y: 26*x + y, [ord(char)-ord('A')+1 for char in s])
