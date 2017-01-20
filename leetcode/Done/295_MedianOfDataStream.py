#https://leetcode.com/problems/find-median-from-data-stream/
''' Given a stream of integers, return median whenever requested. 

Example:
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2
'''
import heapq
class MedianFinder(object):
    ''' Here, we use two heaps to store the upper and lower halves of the array.
    Every time we see a number, we add it to one of the heaps, depending on which
    half of the array this number would fall in. 
    The lower half of the array is stored as a max-heap and the upper half elements
    of the array are stored as a max-heap.

    Afer every insertion, if the sizes between the 2 heaps are greater than one,
    then we pop the head of the greater sized heap and push it into the other
    heap - thus balancing the sizes.
    '''
    def __init__(self):
        self.bottom_half, self.top_half = [], []
        
    def addNum(self, num):
        # If empty upper half list or number falls into upper half, we add it to the min heap
        if not self.top_half or num >= self.top_half[0]:
            heapq.heappush(self.top_half, num)
            # If the heap sizes get imbalanced, then we pop one element from the larger heap and add it to the smaller heap.
            if len(self.top_half)-len(self.bottom_half) > 1:
                popped_num = heapq.heappop(self.top_half)
                heapq.heappush(self.bottom_half, -popped_num)
        else:
            heapq.heappush(self.bottom_half, -num)
            if len(self.bottom_half)-len(self.top_half) > 1:
                popped_num = heapq.heappop(self.bottom_half)
                heapq.heappush(self.top_half, -popped_num)
        
    def findMedian(self):
        # if not any([self.bottom_half, self.top_half]):
            # raise Exception("No data points")
        bottom_len, top_len = len(self.bottom_half), len(self.top_half)
        # If top_half is greater in size than bottom half (ie. #elements is odd), min of top half should be median
        if top_len > bottom_len:
            return self.top_half[0]
        elif bottom_len > top_len:
            return -self.bottom_half[0]
        # If number of elements are even, then we return average of the 2 heap roots
        return 0.5*(-self.bottom_half[0] + self.top_half[0])
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
