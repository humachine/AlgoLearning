//http://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/
#include <iostream>
using namespace std;

typedef struct Node {
    int data;
    struct Node *left, *right;
} Node;

Node *newnode(int value){
    Node *node = new Node;
    node->data = value;
    node->left = NULL;
    node->right = NULL;
}
void printArr(int *ans, int curr){
    for(int i=0;i<curr;i++)
        cout<<ans[i]<<' ';
    cout<<endl;
}
void printPaths(Node *root, int *ans, int curr){
    if(root == NULL)
        return ;

    ans[curr++] = root->data;
    if(root->left ==NULL && root->right == NULL )
        printArr(ans, curr);
    else{
        printPaths(root->left, ans, curr);
        printPaths(root->right, ans, curr);
    }

}

void printRecursivePaths(Node *root){
    int ans[1000];
    printPaths(root, ans, 0);
}

int main(){
    Node *root = newnode(1);
    root->left = newnode(5);
    root->right = newnode(3);
    root->left->left = newnode(14);
    root->left->right = newnode(8);
    root->right->left = newnode(9);
    printRecursivePaths(root);
    return 0;
}
/*
 *             1
 *         5        3
 *       14 8      9
 *
 * */
