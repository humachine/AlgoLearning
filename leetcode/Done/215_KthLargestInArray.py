#https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
Given an array of numbers, find the kth largest number in the array.
    
    Inp: [3, 2, 1, 5, 6, 4], k=2
    Out: 5 (5 is the 2nd largest number in the array)
'''
from heapq import heappush, heappop, heapify, heapreplace
class Solution(object):
    def findKthLargestHeap(self, nums, k):
        ''' We build a min-heap out of the first k elements.
        From k+1-Nth elements, if the element > heap's min, then we pop the min and push the element on to the heap.
        The min of the heap will be the k-th largest element. (the heap itself represents the k largest elements of the array)'''

        h = list(nums[:k])
        heapify(h) #Building a heap out of the first k elements: O(k) complexity
        for i in xrange(k, len(nums)):
            if nums[i] > h[0]: #If new element > min of the heap; remove min and push new element
                heapreplace(h, nums[i]) #heapreplace(heap, element) pops the min and inserts the new element in a single step
        return h[0] #Min of the k largest elements will be the kth-largest element

    # Note: Hoare and Lomuto are partitioning schemes. Lomuto is simpler to understand and implement, but Hoare performs better in the worst degenerate cases. Hoare also uses only 1/3th the number of swaps that Lomuto uses.
    def partitionLomuto(self, nums, left, right):
        '''In the lomuto partitioning scheme, we pick the right most element as the pivot.
        We traverse L-R in the array. We try to establish a zone (from left-i) which contains only elements >= pivot.
        For each element, if it is >= pivot, we swap it with the ith element and increment i.

        In this manner, at every nums[j], it is either >= pivot in which case it gets swapped with nums[i]. Or it is < pivot and is left as is.
        Finally the pivot is swapped in with nums[i]. i is now the partition location.
        '''

        pivot = nums[right]
        i = left #i will alsways represent the next location at which a larger number can be swapped into
        for j in xrange(left, right):
            if nums[j] >= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def partitionHoare(self, nums, left, right):
        ''' In this partitioning scheme, we have 2 pointers (l & r). We also pick the first element as the pivot element. 
        If element at left < pivot <= element at right, we swap left and right.
        If element at left >= pivot, it is left as is and left++
        If element at right < pivot, it is left as is and right--
        
        Finally pivot is swapped with nums[r]. We know this is a valid swap since nums[r] definitely >= pivot. If it was < pivot, right-- would have happened
        The loop breaking condition is l crossing r. This happens either if l goes past right. Or right goes past l.
        l increases only if nums[l] >= pivot.
        r decreases only if nums[r] < pivot. 
        In both cases, nums[r] >= pivot and hence can be safely swapped with pivot
        '''
        pivot = nums[left]
        l, r = left+1, right
        while l<=r:
            # If left element < pivot & pivot < right element, swap the two ends
            if nums[l] < pivot <= nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                # Can optionally add a l++, r-- here (Although that action is replicated in the below if conditions)
            if nums[l] >= pivot:
                l+=1
            if nums[r] < pivot:
                r-=1
        nums[left], nums[r] = nums[r], nums[left]
        return r

    def findKthLargest(self, nums, k):
        ''' We use the quick-select algorithm to find the k-th largest element in an array.
        We first pick a random pivot element and use it as the pivot. 

        Given a pivot, the partition step divides the array into two portions: elements >= pivot on its left. And elements < pivot on its right (we put the greater elements on the left since we want kth LARGEST in an array)
        If the left partition was k-sized then, the pivot itself was the k-th largest element.
        If left partition < k, then we look between partition location and end of array. 
        If left partition > k, we look between left and partition location. 

        At each juncture, we pick one of the halves of the array and partition it. Each partitioning takes O(x) time if there are x elements. 
        '''
        left, right = 0, len(nums)-1

        while True:
            loc = self.partitionHoare(nums, left, right) #Find location of the partition
            # loc = self.partitionLomuto(nums, left, right)
            if loc == k-1: #If the location was at (k-1), then nums[loc] will be the k-th largest in the array
                return nums[loc]
            elif loc < k-1: #If partition location was before k, we try to partition the remaining part of the array (from loc+1..right)
                left = loc+1
            else: #if partition location was after k, we try to partition left..loc-1
                right = loc-1

s = Solution()
print s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print s.findKthLargest([99, 99], 1)
