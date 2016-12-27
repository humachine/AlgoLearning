#https://leetcode.com/problems/paint-fence/
'''
Given a fence with N posts which can each be painted in k colors. 
Return total number of ways to paint the fence.

    Inp: n=3, k=2
    Out: 6 (Say the colors are R & B. RRB, RBR, RBB, BRR, BRB, BBR)
'''
class Solution(object):
    def numWays(self, n, k):
        if not n:  return 0
        # If only 1 post, then there are k ways of coloring it
        if n == 1: return k
        '''
        identical_numWays represents the number of ways you can color the posts seen if you have colored the previous 2 posts in the same color. diff_numWays is the number of coloring ways when the previous 2 posts have DIFFERENT colors.

        identical_numWays[n+1] = diff_numWays[n]*1 way (You have exactly ONE choice of color to pick if you want it to be the same as the previous color)
        diff_numWays = diff_numWays[n]*(k-1) + identical_numWays[n]*(k-1) (Pick any of the remaining k-1 colors so as not to match the preivous color)
        '''
        identical_numWays, diff_numWays = k, k*(k-1)
        for i in xrange(2, n):
            identical_numWays, diff_numWays = diff_numWays, (diff_numWays + identical_numWays)*(k-1)
        # Finally count both diff_numWays+identical_numWays
        return identical_numWays+diff_numWays
s = Solution()
print s.numWays(3, 3)
