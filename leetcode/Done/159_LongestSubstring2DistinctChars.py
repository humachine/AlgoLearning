#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''Given a string, return the length of the longest substring that has at most
2 distinct characters.

Inp: 'eceba'
Out: 2 (ece is the longest such substring)
'''
import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s:
            return 0
        max_len = left = right = 0


        # curr = (most recently seen distinct character, last/most recent index of that character in the CURRENT substring
        # prev = (2nd most recently encountered distinct character, last seen position when prev[0] was seen in the current substring, i.e s[left:right+1]

        # We try all possible ending locations of a substring (i.e right: 0->n)
        # For each right pointer, we check if our current left pointer can result
        # in a valid string. If not, we update the left boundary of the string
        # to the last location at which the prev[0] was seen

        prev, curr = ['', -1], ['', -1]
        # We initialize prev, curr to ['', -1] so that they get initialized automatically
        for right, char in enumerate(s):
            # If character is curr, then we just update the last-seen pointer
            if char == curr[0]:
                curr[1] = right
            # If character is prev, then we update the last-seen pointer
            # We also swap prev & curr, since prev is now the most-recently seen character
            elif char == prev[0]:
                prev[1] = right
                prev, curr = curr, prev
            # If we see a 3rd distinct character, we first update left to after
            # the last seen location of prev.
            # We then discard prev and overwrite it with curr
            # curr is then updated to the newly seen character.
            else:
                left = prev[1]+1
                prev = curr
                curr = [char, right]

            max_len = max(max_len, right-left+1)
        return max_len

s = Solution()
print s.lengthOfLongestSubstringTwoDistinct('eceba')
print s.lengthOfLongestSubstringTwoDistinct('abaccc')
