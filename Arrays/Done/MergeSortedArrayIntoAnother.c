//http://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/
//
//Given two sorted arrays of size m+n and n. The larger array has m elements in it and n vacant spaces at positions arr[m+1..m+n]
//Merge the two arrays into one array of size m+n
//
//Time Complexity = O(m+n)
//Space Complexity = O(1)
//
//Note: If move all numbers to either end is an expensive operation, you could first have a step in moveToEnd() which decides which end you want to move the numbers to and then moves it to the side that would require least number of movements

#include<stdio.h>

#define NA -1
void moveToEnd(int *arr, int);
void merge(int *arr1, int *arr2, int m, int n);
int main(){
    int mPlusN[] = {2, 8, NA, NA, NA, 13, NA, 15, 20};
    int N[] = {5, 7, 9, 25};
    int n = sizeof(N)/sizeof(N[0]);
    int m = sizeof(mPlusN)/sizeof(mPlusN[0]) - n;

    moveToEnd(mPlusN, m+n);
    merge(mPlusN, N, m, n);
    int i;
    for(i=0;i<m+n;i++)
        printf("%d\n", mPlusN[i]);
    return 0;
}

void moveToEnd(int *arr, int len){
    //If movement of elements is an operation way more expensive than reading, then move elements to the side which has the larger sequence of contiguous elements at either end
    //Eg: [1, 3, 5, NA, ... . .. , NA, 13, 14, 15, 17] Move all elements to the right since you have 4 elements lesser to move. In the other case, you have 3 elements(1, 3 & 5) lesser to move

    int i, num, pos=len-1;

    int nextInsertPos=len-1;
    for(i=len-1;i>=0;i--){
        if(arr[i]!=NA){
            if(i==nextInsertPos)
                nextInsertPos--;
            else
                arr[nextInsertPos--]=arr[i];
        }
    }
}

void merge(int *arr1, int *arr2, int m, int n){
    int i, j;
    int k=0;
    i=j=0;

    while(i<m && j<n){
        if(arr1[n+i] <= arr2[j]){
            arr1[k++]=arr1[n+i];
            i++;
        }
        else{
            arr1[k++]=arr2[j++];
        }
    }

    while(j<n)
        arr1[k++]=arr2[j++];
}

