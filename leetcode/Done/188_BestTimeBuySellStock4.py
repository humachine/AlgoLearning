#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''Given the prices of a stock on N consecutive days, find the maximum profit.
You may complete at most k transactions and not hold more than one stock at a time.

Inp: [1, 3, 4, 2, 9, 7, 11], k=3
Out: 14 (=4-1 + 9-2 + 11-7)

Inp: [1, 3, 4, 2, 9, 7], k=2
Out: 10 (=4-1 + 9-2)
'''
class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or not k:
            return 0

        # If more than N/2 transactions allowed, we can greedily perform
        # all possible profitable transactions
        if k>len(prices)/2:
            profit = 0
            for i in xrange(len(prices)-1):
                # If a stock price goes up over a day, then buy it today and
                # sell the next day.
                if prices[i+1]>prices[i]:
                    profit += prices[i+1]-prices[i]
            return profit

        n = len(prices)
        # buy[i] represents the maximum profit possible when we have completed
        # exactly i buys.
        # sell[i] = maxProfit when we have completed exactly i sells
        buy = [float('-inf')]*k
        sell = [0]*k

        for price in prices:
            sell[0] = max(sell[0], buy[0]+price)
            buy[0] = max(buy[0], -price)
            for i in xrange(1, k):
                # sell[i] = prev sell value. Or ith buy value + price (signifying sale on the current day)
                sell[i] = max(sell[i], buy[i]+price)
                # buy[i] = prev buy value. Or (i-1)th sell value - price (signifying a buy on the current day)
                buy[i] = max(buy[i], sell[i-1]-price)
        # We finally return max profit of j sells (j=1...k)
        return max(sell)


s = Solution()
print s.maxProfit(3, [1, 3, 4, 2, 9, 7, 11])
print s.maxProfit(2, [1, 3, 4, 2, 9, 7])
