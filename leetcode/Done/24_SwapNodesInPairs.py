#https://leetcode.com/problems/swap-nodes-in-pairs/
'''Given a linked list, swap nodes of the LL in pairs.

Inp: 1->2->3->4->5
Out: 2->1->4->3->5
'''

import LLLib
class Solution(object):
    def swapPairs(self, head):
        temphead = ListNode(-1)
        temphead.next = head

        start = temphead
        # Start always represents the node 2
        while start.next and start.next.next:
            # Store the first node of the pair
            temp = start.next

            # Alter the connections for the next and the next.next nodes
            start.next = start.next.next
            temp.next = start.next.next
            start.next.next = temp

            # Finally, move the start pointer to the end of the current pair
            start = temp
        return temphead.next

s = LLLib.LinkedList(li=range(1, 6))
ss = Solution()
newL = LLLib.LinkedList(ss.swapPairs(s.getHead()))
newL.printLL()
