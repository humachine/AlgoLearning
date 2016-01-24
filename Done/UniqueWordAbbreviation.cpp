//http://qa.geeksforgeeks.org/4949/check-if-abbreviation-is-unique

#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <cstring>

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
                ( std::ostringstream() << std::dec << x ) ).str()
using namespace std;
int main(){
    int n;
    cin>>n;

    string arr[1000];
    int i, j, k, ans;
    for(i=0; i<n; i++)
        cin>>arr[i];

    map<string, int> hash;
    for(i=0;i<n;i++){
        string s;
        if(arr[i].length() > 2)
            s = arr[i][0]  + SSTR(arr[i].length()-2) + arr[i][arr[i].length()-1];
        else
            s=arr[i];
        hash[s] = 1;
    }
    string qns[] = {"dear", "cart", "cane", "make"};
    for(i=0;i<4;i++){
        string s;
        s=qns[i];
        if(s.length()>2)
            s = qns[i][0] + SSTR(qns[i].length()-2) + qns[i][qns[i].length()-1];
        if(hash.find(s) == hash.end())
            cout<<"Unique "<<qns[i]<<endl;
    }
    return 0;



}
