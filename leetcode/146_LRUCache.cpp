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
#include<list>
using namespace std;
class LRUCache{
    int capacity;
    list<pair<int, int>> li;
    unordered_map<int, list<pair<int, int>>::iterator> cache;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        auto it = cache.find(key);
        if(it == cache.end())   return -1;

        int answer = it->second->second;
        li.splice(li.begin(), li, it->second);
        return answer;
    }

    void set(int key, int value) {
        auto it = cache.find(key);
        if(it != cache.end()){
            //it->second points to the element in the list that needs to be pushed to the front
            //We splice li's (it->second) element to the front of li
            li.splice(li.begin(), li, it->second);
            //Update cache key->listNode pairing
            cache[key] = it->second;
            //Update the value stored for key
            it->second->second = value;
        }
        else{
            if(li.size() == capacity){
                // remove LRU element
                int key_to_remove = li.back().first;
                cache.erase(key_to_remove);
            }
            // Insert new node into list & update cache
            li.emplace_front(key, value);
            cache[key] = li.begin();
        }
    }
};
int main(){
    class LRUCache c(2);
    //2,[get(2),set(2,6),get(1),set(1,5),set(1,2),get(1),get(2)]
    //Output: -1, -1, 2, 6
    cout<<c.get(2)<<endl;

    c.set(2, 6);
    cout<<c.get(1)<<endl;
    c.set(1, 5);
    c.set(1, 2);
    cout<<c.get(1)<<endl;
    cout<<c.get(2)<<endl;
}
