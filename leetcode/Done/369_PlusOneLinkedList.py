#https://leetcode.com/problems/plus-one-linked-list/
'''Given a linked list representing digits of a number, add one to the number.


Inp: 1->2->3
Out: 1->2->4
'''
class Solution(object):
    def plusOne(self, head):
        start = None
        node = head
        # start denotes the last/least significant non-nine node
        # All nodes start and onwards need to be incremented by one.
        while node:
            if node.val != 9:
                start = node
            node = node.next

        # If at least one non-nine node exists
        if start:
            # Increment non-nine node by 1
            start.val += 1
            start = start.next
            # Update all nodes to the right with 0
            while start:
                start.val = 0
                start = start.next
        # If no non-nine node exists, then add a 1 before the head
        # Update all nodes of the LL to 0
        else:
            temphead = ListNode(1)
            temphead.next = node = head
            while node:
                node.val = 0
                node = node.next
            head = temphead
        return head
