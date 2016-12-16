#https://leetcode.com/problems/delete-node-in-a-linked-list/
"""Test cases
    Inp: 1->2->3->4, 3
    Out: 1->2->4 (deleting 3)
"""
class Solution(object):
    def deleteNode(self, node):
        if not node:    
            return
        if not node.next:
            node = None
            return

        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        del node
