#https://leetcode.com/problems/range-addition/
class Solution(object):
    def getModifiedArray(self, length, updates):
        if not updates or length==0:
            return  [0]*length

        changes = [0]*(length + 1)
        # for each set of updates just record the updates at the start and end points
        for startInd, endInd, inc in updates:
            changes[startInd] += inc
            changes[endInd+1] -= inc

        # Start at 0 and maintain a continuous sum of changes. The value of the continuous sum at each i is answer[i]
        for i in xrange(1, length):
            changes[i] += changes[i-1]
        return changes[:-1]

updates = [[1,3,2],[2,4,3],[0,2,-2]]
length = 5
s = Solution()
print s.getModifiedArray(length, updates)

