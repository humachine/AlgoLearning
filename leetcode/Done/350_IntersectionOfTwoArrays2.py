#https://leetcode.com/problems/intersection-of-two-arrays/
'''Given two arrays, return their intersection.

Inp: [1, 2, 2, 1], [2, 2]
Out: [2, 2]

Here, each element should appear in the intersection as many times as it appears in both the arrays.

Follow-Up:
- What if the given array is already sorted? How would you optimize your algorithm?
Use intersectionNoExtraSpace()

- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''
import collections
class Solution(object):
    def intersection(self, nums1, nums2):
        # We form a counter of all the elements of array1.
        # We keep decrementing the counts of any element of array2 that's present in array1.
        # We simultaneously add such elements to the intersection
        num_count_1 = collections.Counter(nums1)
        intersection = []
        for num in nums2:
            if num in num_count_1 and num_count_1[num]>0:
                num_count_1[num] -= 1
                intersection.append(num)
        return intersection

    def intersectionNoExtraSpace(self, nums1, nums2):
        # In this solution, we sort both arrays first.
        # We then use two pointers to move through the two arrays looking for equal
        # elements (which would populate the intersection)
        nums1.sort()
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        intersection = []
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i, j = i+1, j+1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return intersection

s = Solution()
print s.intersectionNoExtraSpace([1, 2, 2, 1], [2, 2])
