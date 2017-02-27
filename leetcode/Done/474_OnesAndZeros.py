#https://leetcode.com/problems/ones-and-zeroes/
'''Given an array of binary strings and m, n - where m & represent the number of
zeros and 1s you have respectively, what is the maximum number of strings you
can build from the array.

Inp: ["10", "0001", "111001", "1", "0"], m = 5, n = 3
Out: 4 (With 5 zeros and 3 ones, we can pick out 10, 0001, 1, 0)

Inp: ["10", "0", "1"], m = 1, n = 1
Out: 2 (We can pick out 0 and 1 using just one one and one zero)
'''
class Solution(object):
    def findMaxForm(self, strs, m, n):
        # counts is a tuple containing the counts of 0s and 1s in the string
        counts = [(x.count('0'), x.count('1')) for x in strs]
        # results[i][j] = #strings that we can pick using i 0s and j 1s using
        # the first k strings
        # We finally return results[m][n] after processing all strings
        results = [[0]*(n+1) for i in xrange(m+1)]
        for zeros, ones in counts:
            for i in xrange(m, -1, -1):
                for j in xrange(n, -1, -1):
                    # DP Recursion:
                    # results[i][j][k] = max(results[i][j][k-1], 1+results[i-zeros][j-ones][k]
                    # To reduce space used, we drop the 3rd dimension (which represents number of strings processed thus far)
                    # This is just an example of 0-1 knapsack problem
                    if i>=zeros and j>=ones:
                        results[i][j] = max(results[i][j],
                                1+results[i-zeros][j-ones])
        return results[m][n]

s = Solution()
print s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
print s.findMaxForm(["10", "0", "1"], m = 1, n = 1)
print s.findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 10)
print s.findMaxForm(["0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 20)
