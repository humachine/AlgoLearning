#https://leetcode.com/problems/counting-bits/
''' Given n, calculate the number of 1 bits that all numbers from 0-n have.

    Inp: n=5
    Out: [0, 1, 1, 2, 1, 2]
'''
class Solution(object):
    def countBits(self, num):
        ''' For eg 7 = 4+3. Which means bin(7) = '1'+bin(3)
        This is the same for values from 4-7. bin(x) = '1'+bin(x-4)
        
        We perform a similar logic to generate binary values for numbers from
        8-15 and 16-31 and ...
        '''
        if num <= 1:
            return [0] if num==0 else [0, 1]

        res, loc, size = [0, 1], 0, 2 #Size represents the size of the window
        # Loc to Loc+size represents a sliding window. 
        # bin(x) = 1+bin(x-size)
        for i in xrange(2, num+1):
            res.append(res[loc]+1) #binary(i) = 1+binary(loc)
            loc+=1
            if loc==size: #If we have used up a window, double the window size
                size = size * 2
                loc = 0
        return res

s = Solution()
print s.countBitsConcise(5)
