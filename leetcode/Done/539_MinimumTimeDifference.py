#https://leetcode.com/problems/minimum-time-difference/
'''Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.

Inp: ["23:59","00:00"]
Out: 1
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        if len(timePoints)<2:
            return 0
        str_to_time = lambda x: int(x[:2])*60 + int(x[3:])
        # Convert the string times to numerical times
        new_times = [str_to_time(x) for x in timePoints]
        new_times.sort()
        min_diff = 1440
        for i in xrange(len(timePoints)):
            # Update min diffs
            min_diff = min(min_diff, (new_times[i]-new_times[i-1])%1440)
            if min_diff == 0:
                break
        return min_diff
s = Solution()
print s.findMinDifference(['23:59', '00:00'])
