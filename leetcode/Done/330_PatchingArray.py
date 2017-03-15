#https://leetcode.com/problems/patching-array/
'''Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Inp: [1, 3], n=6
Out: 1 (Only patch required is 2)

Inp: [1, 5, 10], n=20
Out: 2 (Only patch required is 2 and 4)

Inp: [1, 2, 2], n=5
Out: 0 (No patches required)
'''
class Solution(object):
    def minPatches(self, nums, n):
        ''' This beautiful solution is based on an assumption:
        All 1<=i<num have already been filled by some possible combination
        of all numbers nums[:left]

        For any num, we check if nums[left] <= num. 
        If nums[left] <= num, nums[left] + k = num (k comes from 1..num-1 which
        we already assume that can be found by some combination of nums[:left]

        In case nums[left] >= num, then we have to add num as a patch. 
        If we add num as a patch, all numbers from 1...(2*num-1) can be completed
        as num+k (k=1..num-1)

        Eg: [1, 2, 4, 13]
        When num=8, nums[left] = 13.
        Had nums[left] been 6 instead, we could have performed 6+2 = 8.
        Since nums[left]=13, we add 8 as a patch. Now, all numbers from 8-15
        can be computed as 8+k (where k is a combination of nums[:left]
        '''
        left = patches = 0
        num = 1
        while num <= n:
            # If nums[left] <= num, nums[left]+k = num
            # All numbers from num to nums[left]+num-1 get covered by some 
            # combination of nums[:left+1]
            if left<len(nums) and nums[left] <= num:
                num+=nums[left]
                left+=1
            # If nums[left] > num, all numbers form num to num+num-1 get
            # covered by some combination of nums[:left] and num
            else:
                num += num
                patches += 1
        return patches

s = Solution()
print s.minPatches([1, 3], 6)
print s.minPatches([1, 5, 10], 20)
print s.minPatches([1, 2, 2], 5)
print s.minPatches([], 8)
print s.minPatches([1,2,31,33], 2147483647)
