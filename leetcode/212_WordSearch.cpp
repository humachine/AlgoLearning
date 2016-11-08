//https://leetcode.com/problems/word-search-ii/
#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<algorithm>
using namespace std;
typedef class TrieNode{
    public:
    string word;
    TrieNode *children[26];
    TrieNode(){
        for(int i=0;i<26;i++)
            children[i] = NULL;
    }
} TrieNode;

class Trie{
    TrieNode* root;
    public:
        Trie(){
            root = new TrieNode();
        }
    void insert(string word){
        TrieNode *node = root;
        for(int i=0;i<word.size();i++){
            char c = word[i];
            if(node->children[c-'a'] == NULL){
                node->children[c-'a'] = new TrieNode();
            }
            node = node->children[c-'a'];
        }
        node->word = word;
    }
    bool search(string word){
        TrieNode *node = root;
        for(int i=0;i<word.size();i++){
            char c = word[i];
            if(node->children[c-'a'] == NULL)
                return false;
            node = node->children[c-'a'];
        }
        if(node->word == word)
            return true;
        return false;
    }
    bool startsWith(string word){
        TrieNode *node = root;
        for(int i=0;i<word.size();i++){
            char c = word[i];
            if(node->children[c-'a'] == NULL)
                return false;
            node = node->children[c-'a'];
        }
        return true;
    }

};

class Solution {
    public:
        vector<string> findWords(vector<vector<char> >& board, vector<string>& words) {
        }

};
int main(){
    char a1[] = {'o','a','a','n'};
    char a2[] = {'e','t','a','e'};
    char a3[] = {'i','h','k','r'};
    char a4[] = {'i','f','l','v'};
    vector<vector<char> > board;
    board.push_back(vector<char>(a1, a1+4));
    board.push_back(vector<char>(a2, a2+4));
    board.push_back(vector<char>(a3, a3+4));
    board.push_back(vector<char>(a4, a4+4));

    string dict[] = {"oath","pea","eat","rain"};
    vector<string> words(dict, dict+4);
    class Solution s;
    //vector<string> answer = s.findWords(board, words);

    class Trie t;
    t.insert("hello");
    cout<<t.search("h")<<endl;
    cout<<t.startsWith("he")<<endl;
    cout<<"Done";
    return 0;
}
