#https://leetcode.com/problems/burst-balloons/
''' Given an array of balloons, each with a number of coins associated with it. 
Every time you burst a balloon i, you get the product of balloon i's left balloon's coins * right balloon's coins * balloon's coins.
Imagine that this set of balloons is padded with imaginary balloons of 1 coin each on either end of the set of balloons.

In this situation, what's the maximum number of coins that we can hope to get?

    Inp: [3, 1, 5, 8]
    Out: 167 = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 (3158 -> 358 -> 38 -> 8)
'''
class Solution(object):
    def findBestBurst(self, start, end):
        nums, coins = self.nums, self.coins
        if coins[start][end] > 0: #If we have already computed this value, we reuse it
            return coins[start][end]
        for lastBurst in xrange(start, end):
            currCoins = self.findBestBurst(start, lastBurst) + \
                    self.findBestBurst(lastBurst+1, end) + \
                    nums[lastBurst]*nums[start-1]*nums[end] # coins you get by bursting lastBurst along with balloon before start and balloon at end
            coins[start][end] = max(coins[start][end], currCoins) #coins[start][end] is the max coins possible out of ALL possible lastBurst locations
        return coins[start][end]

    def maxCoins(self, nums):
        ''' The crux of this problem is to decide what are some deterministic pieces of the bursting.
        The only 2 times we can be sure about a balloon's neighbours are if it's the first balloon that's being burst. Or if it's the last balloon that's being burst.

        Say, a balloon i is the last balloon that's being burst. The coins that we can get are the max coins we can get by bursting all balloons from 0...i and max we can get from bursting all balloons i+1..n + 1*nums[i]*1 (for bursting the ith balloon)

        We pick all possible 'lastBurst' locations for the balloons and compute the maxcoins we can make in each occasion. 
        This further breaks down into finding the maximum coins we can make by bursting all balloons from 0..lastBurst-1 and from lastBurst+1..n
        '''
        n = len(nums)
        # coins[i][j] is the maximum number of coins we can make by bursting balloons from i upto j (j excluded)
        # We return coins[0][n] as the result
        self.coins = [[0]*(n+1) for i in xrange(n+1)]
        self.nums = nums
        nums.append(1) #Adding 1 at the end to represent the last imaginary balloon
        return self.findBestBurst(0, n)

    def maxCoins(self, nums):
        if not nums:    return 0
        n = len(nums)
        nums.append(1)
        coins = [[0]*n for i in xrange(n+1)] #We need only a n*n matrix for computations. The last (n+1)th row is present just to prevent out of bounds errors when trying to access coins[lastBurst+1] when lastBurst==n-1

        # We run through different lengths of balloon sequences
        for length in xrange(1, n+1):
            # For each length, we pick all possible valid start locations (and consequently end locations)
            for start in xrange(n-length+1):
                end = start + length - 1
                for lastBurst in xrange(start, end+1): # Between start & end, we pick all possible lastBurst locations and find the coins we can get for each burst location
                    currCoins = nums[lastBurst]*nums[start-1]*nums[end+1] + \
                            coins[start][lastBurst-1] + coins[lastBurst+1][end]
                    coins[start][end] = max(coins[start][end], currCoins) #The max over all lastBurst locations is coins[start][end]
        return coins[0][n-1]

s = Solution()
print s.maxCoins([3, 1, 5, 8])
print s.maxCoins([3])
