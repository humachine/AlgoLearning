#https://leetcode.com/problems/house-robber/

#If money from any house could be negative, then 
#curr = max(stash, prev, prev_prev, prev_prev+stash)
"""Test Cases:
    [1, 3, 6, 5]: 8 (picking 3 & 5)
    [1, 3, 1, 4, 7]: 10 (picking 3 & 7)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        #Prev_prev = max profit possible upto i-2 houses
        #Prev = max profit possible upto i-1 houses
        #curr = max(profit[i-1], profit[i-2]+curr_money)
        #Either pick the max profit possible until the prev house
        #OR pick the max profit upto prev_prev house + curr_profit

        prev_prev = nums[0]
        prev = max(nums[1], prev_prev)

        for stash in nums[2:]:
            prev, prev_prev = max(prev, prev_prev + stash), prev
        return prev

s = Solution()
print s.rob([1, 3, 6, 5])
print s.rob([1, 3, 1, 4, 7])
