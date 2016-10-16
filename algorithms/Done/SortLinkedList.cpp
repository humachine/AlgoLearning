//Sorting a Linked List


#include<iostream>
#include<algorithm>
using namespace std;


struct Node {
    int value;
    struct Node *next;
};
typedef struct Node Node;

Node *merge(Node *a, Node *b){
    cout<<a->value<<' '<<b->value<<endl;
    Node *head, *tail;
    if(a==NULL)
        return b;
    if(b==NULL)
        return a;
    if(a->value <= b->value){
        head=a;
        tail=a;
        a=a->next;
    }
    else{
        head=b;
        tail=b;
        b=b->next;
    }
    while(a!=NULL && b!=NULL){
        cout<<a->value<<' '<<b->value<<endl;
        if(a->value <= b->value){
            tail->next=a;
            tail = tail->next;
            a=a->next;
        }
        else{
            tail->next = b;
            tail = tail->next;
            b=b->next;
        }
    }
    cout<<"Done";
/*
    while(a!=NULL){
        cout<<tail->value<<'\n';
        tail->next = a;
        tail = tail->next;
        a = a->next;
    }
    while(b!=NULL && 0){
       // tail->next = b;
        //tail = tail->next;
        b = b->next;
    }
*/
}
#define pmax(x) #x
int main()
{
    int arr[]={1,3, 5, 834, 123, 88, -14, 77, 2, 10, 11, 10};
    int len=sizeof(arr)/sizeof(arr[0]);
    sort(arr, arr+len);
    
    Node *head;
    head = new Node;

    int i;
    head = NULL;
    Node *middle=NULL;
    for(i=0;i<len;i++)
    {
        Node *temp = new Node;
        temp->value = arr[len-1-i];
        if(i==len/2)
            middle=head;
        temp->next = head;
        head = temp;
    }

    //Node *ans= mergesort(head);
    //cout<<"Sorted..."<<ans->value;


    //Node *merged = merge(head, middle);

    

    return 0;
}

