class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    '''LinkedList class which is a sequential list of ListNodes.'''
    def __init__(self, node=None, li=[]):
        '''Initialize a tree with a node.'''
        # If we have a list, we build a linked list from that list
        if li:
            self.head = self._buildList(li)
        # Alternatively, if we have a node, we initiliaze our list head with node
        else:
            self.head = node

    def _buildList(self, li):
        '''Returns the head of a linked list built from a list of values.'''
        temphead = ListNode(-1)
        head = temphead
        for num in li:
            head.next = ListNode(num)
            head = head.next
        return temphead.next

    def printLL(self, delim='->'):
        '''Prints the nodes of the linked list.'''
        head = self.head
        while head:
            print head.val, delim, 
            head = head.next
        if delim != '\n':
            print

    def getHead(self):
        '''Returns head of the linked list.'''
        return self.head

    def assignHead(self, node):
        '''Sets head of the linked list with a given input node.'''
        self.head = node
