#https://leetcode.com/problems/ugly-number-ii/
'''Given n, return the nth ugly number.
An ugly number is a positive integer whose only prime factors are from 2, 3, 5.

Inp: n=10
Out: 12 (1, 2, 3, 4, 5, 6, 8, 9, 10, 12 are the first 10 ugly numbers)
'''
class Solution(object):
    def nthUglyNumber(self, n):
        num2, num3, num5 = 2, 3, 5
        ind2, ind3, ind5 = 0, 0, 0
        ugly = [1]*n
        # Clearly, only multiples of 2, 3 and 5 are going to be ugly numbers.
        # Further more, only ugly numbers multiplied by 2, 3 or 5 are going
        # to be ugly numbers.
        # We start building up an ugly number list. At each point, ugly[i]*2, 
        # ugly[i]*3 and ugly[i]*5 are going to be future ugly numbers.
        for i in xrange(1, n):
            # num2, num3 and num5 are each numbers which are obtained by
            # multiplying a prior ugly number by 2, 3 or 5.
            ugly[i] = min(num2, num3, num5)
            # If num2 is the current ugly number, update index of num2
            # Also, get the next ugly number based on num2's index
            if num2 == ugly[i]:
                ind2 += 1
                num2 = ugly[ind2]*2
            # We do 3 if conditions instead of if-elif to avoid duplicates.
            # For instance if both num2 and num3 = 6, then both num2 and num3
            # get updated to their next multiples respectively.
            if num3 == ugly[i]:
                ind3 += 1
                num3 = ugly[ind3]*3
            if num5 == ugly[i]:
                ind5 += 1
                num5 = ugly[ind5]*5
        return ugly[-1]
s = Solution()
print s.nthUglyNumber(11)
for i in xrange(1, 11):
    print s.nthUglyNumber(i)
