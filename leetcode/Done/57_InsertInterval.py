#https://leetcode.com/problems/insert-interval/
'''
Given non-overlapping intervals sorted by start time, insert a new interval.
    Inp: [1,3],[6,9], [2, 5]
    Out: [1,5],[6,9]

    Inp: [1,2],[3,5],[6,7],[8,10],[12,16], [4,9]
    Out: [1,2],[3,10],[12,16] 
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '({}, {})'.format(self.start, self.end)

from bisect import bisect_left, bisect_right
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # Note: Since the intervals are disjoint and sorted by starting times, we know that they are also sorted in end times. 
        # Further we know that intervals[i].start <= intervals[i].end < intervals[i+1].start <= intervals[i+1].end < intervals[i+2].start ....
        if not intervals: return [newInterval]

        intervalList = [i.start for i in intervals]
        lInd = bisect_left(intervalList, newInterval.start) 
        rInd = bisect_right(intervalList, newInterval.end) 
        # For all i < lInd, the start is strictly < newInterval.start
        # For all i >= rInd, the start is strictly > newInterval.end
        newStart, newEnd = newInterval.start, newInterval.end

        # The end of the newInterval finishes before the start of ANY interval at all
        if rInd == 0:
            return [newInterval] + intervals

        # If newInterval.start starts AFTER the start of all intervals and starts after the END of all intervals
        if lInd == len(intervals) and intervals[-1].end < newInterval.start:
            return intervals + [newInterval]

        # If there's a previous interval and its end time overlaps with your interval, add that to the merging
        if lInd >0 and intervals[lInd-1].end >= newInterval.start:
            lInd-=1
        newStart = min(intervals[lInd].start, newStart)
        newEnd = max(intervals[rInd-1].end, newInterval.end)
        return intervals[:lInd] + [Interval(newStart, newEnd)] + intervals[rInd:]


    def insertLinear(self, intervals, newInterval):
        if not intervals: return [newInterval]
        leftIntervals, rightIntervals = [], []
        newStart, newEnd = newInterval.start, newInterval.end
        for interval in intervals:
            # If an interval's end is before newInterval's start, it goes into left
            if interval.end < newStart:
                leftIntervals += [interval]
            # If an interval's start is before newInterval's end, it goes into right
            elif interval.start > newEnd:
                rightIntervals += [interval]
            # Else, we add it to the merge
            else:
                newStart = min(interval.start, newStart)
                newEnd = max(interval.end, newEnd)
        return leftIntervals + [Interval(newStart, newEnd)] + rightIntervals

    def insertBinarySearch(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]

        def _custom_bisect(iterable, target, keyFn=lambda x: x, mode='right'):
            ''' Driver function for both bisect modes '''
            if mode!='left':   mode='right'
            left, right = 0, len(iterable)
            while left < right:
                mid = (left + right)/2
                if keyFn(iterable[mid]) < target or (mode=='right' and keyFn(iterable[mid])==target):
                    left = mid+1
                else:
                    right = mid
            return left

        def custom_bisect_left(iterable, target, keyFn=lambda x: x):
            '''Returns k such that for all i>=k, keyFn(iterable[i]) >= target'''
            return _custom_bisect(iterable, target, keyFn, 'left')

        def custom_bisect_right(iterable, target, keyFn=lambda x: x):
            '''Returns k such that for all i>=k, keyFn(iterable[i]) > target'''
            return _custom_bisect(iterable, target, keyFn, 'right')

        # For all i < lInd, intervals[i].end < newInterval.start
        # for all i >= rInd, intervals[i].start > newInterval.end
        lInd = custom_bisect_left(intervals, newInterval.start, lambda x: x.end)
        rInd = custom_bisect_right(intervals, newInterval.end, lambda x: x.start)
        newStart, newEnd = newInterval.start, newInterval.end

        # We now know that only intervals[lInd:rInd] intersects with newInterval
        clashingIntervals = intervals[lInd:rInd]
        if clashingIntervals: # If any clashing intervals are found
            newStart, newEnd = min(newStart, clashingIntervals[0].start)
            newEnd = max(newEnd, clashingIntervals[-1].end)

        # intervals[:lInd] is similar to leftIntervals from insertLinear()
        # intervals[rInd:] is similar to rightIntervals from insertLinear()
        return intervals[:lInd] + [Interval(newStart, newEnd)] + intervals[rInd:]


s = Solution()
intervals = [Interval(3, 4), Interval(6, 9)]
print s.insertBinarySearch(intervals, Interval(1,2))
print

intervals = [Interval(1, 1), Interval(2,3), Interval(6, 9)]
print s.insertBinarySearch(intervals, Interval(3,4))
print

intervals = [Interval(1, 15)]
print s.insertBinarySearch(intervals, Interval(6,8))
print

intervals = [Interval(1, 5)]
print s.insertBinarySearch(intervals, Interval(2,3))
print

intervals = [Interval(1, 5)]
print s.insertBinarySearch(intervals, Interval(6,8))
print
