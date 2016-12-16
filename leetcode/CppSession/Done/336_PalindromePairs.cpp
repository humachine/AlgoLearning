//https://leetcode.com/problems/palindrome-pairs/
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
class Solution{
    void LoadReverseWordMap(vector<string>& words, unordered_map<string, int>& palMap){
        for(int i=0;i<words.size();i++){
            string temp(words[i].rbegin(), words[i].rend());
            palMap[temp] = i+1;
        }
    }
    bool isPalindrome(string s){
        if(s.empty())   return true;
        int i, n=s.size();
        for(int i=0; i<n/2; i++){
            if(s[i] != s[n-i-1])
                return false;
        }
        return true;
    }
    public:
        vector<vector<int>> palindromePairs(vector<string>& words) {
            //Sanitize
            vector<vector<int>> result;
            if(words.empty())
               return result; 
            //Create Reverse Word Dictionary
            unordered_map<string, int> palMap;
            LoadReverseWordMap(words, palMap);

            //For each word in words
            //if words[0...i] is a palindrome, check if words[j...end] has its reverse in palMap
            //if words[i...end] is a palindrome, check if words[0...i] has its reverse in palMap
            int i, j, k;
            string left, right;
            vector<int> v(2, 0);
            for(i=0; i<words.size(); i++){
                for(j=0; j<=words[i].size();j++){
                    left = words[i].substr(0, j);
                    right = words[i].substr(j);
                    if(isPalindrome(left) && palMap[right] > 0 && palMap[right]-1 != i){
                            v[0] = palMap[right]-1;
                            v[1] = i;
                            result.push_back(v);
                    }
                    if(isPalindrome(right) && right.size()>0 && palMap[left] > 0 && palMap[left]-1 != i){
                            v[0] = i;
                            v[1] = palMap[left] - 1;
                            result.push_back(v);
                    }
                }
            }
            return result;
        }
};
int main(){
    //string w[] = {"bat", "tab", "cat"};
    string w[] = {"abcd", "dcba", "lls", "s", "sssll", ""};
    vector<string> words(w, w+6);
    class Solution s;
    vector<vector<int>> answer = s.palindromePairs(words);
    cout<<endl<<endl;
    for(int i=0;i<answer.size();i++)
        cout<<words[answer[i][0]]<<' '<<words[answer[i][1]]<<endl;
}

