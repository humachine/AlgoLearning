#https://leetcode.com/problems/read-n-characters-given-read4/
'''
The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
class Solution(object):
    def read(self, buf, n):
        ''' In this question, we need to keep calling read4() until we have collected n characters OR if the file gets exhausted. Finally, we return the number of characters that we read
        '''
        rem, read, buf4, readSoFar = n, 4, ['']*4, 0
        # While there needs to be characters read AND the file hasn't been exhausted yet
        while rem > 0 and read==4:
            read = read4(buf4)  # Read 4 characters into buf4
            start, end = readSoFar, readSoFar + min(4, rem)
            buf[start:end] = buf4[:min(4, rem)] #put buf4 into the appropriate position at buf
            readSoFar += read if rem>=4 else min(rem, read) #Add the characters read to readSoFar
            rem -= read #Remaining characters goes down by read
        return readSoFar
