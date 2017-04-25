#https://leetcode.com/problems/single-number-ii/
'''In an array, every element appears thrice except one element which appears 
once. Identify the element.

Inp: [1, 1, 7, 1, 5, 5, 5]
Out: 7

Inp: [-2,-2,1,1,-3,1,-3,-3,-4,-2]
Out: -4
'''
class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        answer = 0
        num_bits = 32
        for bit in xrange(num_bits):
            num_count = 0
            for num in nums:
                # For each bit, count the number of numbers in which this bit is set
                num_count += (num >> bit) & 0b1
            # If >< 3k numbers have a bit set as 1, then that bit is present in the answer.
            # This same idea can be extended to any arbitrary number > 3 too.
            if num_count % 3 == 1:
                # Adding that bit to answer
                answer += 1<<bit
        # In case the negative bit is set to 1 in the answer, find the 2's complement.
        if answer>>(num_bits-1) & 0b1:
            return answer-(1<<num_bits)
        return answer

s = Solution()
print s.singleNumber([1, 1, 7, 5, 1, 5, 5])
print s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
