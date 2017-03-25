#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''Given the prices of a stock on N consecutive days, find the maximum profit.
You may complete at most two transactions and not hold more than one stock at a time.

Inp: [1, 3, 4, 2, 9, 7]
Out: 10 (=4-1 + 9-2)

Inp: [5, 4, 3, 2, 1, 9]
Out: 8 (=9-1)
'''
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        first_sell = second_sell = 0
        # We have to set first_buy and second_buy to -inf. If not, then
        # first_buy and second_buy will remain at 0 (Since 0>first/second_buy-price)
        # Hence to ensure that we make a buy before selling, we initalize the buys
        # to -inf to begin with. This way, buying any stock will always be the
        # best/max value for first_buy
        second_buy = first_buy = float('-inf')

        for price in prices:
            # first_buy is the maxProfit one can make by executing just one single buy
            # Hence first_buy = either prev value of first_buy or -price (meaning a purchase happened)
            first_buy = max(first_buy, -price)
            # For first_sell, we either retain the prev best value, or execute a sale
            # on top of the prev best buy (which is first_buy)
            first_sell = max(first_sell, first_buy+price)
            # We perform similar interactions for second_buy and second_sell.
            second_buy = max(second_buy, first_sell-price)
            second_sell = max(second_sell, second_buy+price)
        # We return the max of the profits possible by 1 sell or 2 sells
        return max(second_sell, first_sell)

s = Solution()
print s.maxProfit([1, 3, 4, 2, 9, 7])
print s.maxProfit([5, 4, 3, 2, 1, 9])
