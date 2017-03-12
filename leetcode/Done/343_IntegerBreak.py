#https://leetcode.com/problems/integer-break/
'''Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Inp: n=2
Out: 1 (2=1+1)

Inp: 10
Out: 36 (3+4+4)
'''
class Solution(object):
    def intBreaks(self, n):
        if n in self.products:
            return self.products[n]

        max_prod = 0
        for i in xrange(1, (n+2)/2):
            # max_prod is max(i*(n-i) or i*bestIntBreak(n-i))
            max_prod = max(max_prod, i*max(n-i, self.intBreaks(n-i)))
        self.products[n] = max_prod
        # max_prod represents the biggest product possible by breaking n
        return max_prod

    def integerBreak(self, n):
        self.products = {1:1}
        ans = self.intBreaks(n)
        return ans

s = Solution()
print s.integerBreak(2)
print s.integerBreak(3)
print s.integerBreak(5)
print s.integerBreak(10)
print s.integerBreak(12)
