#https://leetcode.com/problems/text-justification/
'''
Given a sequence of words and a width, put them into a text justified lines.
'''
class Solution(object):
    def _justifyLine(self, words, startInd, endInd, numChars, maxWidth):
        ''' Justifies a line of text given the words and maxWidth '''
        extraSpaces = maxWidth - numChars # Extra spaces that need to be added to this line
        numGaps = max(0, endInd-startInd-1) # The number of gaps between words
        line = words[startInd]

        for i in xrange(startInd+1, endInd):
            line += ((extraSpaces+numGaps-1)/numGaps + 1)*' ' # We add ceil(extraSpaces/numGaps)+1 number of spaces between each word. The +1 is for the standard single space that needs to be added between words by default.
            line += words[i]
            extraSpaces -= (extraSpaces+numGaps-1)/numGaps #decrement the no of extraSpaces and gaps we have
            numGaps -= 1
            
        return line + ' '*(maxWidth-len(line)) #Add any extra spaces to fill up the line

    def fullJustify(self, words, maxWidth):
        if not maxWidth or not words: return ['']

        TOTAL_WORDS, result = len(words), []

        # Find Number of words & numChars to put into a particular line
        numChars, start = len(words[0]), 0
        for i in xrange(1, TOTAL_WORDS):
            # If the current word can be fit on the current line, then add it
            if numChars + 1 + len(words[i]) <= maxWidth:
                numChars += 1 + len(words[i])
            else:
                # If you can't fit any more words, then justify this line
                result.append(self._justifyLine(words, start, i, numChars, maxWidth))
                start, numChars = i, len(words[i]) # Reset start and numChars for the next line

        # All the words that didn't go on the previous line go on the last line
        # Since the last line doesn't need justification (aka doesn't need extra spaces anywhere), we pass numChars=maxWidth
        result.append(self._justifyLine(words, start, TOTAL_WORDS, maxWidth, maxWidth))
        return result

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
print s.fullJustify(words, 16)
