#https://leetcode.com/problems/delete-node-in-a-linked-list/
"""Test cases
    Inp: 1->2->3->4,
    Out: 1<-2<-3<-4
"""
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev, head = head, nextNode
        return prev
