//https://leetcode.com/problems/lru-cache/
#include<iostream>
#include<set>
#include<queue>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<algorithm>
using namespace std;
class Node{
    public:
        int val;
        int key;
        Node *next;
        Node *prev;
        Node(int k, int v){
            key = k;
            val = v;
            next = prev = NULL;
        }
};

class LRUCache{
    int size, capacity;
    Node *head, *tail;
    unordered_map<int, Node*> cache;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        size = 0;
        head = tail = NULL;
    }

    int get(int key) {
        auto it = cache.find(key);
        if(it!=cache.end()){
            if(capacity > 1){
                Node *curr = it->second;
                if(curr!=head){
                    if(curr == tail){
                        tail = curr->next;
                    }
                    curr->next->prev = curr->prev;
                    if(curr->prev)
                        curr->prev->next = curr->next;

                    head->next = curr;
                    curr->prev = head;
                    head = curr;
                }
            }
            cout<<it->second->val<<' ';
            return it->second->val;
        }
        return -1;
    }

    void set(int key, int value) {
        Node *n = new Node(key, value);
        auto it = cache.find(key);
        if(it != cache.end())
            delete it->second;
        cache[key] = n;
        if(size == 0){
            head = tail = n;
            size++;
        }
        else{
            if(capacity == 1){
                cache.erase(head->key);
                head = tail = n;
            }
            else{
                if(size == capacity){
                    Node *temp = tail;
                    tail->next->prev = NULL;
                    tail  = tail->next;
                    delete temp;
                    size--;
                }
                head->next = n;
                n->prev = head;
                head = n;
                size++;
            }
        }
    }
};
int main(){
    class LRUCache c(2);
    //2,[get(2),set(2,6),get(1),set(1,5),set(1,2),get(1),get(2)]
    //-1, -1, 2, 6
    cout<<c.get(2)<<endl;
    c.set(2, 6);
    cout<<c.get(1)<<endl;
    c.set(1, 5);
    c.set(1, 2);
    cout<<c.get(1)<<endl;
    cout<<c.get(2)<<endl;
}
