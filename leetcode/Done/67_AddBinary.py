#https://leetcode.com/problems/add-binary/
"""
Inp: a = '11', b = '1'
Out: '100'
"""
class Solution(object):
    def addBinary(self, a, b):
        if not a or not b:
            return a if not b else b
        m, n = len(a)-1, len(b)-1
        carry = Sum = 0
        ans = []

        #If characters exist in either string, use them
        #Or if carry is non-zero, use it
        # Finally invert the string and return
        while carry>0 or m>=0 or n>=0:
            Sum = carry

            if m>=0:
                Sum += int(a[m])
                m-=1

            if n>=0:
                Sum+= int(b[n])
                n-=1

            carry = Sum/2
            Sum = Sum & 1
            ans.append(Sum)

        ans = map(str, ans)
        return ''.join(ans[::-1])
s = Solution()
print s.addBinary('11', '1')
print s.addBinary('101111', '10')
