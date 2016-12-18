#https://leetcode.com/problems/add-binary/
"""
Inp: a = '11', b = '1'
Out: '100'
"""
class Solution(object):
    def addBinary(self, a, b):
        if not a or not b:
            return a if not b else b
        m, n = len(a), len(b)
        carry = Sum = 0
        ans = []
        for i in xrange(max(m, n)-1, -1, -1):
            Sum = 0
            Sum += carry
            if i<m:
                Sum+= int(a[i])
            if i<n:
                Sum+= int(b[i])
            print Sum
            carry = Sum/2
            Sum = Sum & 1
            ans.append(Sum)
        if carry:
            ans.append(1)
        ans = [str(i) for i in ans]
        return ''.join(ans[::-1])
s = Solution()
print s.addBinary('11', '1')
