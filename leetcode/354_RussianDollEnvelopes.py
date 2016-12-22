#https://leetcode.com/problems/russian-doll-envelopes/
'''
Inp: [[5,4],[6,4],[6,7],[2,3]]
Out: 3  ([2,3] => [5,4] => [6,7])
The maximum number of envelopes you can Russian doll is 3
'''
from bisect import bisect_left, bisect_right
class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:   return 0
        envelopes = [(a[0], a[1]) for a in envelopes]
        envelopes.sort(key = lambda x: (x[0], x[1]))
        n = len(envelopes)
        dp = [1]*n
        maxSoFar = 1
        maxCandidate = envelopes[0]
        print envelopes
        for i in xrange(1, n):
            curr = envelopes[i]
            target = (curr[0]-1, curr[1]-1)
            lowest = bisect_left(envelopes, target)
            if lowest == 0:
                continue
            dp[i] = dp[lowest]+1
            # print lowest, curr, target
        print dp

inp =  [[5,4],[6,4],[6,7],[2,3], [2,5]]
s = Solution()
print s.maxEnvelopes(inp)
