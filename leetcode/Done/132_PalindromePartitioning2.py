#https://leetcode.com/problems/palindrome-partitioning-ii/
'''Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum number of cuts required for a palindrome partitioning

Inp: 'aab'
Out:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n <= 1:
            return 0
        # In addition to the DP below, we use optimized code for 0/1 cut cases.
        if s == s[::-1]:
            return 0
        # Exactly 1 cut case
        for i in xrange(n):
            if s[:i] == s[:i][::-1] and  s[i:] == s[i:][::-1]:
                return 1
        # cuts[i] represents the worst case number of cuts required for the first
        # i characters of s. We use 1+cuts[i-x] during the minCut computation. 
        # But, if i-x=0, then there was no prior cut. Hence 1+cuts[i-x] should be zero,
        # since s[:i+x] is the first palindrome of the entire string. 
        # To avoid using extra if conditions for the first cut of a string, we 
        # initialize cuts[0] to -1
        cuts = range(-1,n)
        for i in xrange(n):
            # Each value of i represents the mid-point of a palindrome that we
            # are trying to build around.
            j = 0
            # Try to build bigger and bigger palindromes around each possible i
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                # For each palindrome that's built from i-x to i+x, we update
                # cuts[i+x+1] (+1 because cuts[j] represents the min cuts for a string of length j)
                # We update cuts[i+x+1] with 1+cuts[i-x] if 1+cuts[i-x] is lesser.
                cuts[i+j+1] = min(cuts[i+j+1], 1+cuts[i-j])
                j+=1

            j = 1
            # Try to build even-length palindromes around i
            while i-j+1>=0 and i+j<n and s[i-j+1]==s[i+j]:
                cuts[i+j+1] = min(cuts[i+j+1], 1+cuts[i-j+1])
                j+=1
        return cuts[-1]


s = Solution()
print s.minCut('aab')
print s.minCut('ab')
print s.minCut("ababababababababababababcbabababababababababababa")
print s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
print s.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
