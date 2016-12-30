#https://leetcode.com/problems/combination-sum-ii/
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

    Inp: [10, 1, 2, 7, 6, 1, 5], target=8
    Out: [ [1, 7], [1, 2, 5], [2, 6], [1, 1, 6] ]

'''
class Solution(object):
    def _backTrack(self, candidates, target, start, path, res):
        # If you have reached the target, add a copy of the path to your result
        if target == 0:
            res.append(list(path))
            return

        for i in xrange(start, len(candidates)):
            cand = candidates[i]
            if cand > target: #If candidate is already > target, then stop (sorted ascending)
                break
            if i>start and cand == candidates[i-1]: #In this backtracking if you've already seen this number, then ignore any duplicates of it
                continue
            path.append(cand) # Add cand to the path
            self._backTrack(candidates, target-cand, i+1, path, res) #Look in the remaining chunk of the array (i+1 to avoid reusing the same candidate twice)
            path.pop() #Remove candidate from path so that other candidates can be added instead

    def combinationSum2(self, candidates, target):
        if not candidates:  return []
        res = []
        candidates.sort()
        # Run a backtracking of the candidates that you pick at each time
        self._backTrack(candidates, target, 0, [], res)
        return res

s = Solution()
print s.combinationSum2Iterative([10, 1, 2, 7, 6, 1, 5], 8)
print s.combinationSum2Iterative([2, 2, 2], 4)
