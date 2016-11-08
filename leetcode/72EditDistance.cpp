#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
    int EditDistance(string word1, int x, string word2, int y){
        if(x==0)
            return y;
        if(y==0)
            return x;
        if(word1[x] == word2[y])
            return EditDistance(word1, x-1, word2, y-1);
        //Insert, Delete, Replace
        return 1 + min(EditDistance(word1, x-1, word2, y-1), //Replace
                min(EditDistance(word1, x-1, word2, y), EditDistance(word1, x, word2, y-1)));
    }
public:
    int minDistance(string word1, string word2) {
        //if(word1.empty())
            //return word2.size();
        //if(word2.empty())
            //return word1.size()
        return EditDistance(word1, word1.size()-1, word2, word2.size()-1);
    }
}
int main(){
    class Solution s;
    cout<<s.minDistance("abc", "abdc")<<endl;
    cout<<s.minDistance("abxc", "abdc")<<endl;
}
