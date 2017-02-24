#https://leetcode.com/problems/pascals-triangle-ii/
'''Given an integer n, return the nth row of the Pascal's Triangle.
'''
class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        prev = [1, 1]
        for row_num in xrange(2, rowIndex+1):
            # Every row starts AND ends with a 1
            row = [1]
            for j in xrange(len(prev)-1):
                # All other elements of a row are just sums of the 2 elements above it.
                row.append(prev[j]+prev[j+1])
            row.append(1)
            prev = row
        return prev

    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        # It can be seen that given a row the next row is obtained by adding
        # row+[0] with [0]+row
        # Eg: [1, 3, 3, 1, 0]
        #   + [0, 1, 3, 3, 1] 
        #   = [1, 4, 6, 4, 1]
        #
        # Similarly, we can see that the next row is always a sum of consecutive
        # elements from [0]+prev+[0]
        prev = [1]
        for row_num in xrange(1, rowIndex+1):
            li = [0] + prev + [0]
            row = [li[i] + li[i+1] for i in xrange(len(li)-1)]
            prev = row
        return prev

    def getRow(self, rowIndex):
        # Similar to the idea above, all we do is append a zero at the end of each row.
        # To get the next row, we continuously sum prev[i]+prev[i-1]
        # When i is 0, prev[i]+prev[i-1] = prev[0]+prev[-1] = prev[0]+0
        prev = [1]
        for row_num in xrange(1, rowIndex+1):
            prev.append(0)
            row = [prev[i]+prev[i-1] for i in xrange(len(prev))]
            prev = row
        return prev

s = Solution()
print s.getRow(4)
