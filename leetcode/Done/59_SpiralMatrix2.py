#https://leetcode.com/problems/spiral-matrix/
'''Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Inp: 3
Out: [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0]*n  for x in xrange(n)]
        # hor_steps, vert_steps are the number of strides/steps that we have to traverse
        # in each direction at the next step of the spiral. 
        # Initially we move n steps horizontally, then m-1 steps vertically, n-1 horizontally reverse
        # m-2 vertically reverse and so on ...
        hor_steps, vert_steps = n, n-1
        x, y = 0, 0
        val = 1
        while hor_steps:
            for j in xrange(y, y+hor_steps):
                matrix[x][j] = val
                # Update the value that is being filled at each box
                val += 1
            # Reduce the step size by 1 for the next time
            hor_steps-=1
            # Update starting point for next set of steps
            x, y = x+1, j

            # If we are out of vertical (or hor) steps, we stop
            if not vert_steps:
                break
            for i in xrange(x, x+vert_steps):
                matrix[i][y] = val
                val += 1
            vert_steps-=1
            x, y = i, y-1

            if not hor_steps:
                break
            for j in xrange(y, y-hor_steps, -1):
                matrix[x][j] = val
                val += 1
            hor_steps-=1
            x, y = x-1, j

            if not vert_steps:
                break
            for i in xrange(x, x-vert_steps, -1):
                matrix[i][y] = val
                val += 1
            vert_steps-=1
            x, y = i, y+1
        return matrix

s = Solution()
print s.generateMatrix(3)
