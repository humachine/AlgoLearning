//http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
//
//While O(logn) sort is easy in a sorted array, think of a sorted pivoted array : 3 4 5 1 2
//Now try to find a given number in O(logn) with O(1) space
//

#include<stdio.h>
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
    int mid = N/2;
    return 0;
}
