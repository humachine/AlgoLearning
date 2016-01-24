//http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/

#include <iostream>
using namespace std;
typedef struct Node{
    int data;
    struct Node *next;
    Node(int value){
        data=value;
    }

} Node;
void reverseList(Node *head);

int main(){
    Node *head = NULL;
    head = new Node(45);

    Node *t = head;
    t->next = new Node(53);
    t=t->next;

    t->next = new Node(78);
    t=t->next;

    t->next = new Node(18);
    t=t->next;
    t->next = new Node(93);
    t=t->next;
    t->next = new Node(3);
    t=t->next;
    t->next = new Node(-7);
    t=t->next;
    t->next = new Node(110);

    while(head){
        cout<<head->data<<endl;
        head=head->next;
    }

    return 0;
}
