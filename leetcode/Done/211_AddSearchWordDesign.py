#https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''
Design a data structure that supports the following two operations:
    void addWord(word)
    bool search(word) - search(word) can search a literal word or a regular expression string containing only letters a-z or .
'''
from collections import defaultdict
# TrieNode class definition
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
    def __str__(self):
        return '{}-{}'.format(self.children.keys(), self.isWord)

# Trie class definition
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Regular trie insert method. We sert the isWord flag to True at the end of a word
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def _searchWildCard(self, word, start, node):
        ''' We perform a trie search including wildcard support. This is a backtracking based search that's used to solve for the . wildcard'''
        # If we have exhausted the whole word, check if it is the end of an actual word
        if start == len(word):
            return node.isWord
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        char = word[start]
        if char == '.':
            # If the character we encounter is the wildcard '.', then we run through all 26 possibilities and recurse on each of them. Even if one of those possibilities leads to a word match, we return true
            for c in ALPHABET:
                # Checking if the character c is in the node's children and leads to a valid word match
                if c in node.children and self._searchWildCard(word, start+1, node.children[c]):
                    return True
            # No matches found despite wildcard search
            return False

        # For non-wildcard characters, if the character does not appear in the children of the node, return False
        if char not in node.children:
            return False
        # if character char is present, search for word[start+1:] from node's char child.
        return self._searchWildCard(word, start+1, node.children[char])

    def searchWildCard(self, word):
        return self._searchWildCard(word, 0, self.root)

class WordDictionaryTrie(object):
    def __init__(self):
        """ initialize your data structure here.  """
        self.trie = Trie()
        
    def addWord(self, word):
        """ Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)
        
    def search(self, word):
        """ Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.searchWildCard(word)

class WordDictionary(object):
    ''' While the trie solution above does work, for wildcard searches, it runs through an extraordinary number of paths before pruning them. 
    This method involves dictionaries where we store all words of the same word length in a dictionary list with key as word length.

    When search for a word, we just search amongst the words that are present in THAT wordlength.
    This can be further sped up by having different Tries for each word-length
    '''
    def __init__(self):
        self.data = defaultdict(list)
        
    def addWord(self, word):
        # Each word gets added into a list. There are separate lists maintained for words of each wordlength
        self.data[len(word)].append(word)
        
    def search(self, word):
        # We only search amongst the words of the same word length
        matchList = self.data[len(word)]
        for possibleMatch in matchList:
            # each character of the word must match OR it must be a wildcard '.'
            for i, char in enumerate(word):
                if char!=possibleMatch[i] and char!='.':
                    break
            # The else portion of the for is executed only if the entire loop completes and terminates naturatlly(without break statements)
            # Here, the else portion of the for means that the whole word has been compared and no mismatches were found.
            else:
                return True
        return False
# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("wick")
print wordDictionary.search("word")
print wordDictionary.search("w.rd")
print wordDictionary.search("w.r")
