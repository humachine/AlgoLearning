//Combinations of a string

#include<iostream>
using namespace std;

static int count=0;
void combinations(string s, int x)
{
    if(x==s.length()){
        int i=0;
        while(i<s.length()){
            if(s[i]!=' ')
                cout<<s[i];
            i++;
        }
        count++;
        cout<<endl;
        return;
    }
    char c = s[x];
    s[x]=' ';
    combinations(s, x+1);
    s[x]=c;
    combinations(s, x+1);
}

int main(){
    string s;
    cin>>s;

    combinations(s, 0);
    cout<<count;

    return 0;
}
