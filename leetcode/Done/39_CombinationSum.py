#https://leetcode.com/problems/combination-sum/
'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. (each candidate can be repeated infinite times)

    Inp: [2, 3, 6, 7], 7
    Out: [ [7], [2, 2, 3] ]
'''
class Solution(object):
    def _backTrack(self, candidates, target, start, path, res):
        ''' We employ a typical backtracking approach to solve this problem.
        We try to find target using candidates[start:].
        If cand <= target, add it to the path and recurse on target-cand

        At any point if cand-target==0, then we add that path to the result.
        '''
        if target == 0: #Since target has been reached, add a copy of the path to result
            res.append(list(path))
        for i in xrange(start, len(candidates)):
            cand = candidates[i]
            if cand <= target:
                path.append(cand)
                self._backTrack(candidates, target-cand, i, path, res)
                path.pop()
            # If cand > target, all further candidates will be > target (sorted ascending)
            else:
                break

    def combinationSumBT(self, candidates, target):
        if not candidates: []
        candidates.sort()
        res = []
        self._backTrack(candidates, target, 0, [], res)
        return res


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
print s.combinationSumBT([2, 3, 7, 6], 7)
