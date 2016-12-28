#https://leetcode.com/problems/find-the-celebrity/
''' A celebrity is a person who everyone in the party knows, but he knows no one.
    Given the number of people and a function knows(a, b) which returns if A->B, give the index of the celebrity (or -1 if None)
'''
class Solution(object):
    def findCelebrity(self, n):
        ''' In the first pass, we attempt to find a probable candidate. In the second pass, we verify the candidate is an actual celebrity. 
        In the first pass, we begin by checking if a knows -> b. If yes, then a cannot be a celebrity. So b is now the new candidate. We compare b with the next candidate and so on. 
        '''
        cand = 0
        for i in xrange(1, n):
            # If cand knows i, then cand can no longer be a celebrity candidate. i is now the new celebrity candidate
            if knows(cand, i):
                cand = i

        # Checking if all others know cand
        for i in xrange(n):
            if i!=cand and not knows(i, cand):
                return -1
        # Verifying if cand knows nobody else
        for i in xrange(cand):
            if knows(cand, i):
                return -1
        return cand
