#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''Given a string and an integer K, return the length of the longest substring
that has at most K distinct characters.

Inp: 'eceba', k=2
Out: 2 (ece is the longest such substring)
'''
import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        # If K>=n, the entire string is the longest possible substring
        if k >= n:
            return n
        max_len = distincts = left = right = 0
        char_counts = collections.defaultdict(int)

        # We try all possible ending locations of a substring (i.e right: 0->n)
        # For each ending location, we find the least starting index for which
        # number of distinct characters <= K (if any)
        for right, char in enumerate(s):
            if char_counts[char] == 0:
                distincts+=1
            # Increment count of each character that appears in the current substring
            char_counts[char] += 1

            # Make the window/substring smaller and smaller until we are left with
            # an empty string OR a string with <= K distinct characters
            while left <= right and distincts > k:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    distincts-=1
                left+=1
            max_len = max(max_len, right-left+1)

        return max_len

s = Solution()
print s.lengthOfLongestSubstringKDistinct('eceba', 2)
print s.lengthOfLongestSubstringKDistinct('eceba', 0)
print s.lengthOfLongestSubstringKDistinct('abaccc', 2)
