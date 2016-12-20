#https://leetcode.com/problems/product-of-array-except-self/
'''
    Inp: [1, 2, 3, 4]
    Out: [24, 12, 8, 6]
'''
class Solution():
    def productExceptSelf(self, nums):
        if not nums:    return []
        result = []
        prod = 1
        # We first compute the running product
        # result[i] = product of all numbers 0..i (i excluded)
        for x in nums:
            result.append(prod)
            prod *= x

        # We now compute the running product from the left
        # prod at a particular i = product of all numbers from i+1..len(nums)
        prod = 1
        for i in xrange(len(nums)-1, -1, -1):
            # Final answer is product of all numbers before it * product of all numbers after it
            result[i] *= prod
            prod *= nums[i]
        return result

s = Solution()
print s.productExceptSelf([1, 2, 3, 4])
