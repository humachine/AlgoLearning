#https://leetcode.com/problems/flatten-nested-list-iterator/
'''
Given a list of lists, design an iterator that implements a next() and hasNext() function

    Inp: [[1,1],2,[1,1]]
    Out: [1, 1, 2, 1, 1]

    Inp: [1,[4,[6]]]
    Out: [1, 4, 6]
'''
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
class NestedIterator(object):
    def __init__(self, nestedList):
        """ Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        We initialize the data structure with a list (masquerading as stack).
        The list is filled with a single nestedList and a location. 

        This question is exactly similar to the manner in which the Flatten Lists Iterator is done.
        In that question, the hasNext() moves the pointers to the next available position. 
        The next() just returns the number at that location. Once it returns the next number, it perturbs the locations so that the next call of hasNext() moves the pointers back to another appropriate position.
        """
        self.st = [[nestedList, 0]] #Note: We use a list rather than a tuple since we want to make changes to the position attribute (li[1])

        
    def next(self):
        ''' In case the appropriate nestedLists haven't been discovered, we call the self.hasNext() just to make sure that we are at appropriate nestedInteger'''
        if self.hasNext():
            li, pos = self.st[-1] #Returning the nested integer that hasNext finds as the next appropriate
            self.st[-1][1] += 1  #perturbing the positions so that hasNext knows to move the pointers forward again.
            return li[pos].getInteger()
        raise Exception('No more Elements in NestedList')

    def hasNext(self):
        st = self.st
        while st: #If nothing on stack, return False
            li, pos = st[-1]
            # If end of current nestedList has been reached, pop it out of stack.
            if pos == len(li):
                st.pop()
                continue
            # If current nestedInteger is an integer, then return True (since we have arrived at the appropriate position)
            if li[pos].isInteger():
                return True
            nesList = li[pos].getList() 
            st[-1][1] += 1 #Forwarding the position pointers of the current list level. 
            st.append([nesList, 0]) #Adding the current list onto the stack

        return False
        
