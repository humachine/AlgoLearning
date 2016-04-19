//http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
//
//While O(logn) sort is easy in a sorted array, think of a sorted pivoted array : 3 4 5 1 2
//Now try to find a given number in O(logn) with O(1) space
//

#include<stdio.h>

int binarySearch(int left, int right, int target)
{
    return left;
}

int main()
{
    int arr[100];
    int i, j, k, N;
    int ans;
    int left, right, mid;

    scanf("%d", &N);
    for(i=0;i<N;i++){
        scanf("%d", &arr[i]);
    }
    mid = N/2;
    left=0;
    right=N;

    while(1){
        mid=(left+right)/2;
        if(mid==right)
            break;
        if(mid==left)
            break;
        if(arr[mid]>arr[right]){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    printf("%d is the pivot position", mid);
    
  
//Find the pivot point
//Do binary search on either side of the pivot


    return 0;
}
