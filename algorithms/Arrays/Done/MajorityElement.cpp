//http://www.geeksforgeeks.org/majority-element/
//
// Given a stream of N numbers, check if there's a majority element. A majority element is defined as an element that appears more than N/2 times in the set
// Time Complexity = O(n)
// Space Complexity = O(n)

#include<iostream>
using namespace std;
int main()
{
    int N;

    cin>>N;
    int i, no, k, maj, ans, count, arr[100];

    cin>>no;
    maj=no;
    count=1;

    for(i=1;i<N;i++){
        cin>>arr[i];
        no=arr[i];
        if(count==0){
            maj=no;
            count=1;
        }
        else{
            if(no==maj)
                count++;
            else{
                count--;
            }
        }
    }
    cout<<maj<<" could be a majority element"<<endl;
    count=0;

    for(i=0;i<N;i++)
        if(arr[i]==maj)
            count++;
    if(count>N/2)
        cout<<maj<<" IS the majority elemnt.";

    
    return 0;
}

