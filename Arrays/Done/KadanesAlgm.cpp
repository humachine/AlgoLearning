//http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
//
//Find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum. 
//
//Time Complexity = O(n)
//Space Complexity = O(1)

#include<iostream>
#include<limits.h>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int i, j, k, sum, ans, arr[1000];
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
        int maxsofar, maxtillhere;
        maxsofar = maxtillhere = 0;
        for(i=0;i<N;i++){
            maxtillhere = maxtillhere + arr[i];
            if(maxtillhere < 0)
                maxtillhere = 0;
            if(maxsofar < maxtillhere)
                maxsofar = maxtillhere;
        }
        cout<<maxsofar<<endl;
    }

    return 0;
}


