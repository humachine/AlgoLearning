#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
''' Given 2 sorted arrays and a number K, return the K pairs that have the 
smallest sums.
'''
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        # We can make a claim that nums1[k] will never appear in the result
        # (Since, nums1[0:k], nums2[0] will always be smaller than nums1[k], nums[any j]
        # Hence, we load the first k-elements of nums1 along with the first element
        # of nums2 into a priority queue.
        # At each juncture, we remove the min of the heap, say (sum, i, j). 
        # We now add (nums1[i]+nums2[j+1], i, j+1) to the heap (if j is valid)
        if not nums1 or not nums2:
            return []
        p_queue, res = [], []
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        # Initializing the priority queue with the first k-elements of nums1, along
        # with the first element of nums2
        for i in xrange(min(m, k)):
            heapq.heappush(p_queue, (nums1[i]+nums2[0], i, 0))

        for i in xrange(k):
            # If no more pairs exist, break
            if not p_queue:
                break
            # Pop the min of the priority queue
            min_pair = heapq.heappop(p_queue)
            res.append([nums1[min_pair[1]], nums2[min_pair[2]]])

            # Add the next pair (if available) to the priority queue
            next_ind1, next_ind2 = min_pair[1], min_pair[2]+1
            if next_ind2 < n:
                heapq.heappush(p_queue, (nums1[next_ind1]+nums2[next_ind2],
                    next_ind1, next_ind2))
        return res

s = Solution()
print s.kSmallestPairs([1, 7, 11], [2,4,6], 3)
print s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2)
print s.kSmallestPairs([1, 2], [3, 4], 4)
print s.kSmallestPairs([1,7,11], [2,4,6], 3)
assert s.kSmallestPairs([], [], 3) == []
