#https://leetcode.com/problems/excel-sheet-column-title/
''' Given a column title as it appears in Excel, return its column number.

    Inp: 1
    Out: A

    Inp: AB
    Out: 28
'''
class Solution(object):
    def convertToTitle(self, n):
        title = []
        while n:
            title.append(chr(ord('A') + (n-1)%26)) # We append (n-1)%26 to the answer so that 26->Z and not to AA.
            n=(n-1)/26 # Similarly we set n to n-1/26
        return ''.join(title[::-1])
