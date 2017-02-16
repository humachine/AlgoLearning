#https://leetcode.com/problems/word-search-ii/
'''Given a grid of characters and a set of words, return all the words that 
appear in the grid.
'''
import collections
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

class Solution(object):
    def dfs(self, board, trie, x, y, curr_str, res, node):
        m, n = self.m, self.n
        # if board[x][y] is either a '#' or will not lead to any words
        if board[x][y] not in node.children:
            return
        node = node.children[board[x][y]]

        # If we have reached a word, append it to result and update its status
        # We update node.is_word to False so that it is not picked up again
        if node.is_word:
            res.append(curr_str+board[x][y])
            node.is_word = False

        c = board[x][y]
        board[x][y] = '#'
        # Spawn off searches from all valid neighbours
        if x-1>=0:
            self.dfs(board, trie, x-1, y, curr_str+c, res, node)
        if x+1<m:
            self.dfs(board, trie, x+1, y, curr_str+c, res, node)
        if y-1>=0:
            self.dfs(board, trie, x, y-1, curr_str+c, res, node)
        if y+1<n:
            self.dfs(board, trie, x, y+1, curr_str+c, res, node)
        # Update the original state of the board
        board[x][y] = c


    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
           return []
        self.m, self.n = len(board), len(board[0])

        #Load all words into trie
        trie = Trie()
        for word in words:
           trie.insert(word)

        #DFS searching for words
        res = []
        for i in xrange(self.m):
           for j in xrange(self.n):
               self.dfs(board, trie, i, j, '', res, trie.root)
        return res

s = Solution()
board  = [ ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'] ]
dic = ['ASA', 'ABCCF', 'ABCC', 'ABFC', 'HELLO']
print s.findWords(board, dic)

board = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
board = [list(x) for x in board]
dic = ["aab"
        "bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
print s.findWords(board, dic)
