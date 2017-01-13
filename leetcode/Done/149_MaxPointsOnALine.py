#https://leetcode.com/problems/max-points-on-a-line/
''' Given the coordinates of a set of points, determine the max number of
points that can lie on a single line.

    Inp: [(1,1), (3,3), (3, 5), (3, 7)]
    Out: 3
'''
import collections
class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        numPoints = len(points)
        INF = float('inf')
        # findSlope finds the slope of the line connecting two points. Returns INF if the points are on the same vertical  line
        findSlope = lambda a, b: INF if b.y == a.y else float(a.x-b.x)/(a.y-b.y)

        maxPointsInLine = 0
        ''' We take a point, then see which of the remaining points lie on the
        same line as this point. We also maintain a count of points that are 
        identical to the current point.
        '''
        for i in xrange(numPoints):
            slopes = collections.defaultdict(int)
            maxSlope = same = 0
            for j in xrange(i+1, numPoints):
                # If the new point is identical to the old point, then increment same count
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same += 1
                else:
                    # Find slope of point
                    slope = findSlope(points[i], points[j])
                    slopes[slope] += 1 # Add the new point to the list of points which have the same slope with point[i]
                    maxSlope = max(slopes[slope], maxSlope)
            maxPointsInLine = max(maxPointsInLine, maxSlope+same) # maxPointsInLine is the maximum of (maxSlope and #same points)
        return maxPointsInLine+1 #Return 1 more than maxPointsInLine (to include the current point of any line of points)
