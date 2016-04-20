//http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
//
//While O(logn) sort is easy in a sorted array, think of a sorted pivoted array : 3 4 5 1 2
//Now try to find a given number in O(logn) with O(1) space
//

#include<stdio.h>
int search(int *array, int left, int right, int target);
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
    int target;
    scanf("%d", &target);
    left = 0;
    right = N;
    int res = search(arr, left, right, target);
    if(res>0)
        printf("%d found at position %d\n", target, res);
    else
        printf("NOT FOUND!\n");
  
    return 0;
}
int search(int *arr, int left, int right, int target){
    if(left > right)
        return -1;
    int mid = (left+right)/2;
    if(arr[mid]==target)
        return mid;
    if(arr[left] < arr[mid]) { //Left subarray is sorted
        if(target > arr[left] && target < arr[mid])
            return search(arr, left, mid-1, target);
        return search(arr, mid+1, right, target);
    }
    
}

