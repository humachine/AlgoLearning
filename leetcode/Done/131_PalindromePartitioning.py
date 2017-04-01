#https://leetcode.com/problems/palindrome-partitioning/
'''Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible partitionings.

Inp: 'aab'
Out:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def _isPalindrome(self, string, start, end):
        '''Routine to check if string[start:end] is a palindrome.'''
        is_pal, left, right = True, start, end-1
        while left<right:
            if string[left]!=string[right]:
                is_pal = False
                break
            left, right = left+1, right-1
        return is_pal

    def getPartitions(self, s, start, curr_path, res):
        # If we have consumed the entire string, then we just add the current path to the result
        if start == len(s):
            res.append(list(curr_path))
            return
        for right in xrange(start, len(s)):
            # If s[start:right+1] is a palindrome, then add it to the path
            # Recurse on rest of the string before backtracking
            if self._isPalindrome(s, start, right+1):
                curr_path.append(s[start:right+1])
                self.getPartitions(s, right+1, curr_path, res)
                curr_path.pop()
            
    def partition(self, s):
        res = []
        self.getPartitions(s, 0, [], res)
        return res

s = Solution()
print s.partition('aab')
