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
    def dfs(self, board, x, y, word):
        if word == "":
            return True
        if word[0] != board[x][y]:
            return False
        char = board[x][y]
        board[x][y] = '#'
        lVal = rVal = topVal = bottomVal = False
        if x>0: topVal = self.dfs(board, x-1, y, word[1:])
        if x<len(board)-1: bottomVal = self.dfs(board, x+1, y, word[1:])
        if y>0: lVal = self.dfs(board, x, y-1, word[1:])
        if y<len(board[0])-1: rVal = self.dfs(board, x, y+1, word[1:])
        board[x][y] = char
        return lVal or rVal or topVal or bottomVal

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:    return True
        if not board or len(board[0])==0:   return False

        m, n = len(board), len(board[0])
        if m==1 and n==1:
            return board[0][0] == word
        for x in xrange(m):
            for y in xrange(n):
                if self.dfs(board, x, y, word):
                    return True
        return False
board  = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
s = Solution()
print s.exist(board, 'ABCCED')
print s.exist(board, 'SEE')
print s.exist(board, 'ABCB')
