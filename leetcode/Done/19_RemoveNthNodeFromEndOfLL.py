#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
    Inp: 1->2->3->4->5, n=2
    Out: 1->2->3->5

    Inp: 1->2, n=1
    Out: 1

    Inp: 1->2, n=2
    Out: 2
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        We maintain a fast and slow pointer. When the fast hits NULL, we delete the slow pointer. 
        Deleting a node's next node is very straightforward. Deleting the current node requires copying of data which can be avoided if slow pointer is just ONE short of the actual slow pointer.
        """

        if not head or not n:    return head
        temphead = ListNode(-1)
        temphead.next = head
        # To keep slow, ONE slower than actual slow, we initialize it to temphead
        slow, fast = temphead, head
        # We push fast up by N places
        for i in xrange(n):
            fast = fast.next
        
        # Until fast hits end of LL, we keep moving fast and slow along
        while fast:
            slow, fast = slow.next, fast.next

        # We now are required to delete slow.next
        slow.next = slow.next.next
        return temphead.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = s.removeNthFromEnd(head)
while head:
    print head.val
