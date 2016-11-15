//https://leetcode.com/problems/word-search-ii/
#include<iostream>
#include<vector>
#include<unordered_set>
#include<unordered_map>
#include<algorithm>
using namespace std;
typedef class TrieNode{
    public:
        TrieNode *children[26];
        bool is_word;
        TrieNode(){
            for(int i=0;i<26;i++)
                children[i] = NULL;
            is_word = false;
        }
} TrieNode;
typedef class Trie{
    TrieNode* search(string word){
        TrieNode* node = root;
        for(int i=0;i<word.size();i++){
            if(!node->children[word[i]-'a'])
                return NULL;
            node = node->children[word[i]-'a'];
        }
        return node;
    }
    public:
        TrieNode *root;
        Trie(){
            root = new TrieNode();
        }
        void insert(string word){
            TrieNode* node = root;
            for(int i=0;i<word.size();i++){
                if(node->children[word[i]-'a'] == NULL){
                    node->children[word[i]-'a'] = new TrieNode();
                }
                node = node->children[word[i]-'a'];
            }
            node->is_word = true;
        }
        bool searchWord(string word){
            TrieNode* result = search(word);
            if(!result) return false;
            return result->is_word;
        }
        bool startsWith(string word){
            if(word.empty())    return true;
            TrieNode* result = search(word);
            if(!result) return false;
            return true;
        }
}Trie;
class Solution{
    void dfs(vector<vector<char> >& board, int x, int y, string res, unordered_set<string>& answer, Trie word_trie){
        if(board[x][y] == '#')  return;
        if(!word_trie.startsWith(res))  return;

        char c = board[x][y];
        board[x][y] = '#';
        //Send off DFS searches
        if(x-1>=0)  dfs(board, x-1, y, res+c, answer, word_trie);
        if(x+1<board.size()) dfs(board, x+1, y, res+c, answer, word_trie);
        if(y+1<board[0].size()) dfs(board, x, y+1, res+c, answer, word_trie);
        if(y-1>=0) dfs(board, x, y-1, res+c, answer, word_trie);

        //Reset changes to board
        board[x][y] = c;

        //Check if current res is word
        if(word_trie.searchWord(res+c)){
            answer.insert(res+c);
            //cout<<res+c<<endl;
        }

    }
    void LoadTrie(Trie& word_trie, vector<string>& words){
        for(int i=0; i<words.size(); i++){
            word_trie.insert(words[i]);
        }
    }
    public:
        vector<string> findWords(vector<vector<char> >& board, vector<string>& words) {
            unordered_set<string> answer;
            if(board.empty())   return vector<string>();
            int m = board.size(), n=board[0].size();

            Trie word_trie;
            LoadTrie(word_trie, words);

            int i, j;
            string res;
            for(i=0; i<m; i++){
                for(j=0; j<n; j++){
                    dfs(board, i, j, "", answer, word_trie);
                }
            }
            return vector<string>(answer.begin(), answer.end());
            
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
