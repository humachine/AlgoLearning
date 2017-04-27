#https://leetcode.com/problems/3sum-closest/
""" Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

    Inp: [-1, 2, 1, -4], 1
    Out: 2 (= -1 + 2 + 1)

    Inp: [0,2,1,-3], 1
    Out: 0

    -3, 0, 1, 2
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        best_diff, best_sum = float('inf'), 0
        for i in xrange(n-2):
            left, right = i+1, n-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                # If current sum is the target, you cannot find a better solution
                if curr_sum == target:
                    return curr_sum
                #If the current triplet gives a lesser difference from target, save it.
                if abs(curr_sum - target) < best_diff:
                    best_sum = curr_sum
                    best_diff = abs(curr_sum - target)
                #If current sum > target, decrease the sum by taking the next lesser number from the right pointer.
                if curr_sum > target:
                    right -= 1
                #If current sum < target, increase the sum by taking the next greatest number from the left pointer. 
                else:
                    left += 1
        return best_sum

s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)
print s.threeSumClosest([0,2,1,-3], 1)
