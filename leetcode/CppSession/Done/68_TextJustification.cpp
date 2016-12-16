//https://leetcode.com/problems/text-justification/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
    int fillString(string& s1, string s2, int start){
        int i;
        for(i=0; i<s2.size(); i++)
            s1[start+i] = s2[i];
        return start+i;
    }
    string JustifyLine(vector<string>& words, int start, int end, int charCount, int maxWidth){
        int num_gaps = end - start - 1;
        int i, j, extra_spaces, space_count;
        extra_spaces = maxWidth - charCount;
        string result(maxWidth, ' ');
        int pos = fillString(result, words[start], 0);

        for(i=start+1; i<end; i++){
            space_count = (extra_spaces+num_gaps-1) / num_gaps;
            num_gaps--;
            extra_spaces -= space_count;
            pos = fillString(result, words[i], pos+1+space_count);
        }
        return result;
    }
    public:
        vector<string> fullJustify(vector<string>& words, const int maxWidth) {
            vector<string> result;
            if(words.empty() || maxWidth==0)    return result;
            int i, j, curr_chars, temp, k;
            int n = words.size();

            string line;
            vector<char> v;
            for(i=0; i<n; i++){
                curr_chars = words[i].size();
                j=i+1;
                while(j<n && curr_chars+1+words[j].size() <= maxWidth){
                    curr_chars += 1 + words[j++].size();
                }
                if(j==n)
                    line = JustifyLine(words, i, n, maxWidth, maxWidth);
                else
                    line = JustifyLine(words, i, j, curr_chars, maxWidth);
                result.push_back(line);
                i = j-1;
            }
            return result;
        }
};

int main(){
    class Solution s;
    string inp[] = {"This", "is", "an", "example", "of", "text", "justification."};
    vector<string> words(inp, inp+7);
    int L = 16;
    vector<string> ans = s.fullJustify(words, L);
    int i=0;
    for(i=0;i<ans.size();i++)
        cout<<ans[i]<<endl;
    return 0;
}
