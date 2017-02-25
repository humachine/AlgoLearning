#https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
'''Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Inp: "aaabb", k = 3
Out: 3 ('aaa' is the longest such string)

Inp: "ababbc", k = 2
Out: 5 ('ababb' is the longest such string)
'''
import collections
class Solution(object):
    def longestSubstring(self, s, k):
        if k<=1 or not s:
            return len(s)

        # We first find the counts of each character in the string. 
        # Any character that has count < k can obviously not figure in the 
        # resultant longest substring. 
        # We therefore split the string on these characters. We recurse on the
        # split sequences to find the biggest one of them to have no character deficits. 
        total_counts = collections.Counter(s)
        deficit_chars = set(x for x in total_counts if total_counts[x] < k)

        if deficit_chars:
            DELIM = ' '
            # replace each deficit_char of the string with a delimiter char
            updated_str = ''.join([DELIM if x in deficit_chars else x for x in s])
            # Split the original string based on the delimiter
            substrings = updated_str.split(DELIM)
            # Return max of the longestSubstrings of all the split substrings
            return max([self.longestSubstring(x, k) for x in substrings])
        # If there are no character deficits, we return length(string)
        return len(s)



s = Solution()
print s.longestSubstring('aaabb', 3)
print s.longestSubstring('ababbc', 2)
print s.longestSubstring("ababacb", 3)
print s.longestSubstring("bbaaacbd", 3)
print s.longestSubstring("baaabcb", 3)
