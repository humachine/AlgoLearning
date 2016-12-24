#https://leetcode.com/problems/anagrams/
'''
Given a set of strings, group anagrams together
    Inp: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Out: [ ["ate", "eat","tea"], ["nat","tan"], ["bat"] ]
'''
from collections import defaultdict
class Solution(object):
    def charCounts(self, string):
        # The hash of a string is just a tuple of all its character counts
        arr = [0]*26
        charIndex = lambda x: ord(x)-ord('a')
        for char in string:
            arr[charIndex(char)]+=1
        return tuple(arr)

    def groupAnagrams(self, strs):
        if not strs:    return []
        anagramGroups = defaultdict(list)
        for string in strs:
            # For each string, we use the charCounts tuple as the hash.
            # Anagrams will have the same hash and hence will get added to the same list
            anagramGroups[self.charCounts(string)].append(string)
        return anagramGroups.values()
s = Solution()
Inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
print s.groupAnagrams(Inp)
