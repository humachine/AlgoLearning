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
    int mid;
    mid=(left+right)/2;
    if(arr[mid]==target)
        return mid;

    if(arr[left] <= arr[mid]){ //Left half of the array is sorted. Pivot point is in the right half
        if(arr[left]<=target && target<=arr[mid])
            return search(arr, left, mid-1, target);
        return search(arr, mid+1, right, target);
    }
    //If left half of the array has the pivot point, then the right half of the array is sorted
    if(arr[mid]<=target && target<=arr[right])
        return search(arr, mid+1, right, target);
    return search(arr, left, mid-1, target);
}

