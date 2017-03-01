#https://leetcode.com/problems/combinations/
'''Given two integers n and k, return all possible combinations of k numbers
out of 1..n

Inp: n=4, k=2
Out:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution(object):
    def findCombinations(self, start, n, curr, rem):
        # If no more numbers remaining, add list to result
        if not rem:
            self.res.append(list(curr))
            return
        if start == n+1:
            return

        # Pick the next number from start to n (both inclusive)
        curr.append(start)
        for num in xrange(start, n+1):
            curr[-1] = num
            self.findCombinations(num+1, n, curr, rem-1)
        curr.pop()

    def combine1(self, n, k):
        # We backtrack until we run out of numbers.
        # The backtracking method becomes very slow for larger N&K
        self.res = []
        if not n or not k:
            return self.res
        self.findCombinations(1, n, [], k)
        return self.res

    def combine(self, n, k):
        # To combat the backtracking method's slowness, we attempt here a 
        # recursive solution based on NcK's recursion.

        # We cannot choose k from less than k numbers
        if n < k:
            return [[]]
        # for k=1, we each singleton is a combination
        elif k==1:
            return [[i] for i in xrange(1, n+1)]
        # for k=n, a single list of ALL the numbers is the combination
        elif k==n:
            return [[i for i in xrange(1, n+1)]]
        # For all other n, k, nCk = n*((N-1)c(k-1)) + (N-1)c(k)
        # (n-1)cK is all the combinations that don't involve N at all.
        # [n] can be added to each of (n-1)c(k-1) to make it a valid NcK combination
        nminus1_kminus1 = self.combine(n-1, k-1)
        nminus1_k = self.combine(n-1, k)
        li = [[n]+i for i in nminus1_kminus1]
        return nminus1_k + li

s = Solution()
print s.combine(4, 2)
print s.combine(20, 16)
