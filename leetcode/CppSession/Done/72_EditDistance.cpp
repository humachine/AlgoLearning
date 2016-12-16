#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    int minDistance(string word1, string word2) {
        if(word1.empty())
            return word2.size();
        if(word2.empty())
            return word1.size();
        if(word1.size() < word2.size())
            word1.swap(word2);
        vector<int> prev_row(word2.size()+1, 0);
        for(int i=0;i<=word2.size();i++)
            prev_row[i]=i;

        int i=0, prev, row=1, curr, col;
        for(row=1;row<=word1.size();row++){
            prev=row;
            for(col=1;col<=word2.size();col++){
                if(word1[row-1] == word2[col-1])
                    curr = prev_row[col-1];
                else{
                    curr = 1 + min(prev, min(prev_row[col], prev_row[col-1]));
                }
                prev_row[col-1] = prev;
                prev = curr;
            }
            prev_row[col-1] = prev;
        }
        return curr;
    }
};

int main(){
    class Solution s;
    cout<<s.minDistance("sea", "ate")<<endl;
}
