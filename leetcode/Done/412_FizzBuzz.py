#https://leetcode.com/problems/fizz-buzz/
class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in xrange(1, n+1):
            # If number divisible by both 3 and 5, return FizzBuzz
            if i%15 == 0:
                res.append('FizzBuzz')
            # If number divisible by 3, return Fizz
            elif i%3 == 0:
                res.append('Fizz')
            # If number divisible by 5, return Buzz
            elif i%5 == 0:
                res.append('Buzz')
            # If number not divisible by 3 or 5, return the number itself
            else:
                res.append(str(i))
        return res
