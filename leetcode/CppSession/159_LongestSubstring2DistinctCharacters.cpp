//https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#include<iostream>
#include<set>
#include<queue>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
    public:
        int lengthOfLongestSubstringTwoDistinct(string s) {
            if(s.size() <= 2)   return s.size();
            char letters[2];
            int start[2], end[2], currStart;
            start[0]=end[0]=0;
            letters[0] = s[0] = letters[1];
            int maxLen = 0;
            int found = 0;
            for(int i=1; i<s.size(); i++){
                maxLen = max(maxLen, i-min(start[0], start[1])+1);
                if(s[i] == s[currStart])
                    continue;
                else{
                    if(s[i] == letters[0]){
                    }
                    else if(s[i] == letters[1]){
                    }
                    else{

                    }
                }
                
            }
            return maxLen;
        }
};

int main(){
    class Solution s;
    cout<<endl;
    string inp = "abaccc";
    //inp = "eceba";
    cout<<s.lengthOfLongestSubstringTwoDistinct(inp)<<endl;
    return 0;
}
