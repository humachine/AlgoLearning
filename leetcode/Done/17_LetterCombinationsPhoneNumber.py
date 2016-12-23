#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
''' Given a digit string, return all possible T9 word combinations
    Inp: '23'
    Out: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
'''
# Note: The non-BT approach uses O(len(result)) amount of space in every iteration
# The BT approach uses only O(len(inputDigits)) amount of STACK space in every iteration.
class Solution(object):
    def letterCombinations(self, digits):
        digitMap = {'0': ' ', '1':'*', '2':'abc', '3':'def', '4':'ghi',
                '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:  return []

        '''Brute force over all possible digit combinations
        Begin l1 as a list containing empty string. For each digit, we add the letter combinations of that digit to every single string in l1. And set the new list back to l1
        '''
        l1 = ['']
        for digit in digits:
            l1 = [x+char for char in digitMap[digit] for x in l1]

        return l1

    def backTrack(self, digits, digitMap, ind, currentStr, result):
        '''
        We start with an empty string. At each level, add a digit combination and recurse. 
        When the recursion has covered all digits, add the final string to result.

        Backtrack and remove this digit combination and try the next combination
        '''
        if ind == len(digits):
            result.append(''.join(currentStr))
            return
        for char in digitMap[digits[ind]]:
            currentStr.append(char)
            self.backTrack(digits, digitMap, ind+1, currentStr, result) 
            currentStr.pop()

    def letterCombinationsBT(self, digits):
        digitMap = {'0': ' ', '1':'*', '2':'abc', '3':'def', '4':'ghi',
                '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:  return []
        result = []
        self.backTrack(digits, digitMap, 0, [], result)
        return result

s = Solution()
print s.letterCombinationsBT('23')
