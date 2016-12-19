#https://leetcode.com/problems/valid-anagram/
"""test cases
    Inp: "anagram", "nagaram"
    Out: True
    Inp: "rat", "car"
    Out: False
"""
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        '''Compute character counts. Make sure that all character counts are zero after visiting both strings'''
        charCounts = defaultdict(int)
        for char in s:
            charCounts[char]+=1
        for char in t:
            charCounts[char]-=1
        counts = charCounts.values()
        return len(counts) == counts.count(0)
s = Solution()
print s.isAnagram("anagram", "nagaram")
print s.isAnagram("rat", "car")
