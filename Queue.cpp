//Queue Implementation

#include<iostream>
using namespace std;

struct Queue {
    int front, rear, size, capacity;
    int *array;

    Queue (int inp){
        front = size = 0;
        capacity=inp;
        rear = capacity - 1;
        array = new int[capacity];
    }

    int enqueue(int inp){
        if(size == capacity){
            cout<<"Queue is full";
            return -1;
        }
        array[(rear+1)%capacity] = inp;
        size+=1;
        rear = (rear+1)%capacity;
    }
    int dequeue()
    {
        if(size==0){
            cout<<"Queue is empty";
            return -1;
        }
        size-=1;
        cout<<array[front];
        front = (front+1)%capacity;
    }
    int isFull(){
        if(size==capacity)
            return 1;
        return 0;
    }
    int isEmpty(){
        if(size==0)
            return 1;
        return 0;
    }

};

int main()
{
    int arr[] = {1, 2, 3, 4, 15};
    int i;
    struct Queue q(20);
    for(i=0;i<5;i++)
        q.enqueue(arr[i]);

    while(!q.isEmpty())
        q.dequeue();
    
    return 0;
}
