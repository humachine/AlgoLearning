#https://leetcode.com/problems/combination-sum/
'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. (each candidate can be repeated infinite times)

    Inp: [2, 3, 6, 7], 7
    Out: [ [7], [2, 2, 3] ]
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates: []
        candidates.sort()
        # numWays[x] represents the all the ways to add up to x only using candidates
        # numWays[x] contains list all of which are in sorted order.
        # Hence, for a particular summation (2+3+2 = 7) only 2, 2, 3 will always be stored
        numWays = [[] for x in xrange(target+1)]
        numWays[0] = [[]] #Initializing numWays[0] to an empty list
        '''For each candidate cand, we go forward and fill up numWays[x] if (x-cand) is either 0 or has some non-empty paths.
        If x-cand is zero, then we add [cand] to numWays.
        Since we go from cand->target, numWays[cand] first gets appended with [cand] since(cand-cand=0).

        At each iteration i, we try to compute paths to every x only involving candidates[:i]
        '''
        for cand in candidates:
            for num in xrange(cand, target+1):
                subSum = num - cand
                numWays[num].extend([x+[cand] for x in numWays[subSum]])

        return numWays[-1]
s = Solution()
print s.combinationSum([2, 3, 7, 6], 7)
