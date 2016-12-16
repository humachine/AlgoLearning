//https://leetcode.com/problems/alien-dictionary/
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
class Solution {
    public:
        string alienOrder(vector<string>& words) {
            if(words.empty())   return "";
            if(words.size()==1) return words[0];
            //Form directed graph of dependencies
            unordered_map<char, unordered_set<char> > graph;
            int i, j, k;
            for(i=0;i<words.size();i++){
                for(j=0;j<words[i].size();j++){
                    auto it = graph.find(words[i][j]);
                    if(it == graph.end()){
                        graph[words[i][j]] = unordered_set<char>();
                    }
                }
            }
            string prev_word, word;
            unordered_map<char, int> degrees;
            for(i=1;i<words.size(); i++){
                prev_word = words[i-1];
                word = words[i];
                for(j=0;j<min(prev_word.size(), word.size()); j++){
                    if(word[j] == prev_word[j])
                        continue;
                    auto iit = graph[prev_word[j]].find(word[j]);
                    if(iit == graph[prev_word[j]].end()){
                        graph[prev_word[j]].insert(word[j]);
                        degrees[word[j]]++;
                    }
                    break;
                }
                if(j<=word.size()-1 && j>prev_word.size())
                    return "";
            }

            //Find nodes that have exactly no incoming edges
            queue<char> q;
            for(auto it=graph.begin(); it!=graph.end(); it++){
                char c = it->first;
                //cout<<c<<' '<<degrees[c]<<endl;
                if(degrees[c] == 0)
                    q.push(c);
            }
            if(q.empty())
                return "";
            if(q.size() == degrees.size()){
                if(q.size() > 1){
                    if(words[words.size()-1].size() > words[words.size()-2].size())
                        return words[words.size()-1];
                    return "";
                }
            }

            //BFS over graph
            vector<char> result;
            while(!q.empty()){
                char c = q.front();
                q.pop();
                cout<<c<<endl;

                result.push_back(c);

                auto it = graph.find(c);
                if(it!=graph.end()){
                    //Go to its neighbours and remove the edge from this node to its neighbour
                    for(auto i = (it->second).begin(); i != (it->second).end(); i++){
                        degrees[*i]--;
                        cout<<*i<<' '<<degrees[*i]<<endl;
                        if(degrees[*i] == 0){
                            q.push(*i);
                        }
                    }
                }
            }
            if(result.size()!=degrees.size())
                return "";

            return string(result.begin(), result.end());
        }
};

int main(){
    //string w[] = {"wrt", "wrf", "er", "ett", "rftt"};
    //string w[] = {"z","z"};
    //string w[] = {"wrtkj","wrt"};
    string w[] = {"wrt","wrtkj"};
    //string w[] = {"za","zb", "ca", "cb"};
    vector<string> words(w, w+4);

    class Solution s;
    cout<<endl;

    cout<<s.alienOrder(words)<<endl;
}
