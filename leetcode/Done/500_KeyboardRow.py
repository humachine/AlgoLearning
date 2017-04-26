#https://leetcode.com/problems/keyboard-row/
'''Given a List of words, return the words that can be typed using letters of alphabet on only one row's of the Qwerty keyboard. 

Inp: ["Hello", "Alaska", "Dad", "Peace"]
Out: ["Alaska", "Dad"]
'''
class Solution(object):
    def findWords(self, words):
        result = []
        TOP, MIDDLE, BOTTOM = 0, 1, 2
        # ROWS contains the letters seen in each row of the keyboard
        ROWS = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for word in words:
            if word:
                row = None
                # We use the first character of the word to determine its intended row.
                if word[0].lower() in ROWS[TOP]:
                    row = TOP
                elif word[0].lower() in ROWS[MIDDLE]:
                    row = MIDDLE
                elif word[0].lower() in ROWS[BOTTOM]:
                    row = BOTTOM
                # We then check if the rest of the word matches the row of the first letter
                for char in word[1:]:
                    if char.lower() not in ROWS[row]:
                        break
                # If all characters belong to the same row (break was not encountered), then append word to result.
                else:
                    result.append(word)
        return result

s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])
