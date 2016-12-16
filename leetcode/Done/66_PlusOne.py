#https://leetcode.com/problems/plus-one/
"""Test cases:
    Inp: [1, 3, 4]
    Out: [1, 3, 5]

    Inp: [9, 9, 9, 9]
    Out: [1, 0, 0, 0, 0]
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = digits[:]
        #While you encounter 9s at the right, keep turning them to zeros
        #If you encounter a non-9 digit, increment it and return
        #If all the digits you've encountered are 9s, insert 1 at the front
        #Instead of inserting 1 at the front, we change the first digit to 1 and append an extra zero a the back
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0]=1
        digits.append(0)
        return digits

s = Solution()
print s.plusOne([9, 9, 9, 9])
print s.plusOne([1, 3, 4])
