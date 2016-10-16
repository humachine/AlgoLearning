#http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#Given an array of numbers find the largest sum contiguous subarray sum
#
# Input : Array of Numbers
# Output : Largest Sum (Optionally start and end points of subarray)
# Time Complexity = O(n)
# Space Complexity = O(1) extra space

T = int(raw_input())

def MaxSumSubarray(arr):
    N = len(arr)
    sum_so_far=arr[0]
    max_so_far=arr[0]
    start=end=0
    currstart=currend=0
    
    for i in xrange(1, N):
        #print i, arr[i], sum_so_far, max_so_far
        m = max(sum_so_far + arr[i], arr[i])
        if sum_so_far < 0:
            if sum_so_far < arr[i]:
                currstart = currend = i
                sum_so_far = arr[i]
        else:
            sum_so_far = sum_so_far + arr[i]
            currend = i

        if sum_so_far > max_so_far:
            start=currstart
            end=currend
            max_so_far = sum_so_far

    return max_so_far, start, end


for _ in xrange(T):
    N=int(raw_input())

    inparray = map(int, raw_input().split())
    ans, start, end = MaxSumSubarray(inparray)
    print ans, start, end

