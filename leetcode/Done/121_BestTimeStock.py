#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""Test cases:
    [7, 1, 5, 3, 6, 4]: 5 [Buy at 1 and sell at 6]
    [7, 6, 4, 3, 1]: 0 [No transaction]
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        #Maintain the lowest price seen yet. 
        #Max(curr_price - lowest price seen yet) = maxProfit
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit
    
    def maxProfitDays(self, prices):
        """If you wish to find the days of max profit too"""
        if not prices:
            return 0

        minDay = 0
        maxProfit = 0

        #Maintain the lowest price seen yet. 
        #Max(curr_price - lowest price seen yet) = maxProfit
        bestSoFar = (0, 0)
        for i in xrange(1, len(prices)):
            if prices[i] < prices[minDay]:
                minDay = i
            if maxProfit < prices[i] - prices[minDay]:
                bestSoFar = (minDay, i)
                maxProfit = prices[i] - prices[minDay]
        return maxProfit, bestSoFar

s = Solution()
print s.maxProfitDays([7, 1, 5, 3, 6, 4])
print s.maxProfitDays([7, 6, 4, 3, 1])
