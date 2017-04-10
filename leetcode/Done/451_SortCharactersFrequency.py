#https://leetcode.com/problems/sort-characters-by-frequency/
'''Given a string, sort it in decreasing order based on the frequency of characters.

Inp: 'tree'
Out: 'eert' ('eetr' is a valid answer too)

Inp: "cccaaa"
Out: 'aaaccc' (or 'cccaaa')

Inp: 'Aabb'
Out: 'bbaA' (case-sensitive)
'''
import collections
class Solution(object):
    def frequencySort(self, s):
        n = len(s)
        c = collections.Counter(s)
        # After putting all the letters into a Counter, we extract the n most_common
        # letters
        freq_letters = c.most_common(n)
        # Finally we join count copies of each letter in freq_letters
        return ''.join([char*cnt for (char, cnt) in freq_letters])

    def frequencySort(self, s):
        c = collections.Counter(s)
        str_li = list(s)
        # After putting all the letters into a Counter, we sort the string by count
        # We resolve ties by the letter's ASCII equivalent so that we group all
        # copies of a letter together
        str_li.sort(key=lambda x: (c[x], ord(x)), reverse=True)
        return ''.join(str_li)

    def frequencySort(self, s):
        # Here we perform a bucket sort of each character, sorted by its frequency
        counts = collections.defaultdict(int)
        max_freq = 0
        for char in s:
            counts[char] += 1
            max_freq = max(max_freq, counts[char])

        result = [[] for i in xrange(max_freq+1)]
        # We add all characters of a frequency to a separate list for each frequency
        for char in counts.keys():
            result[counts[char]].append(char)
        # Finally we join 'freq' copies of each character in descending order
        # of frequencies
        return ''.join([char*i for i in xrange(max_freq, 0, -1) for char in result[i]])


s = Solution()
print s.frequencySort('tree')
print s.frequencySort('aaaccc')
print s.frequencySort('Aabb')
print s.frequencySort("loveleetcode")
