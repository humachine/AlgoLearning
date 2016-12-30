#https://leetcode.com/problems/subsets-ii/
''' Given a collection of integers that might contain duplicates, nums, return all possible subsets.

    Inp: [1, 2, 2]
    Out: [[2], [1], [1,2,2], [2,2], [1,2], []]
'''
class Solution(object):
    def backTrack(self, nums, start, path, res):
        # We add any path we have to the result, since each path is unique and is a subset itself
        res.append(list(path))
        # For each path, add a new starting point to it -> recurse on the remaining set of numbers -> backtrack and try a new starting point
        for i in xrange(start, len(nums)):
            # To prevent the same starting point being used twice at the same level, we ignore duplicates
            if i>start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backTrack(nums, i+1, path, res)
            path.pop()

    def subsetsWithDup(self, nums):
        ''' Similar to other BT solutions for combination sums, we backtrack on all the various subsets possible'''
        nums.sort()
        res = []
        self.backTrack(nums, 0, [], res)
        return res

s = Solution()
print s.subsetsWithDup([1, 2, 2])
