#https://leetcode.com/problems/nim-game/
class Solution(object):
    def canWinNim(self, n):
        '''
            Let dp[i] (i>0) denote whether a player making his turn with i stones left in the game will win or not. 
            dp[1]=dp[2]=dp[3]=True (since the player can play 1-3 stones on his turn and win)

            If i is 4, the current player will always lose. 
            If i is 5, 6, 7, the current player can force the next player to 4 and hence win

            Therefore if player 1 starts at 8 coins, Player 2 begins at 5-7 coins which means he can force player 1 to start at 4 coins and lose. 
            Hence Dp[4] = Dp[8] = dp[12] = ... = dp[4k] = False

            More generally, dp[i] = ~(dp[i-1] & dp[i-2] & dp[i-3])
        '''
        return (n & 0b11)!=0
