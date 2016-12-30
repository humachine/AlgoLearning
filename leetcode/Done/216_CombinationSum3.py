#https://leetcode.com/problems/combination-sum-ii/
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

    Inp: k=3, n=7
    Out: [[1,2,4]]

    Inp: k=3, n=9
    Out: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
    def backTrack(self, remainingNums, target, start, path, res):
        ''' We backtrack on reaching the target within remainingNums no of numbers.
        '''
        # If we have used up k numbers
        if remainingNums==0:
            # If we have reached the target we add the path to the result
            if target == 0:
                res.append(list(path))
            # Regardless of whether or not we reach the target, we terminate the search since we've used up k numbers
            return

        for num in xrange(start, 10):
            # We run through all numbers from 1-9. If num > target, then we stop (sorted ascending)
            if num > target:
                break
            # We add num to the path. And we recurse on target-num, using the numbers (num+1->10)
            path.append(num)
            # We backtrack on target-num using num+1 to 10.
            ''' Note: If each number can be used more than one, we return start=num (instead of num+1) below.  '''
            self.backTrack(remainingNums-1, target-num, num+1, path, res)
            # We remove num from the path and continue
            path.pop()

    def combinationSum3(self, k, n):
        # If either k or n is 0, then no combinations possible
        if not any([k, n]) or k>9:   return []
        res = []
        self.backTrack(k, n, 1, [], res)
        return res

s = Solution()
print s.combinationSum3(3, 7)
print s.combinationSum3(3, 9)
