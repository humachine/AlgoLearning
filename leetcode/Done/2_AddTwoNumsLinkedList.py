#https://leetcode.com/problems/add-two-numbers/
"""Test cases:
    Inp: 2->4->3 & 5->6->4     
    Out: 7->0->8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:  return l2
        if not l2:  return l1
        #Create fake head
        temphead = ListNode(-1)
        head = temphead
        carry = 0

        while l1 or l2 or carry:
            Sum = carry
            if l1:
                Sum+=l1.val
                l1=l1.next
            if l2:
                Sum+=l2.val
                l2 = l2.next
            carry = Sum/10
            head.next = ListNode(Sum%10)
            head = head.next

        return temphead.next

h1 = ListNode(2)
h1.next = ListNode(4)
h1.next.next = ListNode(3)

h2 = ListNode(5)
h2.next = ListNode(6)
h2.next.next = ListNode(4)

s = Solution()
ans = s.addTwoNumbers(h1, h2)
while ans:
    print ans.val
    ans = ans.next
