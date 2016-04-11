//http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
//Given a set of N numbers, Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times.

#include<iostream>
using namespace std;
int main()
{
    int i, j, k, N;
    cin>>N;

    int res;
    cin>>res;
    for(i=1;i<N;i++){
        cin>>j;
        res=res^j;
    }
    cout<<res;

    return 0;

}
