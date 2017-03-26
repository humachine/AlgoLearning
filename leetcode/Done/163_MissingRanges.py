#https://leetcode.com/problems/missing-ranges/
'''Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Inp: [0, 1, 3, 50, 75], lower=0, upper=99
Out: ["2", "4->49", "51->74", "76->99"]
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        # We run through the array, adding missing ranges to the result.
        # If next=prev+1, then we move on, since there is nothing missing here.
        # If next!=prev+1, we add the  missing range.

        # We also add upper+1 at the very end of the array and lower-1 at the
        # front of the array, so as to cover the entire spread from lower to upper, inclusive.
        # Since inserting lower-1 at the beginning of the array is an expensive
        # operation, we add it at the back and start iterating the array from arr[-1]
        nums.extend([upper+1, lower-1])
        res = []
        for i in xrange(-1, len(nums)-2):
            prev, nxt = nums[i], nums[i+1]
            # If next == prev, it's a duplicate and we ignore it
            # If next == prev+1, there's no missing range and we move on
            if nxt not in [prev, prev+1]:
                if nxt==prev+2:
                    res.append(str(prev+1))
                else:
                    res.append('{}->{}'.format(prev+1, nxt-1))
        return res

s = Solution()
print s.findMissingRanges([0, 1, 3,  50,  75], 0, 99)
print s.findMissingRanges([], 0, 10)
print s.findMissingRanges([1, 1, 1], 1, 1)
