#https://leetcode.com/problems/reverse-nodes-in-k-group/
''' Given a set of nodes, reverse them in groups of k.
If k does not divide the number of nodes, then the remainder nodes at the end of the list are left unreversed.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def _reverseSegment(self, start, end):
        ''' This is the function that reverses a sequence of nodes starting AFTER start and ending BEFORE end.'''
        prev, curr = start.next, start.next.next
        while curr and curr!=end:
            # We perform the reversal such:
            # curr.next is stored in a temp variable. 
            # curr.next is now reassigned to previous
            # curr now becomes previous and temp becomes current
            # This can be written as below in a single line because python Tuple assignements are performed after evaluating all the RHS elements before assignements. Also, the tuple assignements are performed variable by variable L-R
            # This means, curr.next is first assigned to prev, curr to the already evaluated value of curr.next (not prev) and prev to the already evaluated value of curr (not curr.next)
            curr.next, curr, prev = prev, curr.next, curr

        # nextStart denotes the location after which the NEXT k-group begins
        nextStart, nextStart.next, start.next = start.next, end, prev
        return nextStart

    def _reverseKGroup(self, prev, k):
        ''' This is a function used to reverse a k-Segment of the linked list.
        Firstly, we start at prev.next and see if there are at least k-1 more nodes in the linked list. 
        If there are not, then we have reached the end of the linked list and hence we just return.
        
        If we have k-nodes, we reverse the k-segment and obtain the last node of the REVERSED sequence.
        That last node becomes the prev(or previous/parent) of the next k-group, if any'''
        fast = prev.next
        for i in xrange(k):
            if not fast:
                return
            fast = fast.next

        newStart = self._reverseSegment(prev, fast)
        self._reverseKGroup(newStart, k)


    def reverseKGroup(self, head, k):
        ''' In this problem, we need to take a linked list of nodes and reverse them in groups of K each. 
        This is performed in a 3-step process:
        i) Find the next k-group to reverse
        ii) Reverse the nodes of the k-group (if any)
        iii) Attach the revrsed k-group back into the original linked list appropriately.
        '''
        if not head or k==1:    return head
        temphead = ListNode(-1)
        temphead.next = head
        self._reverseKGroup(temphead, k)
        return temphead.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
s = Solution()
res = s.reverseKGroup(head, 3)
while res:
    print res.val, '->',
    res = res.next
