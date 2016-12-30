#https://leetcode.com/problems/the-skyline-problem/
'''
Given locations and heights of buildings on a skyline, output the skyline formed by the buildings.

    Inp: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    (From 2-9, building of height 10; From 3-7 building of height 15 and so on...)

    Out: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
    ( (a, b) where a represents a point where the height of the skyline changes. b-new value after change)
'''
from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        ''' This problem requires us to return the set of points where the height of the skyline changes and what it changes to. Based on this, it is obvious that the only points to be looked at are points where buildings begin or end.
        Each time a building begins or ends, if we have the skyline value, we can produce our end result.

        We go through the skyline from L-R:
        i) If we see the start of a building, we push it into a max-heap (height, BLDG_END).
        ii) If we see an end of a building, we remove it from the heap.
        At each point, if the current observed height of the skyline changes, then we add it to the result.

        Note: Here is where we perform a small trick to handle (ii). Say there are 3 overlapping buildings. All buildings get added into the heap. Say, building A has height=100 with BLDG_END=15 and another building B has BLDG_END=20 & height=300 and building C with BLDG_END=25 & height=200.
        Since it's a max-heap on height of building, the tallest building will be at the top of the heap. Building B gets removed at location=20. Building A is still at the bottom of the heap. We can choose to remove building A, but removal from a heap is an O(n) operation.

        Hence, despite building A having completed and been scrolled past, it is still kept 'alive' in the heap as though it's a building that hasn't yet ended. At loc=25 when Building C ends, we pop all buildings at the top of the heap whose end points are before 25.
        '''
        i, n = 0, len(buildings)
        res, h = [], []
        BLDG_START, BLDG_END = 0, 1
        # i<n means there are building start points yet to be seen
        # h!=None means there are buildings whose end points haven't yet been processed
        while i<n or h:
            # Either we have no active buildings in our skyline
            # Or the next PoI is the start of the next building
            if not h or (i<n and buildings[i][BLDG_START] <= -h[0][BLDG_END]):
                loc = buildings[i][BLDG_START]
                # While there are buildings with the same starting location, add them all to the heap
                while i<n and buildings[i][BLDG_START] == loc:
                    heappush(h, (-buildings[i][2], -buildings[i][1]))
                    i+=1
            # The next PoI is the end of a building
            else:
                loc = -h[0][BLDG_END]
                # Remove all buildings ending before or at this point. This is the manner in which some 'zombie' non-alive buildings finally get processed out.
                while h and -h[0][BLDG_END] <= loc:
                    heappop(h)
            # If there's something in the heap, then there's at least one building above us
            height = 0 if not h else -h[0][0]
            # If this is the first height or if the height is different from the previously seen height, then we add this height to the result.
            if (not res and height) or height != res[-1][-1]:
                res.append([loc, height])
        return res
s = Solution()
inp=[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print s.getSkyline(inp)
