#https://leetcode.com/problems/multiply-strings/
''' Given two string numbers, multiply them
'''
class Solution(object):
    def multiply(self, num1, num2):
        ''' The key concept in this problem is that when we multiply 2 digits, say num1[i] and num2[j], their product can affect only answer[i+j+1] and answer[i+j]
        Eg: 123*345, 2*5 (which is num1[1] and num2[2] affect only answer[4] and answer[3] which is what we observe in the answer).
        This is easily seen from the usual long-division method.
        '''
        if num1 == '0' or num2 == '0': #If any nubmer is 0 then the product is definitely zero.
            return '0'
        m, n = len(num1), len(num2)
        ans = [0]*(m+n) #When 2 nums of  m digits & n digits are multiplied, their product can at most have (m+n) digits.
        for i in xrange(m):
            for j in xrange(n):
                digit1, digit2 = int(num1[i]), int(num2[j])
                ans[i+j+1] += (digit1*digit2) #Actually digit1*digit2 affects ans[i+j+1] with the digit product carry going to ans[i+j]
                # Using a carry would also mean that we have to propagate the carry forward at each iteration. 
                # We instead perform a lazy carry propagation
        # After all the digit product sums have been calculated, the carry is propagated forwards at the very end.
        for i in xrange(m+n-1, 0, -1):
            ans[i-1] += ans[i]/10
            ans[i]%=10
        res = ''.join(map(str, ans)) #map(str, ans) converts all the answers to strings, which we then join
        return res.lstrip('0') #Removing any leading 0s
s = Solution()
print s.multiply('3', '14')
print s.multiply('123', '456')
print s.multiply('999', '999')
