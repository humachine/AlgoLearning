#https://leetcode.com/problems/meeting-rooms-ii/
'''
Given meeting start & end times, return the number of meeting rooms required to schedule these meetings

    Inp: [[0, 30],[5, 10],[15, 20]]
    Out: 2 (0-30 in room 1 and the other 2 meetings in room 2)
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from heapq import heappush, heappop
from collections import defaultdict
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)

        # Sort all intervals by starting time
        intervals.sort(key = lambda x: x.start)
        numRooms = 1
        h = [intervals[0].end]

        # Add each meeting's end time into a min heap
        for meeting in intervals[1:]:
            # nextFreeSlot will be the head of the min heap
            nextFreeSlot = h[0]
            # If the meeting's start time is after the end of the nextFreeSlot, then schedule it in that room
            if nextFreeSlot <= meeting.start:
                heappop(h) #Pop the end time of the previous meeting that ends at nextFreeSlot
                heappush(h, meeting.end) #Add the end time of the current meeting
            else:
                # If this meeting cannot be squeezed in an existing room after one of the previous meetings, then add its end time separately into the heap
                heappush(h, meeting.end)
                numRooms = max(numRooms, len(h)) # max meeting rooms required is the highest number of rooms that has ever been required during the entire scheduling
        return numRooms


    def minMeetingRoomsGetSchedule(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)

        # Sort all intervals by starting time
        intervals.sort(key = lambda x: x.start)
        numRooms = 1
        h = [(intervals[0].end, 1)]
        schedules = defaultdict(list)
        schedules[numRooms].append(intervals[0])

        # Add each meeting's end time and room number into a min heap
        for meeting in intervals[1:]:
            # nextFreeSlot will be the head of the min heap
            nextFreeSlot = h[0]
            # If the meeting's start time is after the end of the nextFreeSlot, then schedule it in that room
            if nextFreeSlot[0] <= meeting.start:
                meetingRoom = nextFreeSlot[1]
                heappop(h) #Pop the end time of the previous meeting that ends at nextFreeSlot
            else:
                # If this meeting cannot be squeezed in an existing room after one of the previous meetings, then add its end time separately into the heap
                meetingRoom = len(h) + 1
            heappush(h, (meeting.end, meetingRoom)) #Add the end time of the current meeting and room number to the heap
            numRooms = max(numRooms, len(h)) # max meeting rooms required is the highest number of rooms that has ever been required during the entire scheduling
            schedules[meetingRoom].append(meeting) # Add this meeting to the scheduling

        # Pretty print all meeting schedules (non-unique) 
        for meetingRoom in sorted(schedules.keys()):
            print 'Meeting Room #{}'.format(meetingRoom)
            for meeting in schedules[meetingRoom]:
                print meeting.start, '->', meeting.end

        return numRooms

s = Solution()
inp = [Interval(0, 30),Interval(5, 10),Interval(15, 20)]
print s.minMeetingRoomsGetSchedule(inp)
