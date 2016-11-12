//https://leetcode.com/problems/group-shifted-strings/
#include<iostream>
#include<string>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
    string getCode(string inp){
        if(inp.empty()) return "";
        if(inp.size()==1)   return "0";

        vector<char> result;
        char prev, curr;
        prev = inp[0];
        int diff;

        for(int i=1; i<inp.size(); i++){
            diff = (inp[i] - prev + 26) % 26;
            prev = inp[i];
            result.push_back(diff+'A');
        }
        return string(result.begin(), result.end());
    }
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        vector<vector<string>>answer;
        if(strings.empty()) return answer;
        unordered_map<string, int> stringLoc;

        for(int i=0;i<strings.size();i++){
            string code = getCode(strings[i]);
            if(stringLoc[code] == 0){
                cout<<strings[i]<<endl;
                answer.push_back(vector<string>());

                int loc = answer.size()-1;
                stringLoc[code] = loc+1;
                
                answer[loc].push_back(strings[i]);
            }
            else{
                answer[stringLoc[code]-1].push_back(strings[i]);
            }
        }
        return answer;
    }
};
using namespace std;
int main(){
    string a[] = {"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"};
    class Solution s;
    vector<string> inp(a, a+8);
    s.groupStrings(inp);
}
