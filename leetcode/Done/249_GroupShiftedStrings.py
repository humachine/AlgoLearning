#https://leetcode.com/problems/group-shifted-strings/
'''Given a set of strings, group all strings that belong to the same shifting sequence.

Inp: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Out: [
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
import collections
class Solution(object):
    def groupStrings(self, strings):
        # For each string, we find its tuple of shifts. We use a hashtable to
        # group similar shifted strings together.
        groups = collections.defaultdict(list)
        for string in strings:
            # shifts is a tuple of the differences of each character from the
            # string's first character. We use tuples since they are hashable.
            shifts = tuple([ (ord(c)-ord(string[0])) % 26 for c in string])
            shifts = self.stringShifts(string)
            groups[shifts].append(string)
        return groups.values()

s = Solution()
Inp = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print s.groupStrings(Inp)
