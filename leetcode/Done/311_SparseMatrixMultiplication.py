#https://leetcode.com/problems/sparse-matrix-multiplication/
''' Given 2 sparse matrices A & B, return AB
A = [ [ 1, 0, 0],
  [-1, 0, 3] ]

B = [ [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ] ]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''
from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not any([A, B, len(A[0])]):
            return [[]]
        m, n, p = len(A), len(A[0]), len(B[0])
        # We create 2 dictionaries aLocs and bLocs.
        # aLocs[i][j] holds the value of A[i][j] if A[i][j]!=0
        aLocs = [defaultdict(int) for x in xrange(m)]
        bLocs = [defaultdict(int) for x in xrange(n)]

        # Creating an index table for matrix A
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j]:
                    aLocs[i][j] = A[i][j]

        # Creating an index table for matrix B
        for i in xrange(n):
            for j in xrange(p):
                if B[i][j]:
                    bLocs[j][i] = B[i][j]

        def compProd(row, col):
            ''' This function takes in a rowNumber and a columnNumber, multiples a[row]*b[col] and returns the result
            '''
            aLen, bLen = len(aLocs[row]), len(bLocs[col])
            # If either of the row/column don't have any non-zero values, then return 0
            if not aLen or not bLen:
                return 0
            rowVals, colVals = aLocs[row], bLocs[col]
            # If there are aLen (say =28) values on a row and bLen non-zero values on the columns (say=9), then we iterate through the column instead of the row.
            if aLen > bLen:
                rowVals, colVals = colVals, rowVals
            result = 0
            for i, val in rowVals.iteritems():
                result += val * colVals[i]
            return result

        res = [[0]*p for x in xrange(m)]
        # Compute the values for each cell of the matrix
        for i in xrange(m):
            for j in xrange(p):
                res[i][j] = compProd(i, j)
        return res

s = Solution()
A = [ [ 1, 0, 0],
  [-1, 0, 3] ]

B = [ [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ] ]
print s.multiply(A, B)

A = [[1, -5]]
B = [[12], [-1]]
print s.multiply(A, B)
