#https://leetcode.com/problems/nested-list-weight-sum/
'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Inp: [[1,1],2,[1,1]]
    Out: 10 (four 1's at depth 2, one 2 at depth 1)
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

import collections
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        '''We perform a level order traversal of all elements of the NestedInteger list.
        We first add all the elements of the list to the queue. We then add all NestedIntegers which hold
        just a single integer to the total (weighted by level). 
        If the nestedInteger at any level holds a list, we add the list to the queue for processing at later levels.
        '''
        ni_queue = collections.deque()
        # Adding all elements of input nestedList to the queue
        ni_queue.extend(nestedList)

        level, total = 1, 0
        while ni_queue:
            # length represents the number of elements at the particular level
            length = len(ni_queue) 
            for i in xrange(length):
                ni = ni_queue.popleft()
                # If a NestedInteger contains just an integer, add it to the total weighted by level
                if ni.isInteger():
                    total += ni.getInteger()*level
                else:
                    ni_queue.extend(ni.getList())
            level += 1
        return total
