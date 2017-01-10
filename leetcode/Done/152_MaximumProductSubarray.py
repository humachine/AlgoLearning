#https://leetcode.com/problems/maximum-product-subarray/
'''
Given an array of numbers, return the maximum product of any subarray.

    Inp: [2, 3, -2, 4]
    Out: 6 (2*3)

    Inp: [2, 3, -2, 4, -5]
    Out: 240 (product of all elements)
'''
class Solution(object):
    def maxProduct(self, nums):
        # maxProd refers to the best current running product we have
        # minProd refers to the least current running product we have
        # 
        # If all numbers of the array are positive, the product just keeps accumulating in maxProd
        maxProd = minProd = overallMax = nums[0]
        for i in xrange(1, len(nums)):
            num = nums[i]
            # for both maxProd & minProd below, we either pick between a previous product*num, or start a new subarray product with just 'num'
            if num > 0:  #If number is positive, maxProd = max(prevMaxProd*num, num)
                maxProd = max(maxProd*num, num)
                minProd = min(minProd*num, num)
            else:
                # If number is negative, maxProd = previous minProd *num
                # Say, previous minProd was negative, current maxProd becomes positive
                # If previous minProd was +ve, current maxProd becomes negative
                # Say, the next number is +ve, next maxProd becomes next num
                # Even if the next number is -ve, next maxProd becomes curr minProd*next num > 0
                maxProd, minProd = minProd*num, min(maxProd*num, num)
                # minProd = min(previous maxProd * num, num). We perform a min with num to avoid cases where maxProd itself was -ve (could happen if first element of array was -ve
            overallMax = max(overallMax, maxProd)
        ''' NOTE: The above algorithm even works on fractional numbers.
        '''
        return overallMax

s = Solution()
# print s.maxProduct([2, 3, -2, 4])
# print s.maxProduct([2, 3, -2, 4, -5])
print s.maxProduct([2,-5,-2,-4,3])
# print s.maxProduct([0.8, 1.4, -0.8, 7.9, 0.4, -6.5])
