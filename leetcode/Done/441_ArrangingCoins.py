#https://leetcode.com/problems/arranging-coins/
"""
    Inp: 4
    Out: 2 [*; **]

    Inp: 0
    Out: 0

    Inp: 6
    Out: 3 [*; **; ***]
"""
class Solution(object):
    def arrangeCoins(self, n):
        #Solve the equation k*(k+1)/2 <= n
        #Solve for equality case and return int(solution to eqn)
        ans = (8*n-1)**0.5
        return int((ans-1)/2)
