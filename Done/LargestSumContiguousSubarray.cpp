//http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#include <iostream>
using namespace std;
int main(){
    int arr[] = {4, -3, -2, 8, 7, -11, 4, 9, -3, 1};
    int len = sizeof(arr)/sizeof(arr[0]);

    int i, j, k, ans;

    int bestsofar=0;
    int currsofar=0;

    for(i=0;i<len;i++){
        if(currsofar + arr[i] > bestsofar)
            bestsofar = currsofar + arr[i];

        if(currsofar + arr[i] < 0)
            currsofar = 0;
        else
            currsofar = currsofar + arr[i];
    }
    cout<<bestsofar<<endl;

    return 0;
}
