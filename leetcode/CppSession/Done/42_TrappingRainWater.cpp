//https://leetcode.com/problems/trapping-rain-water/
#include<iostream>
#include<unordered_map>
#include<vector>
#include<algorithm>
using namespace std;
void DrawTowers(vector<int>& inp){
    int peak = *max_element(inp.begin(), inp.end());
    for(int i=0; i<peak; i++){
        string line(inp.size(), ' ');
        for(int j=0; j<inp.size(); j++){
            if(i+inp[j] >= peak)
                line[j] = '+';
        }
        cout<<line<<endl;
    }
    for(int i=0;i<inp.size();i++)
        cout<<inp[i];
    cout<<endl;
}
int CollectWater(vector<int>& inp){
    if(inp.size() <= 2) return 0;
    int n = inp.size();
    int right, left, answer=0;
    right = n-1;

    int right_wall = inp[right--];
    int left_wall = inp[0];
    left = 1;
    while(left <= right){ 
        if(inp[left] > left_wall)
            left_wall = inp[left++];
        else if(inp[right] > right_wall)
            right_wall = inp[right--];
        else{
            if(left_wall <= right_wall)
                answer += left_wall - inp[left++];
            else
                answer += right_wall - inp[right--];
        }
    }
    return answer;
}
int main(){
    //int arr[] = {8, 3, 5, 2, 2, 2, 8, 5, 5, 7, 9, 7};
    int arr[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    vector<int> inp(arr, arr+sizeof(arr)/sizeof(arr[0]));
    DrawTowers(inp);
    cout<<CollectWater(inp)<<endl;
    return 0;
}
