#https://leetcode.com/problems/alien-dictionary/
'''Given a list of non-empty words from the dictionary, where words are sorted
lexicographically by the rules of a new language.
Derive the order of letters in this language.

Inp:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Out: 'wertf'

Inp:
[
  "z",
  "x"
]
Out: 'zx'

Inp:
[
  "z",
  "x",
  "z"
]
Out: '' (Invalid ordering)
'''
import collections
class Solution(object):
    def _addEdge(self, char_a, char_b):
        parents, children = self.parents, self.children
        # Add an edge from A->B by adding A as B's parent and B as A's child
        parents[char_b].add(char_a)
        children[char_a].add(char_b)
        return True

    def findOrder(self, parents, children, chars_seen):
        queue = collections.deque()
        res = []
        # For all the characters present in the word list, pick out characters
        # that don't have any parents as seeds for the topo sort
        for char in chars_seen:
            if char not in parents:
                queue.append(char)

        while queue:
            # For each character in the queue, remove the link to each of its children.
            char = queue.popleft()
            for child in children[char]:
                parents[child].remove(char)
                # If the child has no more parents, then add it to the queue
                if not parents[child]:
                    queue.append(child)
            # Add character to result. And remove it from chars_seen
            res.append(char)
            chars_seen.remove(char)
        # If there are still characters_left, then these haven't been processed
        # ever. Which means these characters are involved in a cycle (inconsistency)
        if chars_seen:
            return ''
        return ''.join(res)

    def alienOrder(self, words):
        if not words:
            return ''
        n = len(words)
        if n==1:
            return ''.join(list(set(words[0])))

        # We attempt to build a graph between characters. Character A->B has an
        # edge, if A lexicographically < B

        # parents[char] is a set of all the parents that a character has
        # children[char] is a set of all the characters that are known to be
        # lexicographically greater than char
        # chars_seen is the set of all unique characters seen in the wordlist
        self.parents = collections.defaultdict(set)
        self.children = collections.defaultdict(set)
        chars_seen = set(words[0])

        for i in xrange(n-1):
            prev_word, next_word = words[i], words[i+1]
            # Adding all the characters of next_word to the char_seen set
            chars_seen.update(next_word)

            # Find the first character at which prev_word and next_word differ.
            # Note: ABC < ABC* (i.e given a common prefix, empty suffix appears
            # before suffixes of any length.
            # Hence, if we traverse through all characters of prev_word, we will
            # find a character that differs in next_word. If not, it means that
            # the prefixes are identical, but prev_word has an empty suffix
            for j, prev_char in enumerate(prev_word):
                if prev_char != next_word[j]:
                    # If characters differ, add an edge to the graph
                    self._addEdge(prev_char, next_word[j])
                    break

        # Run a topological sort and return the ordering
        return self.findOrder(self.parents, self.children, chars_seen)

s = Solution()
inp = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
print s.alienOrder(inp)

inp = [
  "z",
  "x"
]
print s.alienOrder(inp)

inp = [
  "z",
  "x",
  "z"
]
print s.alienOrder(inp)

inp = ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
print s.alienOrder(inp)

inp = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"]
print s.alienOrder(inp)
