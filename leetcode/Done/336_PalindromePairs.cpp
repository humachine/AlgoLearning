//https://leetcode.com/problems/palindrome-pairs/
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
class Solution{
        void LoadReverseWords(const vector<string>& words, unordered_map<string, int>& pal_map){
            int i=0;
            for(i=0;i<words.size();i++){
                string word(words[i].rbegin(), words[i].rend());
                pal_map.insert(make_pair(word, i));
            }
        }
        bool isPalindrome(string s){
            if(s.empty() || s.size()==1)   return true;
            int i, j;
            for(i=0, j=s.size()-1; i<j;i++, j--){
                if(s[i] != s[j])
                    return false;
            }
            return true;
        }
        void addPalindromes(const vector<string>& words,
                const unordered_map<string, int>& pal_map, vector<vector<int>>& answer){
            int i=0, emptyStrLoc;
            auto it = pal_map.find("");
            emptyStrLoc = it->second;

            for(i=0;i<words.size();i++){
                string word = words[i];
                if(word == "")  continue;
                if(isPalindrome(word)){
                    vector<int> v(2, 0);
                    v[0] = emptyStrLoc; v[1]=i;
                    answer.push_back(v);
                    v[0] = i; v[1]=emptyStrLoc;
                    answer.push_back(v);
                }
            }
        }
    public:
        vector<vector<int>> palindromePairs(vector<string>& words) {
            vector<vector<int>> answer;
            if(words.empty()){
                return answer;
            }
            if(words.size()==1){
                answer.push_back(vector<int>());
                return answer;
            }
            unordered_map<string, int> pal_map;
            LoadReverseWords(words, pal_map);
            
            //For each word
            int i, j, left, mid, right;
            bool has_empty = false;
            vector<int> v(2, 0);
            for(i=0; i<words.size(); i++){
                string word = words[i];
                for(j=0; j<word.size(); j++){
                    string leftw = word.substr(0, j);
                    string rightw = word.substr(j, word.size()-j);
                    if(isPalindrome(leftw) && rightw!=""){
                        auto it = pal_map.find(rightw);
                        if(it!=pal_map.end()){
                            v[0] = it->second;
                            v[1] = i;
                            if(i != it->second)
                                answer.push_back(v);
                        }
                    }
                    if(isPalindrome(rightw) && leftw!=""){
                        auto it = pal_map.find(leftw);
                        if(it!=pal_map.end()){
                            v[0] = i;
                            v[1] = it->second;
                            if(i != it->second)
                                answer.push_back(v);
                        }
                    }
                }
                if(word == "")
                    has_empty = true;
            }
            if(has_empty)
                addPalindromes(words, pal_map, answer);
            return answer;
        }
};
int main(){
    //string w[] = {"bat", "tab", "cat"};
    string w[] = {"abcd", "dcba", "lls", "s", "sssll"};
    vector<string> words(w, w+5);
    class Solution s;
    vector<vector<int>> answer = s.palindromePairs(words);
    for(int i=0;i<answer.size();i++)
        cout<<words[answer[i][0]]<<' '<<words[answer[i][1]]<<endl;
}

