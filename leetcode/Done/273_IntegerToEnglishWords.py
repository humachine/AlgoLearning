#https://leetcode.com/problems/integer-to-english-words/
''' Given an integer convert it to english words. 
    Inp: 123
    Out: "One Hundred Twenty Three"
    Inp: 12345
    Out: "Twelve Thousand Three Hundred Forty Five"
    Inp: 1234567
    Out: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
class Solution(object):
    def numToWords(self, n):
        hundreds, tens, units, res = n/100, (n%100)/10, n%10, []

        digitStrs = ' One Two Three Four Five Six Seven Eight Nine'.split(' ')
        teenStrs = 'Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tenStrs = '  Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(' ')

        if hundreds:
            res.extend([digitStrs[hundreds], 'Hundred'])
        if tens>0:
            res.append(teenStrs[units] if tens==1 else tenStrs[tens])
        if units>0 and tens!=1:
            res.append(digitStrs[units])
        return ' '.join(res)

    def numberToWords(self, num):
        ''' To convert a number into its English form, we perform 2 tasks. We first divide the number into sets of 3 digits and convert 3 digits at a time into an English string.
        Then we append multipliers as and when required.
        '''
        thousandMultipliers = ['', 'Thousand', 'Million', 'Billion']
        ans, res = [], []
        while num:
        # For each set of 3 digits, we convert it into a English string and put it into a list
            ans.append(self.numToWords(num%1000))
            num/=1000

        # For all the valid set of 3digits we have, we attach multipliers wherever required
        for multiplier in xrange(len(ans)):
            # If we have a valid multiplier and we have a non-zero 3digits, we add prefix + number
            if thousandMultipliers[multiplier] and ans[multiplier]:
                res.extend([thousandMultipliers[multiplier], ans[multiplier]])
            # If we only have a non-zero 3 digits, then we add just the string of the 3-digits
            elif ans[multiplier]:
                res.append(ans[multiplier])
        # We finally reverse all the strings and prefixes and join them
        englishNumber = ' '.join(res[::-1])

        return englishNumber if englishNumber else 'Zero'

s = Solution()
print s.numberToWords(25)
print s.numberToWords(123456789)
print s.numberToWords(1230009)
print s.numberToWords(1000010)
print s.numberToWords(123)
print s.numberToWords(0)
print s.numberToWords(12345)
