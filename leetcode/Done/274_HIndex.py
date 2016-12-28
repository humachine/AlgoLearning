#https://leetcode.com/problems/h-index/
'''
H-index of a person is h, if a person has h papers with at least h-citations each. 
AND the other n-h papers have at most h citations each

    Inp: [3, 0, 6, 1, 5]
    Out: 3 (3 papers have at least 3 citations each - 3, 6, 5 and the other papers have <= 3 citations each)

    Inp: [4, 0, 6, 1, 5]
    Out: 3 (3 papers have at least 3 citations each - 3, 6, 5 and the other papers have <= 3 citations each)
'''
class Solution(object):
    def hIndexSort(self, citations):
        if not citations:   return 0
        citations.sort()
        '''
        We know that the possible candidates for h-index range from 0-n.
        We sort the array first. We traverse the array from the back, each time increasing h-index.
        For example, for h-Index 4, we check if the array[-4]>=4 and array[-5]<=4
        If this is true, then 4 is a viable h-index candidate. 

        We proceed until, we hit an h-Index for which array[-hIndex] < hIndex. Since it's roted in ascending order, we know that for any greater hIndex, array[-hIndex] will always be < hIndex. Hence we terminate the search at this point
        '''

        hInd, n = 0, len(citations)
        candidate = 0
        # Running through all possible h-indices
        for hInd in xrange(1, n+1):
            if citations[-hInd] >= hInd:
                # Checking if candidate is viable or not
                if hInd == n or citations[-hInd-1] <= hInd:
                    candidate = hInd
            # If we have citations[-hInd] < hInd, then it will be true for all greater hInd. Hence, we know that there will be no more candidates produced in this search.
            else:
                break
        return candidate


    def hIndex(self, citations):
        if not citations:   return 0
        n = len(citations)
        counts = [0]*(n+1)

        # Counts contains the counts of each number. 
        # Counts[-1] contains the counts of all numbers >= n
        for cite in citations:
            if cite>=n:
                counts[-1]+=1
            else:
                counts[cite]+=1

        greaterCount = 0
        for hInd in xrange(n, -1, -1):
            greaterCount+=counts[hInd]
            # If at a particular hInd, you have >= hInd number of papers with >= hInd citations, then return hInd
            # Since we are visiting hInd in decreasing order, the first hInd that matches our requirements will be the best hInd possible
            if greaterCount >= hInd:
                return hInd
        return 0


s = Solution()
print s.hIndex([3, 0, 6, 1, 5])
print s.hIndex([1])
print s.hIndex([8, 9, 17])
