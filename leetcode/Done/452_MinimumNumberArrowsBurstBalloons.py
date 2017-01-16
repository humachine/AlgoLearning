#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
''' Given a set of balloons (each represented by an interval), what's the minimum number of balloons required to fire at and burst all balloons.  
Alternatively, imagine each interval is the times at which people visit a cafe. Imagine you want to make an announcement that reaches all people. What is the minimum number of times you need to make a speech such that you reach all people.

    Inp: [[10,16], [2,8], [1,6], [7,12]]
    Out: 2 (One anytime between 2 and 6. Another anytime between 10 and 12)
'''
class Solution(object):
    def findMinArrowShots(self, points):
        if not points:  return 0
        points.sort(key = lambda x: x[0])
        res = points[0]
        ''' We regard this as an intervals problem. We sort all intervals by start time. The locations at which 2 balloons can be burst are at their intersection. 
        For consecutive pairs of balloons, they can be burst with just one arrow if they have an overlap. Else, you'll have to use 2 arrows. We just store the intersections between intervals.
        '''
        arrows = 1
        for interval in points:
            start, end = interval
            if start <= res[1]: #If this interval starts before the end of the previous interval, then we can just use a single well-placed arrow to burst both this balloon and the previous balloon.
                res[0] = max(res[0], start) # Updating intersection start
                res[1] = min(res[1], end) # Intersection end = min(prevEnd, currEnd)
            else:
                arrows+=1
                res = interval #If there's no intersection, we use a full new arrow for this interval
        return arrows
s = Solution()
inp = [[10,16], [2,8], [1,6], [7,12]]
print s.findMinArrowShots(inp)
