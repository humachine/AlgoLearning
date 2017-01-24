#https://leetcode.com/problems/word-ladder-ii/
'''Given a start word, end word and a dictionary of words; print all the 
word transformations possible from start word to end word.
Note: All intermediate words in the transformation (except beginWord) must exist
in the dictionary

    Inp: 'hit', 'cog', ['hot', 'dog', 'dot', 'lot', 'log', cog']
    Out: [ ["hit","hot","dot","dog","cog"],
            ["hit","hot","lot","log","cog"] ]
'''
import collections
class Solution(object):
    def addPath(self, word, neigh, forward_dirn):
        # Adds a word, neighbour to the word transformation tree. i.e adds a single edge to the tree
        # The edges always need to point from the word closer to beginWord
        # to the word closer to endWord

        # If the direction is forward, we add $neigh as the next node from $word
        if forward_dirn:
            self.word_paths[word].add(neigh)
        else:
            self.word_paths[neigh].add(word)

    def generateTransformations(self, beginWord, endWord):
        # generateTransformations generates a list of all transformation sequences
        # possible from a given beginWord->endWord
        # If we have reached the end word, we just return a single list with endWord in it
        if beginWord == endWord:
            return [[beginWord]]
        # If we have already computed the paths from this beginWord to the endWord, we reuse it
        if (beginWord, endWord) not in self.found_paths:
            # neighbour_paths is the list of all paths from any neighbour of the current
            # word to endWord
            neighbour_paths = (path for neighbour in self.word_paths[beginWord]
                for path in self.generateTransformations(neighbour, endWord))
            # Adding (beginWord, endWord) to the 'found' dictionary
            self.found_paths[(beginWord, endWord)] = list(neighbour_paths)
        # Return current_word + each path possible from each of its neighbours
        return [[beginWord] + path for path in self.found_paths[(beginWord, endWord)]]

    def buildWordPaths(self, front, back, forward_dirn):
        # Here, we build the word_tree which has the set of edges from each word
        # to its neighbours if it could be a part of the word ladder.
        # Returns: True (if path exists from beginWord->endWord) else False

        if not front:
            # If we are out of words, then we have reached a dead-end. No more valid transformations were possible
            return False
        # Bi-directional BFS: If front gets large, we run the search from back
        # This reduces the complexity by sqRt(D) where D is the number of levels from beginWord->endWord
        if len(front) > len(back):
            return self.buildWordPaths(back, front, not forward_dirn)

        # Delete all words that are present in either front or back from the dictionary
        self.word_list -= (front | back)
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        reached_endWord, next_level = False, set()

        for word in front:
            # neighbours is the list of all possible english alphabet neighbours from a word
            neighbours = (word[:i]+c+word[i+1:] for c in ALPHABET for i in xrange(len(word)))

            for neigh in neighbours:
                # If neigh in back, we have reached the end word
                if neigh in back:
                    reached_endWord = True
                    self.addPath(word, neigh, forward_dirn)
                # If we have not reached_endWord but $neigh is in the dictionary,
                # then we just add it to the next_level of the tree
                if not reached_endWord and neigh in self.word_list:
                    next_level.add(neigh)
                    self.addPath(word, neigh, forward_dirn)

        return reached_endWord or self.buildWordPaths(next_level, back, forward_dirn)

    def findLadders(self, beginWord, endWord, wordList):
        # In this question we perform a bi-directional BFS, all the while maintaining
        # a tree of the word paths. For each word its neighbours in the word ladder
        # are stored.
        # Finally, if we have a valid word ladder, we build it and return it.
        front, back  = {beginWord}, {endWord}
        self.word_list = set(wordList)
        # If endWord is not in the dictionary, no transformations possible
        if endWord not in self.word_list:
            return []

        self.word_paths = collections.defaultdict(set)
        path_exists = self.buildWordPaths(front, back, True)
        # If no path exists, return []
        if not path_exists:
            return []
        # self.found_paths is used to memoize paths that have already been calculated
        self.found_paths = {}
        return self.generateTransformations(beginWord, endWord)

s = Solution()
print s.findLadders('hit', 'cog', ['hot', 'dog', 'dot', 'lot', 'log', 'cog'])
print s.findLadders('abc', 'abc', ['def'])
print s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
