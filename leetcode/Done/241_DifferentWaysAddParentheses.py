#https://leetcode.com/problems/different-ways-to-add-parentheses/
'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. (+,-,*)

    Inp: '2-1-1'
    Out: [0, 2] ((2-1)-1), (2-(1-1))

    Inp: '2*3-4*5'
    Out: [-34, -14, -10, -10, 10] obtained from:
        (2*(3-(4*5))) = -34
        ((2*3)-(4*5)) = -14
        ((2*(3-4))*5) = -10
        (2*((3-4)*5)) = -10
        (((2*3)-4)*5) = 10
'''
import operator
import collections
class Solution(object):
    def diffWaysToComputeNoMemoization(self, input):
        ''' We try to compute the various ways in which we can compute a substring.
        We then pick all possible starting operator locations and compute leftValue operator rightValue.

        We see that we use each operator i as a point at which we divide the string into 2 halves, compute subresults and combine.
        Therefore the complexity is O(#operators) * O(N) ~ O(N*N) if each number is a single digit number (or #operators in order of number of numbers)
        Each subproblem requires a scan of the substring (like inp[:i]) which takes O(N) time.
        '''
        inp, res = input, []
        for i, char in enumerate(inp):
            if char in '+-*':
                res1 = self.diffWaysToCompute(inp[:i]) # Returns the various outputs obtained by adding parens to inp[:i]
                res2 = self.diffWaysToCompute(inp[i+1:])
                if char == '+':
                    result = [x+y for x in res1 for y in res2]
                elif char == '*':
                    result = [x*y for x in res1 for y in res2]
                elif char == '-':
                    result = [x-y for x in res1 for y in res2]
                res.extend(result)

        if len(res) == 0: #If we found no operator, we just use the value of the number as the only possibility
            res.append(int(inp))
        return res

# ---------------------------------------------------------------------------

    def computeWays(self, inp, start, end):
        if (start, end) in self.pre_computed: #Memoization step
            return self.pre_computed[(start, end)]
        res = []
        operators = {'+': operator.add, '-':operator.sub, '*':operator.mul} # Dictionary containing functions for each operator
        for i in xrange(start, end):
            char = inp[i]
            if char in '+-*': #If we encounter an operator, we obtain the values to each subproblem
                res1 = self.computeWays(inp, start, i)
                res2 = self.computeWays(inp, i+1, end)
                res.extend([operators[char](x, y) for x in res1 for y in res2]) # this is equivalent to for x in res1: for y in res2: res.append(x appropriateOperator y)

        # If there are no operators in the string, then the only possible value is the number itself
        self.pre_computed[(start, end)] = res if res else [int(inp[start:end])]
        return self.pre_computed[(start, end)]

    def diffWaysToCompute(self, input):
        inp, res, self.pre_computed = input, [], {}
        return self.computeWays(inp, 0, len(inp))

s = Solution()
print s.diffWaysToCompute('12-1-1')
print s.diffWaysToCompute('2*3-4*5')
