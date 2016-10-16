//http://www.geeksforgeeks.org/majority-element/
//Given an array of numbers, print the majority element. Any element which appears more than N/2 times is a majority element
//
//Input: Array of elements
//Output: Majority Element
//
//Time Complexity = O(n) + STREAMING
//Space Complexity = O(1)

#include<iostream>

using namespace std;

int main()
{
    int i, j, k;
    int ii, jj, kk;
    int T, N, result, temp, maj;

    cin>>T;

    for(ii=0; ii<T; ii++){
        int score=0;
        cin>>N;

        for(jj=0; jj<N; jj++){
            cin>>temp;
            if(score==0){
                maj=temp;
                score++;
            }
            else{
                if(temp==maj)
                    score++;
                else
                    score--;
            }
        }
        cout<<maj<<endl;
    }

    return 0;

}
