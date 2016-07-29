//http://quiz.geeksforgeeks.org/stack-set-1/
//
//Implementing a stack using a linked list
//
//Input: N followed by N integers to push onto stack. 
//P - Number of pops to perform
//
//O/P - Pop output plus peek at final stack

#include<iostream>
using namespace std;

struct StackNode{
    int value;
    struct StackNode *next;
};
typedef struct StackNode Node;
void insertNode(Node **root, int temp){
    Node *newNode = new Node;
    newNode->value = temp;
    newNode->next = *root;
    *root = newNode;
}
void popNode(Node **root){
    if(*root == NULL)
       cout<<"-1 "; 
    else{
        cout<<(*root)->value<<' ';
        *root = (*root)->next;
    }
}
bool isEmpty(Node *root){
    return !root;
}
void peek(Node *root){
    if(root == NULL)
        cout<<"-1 ";
    else{
        cout<<root->value<<' ';
    }
}
void emptyStack(Node *root){
    Node *temp=root;
    while(temp!=NULL){
        root = temp->next;
        delete temp;
        temp = root;
    }
}
int main(){
    int T;
    cin>>T;

    int i, j, k, N, P;
    int ii, temp;

    struct StackNode *root = NULL;

    for(ii=0;ii<T;ii++){
        root=NULL;
        cin>>N;
        for(i=0;i<N;i++){
            cin>>temp;
            insertNode(&root, temp);
        }
        cin>>P;
        for(i=0;i<P;i++)
            popNode(&root);
        peek(root);
        cout<<endl;
        emptyStack(root);
    }
    return 0;
}
