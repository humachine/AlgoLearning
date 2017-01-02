#https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
'''Given an api Read4(), construct a function read(n) which reads n characters into a buffer by using read4()
Now, given that read() can be called multiple times, how can you improve the function?

    Inp: read(1); File contents - "abcd"
    Calling read4() will return abcd. 
    Since we require only 1 character, we can return 'a', 1.

    Since read() can be called multiple times, calling read(5) the next time returns '', 0 since the file pointer has already reached the end of the array. The read(5) should return 'bcd', 3 as the output instead.
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
class Solution(object):
    def __init__(self):
        # We store all leftovers in this instance string
        self.leftOvers = ''

    def read(self, buf, n):
        # readSoFar - #useful characters read so far
        # rem - #characters remaining to reach target of n
        readSoFar, rem, buf4, read = 0, n, ['']*4, 4
        if self.leftOvers:
            numLeftOvers = len(self.leftOvers)
            toBeUsed = min(numLeftOvers, rem) # If there exist leftovers, use all of it unless requirement is < numLeftOvers

            buf[:toBeUsed] = self.leftOvers[:toBeUsed] # Use up as much characters as is required
            readSoFar, rem = readSoFar+toBeUsed, rem-toBeUsed 

            self.leftOvers = self.leftOvers[toBeUsed:] if toBeUsed < numLeftOvers else ''
            # If not even numLeftOvers characters were consumed, update the leftovers

        while rem>0 and read == 4:
            # While characters are still required and EOF was not hit, read4()
            read = read4(buf4)
            toBeUsed = min(read, rem) #Of the buf4 read, use as much as is required

            buf[readSoFar:readSoFar+toBeUsed] = buf4[:toBeUsed]
            rem, readSoFar = rem-toBeUsed, readSoFar+toBeUsed

            if toBeUsed < read: #If even the buf4 was not entirely used up, update the remaining as leftovers
                self.leftOvers = buf4[toBeUsed:read]

        return readSoFar
