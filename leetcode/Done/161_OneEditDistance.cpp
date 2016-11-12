#include<iostream>
#include<queue>
#include<string>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if(abs(int(s.size()) - int(t.size())) > 1)
            return false;
        // cout<<s.size()<<' '<<t.size();

        if(s.size() > t.size())
            s.swap(t);
        // cout<<s.size()<<' '<<t.size();
        if(s.empty())   return t.size()==1;
        
        int i, j, diff=0, lendiff=t.size()-s.size();
        for(i=0, j=0;i<s.size();i++, j++){
            if(s[i] != t[j]){
                return (s.substr(i+1) == t.substr(j+1))
                    || (s.substr(i) == t.substr(j+1));
            }
        }
        return false;
    }
};

int main(){
    class Solution s;
    string s1 = "ab";
    string s2 = "bc";
    cout<<endl;
    cout<<s.isOneEditDistance(s1, s2);
    cout<<endl;
}
