#https://leetcode.com/problems/linked-list-random-node/
'''Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
'''
import random
class Solution(object):
    def __init__(self, head):
        self.head = head
        
    def getRandom(self):
        # Here we perform reservoir sampling on the nodes of the linked list
        head = self.head
        node = None
        # count represents the number of nodes seen thus far in the linked list.
        count = 0
        while head:
            # randrange(n) gives values from 0...n-1 (both inclusive)
            # when randrange(count+1) is count, then we change the value of the 
            # selected random node.
            count += 1
            if random.randrange(count) == 0:
                node = head
            head = head.next
        # The final value of the final random node is returned.
        return node.val
