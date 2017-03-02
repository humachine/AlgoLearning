#https://leetcode.com/problems/permutation-sequence/
'''The number 123..n has  n! different permutations of its digits. Given n and
a number k, return the kth permutation (when permutations are in ascending order).

Inp: 3, 5
Out: 312 [123, 132, 213, 231, 312]
'''
class Solution(object):
    def getPermutation(self, n, k):
        if n==1:
            return '1'
        if k==1:
            return ''.join([str(x) for x in range(1, n+1)])
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]

        # With the first digit of the number fixed, we can get (n-1)! possibilities
        # Keeping this in mind, we try changing the first digit of the number, 
        # until we find we need to find less than (n-1)! permutation.
        count, digit = 0, 1
        while count + factorials[n-1]<k:
            digit+=1
            count+=factorials[n-1]

        # We now look for the k-count permutation from (n-1) digits
        perm = list(self.getPermutation(n-1, k-count))
        for i in xrange(n-1):
            # All digits that are greater than $digit are incremented by 1, to 
            # match with the actual permutation
            if int(perm[i]) >= digit:
                perm[i] = chr(ord(perm[i])+1)
        return str(digit)+''.join(perm)

s = Solution()
print s.getPermutation(3, 5)
print s.getPermutation(3, 2)
