#https://leetcode.com/problems/paint-house-ii/
'''
The cost of painting each house with a certain color is represented by a n x k cost matrix. Find the minimum cost to paint all houses such that no two adjacent houses have the same color.
'''
class Solution(object):
    def minCostII(self, costs):
        if not costs:   return 0
        n, k = len(costs), len(costs[0])
        ''' moneySpent[h][c] = min amount required to paint house h in color c such that no two consecutive houses are painted in the same color.
        '''
        INTMAX = float('inf')
        moneySpent = [[INTMAX]*k for _ in xrange(n)]
        # Cost to paint the first house in each color is directly costs[0]
        moneySpent[0] = costs[0]

        for house in xrange(1, n):
            # For each house h and color c, we attempt to find the minimum cost to paint the previous house in any color that's not in color c
            # moneySpent[h][c] = min(moneySpent[h-1][c]) + cost[h][c]
            # Finding min is usually an O(k) complexity operation for k colors x n houses -> O(nk*k) complexity

            # To get past that we compute 2 running minimums from L->R and R->L. The minimum of the 2 minimums is the actual minimum

            minimum = moneySpent[house-1][0]
            # Computing L-R minimum
            for color in xrange(1, k):
                # Initially assign each house to the L-R minimum
                moneySpent[house][color] = minimum
                minimum = min(minimum, moneySpent[house-1][color])

            moneySpent[house][-1] += costs[house][-1] #MoneySpent on the last color can be computed based on just L-R minimum since there are no more colors after it

            minimum = moneySpent[house-1][-1] #Now finding R-L minimum
            for color in xrange(k-2, -1, -1):
                # MoneySpent[h][c] = min(L-R minimum, R-L minimum) + costs[h][c]
                moneySpent[house][color] = min(moneySpent[house][color], minimum) + costs[house][color]
                minimum = min(minimum, moneySpent[house-1][color])
        return min(moneySpent[-1])

    def minCostNoExtraSpace(self, costs):
        if not costs:   return 0
        n, k = len(costs), len(costs[0])
        ''' moneySpent[h][c] = min amount required to paint house h in color c such that no two consecutive houses are painted in the same color.

        Based on the previous solution, we can do a few things to reduce the space complexity. Firstly, we don't need N rows of moneySpent. We only need the previous moneySpent row.
        This brings the space complexity down to O(k) from O(nk)

        Next up, we can observe that we don't need the entire O(k) row. All we need is to be able to find the minimum of the remaining previous colors for any color. This can be computed as prevMinimum if minColor!=color else prevSecondMin
        Thus we just need 3 variables to store all the essential information of the previous entire row.
        '''
        INTMAX = float('inf')
        prevMinimum, prevSecondMin, prevMinColor = 0, 0, -1
        for house in xrange(n):
            minimum, secondMin, minColor = INTMAX, INTMAX, -1
            for color in xrange(k):
                # Painting cost = cost of painting house h in color c + prevMinimum of all other colors
                paintingCost = costs[house][color] + (prevMinimum if color != prevMinColor else prevSecondMin)
                if minColor < 0: #If this is the first color we are observing for this set of houses
                    minimum, minColor = paintingCost, color
                elif paintingCost < minimum: #If paintingCost < minimum, reset minimum and secondMin accordingly
                    secondMin = minimum
                    minimum, minColor = paintingCost, color
                elif paintingCost < secondMin:
                    secondMin = paintingCost
            # The current minimums now become the previous minimums
            prevMinimum, prevSecondMin, prevMinColor = minimum, secondMin, minColor
        return minimum


inp = [[20,18,4],[9,9,10]]
inp = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
s = Solution()
print s.minCostNoExtraSpace(inp)
