#https://leetcode.com/problems/merge-sorted-array/
''' Given two sorted arrays A and B, merge them into one array.
Assume that A has enough space to accomodate the values of A and B.

Inp: [1, 3, 5], [2, 4, 6]
Out: [1, 2, 3, 4, 5, 6]
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = m-1, n-1
        # We only need to try and merge all elements of B into A. 
        # The moment we have merged each element of B into A, we are done.
        while j>=0:
            # If A has no more elements, just paste all of B's remaining elements
            # Or, if A's element < B's element, pick up and use B's element
            if i<0 or nums1[i] < nums2[j]:
                nums1[i+j+1] = nums2[j]
                j-=1
            else:
                nums1[i+j+1] = nums1[i]
                i-=1
        return nums1
s = Solution()
print s.merge([1, 0], 1, [2], 1)
