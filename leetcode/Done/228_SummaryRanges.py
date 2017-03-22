#https://leetcode.com/problems/summary-ranges/
'''Given a sorted integer array without duplicates, return the summary of its ranges.

Inp: [0,1,2,4,5,7]
Out: ["0->2","4->5","7"]
'''
class Solution(object):
    def summaryRanges(self, nums):
        res = []
        # We iterate through each number in sequence. As long as we keep getting
        # consecutive numbers, we keep adding it to the previous range. 
        # If the next number is outside of the previous range, we add the previous
        # range to the result and then start a new range with the next number.
        if nums:
            # We append a number much greater than nums[-1] so that the range
            # containing nums[-1] gets added to the result
            nums.append(nums[-1]+2)
            start = end = nums[0]
            for i in xrange(1, len(nums)):
                num = nums[i]
                # If the number we see is the next number of the current range, 
                # extend the current range
                if num == end+1:
                    end = num
                else:
                    if start == end:
                        res.append(str(end))
                    else:
                        res.append('{}->{}'.format(start, end))
                    # Reset start and end to begin a new range
                    start = end = num
        return res

s = Solution()
print s.summaryRanges([0, 1, 2, 4, 5, 7])
