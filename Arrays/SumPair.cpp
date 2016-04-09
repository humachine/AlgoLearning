//http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/

// Given an array of numbers. Find any two numbers that sum up to a given value
// Input : N followed by N numbers; X
// Output: A & B if A+B=X and A, B both belong to the array


#include<iostream>
#include<map>
#include<unordered_map>

using namespace std;
int main()
{
    int n;
    cin>>n;

    int i, x;
    int arr[1000];
    for(i=0;i<n;i++)
        cin>>arr[i];
    cin>>x;

    unordered_map<int, int> hashtable;
    for(i=0;i<n;i++){
        hashtable.emplace(arr[i], x-arr[i]);
        if(hashtable.find(x-arr[i])!=hashtable.end())
            cout<<"Found "<<arr[i]<<" and "<<x-arr[i]<<endl;
    }

 
    return 0;
}
