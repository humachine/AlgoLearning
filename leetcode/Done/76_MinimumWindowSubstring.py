#https://leetcode.com/problems/minimum-window-substring/
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T.

    Inp: "ADOBECODEBANC","ABC"
    Out: "BANC"
'''
from collections import defaultdict, Counter
class Solution(object):
    def minWindow(self, s, t):
        if not t: return 0

        charCounts = defaultdict(int)
        #Build Character Counts Map
        charCounts = Counter(t)
        start = end = head = tail = 0
        counter, minLen = len(t), len(s)+1

        while end < len(s):
            # If charCount is >0, then we haven't yet seen enough of this character
            # Every time we come across charCounts[s[end]]>0, we know that this is still a valid character of t that NEEDS to be accounted for in s. So, we decrement missing by 1
            # If for instance we decremented missing by 1 even if charCounts[s[end]] was < 0, then we would reach counter=0 even without covering all the unique characters.
            # Eg: ABDBEEE, ABC. Counter starts at 3 and decrements to 0 after encountering 1A & 2B which is INCORRECT
            if charCounts[s[end]]>0:
                counter-=1

            # Each time we see a character, its character counts go down
            charCounts[s[end]]-=1
            end+=1

            # Counter = 0 is hit when all the characters have been seen atleast the amount of times they appeared in t
            while counter==0:
                # If you have a new minLength string, we update the head and tail of the result
                if end-start < minLen:
                    head, tail = start, end
                    minLen = end-start

                # Keep incrementing counts for each character we see
                charCounts[s[start]] += 1
                # If any counts shoot past zero, then you know you haven't covered all the characters of t. You update counter to 1 
                if charCounts[s[start]] > 0:
                    counter+=1
                start+=1
        return s[head:tail] if minLen != len(s)+1 else ''


                    
s = Solution()

print s.minWindow('ADOBECODEBANC', 'ABC')
print s.minWindow('ADOBEBODEBANA', 'ABC')
