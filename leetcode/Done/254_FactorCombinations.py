#https://leetcode.com/problems/factor-combinations/
'''Given an integer, return all possible combinations of factors.

Inp: 8
Out: [[2, 2, 2], [2, 4]]

Note: All factors must be >= 1 and < the input number
'''
class Solution(object):
    def backTrack(self, num, res, curr_path, prev):
        # If the factors multiply up to the input number and path_length > 1,
        # then we are sure that it's not the single factor = input number
        # We hence add a copy of the current path to the result
        if num == 1 and len(curr_path)>1:
            res.append(list(curr_path))
            return

        # Since we are looking for non-decreasing factors, we always start searching
        # from the previous factor upto sqrt(num)+1 (both inclusive)
        # int(num**0.5)+1 = sqrt(num)+1. We use int(num**0.5)+2 since the range function
        # has a non-inclusive interval endpoint
        for i in xrange(prev, int(num**0.5)+2):
            if num%i == 0:
                curr_path.append(i)
                self.backTrack(num/i, res, curr_path, i)
                curr_path.pop()

        # We also individually execute the case where the number itself is a factor.
        # We check if int(num**0.5)+1<num, just to ensure that we don't backtrack
        # on num, if it has already been covered in the above loop.
        if num >= prev and int(num**0.5)+1 < num:
            curr_path.append(num)
            self.backTrack(1, res, curr_path, num)
            curr_path.pop()


    def getFactors(self, n):
        # Here, we backtrack on finding all the factors of a number (and it's factors)
        # recursively. We ensure that the factors are always non-decreasing.
        res = []
        self.backTrack(n, res, [], 2)
        return res

s = Solution()
print s.getFactors(4)
print s.getFactors(8)
print s.getFactors(12)
print s.getFactors(32)
