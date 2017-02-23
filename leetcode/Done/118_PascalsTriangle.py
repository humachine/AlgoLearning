#https://leetcode.com/problems/pascals-triangle/
'''Given an integer n, generate the first n rows of the Pascal's Triangle.
'''
class Solution(object):
    def generate(self, numRows):
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for row_num in xrange(2, numRows):
            # Every row starts AND ends with a 1
            row = [1]
            for j in xrange(len(res[-1])-1):
                # All other elements of a row are just sums of the 2 elements above it.
                row.append(res[-1][j]+res[-1][j+1])
            row.append(1)
            res.append(row)
        return res

s = Solution()
res = s.generate(5)
for i in xrange(5):
    print res[i]
