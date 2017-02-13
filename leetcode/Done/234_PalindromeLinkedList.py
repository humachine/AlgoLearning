#https://leetcode.com/problems/palindrome-linked-list/
'''Given a singly linked list, check if it's a palindrome.

Inp: 1->2->3->2->1
Out: True
'''
class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head
        # Find the midpoint of the linked list using a slow and fast pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If the fast pointer is on the last node, we then have an odd length LL
        start = slow
        if fast:
            start = slow.next

        # Reverse the linked list from the midpoint onwards
        prev = None
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        head1, head2 = prev, head
        is_palindrome = True
        # Traverse through the reversed half and check if it's identical to the first half
        while head1:
            if head1.val!=head2.val:
                is_palindrome = False
                break
            head1, head2 = head1.next, head2.next


        return is_palindrome

from LLLib import LinkedList
s = Solution()
l = LinkedList(li=range(8))
print s.isPalindrome(l.getHead())
l = LinkedList(li=[1, 2, 3, 2, 1])
print s.isPalindrome(l.getHead())
l = LinkedList(li=[1, 2, 3, 3, 2, 1])
print s.isPalindrome(l.getHead())
l = LinkedList(li=[])
print s.isPalindrome(l.getHead())
