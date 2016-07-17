//http://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/
//
//Given an array of size M+N containing M elements and another array of size N containing N elements, merge the
//two arrays into the array of size M+N in-place
//
//Input: Array1 of size M+N containing M elements & Array2 of size N containing N elements
//Output: Array1 containing all M+N elements
//
//Time Complexity=O(M+N)
//Space Complexity = O(1) extra space

#include<iostream>
using namespace std;
void ArrayMerge(int *arr1, int *arr2, int N, int M){
    int i, j, k, temp;
    i=N-1;
    j=M-1;
    k=M+N-1;

    while(i>=0 && j>=0){
        if(arr1[i] > arr2[j]){
            arr2[k] = arr1[i];
            k--;
            i--;
        }
        else{
            arr2[k] = arr2[j];
            k--;
            j--;
        }
    }
    while(j>=0){
        arr2[k]=arr2[j];
        k--;
        j--;
    }
    while(i>=0){
        arr2[k]=arr1[i];
        k--;
        i--;
    }

    for(i=0;i<N+M;i++)
        cout<<arr2[i]<<' ';
    cout<<endl;
    delete []arr1;
    delete []arr2;

}

int main(){
    int T, M, N;
    int ii, jj, kk;
    cin>>T;

    for(ii=0;ii<T;ii++){
        cin>>N>>M;
        int *arr1 = new int[N];
        int *arr2 = new int[M+N];

        for(jj=0; jj<N; jj++)
            cin>>arr1[jj];
        for(jj=0; jj<M; jj++)
            cin>>arr2[jj];
        ArrayMerge(arr1, arr2, N, M);
    }
}
