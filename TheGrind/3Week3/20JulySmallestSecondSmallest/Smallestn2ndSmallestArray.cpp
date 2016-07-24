//http://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
//
//Find the smallest and second smallest element in an array
//
//Input : Array of numbers
//O/P : Smallest & 2nd Smallest Number
//
//Time Complexity = O(n)
//Space Complexity = O(1)

#include <iostream>
using namespace std;

int main(){
    int T, N, i, j, k, inp;
    int min, min2;

    cin>>T;
    // Accept Inputs
    for(i=0;i<T;i++){
        cin>>N;
        // Check for Invalid Case
        if(N==1){
            cin>>inp;
            cout<<"N < 2. Error!";
        }
        else{
            cin>>inp;
            cin>>min2;
            if(min2 < inp){
                min = min2;
                min2 = inp;
            }
            else
                min = inp;

            //Accept more inputs if N>2
            for(j=2;j<N;j++){
                cin>>inp;
                if(inp < min){
                    min2=min;
                    min=inp;
                }
                else if(inp < min2){
                    min2=inp;
                }
            }
        }
        cout<<min<<' '<<min2<<endl;
    }
    
    return 0;
}



