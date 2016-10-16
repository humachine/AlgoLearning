// Building a binary tree

#include <iostream>
#include <queue>
using namespace std;

typedef struct Node Node;
struct Node{
    int data;
    struct Node *parent;
    struct Node *left, *right;
};

void BuildBinaryTree(Node *root, int i){
}


int main()
{
    int arr[]={1,3,4,78,9,11,1037};
    Node *root = new Node;
    root->data = arr[0];
    
    queue<Node> nodeq;
    long int n=1;

    nodeq.push(
    while(!nodeq.empty())
    {


    return 0;
}
