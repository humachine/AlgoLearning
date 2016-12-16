//https://leetcode.com/problems/3sum/
#include<iostream>
#include<vector>
#include<algorithm>
#include<stdexcept>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> answer;
        if(nums.size() <= 2)    return answer;

        sort(nums.begin(), nums.end());
        int prev = nums[0]-1;
        int i, target, sum;
        int left, right, prev_left, prev_right;
        vector<int> v(3, 0);
        for(i=0;i<nums.size()-1;i++){
            if(nums[i] == prev) continue;


            left = i+1;
            right = nums.size()-1;
            prev_left = nums[0]-1;
            prev_right = nums[nums.size()-1]+1;
            target = -nums[i];
            while(left < right){
                if(nums[left] == prev_left)
                    left++;
                else if(nums[right] == prev_right)
                    right--;
                else{
                    sum = nums[left] + nums[right];
                    if(sum < target){
                        prev_left = nums[left++];
                    }
                    else if(sum > target){
                        prev_right = nums[right--];
                    }
                    else{
                        v[0] = nums[i];
                        v[1] = nums[left];
                        v[2] = nums[right];
                        answer.push_back(v);
                        prev_left = nums[left++];
                        prev_right = nums[right--];

                    }
                }
            }
            prev = nums[i];
        }
        return answer;
    }
};


int main(){
    class Solution s;
    int arr[] = {-1, 0, 1, 2, -1, -4};
    vector<int> inp(arr, arr+6);

    s.threeSum(inp);
    return 0;
}
