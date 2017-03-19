#https://leetcode.com/problems/word-pattern-ii/
''' Given a pattern and a string str, find if there exists a bijection between
each letter of pattern and a non-empty substring of str.

Inp: "abab", "redblueredblue"
Out: True.
'''
class Solution(object):
    def findPattern(self, pattern, p_st, string, str_st, mapping, rev_map):
        m, n = self.m, self.n
        # If both strings have been exhausted, then we have a consistent mapping
        if p_st==m and str_st==n:
            return True
        # If either string was exhausted before the other, we have some inconsistency
        if p_st == m or str_st==n:
            return False

        valid_pattern = False
        sub_str = ''
        char = pattern[p_st]

        # If the current character already has a mapping, we try to check
        # if the same mapping is possible again.
        if char in mapping:
            word = mapping[char]
            # If same mapping is not possible, we return False, since this
            # character's mapping is inconsistent
            if string[str_st:str_st+len(word)] != word:
                valid_pattern = False
            # If the same mapping is possible, we recurse on the rest of the
            # string vs the next character of the pattern
            else:
                valid_pattern = self.findPattern(pattern, p_st+1, string,
                        str_st+len(word), mapping, rev_map)
        
        # If the current character has no mapping, we try to create one
        else:
            for i in xrange(str_st, n):
                sub_str += string[i]
                # If the current substring does not already belong to some
                # other character's mapping, we try it out. 
                if sub_str not in rev_map:
                    mapping[char] = sub_str
                    rev_map.add(sub_str)
                    # If this character's mapping can lead to a full valid mapping
                    # of the entire string, we return True
                    if self.findPattern(pattern, p_st+1, string, i+1, mapping, rev_map):
                        valid_pattern = True
                        break
                    # If the current substring didn't lead to a valid mapping, 
                    # we then delete this mapping and go on to try out bigger
                    # substrings for this character's mapping.
                    del mapping[char]
                    rev_map.remove(sub_str)
        return valid_pattern

    def wordPatternMatch(self, pattern, str):
        # In this problem, we pick a substring for each character of pattern.
        # We then continue on the rest of the string checking if this mapping
        # could lead to valid string mapping.
        # If it doesn't, we backtrack and try a bigger substring for the current
        # character and continue.
        # If no lenght of substrings can lead to a valid mapping, we return False.
        self.m, self.n = len(pattern), len(str)
        mapping, rev_map = {}, set()
        ans = self.findPattern(pattern, 0, str, 0, mapping, rev_map)
        return ans

s = Solution()
print s.wordPatternMatch('abab', 'redblueredblue')
print s.wordPatternMatch('d', 'ef')
print s.wordPatternMatch('', '')
print
print s.wordPatternMatch('ab', 'aa')
print s.wordPatternMatch('', 'a')
print s.wordPatternMatch('b', '')
