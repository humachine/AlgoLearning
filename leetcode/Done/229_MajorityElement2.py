#https://leetcode.com/problems/majority-element-ii/
''' Given an unsorted array of numbers, find the majority elements in the array (appear more than int(n/3) times). 

    Inp: [2, 2, 3, 2, 3]
    Out: 2

    Inp: [2, 2, 2, 3, 3, 3, 3, 3, 2]
    Out: 3
'''
class Solution(object):
    def majorityElement(self, nums):
        ''' NOTE: Boyer Moore Voting Algorithm requires that if count of a candidate hits ZERO, we switch candidates.
        '''
        if not nums:    return []
        cand1, cand2 = -1, -2 #Arbitrarily set two candidates. If they indeed are candidates, their counts will get updated. Else, candidates will get updated
        ct1, ct2 = 0, 0
        for num in nums:
            if num == cand1: #If num is equal to either candidate, increment appropriate count
                ct1+=1
            elif num == cand2:
                ct2+=1
            elif ct1==0: #If count is zero, then this candidate is due a change
                cand1, ct1 = num, 1
            elif ct2==0:
                cand2, ct2 = num, 1
            else: #If both candidates have healthy counts, we chip away at their majority.
                ct1-=1; ct2-=1;
        ct1, ct2, reqdCount = 0, 0, len(nums)/3
        for num in nums:
            ct1+= (num==cand1)
            ct2+= (num==cand2)
        cands, cts = [cand1, cand2], [ct1, ct2]
        res = [cands[i] for i in [0, 1] if cts[i]>reqdCount] #Finding the candidates who have above reqdCount majority
        return res

s = Solution()
print s.majorityElement([1, 1, 1, 2, 2, 2])
print s.majorityElement([1,1,1,3,3,2,2,2])
print s.majorityElement([1,1,1,2,3,4,5,6])
print s.majorityElement([1, 2, 3, 4])
print s.majorityElement([2, 2, 3, 2, 3, 2, 3])
print s.majorityElement([2, 2, 2, 3, 3, 3, 3, 3, 2])
