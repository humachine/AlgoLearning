#https://leetcode.com/problems/add-binary/
"""
Inp: a = '11', b = '1'
Out: '100'
"""
class Solution(object):
    def addBinary(self, a, b):
        total = carry = 0
        i, j = len(a)-1, len(b)-1
        res = []

        # As long as there are digits on either number (or carry remaining), 
        # use them up
        while carry or i>=0 or j>=0:
            term1 = i>=0 and int(a[i])
            term2 = j>=0 and int(b[j])

            total = term1 + term2 + carry
            res.append(total%2)

            carry = total/2
            i, j = i-1, j-1

        # Reverse the list and convert to a string
        return ''.join([str(x) for x in res[::-1]])

s = Solution()
assert s.addBinary('11', '1') == '100'
assert s.addBinary('101111', '10') == '110001'
