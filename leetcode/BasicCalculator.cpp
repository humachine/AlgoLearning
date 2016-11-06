#include<iostream>
#include<string>
using namespace std;
int main(){
class Solution {
public:
    int calculate(string s) {
        int i=0;
        if(s.empty())
            return 0;
        int result = 0;
        int curr_num=0;
        stack<int> num_stack;
        stack<char> op_stack;
        for(i=0;i<s.size();i++){
            if(s[i]==' ')
                continue;
            else if(isdigit(s[i])){
                last = last*10 + (s[i]-'0');
                if(!num_stack.empty()){
                    num_stack.pop();
                }
                num_stack.push(last);
                
            }
            else if(s[i] == '+' || s[i]=='-' ){
                last = 0;
                num_stack.push(last);
                op_stack.push(s[i]);
            }
            else if(s[i]=='*' || s[i]=='/'){
                last = 0;
                num_stack.push(last);
            }
            else if(s[i] == '(' || s[i]==')'){
                
            }
            
        }
        return num_stack.top();;
    }
};

int main(){
    class Solution s;
    qn = "1+3+5-8";
    cout<<s.calculate(qn)<<endl;
    return 0;
}
