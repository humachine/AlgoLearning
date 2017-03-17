#https://leetcode.com/problems/coin-change/
'''Given an infinite amount coins of different denominations, find the fewest
number of coins required to make up a given amount.

Inp: [1, 2, 5], 11
Out: 3 (11=1+5+5)

Inp: [2], 3
Out: -1 (No denomination of coins can make up 3)
'''
class Solution(object):
    def coinChange(self, coins, amount):
        # The DP solution may be simpler to implement, but the BFS solution
        # may be faster in certain large input cases.
        # If amount is zero, zero coins are required.
        if not amount:
            return 0
        coins = sorted(set(coins))
        # If amount < smallest denomination, no split possible
        if amount < coins[0]:
            return -1
        # denom[i] = min coins required to sum up to i
        denom = [0]+[float('inf')]*amount
        for i in xrange(1, amount+1):
            for coin in coins:
                # denom[i] is 1+denom[i-coin] if that's lesser
                if i>=coin:
                    denom[i] = min(denom[i], 1+denom[i-coin])
        # If denom[-1] is still float('inf') then no split possible
        return -1 if denom[-1] == float('inf') else denom[-1]

    def coinChange(self, coins, amount):
        # In this BFS solution, we begin a BFS with a node for amount at one end
        # and nodes for each coin at the other end. 
        # From amount, we spread out in a BFS, where each level represents the nodes
        # with value = amount-x (where x is each value of coins).
        # When the top level meets the bottom level, we have found the minimum
        # number of coins required.
        coins = sorted(set(coins))
        if not amount:
            return 0
        if amount < coins[0]:
            return -1
        targets, visited = {amount}, {amount}
        count = 0
        # While there are still nodes in the top level
        while targets:
            count += 1
            next_level = set()
            for target in targets:
                for coin in coins:
                    # If the 2 levels have a common point, we have found the minDenomination
                    if coin == target:
                        return count
                    # If coin > target, every future value of coin > target (ascending array)
                    elif coin > target:
                        break
                    # If target-coin is not a node that has existed in prev
                    # levels, we add it to the next level
                    elif target-coin not in visited:
                        visited.add(target-coin)
                        next_level.add(target-coin)
            # The next_level is now the new target level.
            targets = next_level
        # If none of the levels had any common nodes, then a denomination
        # split is impossible.
        return -1

s = Solution()
print s.coinChange([1, 2, 5], 11)
print s.coinChange([2], 3)
print s.coinChange([1], 0)
print s.coinChange([1, 3, 5], 8)
