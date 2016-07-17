//http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
//
//Given an rotated sorted array, search for an element in this array
//
//Input : Array of numbers. 
//Output : Location of number or -1
//
//Time Complexity = O(logN)
//Space Complexity = O(1) extra space

#include <iostream>
#include <vector>
using namespace std;

int pivotedBinarySearch(vector<int> vec, int x){
    return -1;
}
int main(){
    int T, N, ii, jj;
    int i, j, k, temp, x;

    cin>>T;

    vector<int> vec;
    for(ii=0;ii<T;ii++){
        cin>>N;
        for(jj=0;jj<N;jj++){
            cin>>temp;
            vec.push_back(temp);
        }
        cin>>x;
        cout<<pivotedBinarySearch(vec, x)<<endl;
    }

    return 0;
}
