#https://leetcode.com/problems/min-stack/
'''Implement a stack which also stores the minimum value of the stack elements
at all times.
'''
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        
    def push(self, x):
        # If the element being pushed <= existing minimum, add a copy of the existing
        # minimum to the top of the stack. Then, push the new element on to
        # the stack.
        if x <= self.minimum:
            self.stack.append(self.minimum)
            self.minimum = x
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        # if not self.stack:
            # raise Exception("No elements in stack")
        # If we popped the min-element, then we update the current min, by popping
        # the next element
        if self.stack.pop() == self.minimum:
            self.minimum = self.stack.pop()
        
    def top(self):
        # if not self.stack:
            # raise Exception("No elements in stack")
        return self.stack[-1]
        
    def getMin(self):
        return self.minimum
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
