#https://leetcode.com/problems/contiguous-array/
'''Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Inp: [0, 1]
Out: 2

Inp: [0, 1, 0]
Out: 2  (01 or 10 is the longest valid subarray)
'''
class Solution(object):
    def findMaxLength(self, nums):
        counts = {0:-1}
        max_len = count = 0
        # We maintain a continuous count/score of the array seen so far. 
        # If we see the same score again in the array, the subarray between
        # the last occurence of this score and current location has equal
        # number of 0s and 1s
        for i, num in enumerate(nums):
            # Count increases by +1 if num is 1, else -1
            count += (2*num-1)
            # If this count has already been seen, counts[count]...i is a 
            # subarray with equal number of 1s and 0s
            if count in counts:
                # Note: We do not update counts[count] with the new location, 
                # because using the earliest occurence of counts[count] will
                # give us the largest subarray
                max_len = max(max_len, i-counts[count])
            else:
                counts[count] = i
        return max_len

s = Solution()
print s.findMaxLength([0, 1])
print s.findMaxLength([0, 1, 0])
