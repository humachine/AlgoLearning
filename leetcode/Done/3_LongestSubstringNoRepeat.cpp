//https://leetcode.com/problems/longest-substring-without-repeating-characters/
#include<iostream>
#include<unordered_map>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            if(s.size()<=1) return s.size();
            unordered_map<char, int> charLocs;
            int left=0, right, maxLen=0;

            for(right=0;right<s.size();right++){
                if(charLocs[s[right]]>left)
                    left = charLocs[s[right]];
                charLocs[s[right]] = right+1;
                maxLen = max(maxLen, right-left+1);
            }
            return maxLen;
        }
};
int main(){
    class Solution s;
    string inp = "abba";
    cout<<s.lengthOfLongestSubstring(inp);
    return 0;
}
