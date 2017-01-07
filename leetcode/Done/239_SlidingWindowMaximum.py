#https://leetcode.com/problems/sliding-window-maximum/
'''
Given an array of numbers and a window size, return a list of maximums of the window at each moment.

    Inp:  [1,3,-1,-3,5,3,6,7], k=3
    Out: [3, 3, 5, 5, 6, 7]
'''
from collections import deque
class Solution(object):
    def maxSlidingWindowDeque(self, nums, k):
        ''' In this question, we maintain a double ended queue of size k. 
        We only hold possible max candidates in the deque. If there is an element in the queue and the next element after it is bigger than the element, we remove it from the queue and replace it with the next element (next element is bigger and is bound to figure in the max window for a longer duration)

        We store indices of every element in the queue. If an element is < tail of queue (q[-1]), then we just append it to the queue. (this number could be a future max candidate)
        If new element > tail of queue, keep popping tail of queue, until queue becomes empty or tail of queue element >= new element.

        Head of queue always contains the index of the max element of the current window.
        '''
        if not nums:
            return nums
        q, res = deque(), []
        for i in xrange(len(nums)+1): #We run till len(nums)+1, so that we pop the last maximum after processing the final sliding window.
            if i>=k:
                if q[0] > i-k: #If queue head index within the k-window, just add the queue head value
                    res.append(nums[q[0]])
                else: #If the queue head index falls beyond a k-window of i, remove it from the queue.
                    res.append(nums[q.popleft()])
            while q and i<len(nums) and nums[i] > nums[q[-1]]: # Remove all smaller candidates from the queue
                q.pop()
            q.append(i) #Add element to the window (represents sliding the window by 1)
        return res

    def maxSlidingWindow(self, nums, k):
        ''' In this innovative solution, we run two passes across the array to preprocess window maxes. Then we consolidate in O(n-k) time to get the result we wish.
        We first build the lmax array by dividing the array into non-overlapping windows of size k-each.
        lmax[i] = max to the left in the current k-Window
        rmax[i] = max to the right in the current k-window

        SlidingWindowMax[i] = max(rmax[i], lmax[i+k-1])
        We use rmax[i] since it gives us the value of the highest element in the current static window of k-size. (static windows are the non-overlapping windows that we divide the array into)
        The current sliding window can either be across two static windows or is entirely one static window.
        If it's across 2 static windows, rmax[i] will give us the best from the rest of this static window. And lmax[i+k-1] will give us the best of the first few elements of the next static window.
        If it's just one single window, rmax[i] AND lmax[i+k-1] will both have the max of the current static window, which is exactly what we are looking for.
        '''
        if not nums:    return []
        
        n = len(nums)
        lmax, rmax, res = [0]*n, [0]*n, []
        lmax[0], rmax[-1] = nums[0], nums[-1] #Initializing lmax & rmax
        for i in xrange(1, len(nums)):
            lmax[i] = max(lmax[i-1], nums[i]) if i%k!=0 else nums[i] #lmax = max(prevLMax, currElement) if within same static window else we restart a new window by setting it to currElement
            j = n-i-1
            rmax[j] = max(rmax[j+1], nums[j]) if (j+1)%k!=0 else nums[j] # We perform a similar action for rmax too
        for i in xrange(len(nums)-k+1):
            res.append(max(lmax[i+k-1], rmax[i])) #res[i] = max(rmax[i], lmax[i+k-1])
        return res


s = Solution()
inp = [1, 3, -1, -3, 5, 3, 6, 7]
print s.maxSlidingWindow(inp, 3)
# print s.maxSlidingWindow([7, 2, 4], 2)
