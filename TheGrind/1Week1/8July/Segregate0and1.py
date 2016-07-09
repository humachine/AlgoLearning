#http://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
# Segregate all the 0s to the left and all the 1s to the right in an array in a single pass
# Input : Array of bits
# Output : Array with all zeros on the left and ones on the right
# Time Complexity = O(n)
# Space Complexity = O(1) extra

def Segregate(arr):
    right=len(arr)-1
    left=0

    #Using two variables to swap zeros and ones
    while left < right:
        if arr[left]==1 and arr[right]==0:
            arr[right]=1
            arr[left]=0
            right-=1
            left+=1
        else:
            if arr[left]==0:
                left+=1
            if arr[right]==1:
                right-=1
    print arr
    
T=int(input())
for i in xrange(T):
    N=int(input())
    arr=map(int, input().split())
    Segregate(arr)
