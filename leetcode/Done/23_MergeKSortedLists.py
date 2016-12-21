#https://leetcode.com/problems/merge-k-sorted-lists/
'''
Given k sorted linked lists, merge and sort them all 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop, heapify, heapreplace
class Solution(object):
    def mergeKLists(self, lists):
        """
        Put heads of all non-NULL nodes of the k nodes into a min-heap.
        Keep extracting min. Once min is extracted, push minList.next into the heap
        """
        if not lists:
            return []
        heap = [(x.val, x) for x in lists if x]
        heapify(heap)


        temphhead = ListNode(-1)
        head = temphhead

        while heap:
            '''Here we pop the min element every time and we often push minList.next back into the heap. Popping the min takes O(logN) time to keep the next min ready. Pushing minList.next will need another O(logN) to keep the heap again ready. 
            To avoid this extra overhead, we pop only when minList.next = NULL
            '''
            # val, lis = heappop(heap)
            # if lis.next:
                # heappush(heap, (lis.next.val, lis.next))
            val, lis = heap[0]
            if not lis.next:
                heappop(heap)
            else:
                heapreplace(h, (lis.next.val, lis.next))
            head.next = lis
            head = head.next
        return temphhead.next

s = Solution()
lists = [ListNode(0), ListNode(1), ListNode(-3)]
head = s.mergeKLists(lists)
while head:
    print head.val
    head = head.next
