//Linked List Implementation
#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

int main()
{
    struct Node *head=NULL;
    head = (struct Node *) malloc(sizeof(struct Node));
    
    struct Node *tail=NULL;
    tail = (struct Node *) malloc(sizeof(struct Node));

    head->data = 3;
    head->next = tail;

    tail->next=NULL;
    tail->data=4;

    printf("%d", (head->next)->data);

    free(head);
    free(tail);

    return 0;
}


