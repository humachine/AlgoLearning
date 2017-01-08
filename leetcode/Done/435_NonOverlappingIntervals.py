#https://leetcode.com/problems/non-overlapping-intervals/
''' Given a set of intervals, find the least number of intervals that need to removed to make them non-overlapping.
Two intervals that touch each other are considered as non-overlapping.

    Inp: [ [1,2], [2,3], [3,4], [1,3] ]
    Out: 1 (Remove 1,3 to make it non-overlapping)
'''
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        ''' We observe that sorting by start time might not work best. An interval might start early but span a really long amount of time. If we don't remove it just on the basis of its early start time, then we have to remove a greater number of other overlapping intervals to compensate for this. 
        Eg: [[1, 45], [2, 6], [5, 8], [6, 11]]
        If we don't remove [1, 45], we have to remove everything else.
        If we remove [1, 45], we just have to remove [5, 8] for all the intervals to become non-overlapping

        Sorting ascending by end time gives us 'more space' to fit in more intervals at a later time.
        '''
        if not intervals:   return 0
        intervals.sort(key = lambda x: x.end)

        prevEnd, removals = intervals[0].start-1, 0 #Initialize prevEnd to before the start of the first interval

        for interval in intervals:
            if interval.start < prevEnd: #If interval starts before previous end (i.e interval overlaps with previous interval, then delete it)
                removals += 1
            else:
                prevEnd = interval.end #Else, just update the end of the previous interval to use for later scheduling
        return removals

s = Solution()
inp = [ [1,2], [2,3], [3,4], [1,3] ]
print s.eraseOverlapIntervals(inp)

