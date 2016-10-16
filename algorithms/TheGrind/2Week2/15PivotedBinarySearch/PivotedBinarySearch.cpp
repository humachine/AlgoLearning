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
    int len = vec.size();
    int left = 0;
    int right = len-1;

    int mid = (left+right)/2;
    while(left <= right){
        mid = (left+right)/2;
        if(vec[mid] == x)
            return mid;
        //If left half is sorted
        if (vec[left] <= vec[mid]){
            if(vec[left] <= x && x < vec[mid]){
                right = mid-1;
                continue;
            }
            left=mid+1;
            continue;
        }
        if (vec[mid] < x && x <= vec[right]){
            left = mid+1;
            continue;
        }
        right = mid-1;
        continue;
    }
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
        vec.clear();
    }

    return 0;
}
