#https://leetcode.com/problems/count-and-say/
'''
All sequences start with '1'
1 is one 1 = 11
11 is two 1s = 21
21 is one 2 one 1 = 1211
1211 is one 1 one 2 two 1s = 111211

Given a number n, return the nth number string in this sequence.
''' 
class Solution(object):
    def findNextSequence(self, curr):
        res = [1, curr[0]]
        for i in xrange(1, len(curr)):
            # If the current digit is same as the previous, increment the count of the previous digit
            if curr[i] == res[-1]:
                res[-2]+=1
            # Else, add a separate new count for the current digit
            else:
                res.extend([1, curr[i]])
        return res

    def countAndSay(self, n):
        seq = [1]
        # Keep generating new sequences N-1 times
        for i in xrange(n-1):
            seq = self.findNextSequence(seq)
        return ''.join([str(x) for x in seq])

s = Solution()
print s.countAndSay(5)
