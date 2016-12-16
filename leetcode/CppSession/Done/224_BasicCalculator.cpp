//https://leetcode.com/problems/basic-calculator/
#include<iostream>
#include<sstream>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        if(s.empty())   return 0;
        stack<int> num_stack;

        int i, j, answer, curr, temp;
        char c;
        int result = 0, sign=1;
        for(i=0;i<s.size();i++){
            c = s[i];
            if(c == '('){
                num_stack.push(result);
                num_stack.push(sign);
                sign = 1;
                result = 0;
            }
            else if(c==')'){
                result =  result*num_stack.top();
                num_stack.pop();
                result += num_stack.top();
                num_stack.pop();
            }
            else if(c == '+')
                sign=1;
            else if(c=='-')
                sign=-1;
            else if(isdigit(c)){
                temp = s[i]-'0';
                while(i+1 < s.size() && isdigit(s[i+1])){
                    temp = temp*10 + s[i+1]-'0';
                    i++;
                }
                result += temp*sign;
            }
        }
        return result;
    }
};


int main(){
    Solution s;
    cout<<endl;
    cout<<s.calculate("3-(58-32)+42");
}
