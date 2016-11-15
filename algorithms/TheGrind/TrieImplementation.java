class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWord;
    // Constructor
    public TrieNode() {
        for(int i=0; i<26; i++)
            children[i] = null;
        isWord = false;
    }
}

public class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    // Inserts a word into the trie. O(length of word)
    public void insert(String word) {
        TrieNode node = root;
        //For each letter in the word, traverse down the trie. 
        //If any node's in the trie don't exist, create them and continue traversing
        for(int i = 0; i< word.length; i++){
            char c = word[i];
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new TrieNode();
            }
            node = node.children[c - 'a'];
        }
        node.isWord = true;
    }

    // Returns true if the entire word is in the trie.
    // O(length of word)
    public boolean searchFullWord(String word) {
        TrieNode node = root;
        //Traverse down the trie and check if your final node's isWord is true
        //If you encounter a null node during traversal, return false
        for(int i=0; i<word.length; i++){
            char c = word[i];
            if(node.children[c - 'a'] == null)
                return false;
            else
                node = node.children[c - 'a'];
        }
        return node.isWord;
    }

    // Returns if there is any word in the trie that starts with the given prefix.
    // O(length of word)
    public boolean startsWith(Sring word) {
        TrieNode node = root;
        //Traverse down the trie - If you encounter a null node during traversal, return false
        //Else - Return true
        for(int i=0; i<word.length; i++){
            char c = word[i];
            if(node.children[c - 'a'] == null)
                return false;
            else
                node = node.children[c - 'a'];
        }
        return true;
    }
}
