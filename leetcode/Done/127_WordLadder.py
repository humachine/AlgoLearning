#https://leetcode.com/problems/word-ladder/
''' Given 2 words and a set of dictionary words, find the length of the shortest transformation sequence between the startWord & endWord. Each transformation is valid only if all intermediate words are in the list. And each word can only be changed one letter in each step.

    Inp: 'hit', 'cog', ["hot","dot","dog","lot","log"]
    Out: 'hit'->'hot'->'dot'->'dog'->'cog' (sequence length = 5)

    Inp: 'hit', 'nom', ["hot","dot","dog","lom","log"]
    Out: 'hit'->'hot'->'dot'->'dog'->'log'->'lom'->'nom' (sequence length = 7)
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        front, back = {beginWord}, {endWord} # Front and back are sets that represent the two end zones that we are trying to connect
        ALPHABET, seqLength = 'abcdefghijklmnopqrstuvwxyz', 2 #seqLength is atleast 2 for any beginWord->endWord

        wordList.add(endWord)
        while front:
            # We remove the words of front from the wordList
            # At each stage, front morphs into the words that are one edit distance from the words of front
            # We remove from wordList so that the morphed 'front' does not contain any words from the old front
            wordList-=front
            # We first generate all the words that we can reach with 1 edit from the words of front. 
            # For each word, we replace each letter with all 26 combinations and add it to the new list.
            front = set(word[:i]+c+word[i+1:] for c in ALPHABET for i in xrange(len(beginWord)) for word in front if word[:i]+c+word[i+1:] in wordList)
            if front & back: # If front & back intersect, we return seqLength
                return seqLength

            seqLength += 1
            if len(front) > len(back): #If front has more words than back, we perform the BFS from the back (bi-directional BFS)
                back, front = front, back
        return 0
s = Solution()
wordList = set(['hot', 'dot', 'dog', 'lot', 'log'])
print s.ladderLength('hit', 'cog', wordList)

wordList = set(['hot', 'dot', 'dog', 'log', 'lom'])
print s.ladderLength('hit', 'nom', wordList)

wordList = set(['hot', 'dot', 'dog', 'log', 'lom'])
print s.ladderLength('hit', 'noz', wordList)
