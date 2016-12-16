//https://leetcode.com/problems/two-sum/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> qn = nums;
            sort(qn.begin(), qn.end());

            vector<int> answer;
            int i, j;

            for(i=0;i<qn.size();i++){
                //If such a pair exists
                if(binary_search(qn.begin()+i, qn.end(), target-qn[i])){
                    for(j=0; j<nums.size();j++){
                        if(nums[j]==qn[i]){
                            answer.push_back(j);
                            break;
                        }
                    }
                    for(j=0;j<nums.size();j++){
                        if(nums[j]==target-qn[i] && j!=answer[0]){
                            answer.push_back(j);
                            break;
                        }
                    }
                    break;
                }
            }
            return answer;
        }

};
int main(){
    class Solution s;
    int nos[] = {2, 7, 11, -3};
    vector<int> qn(nos, nos+sizeof(nos)/sizeof(nos[0]));
    vector<int> answer = s.twoSum(qn, 8);

    cout<<answer[0]<<' '<<answer[1]<<endl;
    return 0;
}
