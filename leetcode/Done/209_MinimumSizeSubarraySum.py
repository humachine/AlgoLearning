#https://leetcode.com/problems/minimum-size-subarray-sum/
'''
Given an array of N positive integers and a +ve integer s, find the length of the smallest subarry whose sum >= s. If there is None, return 0

    Inp: [2, 3, 1, 2, 4, 3], 7
    Out: 2 ([4, 3] is the smallest subarray which has that sum)
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        '''
        We use a sliding window two-pointer approach to compute the sums
        Similar to the 3-Sum problem, we set up our sum with a left and right.
        
        Since all numbers are +ve, increasing right increases the total and increasing left decreases our total.
        We move both our pointers until we can keep finding newer and newer window sums.
        Once we find a valid window, we update minLen if applicable.
        '''
        if not nums:    return 0
        if len(nums) == 1:  return int(nums[0] >= s)
        n = len(nums)
        left, right, total, minLen = 0, 0, 0, n+1
        # [left, right) is the window that we are looking at
        while left<= right and right<=n:
            # If total is < s, we add then number at right and push right forward
            if total < s:
                if right == n:
                    break
                total+=nums[right]
                right+=1
            else:
            # If total >=s, we've found a valid window. We update minLen, if necessary
                minLen = min(minLen, right-left)
                # If we have reached a 1-size window, we cannot go any smaller
                if minLen == 1:
                    return 1
                total-=nums[left]
                left+=1
        # We set minLen = n+1 at the start. If minLen is still at n+1, then we didn't discover any valid window and hence we return 0
        return minLen if minLen < n+1 else 0
s = Solution()
print s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
