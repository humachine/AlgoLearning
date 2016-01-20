//Permutations of a string - with Repetitions
// http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
#include<iostream>
#include<cstring>
using namespace std;

void permute(char *a, int left, int right);

int main()
{
    char a[100];
    cin>>a;

    int len=strlen(a);

    permute(a, 0, len-1);
    
    return 0;
}
void swap(char *a, char *b)
{
    char temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
void permute(char *a, int left, int right)
{
    int i, j, k;
    if(left==right)
        cout<<a<<endl;
    else
    {
        for(i=left;i<=right;i++)
        {
            swap((a+left), (a+i));
            permute(a, left+1, right);
            swap((a+left), (a+i));
        }
    }
}
