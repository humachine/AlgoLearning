#https://leetcode.com/problems/meeting-rooms/
''' Given a set of meeting timings, determine if a person could attend all of them.
    
    Inp: [[0, 30],[5, 10],[15, 20]]
    Out: False (Meeting at 5, 10 clashes with 0, 30)
'''
class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals:   return True
        # We could sort either by ascending or descending order. 
        # Only if intervals[i].start <= intervals[i].end <= intervals[i+1].start < intervals[i+1].end ..., this can be a valid meeting schedule

        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]
        for i in xrange(1, len(intervals)):
            # If the current meeting begins before the end of the previous meeting, then return False
            if intervals[i].start < prev.end:
                return False
            prev = intervals[i]
        return True
