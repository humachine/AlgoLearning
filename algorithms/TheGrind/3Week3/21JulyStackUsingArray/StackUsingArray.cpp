//http://quiz.geeksforgeeks.org/stack-set-1/
//
//Stack implementation using array
//
//Time Complexity for insert, delete: O(1)

#include<vector>
#include<iostream>
using namespace std;
struct Stack{
    int top;
    int capacity;
    int *arr;
};
typedef struct Stack Stack;
Stack *createStack(int capacity){
    Stack *st = new Stack;
    st->capacity = capacity;
    st->top = -1;
    st->arr = new int[capacity];
    return st;
}
bool isFull(Stack *st){
    return st->top == st->capacity-1;
}
bool isEmpty(Stack *st){
    return st->top == -1;
}
void push(Stack *st, int num){
    if(isFull(st)){
        cout<<"Stack is full. Go away\n";
        return;
    }
    st->top++;
    st->arr[st->top] = num;
}
int pop(Stack *st){
    if(isEmpty(st)){
        return -1;
    }
    return st->arr[st->top--];
}
int peek(Stack *st){
    if(isEmpty(st)){
        return -1;
    }
    return st->arr[st->top];
}
int main(){
    int T;
    cin>>T;
    int i, j, k, N, P, temp, ii;
    Stack *st=NULL;
    for(i=0;i<T;i++){
        cin>>temp;
        st = createStack(temp);
        cin>>N;
        for(j=0;j<N;j++){
            cin>>temp;
            push(st, temp);
        }
        cin>>P;
        for(j=0;j<P;j++){
            cout<<pop(st)<<' ';
        }
        cout<<peek(st)<<endl;
    }
    delete st;
}
