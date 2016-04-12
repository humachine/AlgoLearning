//http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
//
//Find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum. 

#include<iostream>
#include<limits.h>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int i, j, k, sum, ans;
    int max;
    cin>>max;
    int allneg=1;

    for(i=1;i<N;i++){
        cin>>arr[i];
        if(arr[i]>max)
            max=arr[i];
        if(arr[i]>0)
            allneg=0;
    }

    if(allneg)
        cout<<max<<endl;
    else{
        ans=arr[0];
        for(i=1;i<N;i++){
            if(arr[i]>
        }
    }
    return 0;
}


