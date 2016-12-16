//https://leetcode.com/problems/decode-ways/
#include<iostream>
#include<vector>
#include<algorithm>
#include<stdexcept>
using namespace std;
class Solution {
    public:
        int numDecodings(string s) {
            if(s.empty())   return 0;
            if(s.length()==1 && s[0]!='0')
                return 1;
            int n = s.size(), i, temp;
            vector<int> answer(n+2, 0);
            answer[n] = 1;
            answer[n+1] = 0;
            for(i=n-1;i>=0;i--){
                switch(s[i]){
                    case '0':
                        answer[i] = 0;
                        break;
                    case '1':
                        answer[i] = answer[i+1] + answer[i+2];
                        break;
                    case '2':
                        answer[i] = answer[i+1] + ((s[i+1] <= '6') ? answer[i+2] : 0);
                        break;
                    default:
                        answer[i] = answer[i+1];
                }
            }
            return answer[0];
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
    int answer = s.numDecodings("212");
    //cout<<"Solution\n";
    cout<<answer<<endl;
    answer = s.numDecodings("17");
    answer = s.numDecodings("108");
    cout<<answer<<endl;

    return 0;
}
