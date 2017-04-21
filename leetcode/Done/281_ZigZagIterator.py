#https://leetcode.com/problems/zigzag-iterator/
'''Given k 1-D vectors, write an iterator that will return elements of the vectors
cyclically.

Inp: [1, 2], [3, 4, 5, 6]
Out: [1, 3, 2, 4, 5, 6]

Inp: [1, 2, 3], [4, 5, 6, 7], [8, 9]
Out: [1, 4, 8, 2, 5, 9, 3, 6, 7]
'''
import collections
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        # We put the first elements of both (or all) vectors into a queue.
        self.queue = collections.deque()
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))
        
    def next(self):
        if not self.hasNext():
            raise Exception('No more elements')
        # We pop the next element out of the queue. Meanwhile we also add the
        # next element from that vector (if it exists) to the end of the queue.
        li, pos = self.queue.popleft()
        if pos+1 < len(li):
            self.queue.append((li, pos+1))
        return li[pos]
        
    def hasNext(self):
        return len(self.queue)>0
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
