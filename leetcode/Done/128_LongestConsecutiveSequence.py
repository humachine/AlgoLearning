#https://leetcode.com/problems/longest-consecutive-sequence/
'''
Return length of longest consecutive sequence that can be formed using the numbers in the input
    Inp: [100, 4, 200, 1, 3, 2]
    Out: 4 (1, 2, 3, 4)
'''
from collections import namedtuple
class Solution(object):
    def longestConsecutive(self, nums):
        '''
        Here, we attempt to form intervals of consecutive numbers. The length of the longest interval should be the longestConsecutive sequence length.

        For each number, if the number is not already present in numLocs, we add it to a new (num, num) one-length interval. Next, we check if we can merge it into the interval of its predecessor.
        Next, we also check if we can merge it with the interval of its successor.

        Note: For each interval (x,y) only numLocs[x] and numLocs[y] has the accurate ranges.
        '''
        if len(nums)<=1:
            return len(nums)
        Sequence = namedtuple('Sequence', 'start end')
        numLocs, maxLen = {}, 1
        for num in nums:
            # We try to put it into ranges only if it has previously not been seen
            if num not in numLocs:
                numLocs[num] = Sequence(num, num)

                # If the predecessor exists, we merge the two ranges
                if num-1 in numLocs:
                    prevStart, prevEnd = numLocs[num-1]
                    numLocs[num] = numLocs[prevStart] = Sequence(prevStart, num)
                    maxLen = max(maxLen, num-prevStart+1)
                # If the successor exists, we merge the two ranges
                if num+1 in numLocs:
                    prevStart, prevEnd = numLocs[num].start, numLocs[num+1].end
                    numLocs[prevStart] = numLocs[prevEnd] = Sequence(prevStart, prevEnd)
                    maxLen = max(maxLen, prevEnd-prevStart+1)
        return maxLen


    def longestConsecutiveConcise(self, nums):
        if len(nums)<=1:
            return len(nums)
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num-1 not in numSet:
                start, end = num, num+1
                while end in numSet:
                    end+=1
                maxLen = max(maxLen, end-start)
        return maxLen

s = Solution()
inp=[100, 4, 200, 1, 3, 2]
# inp = [0,3,7,2,5,8,4,6,0,1]
# inp = [4,2,2,-4,0,-2,4,-3,-4,-4,-5,1,4,-9,5,0,6,-8,-1,-3,6,5,-8,-1,-5,-1,2,-9,1]
print s.longestConsecutiveConcise(inp)
