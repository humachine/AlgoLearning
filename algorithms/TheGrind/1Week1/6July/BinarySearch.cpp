// http://quiz.geeksforgeeks.org/binary-search/
//Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
//Ties are resolved randomly.
//
// Input: Array of N numbers
// Output: -1 if number doesn't exist, position of number if it exists
// Complexity : O(logN)

#include<iostream>
#include<vector>
using namespace std;

//Binary Search Function
int binarySearch(vector<int> vec, int x){
    int right=vec.size();
    int left=0;

    int mid=(left+right)/2;

    while(left <= right){
        mid=(left+right)/2;
        cout<<mid<<vec[mid];

        //If element has been found
        if(vec[mid]==x)
            return mid;
        
        if(vec[mid] < x){
            left=mid+1;
        }
        else
            right=mid-1;
    }
    return -1;
}

//Main Driver Function
int main()
{
    int T, N;
    cin>>T;

    int i, j, k, temp, x;
    int result;

    vector<int> vec;
    for(i=0;i<T;i++){
        cin>>N;

        for(j=0;j<N;j++){
            cin>>temp;
            vec.push_back(temp);
        }
        cin>>x;

        result=binarySearch(vec, x);
        cout<<result<<endl;

        vec.clear();
    }

    return 0;
}
