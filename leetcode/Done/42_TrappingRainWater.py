#https://leetcode.com/problems/trapping-rain-water/
"""Test cases:
    Inp: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    3               x                                       
    2       x O O O x x O x                                   
    1 _ x O x x O x x x x x x
    Out: 6
    All the Os are water filled between the walls (xs)
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        n = len(height)
        left_wall, right_wall = height[0], height[n-1]
        left, right = 1, n-2

        #Set left and right walls
        #If you see your current left is greater than left wall, update left wall and move on
        #Else if you see your current is greater than right wall, update right wall and move on
        #Currently, your safe level is determined by the lower of the two walls

        rainfall = 0
        while left<=right:
            if height[left] > left_wall:
                left_wall = height[left]
                left+=1
            elif height[right] > right_wall:
                right_wall = height[right]
                right-=1
            else:
                if left_wall < right_wall:
                    rainfall += left_wall - height[left]
                    left += 1
                else:
                    rainfall += right_wall - height[right]
                    right -= 1
        return rainfall

s = Solution()
Inp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print s.trap(Inp)
Inp = [0, 3, 0, 2, 0, 0, 0, 1]
print s.trap(Inp)
