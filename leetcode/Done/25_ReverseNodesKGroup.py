#https://leetcode.com/problems/reverse-nodes-in-k-groupx/
''' Given a set of nodes, reverse them in groups of k.
If k does not divide the number of nodes, then the remainder nodes at the end of the list are left unreversed.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def _reverseSegment(self, prev, end):
        ''' This is the function that reverses a sequence of nodes preving AFTER prev and ending BEFORE end.'''
        pprev = prev
        prev, curr = prev.next, prev.next.next
        while curr and curr!=end:
            # We perform the reversal such:
            # curr.next is stored in a temp variable. 
            # curr.next is now reassigned to previous
            # curr now becomes previous and temp becomes current
            # This can be written as below in a single line because python Tuple assignements are performed after evaluating all the RHS elements before assignements. Also, the tuple assignements are performed variable by variable L-R
            # This means, curr.next is first assigned to prev, curr to the already evaluated value of curr.next (not prev) and prev to the already evaluated value of curr (not curr.next)
            curr.next, curr, prev = prev, curr.next, curr
        # node = pprev
        # while node!=end:
            # print node.val
            # node = node.next
        print 'attaching', pprev.next.val, '->', end.val
        next_start = pprev.next
        pprev.next.next = end
        print 'attaching', pprev.val, '->', prev.val
        pprev.next = prev
        node = pprev
        while node:
            print node.val, '->',
            node = node.next
        print
        print next_start.val, next_start.next.val

        # nextStart denotes the location after which the NEXT k-group begins
        # nextStart, nextStart.next, prev.next = prev.next, end, prev
        return next_start


    def reverseKGroup(self, head, k):
        ''' In this problem, we need to take a linked list of nodes and reverse them in groups of K each. 
        This is performed in a 3-step process:
        i) Find the next k-group to reverse
        ii) Reverse the nodes of the k-group (if any)
        iii) Attach the reversed k-group back into the original linked list appropriately.
        '''
        temphead = ListNode(-1)
        temphead.next = head

        prev = temphead
        curr = prev.next
        while curr:
            for i in xrange(k):
                if not curr:
                    #If there are less than K nodes in the current group, break and return
                    return temphead.next
                curr = curr.next
    
            newStart = self._reverseSegment(prev, curr)
            prev, curr = newStart, newStart.next
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
     
