#https://leetcode.com/problems/increasing-triplet-subsequence/
'''
If there exist i, j, k in an array (i < j < k) such that arr[i] < arr[j] < arr[k], return True
Inp: [1, 2, 3, 4, 5]
Out: True

Inp: [5, 4, 3, 2, 1]
Out: False
'''
class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:   return False
        # OneSeq represents the smallest 1-length increasing sequence seen so far (i.e min element seen so far)
        # twoSeq represents the end of a smallest 2-length increasing sequence seen so far
        oneSeq = nums[0]
        twoSeq = None
        for num in nums[1:]:
            # If there is a non-None twoSeq and current number > twoSeq, then we have an increasing triplet subsequence
            if twoSeq is not None and num > twoSeq:
                return True
            # If the current > the smallest number seen so far, then we have a 2-sequence
            if num > oneSeq:
                # If we haven't seen any 2-seq so far, we assign twoSeq to the number we are seeing
                if not twoSeq:
                    twoSeq = num
                else:
                # We try to have the smallest value twoSeq always
                    twoSeq = min(twoSeq, num)
            oneSeq = min(oneSeq, num)

        return False
s = Solution()
print s.increasingTriplet(range(5))
print s.increasingTriplet(range(5)[::-1])
