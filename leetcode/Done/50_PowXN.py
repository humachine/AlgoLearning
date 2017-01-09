#https://leetcode.com/problems/powx-n/
'''
Given x, n return x^n

    Inp: 3, 4
    Out: 81
'''
class Solution(object):
    def findPower(self, x, n):
        if n in self.found: #If already found, we return the found value
            return self.found[n]
        if n%2==0: #If n is even, return x^(n/2) * x^(n/2)
            res = self.findPower(x, n/2)
            self.found[n] = res*res
        else: # If n is odd, return x*(x^n-1)
            res = self.findPower(x, (n-1))
            self.found[n] = x*res
        return self.found[n]

    def myPow(self, x, n):
        ''' We create a dictionary of powers of x that we have computed (memoization) '''
        self.found = {0:1} # x^0 = 1 for all x
        if n<0: # If negative power, we return 1/(x^-n)
            return 1.0/self.findPower(x, -n)
        return self.findPower(x, n)

    def myPowIterative(self, x, n):
        ans, negativePower = 1, n<0
        n = abs(n)
        while n>0:
            if n & 0b1: #If n is odd, multiply ans by x
                ans*=x
            x*=x #x = x*x ; We keep building x as x^(2i), ie x^2, x^4, x^8 etc etc
            ''' For instance if we want x^21 = x^16*x^4*x
            ans*=x occurs when x=x and when x becomes x^4 and again when x=x^16

            And every number > 0, must have at least one 1-bit. Hence ans*=x will occur at least once for any number.
            '''
            n/=2 # We divide n/2, since we are now looking to calculate smaller powers of x

        return ans if not negativePower else 1.0/ans
            
s = Solution()
print s.myPowIterative(3, 4)
print s.myPowIterative(8.88023, -3)
