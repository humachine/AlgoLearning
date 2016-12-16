#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""Test cases:
    Inp: [3, 7, 2, 3, 6]
    Out: 8 (7-3 + 6-2)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0

        #Since unlimited number of transactions are allowed, if the rate increases over a day, 
        #buy on previous day and sell on next day.
        #
        #Even cases were rate continuously increases over 3 days are covered by 3 piecewise increases
        profit = 0
        for i in xrange(len(prices)-1):
            profit += max(0, prices[i+1]-prices[i])
        return profit

s = Solution()
print s.maxProfit([3, 7, 2, 3, 6])
