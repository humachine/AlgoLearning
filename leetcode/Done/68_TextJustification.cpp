//https://leetcode.com/problems/text-justification/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
        string JustifyLine(vector<string>& words, const int maxWidth, int start, int num_words){
            string answer(maxWidth, ' ');

            //Calculate number of characters in line
            int i=0, j, num_gaps, num_chars, num_spaces;
            num_gaps = (num_words==1) ? 1: num_words-1;
            num_chars = 0;
            for(j=start;j<start+num_words;j++){
                num_chars += words[j].size();
            }
            //Calculate number of spaces for this line
            num_spaces = maxWidth - num_chars;
            num_spaces -= num_gaps;

            //Paste strings into line
            int pos = 0;
            pos = putStringIntoVector(answer, words[start], pos);
            for(j=start+1;j<start+num_words;j++, num_gaps--){
                pos+= ceil(float(num_spaces)/num_gaps) + 1;
                num_spaces -= ceil(float(num_spaces)/num_gaps);
                pos = putStringIntoVector(answer, words[j], pos);
            }
            return answer;
        }
        int putStringIntoVector(string& line, string s, int pos){
            int i, j;
            for(i=pos, j=0;j<s.size();i++, j++)
                line[i] = s[j];
            return i;
        }
    public:
        vector<string> fullJustify(vector<string>& words, const int maxWidth) {
            vector<string> answer;
            if(words.empty()){
                answer.push_back("");
                return answer;
            }
            int i, curr_count, start, num_words;
            for(i=0; i<words.size();){
                curr_count = words[i].size();
                start = i++, num_words = 1;

                while(i<words.size() && curr_count+words[i].size()+1 <= maxWidth){
                    curr_count+=words[i++].size() + 1;
                    num_words++;
                }
                if(i < words.size() ){
                    answer.push_back(JustifyLine(words, maxWidth, start, num_words));
                }
                else{
                    string line(maxWidth, ' ');
                    int pos = putStringIntoVector(line, words[start], 0);
                    for(int j=start+1;j<words.size();j++){
                        pos++;
                        pos = putStringIntoVector(line, words[j], pos);
                    }
                    answer.push_back(line);
                }
            }
            return answer;
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
