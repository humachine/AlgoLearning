#https://leetcode.com/problems/sliding-window-median/
''' Given a stream of numbers, return the median of all the numbers that are present within a sliding window.

    Inp: [1, 2, 3, 4, 5, 4, 3, 2, 1], k=3
    Out: [2, 3, 4, 4, 4, 3, 2]

    Inp: [1, 3, -1, -3, 5, 3, 6, 7]
    Out: [1, -1, -1,  3, 5, 6]
'''
import collections
from heapq import heappush, heappop, heapify
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        '''Similar to the median stream problem, we maintain 2 heaps which represent
        the top and bottom halves of the window.
        Since deletion from a heap is an O(1) operation, we perform it lazily. 

        At any time, if a number leaves a window, we delete it if it is at the top
        of the heap. Else, we stage it for deletion, but alter the count of this 
        half of the array.

        When this element eventually comes to the top of the heap at a later instance, 
        we perform the staged deletions.
        '''
        to_be_deleted, res = collections.defaultdict(int), []
        top_half, bottom_half = nums[:k], []
        # We first begin by heapifying the first k-window
        heapify(top_half)

        # Balancing the top and bottom halves of the k-window
        while len(top_half) - len(bottom_half) > 1:
            heappush(bottom_half, -heappop(top_half))

        for i in xrange(k, len(nums)+1):
            median = top_half[0] if k%2 else 0.5*(top_half[0]-bottom_half[0])
            res.append(median)
            if i<len(nums):
                num, num_to_be_deleted = nums[i], nums[i-k]
                top_bottom_balance = 0 #top_bottom_balance = len(top_half) - len(bottom_half)

                # If number to be deleted is in the top half, we decrement the top_bottom_balance
                if num_to_be_deleted >= top_half[0]:
                    top_bottom_balance-=1
                    # If the number to be deleted is at the top of the heap, we remove the entry
                    if num_to_be_deleted == top_half[0]:
                        heappop(top_half)
                    # Else, we keep track of this number for later deletion
                    else:
                        to_be_deleted[num_to_be_deleted]+=1
                else:
                    top_bottom_balance+=1
                    if num_to_be_deleted == -bottom_half[0]:
                        heappop(bottom_half)
                    else:
                        to_be_deleted[num_to_be_deleted]+=1

                # If the new number to be inserted falls into the top half, we insert it there and update the top_bottom_balance
                if top_half and num >= top_half[0]:
                    top_bottom_balance+=1
                    heappush(top_half, num)
                else:
                    top_bottom_balance-=1
                    heappush(bottom_half, -num)

                # top_bottom_balance can only be -2, 0 or +2
                # If top_bottom_balance is -2, then we deleted num_to_be_deleted from the top half AND added the new number to the bottom half
                # We hence add the head of the bottom half to the top half to balance both trees
                if top_bottom_balance>0:
                    heappush(bottom_half, -heappop(top_half))
                elif top_bottom_balance<0:
                    heappush(top_half, -heappop(bottom_half))

                # While the head of the top_half has been staged for deletion
                # previously, remove it from the heap
                while top_half and to_be_deleted[top_half[0]]:
                    to_be_deleted[top_half[0]]-=1
                    heappop(top_half)
                while bottom_half and to_be_deleted[-bottom_half[0]]:
                    to_be_deleted[-bottom_half[0]]-=1
                    heappop(bottom_half)
        return map(float, res)
s = Solution()
print s.medianSlidingWindow(range(1, 6)+ range(4, 0, -1), 3)
print s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print s.medianSlidingWindow([33,1,2,3,4,5,6,7,33],2)
print s.medianSlidingWindow([1], 1)
