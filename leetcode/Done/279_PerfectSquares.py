#https://leetcode.com/problems/perfect-squares/
'''Given a positive integer n, find the least number of perfect square numbers
which sum up to n.

Inp: 12
Out: 3 (4+4+4)
'''
class Solution(object):
    def numSquares(self, n):
        # squares[i] = min number of squares required to sum up to i
        squares = [0]+range(1, n+1)
        for i in xrange(2, n+1):
            # For each i, squares[i] = min(squares[i], 1+squares[i-j*j]) as long as i-j*j >= 0
            sq_rt = int(i**0.5)
            for j in xrange(1, sq_rt+1):
                squares[i] = min(squares[i], 1+squares[i-j*j])
        # Below we print out ONE of the possible ways in which perfect squares
        # sum up to n in the least number of such squares
        # We just retrace the DP table back from squares[n] to squares[0]
        # num = n
        # while num > 0:
            # sq_rt = int(num**0.5)
            # for j in xrange(1, sq_rt+1):
                # if squares[num] == 1+squares[num-j*j]:
                    # num = num-j*j
                    # print j*j, 
                    # break
        # print 
        return squares[-1]

    def numSquares(self, n):
        # This is a BFS solution where we see the number of levels required to reach
        # n starting from the 0th level comprising of all square numbers <= n
        sq_rt = int(n**0.5)
        # squares represents all the nodes in the base level.
        # targets is all the nodes in the current level.
        # we descend levels until targets & squares have some overlap. At the 
        # time of overlap, the number of levels descended (or ascended) is the
        # minimum numSquares
        squares = [i*i for i in xrange(1, sq_rt+1)]
        targets, count = {n}, 0

        while targets:
            count += 1
            next_level = set()
            # For each node in this level, if there's some overlap with a node
            # of the base level, then we have touched the base level. 
            # Else, we populate the next level and recurse.
            for target in targets:
                for sq in squares:
                    if target == sq:
                        return count
                    elif target < sq:
                        break
                    next_level.add(target-sq)
            targets = next_level
        return count
        
s = Solution()
print s.numSquares(12)
print s.numSquares(14)
print s.numSquares(1535)
print s.numSquares(43)
