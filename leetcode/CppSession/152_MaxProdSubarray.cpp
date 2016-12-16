//https://leetcode.com/problems/maximum-product-subarray/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(nums.empty())
            return 0;

        int i=0, answer;
        int currProd, negProd;
        //currProd = 1; negProd = -1;

        int maxSeen = 1;
        for(i=0;i<nums.size();i++){
            if(nums[i]>0){
            }
            else if(nums[i] < 0){
            }
            else{
            }
        }
        return maxSeen;
        /*
         *
         * If number is +ve, ans = num*maxSum(rest) || maxSum(rest)
         * If num is -ve, ans=num*negSum(rest) || maxSum(rest)
         * */
    }
};
int main(){
    class Solution s;
    int arr[] = {2, 3, -2, 4};
    vector<int> v(arr, arr+4);
    cout<<s.maxProduct(v);
    return 0;
}

