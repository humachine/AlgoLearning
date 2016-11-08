//https://leetcode.com/problems/word-search-ii/
#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<algorithm>
using namespace std;
typedef class TrieNode{
    public:
        string text;
        TrieNode* children[26];
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
        for(int i=0; i<word.size(); i++){
            if(node->children[word[i]-'a'] == NULL){
                node->children[word[i]-'a'] = new TrieNode();
            }
            node = node->children[word[i]-'a'];
        }
        node->text = word;
    }
    bool search(string word){
        TrieNode *node = root;
        for(int i=0; i<word.size(); i++){
            if(node->children[word[i]-'a'] == NULL)
                return false;
            node = node->children[word[i]-'a'];
        }
        return node->text == word;
    }
    bool startsWith(string word){
        if(word.empty())    return false;
        TrieNode *node = root;
        for(int i=0; i<word.size(); i++){
            if(node->children[word[i]-'a'] == NULL)
                return false;
            node = node->children[word[i]-'a'];
        }
        return true;
    }
};

class Solution {
    void createTrie(vector<string>& words, Trie& tr){
        for(auto word: words)
            tr.insert(word);
    }
    void dfs(vector<vector<char> >& board, int x, int y, string res,
            unordered_set<string>& answer, Trie& tr){
        if(board[x][y] == '#')  return;

        if(tr.startsWith(res+board[x][y])){
            char c = board[x][y];
            board[x][y] = '#';

            int i=x, j=y;
            if(i>0) dfs(board, i-1, j, res+c, answer, tr);
            if(i<board.size()-1) dfs(board, i+1, j, res+c, answer, tr);
            if(j>0) dfs(board, i, j-1, res+c, answer, tr);
            if(j<board[0].size()-1) dfs(board, i, j+1, res+c, answer, tr);

            board[x][y] = c;
        }
        if(tr.search(res+board[x][y]))
            answer.insert(res+board[x][y]);

    }
    public:
        vector<string> findWords(vector<vector<char> >& board, vector<string>& words) {
            unordered_set<string> answer;
            vector<string> finalanswer;
            if(board.empty() || board[0].empty())   return finalanswer;

            Trie tr;
            createTrie(words, tr);

            int i, j, m=board.size(), n=board[0].size();
            for(i=0;i<m;i++){
                for(j=0; j<n; j++){
                    string res = "";
                    dfs(board, i, j, res, answer, tr);

                }
            }
            return vector<string>(answer.begin(), answer.end());
            return finalanswer;
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
    vector<string> answer = s.findWords(board, words);
    for(auto str: answer)
        cout<<str<<endl;

    //cout<<t.search("hello")<<endl;
    //cout<<t.startsWith("hel")<<endl;
    return 0;
}
