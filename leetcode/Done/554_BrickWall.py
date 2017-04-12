#https://leetcode.com/problems/brick-wall/
'''Given a brick wall which consists of rows of bricks of same height but varying
width, draw a vertical line from top to bottom crossing the least bricks.

Inp:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]

Out: 2
'''
import collections
class Solution(object):
    def leastBricks(self, wall):
        # crossings stores the number of bricks that would be avoided if a 
        # cut was made at that location. If a key does not exist in crossings,
        # then a cut at location=key will cut through all rows of bricks.
        crossings = collections.defaultdict(int)
        for row in wall:
            locn = 0
            for brick in row[:-1]:
                locn += brick
                crossings[locn] += 1

        # Find the location at which max number of bricks are missed while making a cut
        max_misses = 0
        for locn in crossings:
            max_misses = max(max_misses, crossings[locn])
        return len(wall) - max_misses
s = Solution()
inp = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
print s.leastBricks(inp)
