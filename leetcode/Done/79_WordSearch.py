# https://leetcode.com/problems/word-search/
'''
Given a grid of letters and a word, return if word exists in grid
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Inp: "ABCCED"
Out: True

Inp: "SEE"
Out: True

Inp: "ABCB"
Out: False

'''
class Solution(object):
    def dfs(self, board, x, y, word, start):
        # If we have reached end of word, then return True
        if start == len(word):
            return True
        # If the current letter does not match, return False
        if word[start] != board[x][y]:
            return False
        char = board[x][y]
        # Set the board[x][y] to '#' to prevent us from repeating this position again
        board[x][y] = '#'
        res = False
        if x>0: res = self.dfs(board, x-1, y, word, start+1)
        if not res and x<len(board)-1: res = self.dfs(board, x+1, y, word, start+1)
        if not res and y>0: res = self.dfs(board, x, y-1, word, start+1)
        if not res and  y<len(board[0])-1: res = self.dfs(board, x, y+1, word, start+1)
        # Backtrack and reset the value of board[x][y]
        board[x][y] = char
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:    return True
        if not board or len(board[0])==0:   return False

        m, n = len(board), len(board[0])
        # If board is of size 1x1, compare directly with word
        if m==1 and n==1:
            return board[0][0] == word

        # If the first letter matches, trigger DFS
        for x in xrange(m):
            for y in xrange(n):
                if word[0] == board[x][y] and self.dfs(board, x, y, word, 0):
                    return True
        return False

s = Solution()
board  = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
print s.exist(board, 'ABCCED')
board  = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
print s.exist(board, 'SEE')
board  = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
print s.exist(board, 'ABCB')

board = [list("CAA"), list('AAA'), list("BCD")]
print s.exist(board, 'AAB')
board = [list("ABCE"),list("SFES"),list("ADEE")]
print s.exist(board, "ABCESEEEFS")
