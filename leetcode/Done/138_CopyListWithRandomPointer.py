#https://leetcode.com/problems/copy-list-with-random-pointer/
'''Given a linked list which has a pointer that points to a random node of the list, 
clone the entire linked list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def __str__(self):
        return '{} {}'.format(self.label, None if not self.random else self.random.label)

class Solution(object):
    def copyRandomList(self, head):
        # In this problem, we first insert a clone of each node between a node
        # of the original LL and the next node. 
        # We then traverse this LL (of length 2*N).

        # Each clone's random = it's original node's random's next
        # i.e clone.random = original.random.next
        # i.e original.next.random = original.random.next (assuming that original.random exists)
        # Insert copy nodes between each pair of nodes
        start = head
        while start:
            new_node = RandomListNode(start.label)
            new_node.next = start.next
            start.next = new_node
            start = new_node.next

        # Traverse the list, assigning random pointers (if any)
        start = head
        while start:
            if start.random:
                start.next.random = start.random.next
            start = start.next.next

        # Separate the 2 linkedlists
        temp_head = RandomListNode(-1)
        start, clone_start = head, temp_head
        while start:
            clone_start.next = start.next
            clone_start = clone_start.next

            start.next = start.next.next
            start = start.next
        return temp_head.next

s = Solution()
head = RandomListNode(-1)
head.random = head

clone = s.copyRandomList(head)
print clone
print clone.next
