#https://leetcode.com/problems/merge-k-sorted-lists/
'''
Given k sorted linked lists, merge and sort them all 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        heap = []
        for i in xrange(len(lists)):
            if lists[i]:
                heappush(heap, lists[i])
        print [x.val for x in heap]

        temphhead = ListNode(-1)
        head = temphhead
        while heap:
            lis = heappop(heap)
            if lis.next:
                heappush(heap, lis.next)
            head.next = lis
            head = head.next
        return temphhead.next

s = Solution()
lists = [ListNode(0), ListNode(1), ListNode(-3)]
head = s.mergeKLists(lists)
while head:
    print head.val
    head = head.next
