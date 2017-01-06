#https://leetcode.com/problems/maximal-rectangle/
'''
Given a grid, what is the size of the largest rectangle that can be formed from this grid
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Out: 6
'''
class Solution(object):
    def maxAreaRectangleHistogram(self, heights):
        ''' Function that finds the max area rectangle in a histogram. We visualize each row of the grid as the base of a histogram and find the max area possible in it.
        The maximum of all these max-es gives us the maximalRectangle. 
        '''
        maxRectangle = 0
        heights.append(-1) # When a height < stack top's height comes, we pop all heights at the top of the stack which are < newHeight. We hence, insert a -1 or 0 or any negative number at the end of the heights list. When this number is encountered all preceding heights get processed and popped out.
        st, maxArea = [-1], 0 
        for i, height in enumerate(heights):
            while height < heights[st[-1]]: # If currHeight < stack top's height, we keep popping from the top of the stack.
                h = heights[st.pop()]
                w = i - (st[-1]+1) # width = i - (newStackTop + 1)
                maxArea = max(maxArea, h*w)
            st.append(i)
        heights.pop()
        return maxArea

    def maximalRectangle(self, matrix):
        ''' Returns the maximal rectangle that can be formed from the grid. '''
        if not matrix:  return 0

        heights = [0] * len(matrix[0])
        maxRectangle = 0

        for row in xrange(len(matrix)):
            for col in xrange(len(matrix[0])):
                cellVal = int(matrix[row][col])
                heights[col] = heights[col] + cellVal if cellVal else 0 #heights increases by 1 if cellVal is 1, else becomes 0
            maxRectangle = max(maxRectangle, self.maxAreaRectangleHistogram(heights))

        return maxRectangle


strs  = ['10100', '10111', '11111', '10010']
inp = [list(i) for i in strs]
s = Solution()
print s.maximalRectangle(inp)
