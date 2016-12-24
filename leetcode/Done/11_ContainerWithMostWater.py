#https://leetcode.com/problems/container-with-most-water/
'''
Given n non-neg integers ai which each represent a point (i, ai). 
Find the max area rectangle you can have with 2 of these points and the x-axis
'''
class Solution(object):
    def maxArea(self, height):
        if len(height) < 2: return 0

        # Start from both ends and set up a starting value for area. As you come in inwards, the base width decreases, so the only way the area can go up is if the heights are getting larger and larger

        left, right, n = 0, len(height)-1, len(height)
        maxContainerArea = 0
        while left < right:
            # Container can only have min(two heights) * base width amount of water
            area = (right-left)*min(height[left], height[right])
            maxContainerArea = max(maxContainerArea, area)
            # To find another competing container, at least one of the heights MUST get bigger since the widths are getting smaller by 1 every iteration
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return maxContainerArea


    def maxAreaOptim(self, height):
        '''
        In the function above, we move left/right at every iteration and keep recomputing areas. To avoid performing multiple costly multiplications, we keep moving left and right as many times as required to find a possible candidate before we perform area computations.
        Since width is constantly decreasing by 1, the currHeight must become greater for the new points to be possible candidates.
        '''
        if len(height) < 2: return 0

        left, right, maxContainerArea = 0, len(height)-1, 0
        while left < right:
            currHeight = min(height[left], height[right])
            maxContainerArea = max(maxContainerArea, currHeight*(right-left))
            # We push left rightwards until we can find a possible candidate and vice versa for right leftwards
            while height[left] <= currHeight and left<right: left+=1
            while height[right] <= currHeight and left<right:    right-=1
        return maxContainerArea
s = Solution()
print s.maxAreaOptim([4, 3, 2, 7, 4, 19, 8, 7])
