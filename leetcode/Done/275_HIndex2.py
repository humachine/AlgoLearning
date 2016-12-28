#https://leetcode.com/problems/h-index-ii/
'''
H-index of a person is h, if a person has h papers with at least h-citations each. 
AND the other n-h papers have at most h citations each. Assume that the input array is sorted

    Inp: [0, 1, 3, 5, 6]
    Out: 3 (3 papers have at least 3 citations each - 3, 6, 5 and the other papers have <= 3 citations each)

    Inp: [0, 1, 4, 5, 6]
    Out: 3 (3 papers have at least 3 citations each - 3, 6, 5 and the other papers have <= 3 citations each)

'''
class Solution(object):
    def hIndex(self, citations):
        if not citations:   return 0
        '''
        We know that the possible candidates for h-index range from 0-n.
        For example, for h-Index 4, we check if the array[-4]>=4 and array[-5]<=4
        If this is true, then 4 is a viable h-index candidate. 

        We perform a binary search for a particular h-Index for which citations[n-hIndex] >= hIndex and citations[n-hIndex-1] <= hIndex
        '''

        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left+right)/2
            hInd = n-mid
            if citations[mid] >= hInd:  #Then we are in the half that contains the best hIndex
                if mid==0 or citations[mid-1] <= hInd:
                    return hInd
                else:
                    right = mid
            else:
                left = mid+1
        return 0


s = Solution()
print s.hIndex([3, 0, 6, 1, 5])
print s.hIndex([1])
print s.hIndex([8, 9, 17])
print s.hIndex([0, 0, 0])
