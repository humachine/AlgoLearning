#https://leetcode.com/problems/largest-rectangle-in-histogram/
'''Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

    Inp:  [2,1,5,6,2,3]
    Out: 10 (the bars with height 5, 6 and base width as 2 gives a rectangle of size 5*2 = 10)
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        ''' We keep pushing ascending heights into the stack. Each time, we get a height that is lower than the top of the stack, we pop from the stack until the top of the stack is <= currHeight.
        Only if there's a smaller building on building's right, does that building get flushed out. 

        To make sure that the entire stack gets processed and emptied in the function, we append a -1 to the end of the heightst list. Thus, when we encounter the -1, it will flush all heights that are present on the stack.
        '''
        heights.append(-1) 
        st, maxArea = [-1], 0 #We also start st initialized with -1. heights[st[-1]] = heights[-1] = -1 (Since st=[-1] and we appended a -1 to heights.
        for i in xrange(len(heights)):
            while heights[i] < heights[st[-1]]:
                ht = heights[st.pop()] #Keep popping heights from the stack until currHeight >= top of stack
                width = i - st[-1] - 1 # width of the rectangle = i - (top of stack + 1)
                maxArea = max(maxArea, ht*width) 
            st.append(i)
        return maxArea
s = Solution()
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
