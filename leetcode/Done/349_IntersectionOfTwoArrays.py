#https://leetcode.com/problems/intersection-of-two-arrays/
'''Given two arrays, return their intersection.

Inp: [1, 2, 2, 1], [2, 2]
Out: [2] (The arrays are considered as sets)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        # If either of the two arrays are empty, return empty set
        if not nums1 or not nums2:
            return []
        seen = set(nums1)
        intersection = set()
        # For each number of array2, check if it is present in array1
        for num in nums2:
            if num in seen:
                # Adding to a set preserves uniqueness of the intersection elements
                intersection.add(num) 
        return list(intersection)

    def intersection(self, nums1, nums2):
        return list(nums1 & nums2)

    def intersectionNoExtraSpace(self, nums1, nums2):
        # In this solution, we sort both arrays first.
        # We then use two poitners to move through the two arrays looking for equal
        # elements (which would populate the intersection)
        nums1.sort()
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        intersection = []
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                # Making sure you don't reinsert equal numbers
                if not intersection or intersection[-1] != nums1[i]:
                    intersection.append(nums1[i])
                i, j = i+1, j+1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return intersection

s = Solution()
print s.intersectionNoExtraSpace([1, 2, 2, 1], [2, 2])
