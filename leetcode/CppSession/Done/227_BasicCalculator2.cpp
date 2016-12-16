//https://leetcode.com/problems/basic-calculator/
#include<iostream>
#include<sstream>
#include<set>
#include<queue>
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
        istringstream in("+" + s + "+");
        int total, curr, last;
        char op;
        total = curr = last = 0;
        while(in>>op){
            if(op==' ') continue;
            if(op=='+' || op=='-'){
                total += last;
                in>>last;
                last = last* (op=='+'?1:-1);
            }
            else{
                in>>curr;
                if(op=='+')
                    last = last*curr;
                else
                    last /= curr;
            }
        }
        return total;
    }
};


int main(){
    Solution s;
    cout<<endl;
    cout<<s.calculate("3+58");
}
