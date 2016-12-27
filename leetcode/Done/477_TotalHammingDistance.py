#https://leetcode.com/problems/total-hamming-distance/
'''
Hamming distance between 2 numbers is the number of btis that differe between the 2 numbers. 
Given an array of N numbers, return summation of all their Hamming Distances.

    Inp: [4,  14, 2]
    Out: 6 (Hamming distance between each of the 3 pairs is 2)
'''
class Solution(object):
    def totalHammingDistance(self, nums):
        ''' Hamming distance between two numbers is the number of bits that differ between them.

        Say x out of n numbers have the ith bit set to 1. This means n-x numbers have the ith bit set to 0.
        For each of these x numbers, their hamming distance with the other n-x numbers increases by 1.
        Nothing is added to the hamming distances of the pairs of numbers both belonging to x (or both belonging to the n-x set)
        '''
        if len(nums) <= 1:  return 0
        bitStrings = [format(x, '064b') for x in nums] #Using 64 bit numbers

        total, n = 0, len(nums)
        for bit in xrange(64):
            oneCount = 0
            for i in xrange(n):
                if bitStrings[i][bit] == '1':
                    oneCount+=1
            # The total hamming distance sum increases by oneCount times the number of numbers who had 0 at this bit
            total += oneCount * (n-oneCount)
        return total
s = Solution()
print s.totalHammingDistance([4, 14, 2])
