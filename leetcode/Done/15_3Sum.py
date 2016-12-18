#https://leetcode.com/problems/3sum/
"""
    Unique triplets that add up to zero
    Inp: [-1, 0, 1, 2, -1, 4]
    Out: [-1, 0, 1], [-1, -1, 2]
"""
class Solution(object):
    def threeSum(self, nums):
        if len(nums)<2: return []

        TARGET = 0
        nums = sorted(nums)
        n = len(nums)
        solutionSet = set()
        for i in xrange(n-2):
            left, right = i+1, n-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > TARGET:
                    right -= 1
                elif currSum < TARGET:
                    left += 1
                else:
                    solutionSet.add((nums[i], nums[left], nums[right]))
                    left, right = left+1, right-1
        return [[i[0], i[1], i[2]] for i in solutionSet]

    def threeSumCheckPrevious(self, nums):
        """In this function, we perform the same 3Sum code. 
        In addition, if the first number is the same as the previous number in the array, we skip it
        """
        if len(nums)<2: return []

        TARGET = 0
        nums = sorted(nums)
        n = len(nums)
        solutionSet = []
        prev = nums[0]-1
        for i in xrange(n-2):
            if nums[i] == prev:
                continue
            left, right = i+1, n-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > TARGET:
                    right -= 1
                elif currSum < TARGET:
                    left += 1
                else:
                    solutionSet.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left, right = left+1, right-1
            prev = nums[i]
        return solutionSet

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, 4])
