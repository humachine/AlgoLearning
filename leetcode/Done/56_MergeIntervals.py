#https://leetcode.com/problems/merge-intervals/
'''
Given a set of intervals, merge any overlapping intervals
    Inp: [1,3],[2,6],[8,10],[15,18]
    Out: [1,6],[8,10],[15,18] (merging 1,3 & 2,6 into 1, 6)
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return '({}, {})'.format(self.start, self.end) 

'''
Note: To solve this problem, the intervals need to be sorted ascending in start values or descending in end values. 
If we sort ascending in end values, we get this error when merging adjacent intervals
[1, 2], [3, 5], [1, 6] are the intervals sorted in ascending order of end.
Merging them will give us: [1,2], [1, 6] when the answer should be [1, 6]
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:   return intervals
        intervals.sort(key = lambda x: x.start

        prev = intervals[0]
        res = []
        for i, curr in enumerate(intervals[1:]):
            # If the previous interval can be merged with current interval, merge it
            if prev.end >=  curr.start:
                # prev.start, prev.end = min(curr.start, prev.start), max(prev.end, curr.end)
                # Since the intervals are arranged in ascending order of starttime,
                # min(prev.start, curr.start) always is prev.start
                prev.start, prev.end = prev.start, max(prev.end, curr.end)
            else:
            # If current and previous intervals are disjoint, add previous interval to result
                res.append(prev)
                prev = curr
        # We just append the last remaining interval (prev) to the result
        res.append(prev)
        return res

inp = [Interval(1, 3), Interval(8, 10), Interval(15, 18), Interval(2, 6)]
s = Solution()
ans= s.merge(inp)
print ans
