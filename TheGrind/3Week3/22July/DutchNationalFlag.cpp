//http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
//
//Given an array of 0s, 1s and 2s, segregate all the 0s to the left and 2s to the right
//
//Input: An Array of 0s, 1s and 2s
//Output: Segregated Array
//
//Time Complexity = 
//Space Complexity =

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void DutchNationalFlag(vector<int> &vec){
    int N=vec.size();

    int low, mid, high;
    low=mid=0;
    high=N-1;

    while(mid<=high){
        if(vec[mid]==1)
            mid++;
        else if(vec[mid]==0){
            if(vec[low]!=vec[mid])
                swap(vec[low], vec[mid]);
            low++, mid++;
        }
        else{
            if(vec[high]!=vec[mid])
                swap(vec[mid], vec[high]);
            high--;
        }
    }
}
int main()
{
    int T;
    cin>>T;

    int i, j, k, N;
    vector<int> vec;

    for(i=0;i<T;i++){
        cin>>N;
        for(j=0;j<N;j++){
            cin>>k;
            vec.push_back(k);
        }
        DutchNationalFlag(vec);
        for(k=0;k<vec.size();k++)
            cout<<vec[k]<<' ';
        cout<<endl;
        vec.clear();
            
    }
    return 0;
}
