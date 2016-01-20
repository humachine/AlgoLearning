#include<iostream>
using namespace std;

struct Stack {
    int top;
    int capacity;
    int *array;

    Stack(int x)
    {
        top = -1;
        capacity = x;
        array = new int[capacity];
    }

    int pop()
    {
        if(top == -1)
            return -1;
        cout<<array[top]<<endl;
        return array[top--];
    }

    int push(int x)
    {
        if(top==capacity){
            cout<<"Stack is full";
            return -1;
        }

        top++;
        array[top]=x;
        return 0;
    }

    int isEmpty(){
        return (top==-1);
    }
    void printStack(){
        int i;
        if(isEmpty())
            cout<<"Stack is Empty";
        else
        {
            for(i=0;i<=top;i++)
                cout<<array[i]<<endl;
        }
    }
    ~Stack() {
        delete array;
    }


};
typedef struct Stack Stack;

int main()
{
    int capacity = 100;
    int arr[]={3, 5, 10, 30, 13409};

    Stack s(20);
    int i;
    for(i=0;i<5;i++)
        s.push(arr[i]);

    while(!s.isEmpty())
        s.pop();


    
    return 0;
}
