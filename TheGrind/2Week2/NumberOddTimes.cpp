//http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
//
//Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times.
//
//Input: Array of Numbers
//Output: Number that occurs odd number of times
//
//Time Complexity = O(n) + STREAMING
//Space Complexity = O(1)

#include <iostream>
#include <vector>

using namespace std;

int FindOddNumber(vector<int> vec);
int main()
{
    int T;
    cin>>T;
    
    int ii, jj, kk;
    int i, j, k, ans, temp;
    int N;

    vector<int> vec;

    for(ii=0;ii<T;ii++){
        cin>>N;
        for(jj=0;jj<N;jj++){
            cin>>temp;
            vec.push_back(temp);
        }
        int result=FindOddNumber(vec);
        cout<<result;
    }
    return 0;
}
