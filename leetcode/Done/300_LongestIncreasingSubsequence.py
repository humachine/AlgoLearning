#https://leetcode.com/problems/longest-increasing-subsequence/
'''Given an array of integers, return the length of the longest increasing
subsequence in the array.

Inp: [10, 9, 2, 5, 3, 7, 101, 18]
Out: 4  (2, 3, 7, 101)
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        '''This is a simple dynamic programming solution in O(N^2) time and O(N) space.
        seq_lengths[i] = the length of the LIS that ends at nums[i]
        '''
        n, max_len = len(nums), 0
        seq_lengths = [0]*(n)
        for i in xrange(n):
            # Every i has at least a trivial 1-length sequence ending at i
            seq_lengths[i] = 1
            for j in xrange(i):
                # If nums[i] > some previous number, see if we can get a bigger
                # seq_length by adding nums[i] at the end of nums[j]'s sequence
                if nums[i] > nums[j]:
                    seq_lengths[i] = max(seq_lengths[i], 1+seq_lengths[j])
            # Update overall max LIS
            max_len = max(max_len, seq_lengths[i])
        return max_len

    def lengthOfLIS(self, nums):
        ''' This is a O(NlogN) solution for the LIS problem. We maintain a list
        which has the smallest end number (or their respective index) of increasing
        sequences of all possible lengths.
        The longest sequence we can build will be the LIS.
        '''
        if not nums:
            return 0
        n, max_len = len(nums), 0
        # best_seqs[i] = j if nums[j] is the lowest end point of an increasing
        # sequence of length i+1

        # For each number in the array ($num), we check if it could be the smallest 
        # endpoint of an increasing sequence of lengths found before. In other
        # words, we see if it can replace some other number as the endpoint of
        # an increasing sequence from the sequences we found earlier. 
        # If not, then this number gets added as the endpoint of the increasing
        # sequence of the prev_max_length+1.
        best_seqs = [0]
        for i, num in enumerate(nums):
            # best_seqs[i] hold indices to numbers who form tails of the best
            # inc sequences of length i+1. From this we can see that the tails
            # will be an increasing array. (If a tail of, say length 3, < tail
            # of length 2, then this tail[3] could replace the tail[2].
            left, right = 0, len(best_seqs)
            # We perform a binary search to find the index of best_seqs at which
            # this new number would be the tail (if at all)
            while left<right:
                mid = (left+right)/2
                best_seq = nums[best_seqs[mid]]
                if best_seq == num:
                    right = mid
                    break
                elif best_seq < num:
                    left = mid+1
                elif best_seq > num:
                    right = mid
            # if right is end of best_seqs, then this new number could be 
            # added at the end of sequence ending at best_seqs[-1] and extend it
            # further by 1 length.
            if right == len(best_seqs):
                best_seqs.append(i)
            # In all other cases, update the value of the tail of some best sequence.
            else:
                best_seqs[right] = i
        # Length of the tail array (i.e best_seqs) will be the length of LIS
        return len(best_seqs)
s = Solution()
print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
