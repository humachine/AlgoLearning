#https://leetcode.com/problems/gray-code/
'''Given a number N representing the number of bits in a code, return A gray code
sequence for the N bits.
Note: In a gray code seequence, consecutive number of the sequence must differ by 
exactly one bit.

Inp: 2
Out: [0, 1, 3, 2] (00->01->11->10)
     [0, 2, 3, 1] is also a valid answer.
'''
class Solution(object):
    def findCodes(self, number, used, sequence, n):
        '''number: list(int), represents the current binary number that we have.
        used: set(), set of numbers that have already appeared in the sequence
        sequence: list, the gray code sequence
        '''
        # If we have used up all n-bit numbers, we return
        if len(used) == 2**n:
            return True

        # val is the current number's numerical value.
        val = int(''.join(map(str, number)), 2)
        valid_code = False
        for digit in xrange(n-1, -1, -1):
            bit, old_val = number[digit], val
            new_bit = 1-bit
            # Updating the value of the number after the bit flip
            val = val - (bit<<(n-1-digit)) + (new_bit<<(n-1-digit))

            # If this value hasn't already appeared in the sequence, add it
            # to the sequence and see if it results in a valid sequence eventually.
            if val not in used:
                number[digit] = new_bit
                used.add(val)
                sequence.append(val)
                if self.findCodes(number, used, sequence, n):
                    valid_code = True
                    break
                # If this number didn't result in a valid sequence, backtrack and try another value.
                sequence.pop()
                used.remove(val)
                number[digit] = bit

            # Restoring the changes made to value
            val = old_val
        return valid_code

    def grayCode(self, n):
        # Here, we start with a beginning seed number (in this case 0x0)
        # We try flipping each bit of the number. While doing so, we also check
        # if the new number is already a part of the sequence. 
        # If so, we flip back this bit and move on to the next bit until we
        # finally find a bit that can lead to a valid gray code
        number, used, sequence = [0]*n, {0}, [0]
        self.findCodes(number, used, sequence, n)
        return sequence

    def grayCode(self, n):
        # Gray codes also called reflected binary codes can be formed by 
        # appending gray codes of the previous bitlength after 0. And then 
        # adding '1'+grayCodes of previous bitlength to get a new gray code

        # Eg: n = 2, gray code = [00, 01, 11, 10]
        # For n=3, grayCode = [000, 001, 011, 010]+[110, 111, 101, 100]
        # This essentially 0+each of GC(2) + 1+GC(2)[::-1]
        if not n:
            return [0]
        prev_seq = ['']
        for i in xrange(n):
            seq = ['0'+x for x in prev_seq]
            seq.extend(['1'+x for x in prev_seq[::-1]])
            prev_seq = seq
        # Convert all the sequences back to integers
        return [int(x, 2) for x in prev_seq]

s = Solution()
print s.grayCode(2)
print s.grayCode(1)
print s.grayCode(5)
print s.grayCode(3)
print s.grayCode(0)
