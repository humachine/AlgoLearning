//Wiggle Sort - Alternate Ascending Descending sequence

#include<iostream>
using namespace std;
void swap(int *a, int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int main()
{
    int num[1000];
    int n;
    cin>>n;
    int i, j, k;

    for(i=0;i<n;i++)
        cin>>num[i];

    for(i=0;i<n-1;i++)
    {
        if(i%2==0){
            if(num[i]>num[i+1])
                swap(&num[i], &num[i+1]);
        }
        else {
            if(num[i]<num[i+1])
                swap(&num[i], &num[i+1]);
        }
    }
    for(i=0;i<n;i++)
        cout<<num[i]<<' ';
    cout<<endl;
    return 0;


}
