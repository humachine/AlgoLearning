//https://leetcode.com/problems/decode-ways/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
    public:
        int numDecodings(string s) {
            if(s.length()==1 && s[0]!='0')
                return 1;
        }
};
/* Test cases:
 *
 * 7        1
 * 17       2
 * 212      3        2,1,2   21,2    2,12
 * 108      1 
 *
 * */





int main(){
    class Solution s;
    int answer = s.numDecodings("7");
    cout<<answer<<endl;
    answer = s.numDecodings("17");
    cout<<answer<<endl;

    return 0;
}
