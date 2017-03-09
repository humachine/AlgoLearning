#https://leetcode.com/problems/can-i-win/
'''In a game, two players take turns adding, to a running total, any integer from 1..maxChoosableInteger. The player who first causes the running total to reach or exceed desiredTotal wins.
Note: Integers cannot be reused in the game.

Inp: 10, 11
Out: False (No matter what Player 1 plays, player 2 can play an unused number
to make the total go past 11)

Inp: 3, 5
Out: True (Player 1 can play 1 to start with. No matter what player 2 plays, player
1 can play the other number to cross the total of 5)
'''
class Solution(object):
    def winPossible(self, max_int, total, used):
        used_tuple = tuple(used)
        # If already we have computed the result for this total with these number
        # choices, we return the precalculated result.
        if (total, used_tuple) in self.cache:
            return self.cache[(total, used_tuple)]
        win = False
        for num in xrange(max_int, 0, -1):
            # If number is not used, then we are free to play this number choice now.
            if not used[num-1]:
                used[num-1] = True
                # If by playing this number, we cross the desiredTotal
                # (i.e total -> <=0), then we win this game
                if total - num <= 0:
                    result = False
                else:
                # Else, we just try to see what happens to the other player
                # when he plays with the reduced option set to cross total-num
                    result = self.winPossible(max_int, total-num, used)
                # We restore the option usage, so that we can try out other
                # options later.
                used[num-1] = False
                # If the other player lost, then this player certainly wins
                if not result:
                    win = True
                    break
        self.cache[(total, used_tuple)] = win
        return win

    def canIWin(self, maxChoosableInteger, desiredTotal):
        # We make Player1(P1) play every possible move he has. Corresponding to 
        # each of those moves, we observe if P2 is forced to lose. If any of P1's
        # moves forces P2 to lose, then P1 will definitely win always

        # If sum of all integer choices < desiredTotal, then P1 can never win. 
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        self.cache = {}
        # used represents the numbers that have been used so far by either 
        # player in the current game.
        used = [False]*maxChoosableInteger
        return self.winPossible(maxChoosableInteger, desiredTotal, used)

s = Solution()
print s.canIWin(10, 11)
print s.canIWin(3, 5)
print s.canIWin(18, 50)
print s.canIWin(18, 79)
print s.canIWin(18, 171)
