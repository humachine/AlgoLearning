#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''Given the prices of a stock on N consecutive days, determine the max profit 
that can be made, assuming that only one stock can be held at a time. Also, buy
and sell must happen on different days. And there has to be a cooldown of 1 day
after selling the stock.

Inp: [1, 2, 3, 0, 2]
Out: 3 (buy, sell, cooldown, buy, sell)
'''
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        # buy = max(prev_rest-price, prev_buy). With prev_rest set to zero, 
        # prev_rest-price always goes negative. If prev_buy is zero, buy will
        # always remain at zero throughout. We hence initialize prev_buy to -inf
        prev_buy = float('-inf')
        # Buy represents the greatest profit you can make after the current day
        # when the last action (buy/sell) that was performed was a BUY. 
        # Likewise for sell & rest too. prev_buy, prev_sell, prev_rest represent
        # the corresponding buy/sell/rest values at the end of the previous day.
        buy = prev_sell = sell = rest = prev_rest = 0

        for day, price in enumerate(prices):
            # buy[after day days] = buy[day-1] or rest[day-1]-price
            # i.e buy[day] = max(BuyRest or RestBuy) 
            buy = max(prev_rest-price, prev_buy)
            # sell[after day days] = buy[day-1]+price or sell[day-1]
            # i.e sell[day] = max(BS or SR)
            sell = max(prev_buy+price, prev_sell)
            # rest[after day days] = buy[day-1] or sell[day-1] or rest[day-1]
            # i.e rest[day] = max(SR or BR or RR)
            rest = max(prev_rest, prev_buy, prev_sell)
            prev_buy, prev_sell, prev_rest = buy, sell, rest
        # We return sell since having sell as last money action gives us the maximum profits
        return max(sell, buy, rest)

s = Solution()
print s.maxProfit([1, 2, 3, 0, 2])
print s.maxProfit([])
