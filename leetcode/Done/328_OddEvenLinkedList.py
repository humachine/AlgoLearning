#https://leetcode.com/problems/odd-even-linked-list/
'''Given a singly linked list, group all odd nodes together followed by the even nodes. (odd even in node number and not value of node)
    
    Inp: 1->2->3->4->5->NULL
    Out: 1->3->5->2->4->NULL

    Inp: 1->2->3->4->5->6->7->8->9->NULL
    Out: 1->3->5->7->9->2->4->6->8->NULL
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import LLLib
class Solution(object):
    def oddEvenList(self, head):
        # We build two separate lists - one each for odd & even numbered nodes
        oddDummy, evenDummy = ListNode(-1), ListNode(-1)
        odd, even = oddDummy, evenDummy
        while head: 
            odd.next = head #The first node goes to the odd list
            even.next = head.next #The next node goes to the even list (or could be none, if we have exhausted the entire list)

            odd, even = odd.next, even.next #We push odd & even pointers forward
            head = head.next.next if head.next else None #If head.next exists, head is the node after that

        # Finally, we append the even list at the end of the odd list
        odd.next = evenDummy.next
        return oddDummy.next
s = Solution()
ll = LLLib.LinkedList()
ll.buildList(range(1,10))
ll.printLL()

res = s.oddEvenList(ll.getHead())
ll.assignHead(res)
ll.printLL()
