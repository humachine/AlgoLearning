#https://leetcode.com/problems/dungeon-game/
'''
-2 -3  1
-5 -10 3
10 30 -5 

Out: 7 (The lowest health needed to navigate through the dungeon and come out alive is 7 (-2, -3, 1, 3, -5). If he starts with 7 health, he'll finish with >0 (1 health) and hence be alive at the end.
Note: The PathSums from -2, -5, 10, 30, -5 is 28 >> -6, but the lowest health reached on this path is much lower

 1 -3  3
 0 -2  0
-3 -3 -3
Out: 3 (1, -3, 3, 0, -3 needs only a starting health of 3 to reach the bottomRight alive)

Out: 
'''
from collections import namedtuple
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        if not dungeon: return 0
        m, n = len(dungeon), len(dungeon[0])
        ''' In this problem, we need to calculate the health we need to start with so as to make it out of the dungeon alive
        Let healthTable[i][j] = minHealth required to start from (i, j) and reach the end of the dungeon alive

        healthTable[i][j] = min(max(1, healthTable[i][j+1] - dungeon[i][j]), max(1, healthTable[i+1][j]-dungeon[i][j]))
        From any (i, j), we have 2 paths (right & Down). Of the two paths, we pick the path that needs us to have the least healthto start from i, j
        '''
        healthTable = [ [0 for j in xrange(n)] for i in xrange(m)]
        # If the last cell is +ve, you just need to have 1 health when you start that cell
        # If the last cell is -ve, you need to have one more than the health you'd lose in that cell
        healthTable[m-1][n-1] = max(0, -dungeon[m-1][n-1])+1

        # For the right most and bottom columns, we can initialize values since they have only one path to take
        # If you need, say 8 health to begin the next cell and make it out alive and if your current cell has a health orb giving +5 health, then you need to have just 8-5=3 health to begin this cell. 
        # Similary if your current cell has demons who robs -7 health from you, then you need to have 8-(-7)=15 health to begin this cell.
        # This said, if your current cell has a health orb of +20, you cannot have 8-20=-12 health to begin this cell, since you need to be alive at all points. Hence, we perform max(1, nextMinimumHealth - healthBoostOrLossFromThisCell)
        for i in xrange(m-2, -1, -1):
            healthTable[i][n-1] = max(1, healthTable[i+1][n-1] - dungeon[i][n-1])
        for j in xrange(n-2, -1, -1):
            healthTable[m-1][j] = max(1, healthTable[m-1][j+1] - dungeon[m-1][j])

        # At each cell, we can take 2 paths. We compute the minimum health needed to begin a cell (i, j) if we want to go down and stay alive AND if we want to go right and stay alive. We then take the minimum of those 2 paths

        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                right, below, orbs = healthTable[i][j+1], healthTable[i+1][j], dungeon[i][j]
                # healthTable[i][j] = min(max(1, right - dungeon[i][j]), max(1, below - dungeon[i][j]))
                healthTable[i][j] = max(min(right, below) - dungeon[i][j], 1) #This line is equivalent to the above line
        return healthTable[0][0]


    def calculateMinimumHPConcise(self, dungeon):
        if not dungeon: return 0
        m, n, INTMAX = len(dungeon), len(dungeon[0]), 2**31
        # healthTable is filled with INTMAX except for the last element which is set to 1
        healthTable = [INTMAX]*(n-1) + [1]


        '''
        In this beautiful O(n) space solution, we use a slightly tweaked formula
        Traditionally, we perform max(min(below, right) - orb, 1). For the bottom most row, there's no below. 
        Imagine we add a new row at the bottom, which would be filled with INT_MAX
        max(min(INT_MAX, right)-...  would still give us the same result

        Instead of having a table for the BFS, we instead just maintain a single row (that represents the level BELOW the current level)
        max(min(below, right)... -> max(min(row[currentLoc], right))
        This can be further boiled down to max(min(row[currentLoc:currentLoc+2]) ... 

        Python slicing respects the list boundaries. range(5)[3:8] will not throw error but just give you [3, 4]
        '''
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                # Once we compute a row of healthTable, it becomes the below row for the next row
                healthTable[j] = max(min(healthTable[j:j+2]) - row[j], 1)
        return healthTable[0]
s = Solution()
inp = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
# inp = [[1,-3,3], [0,-2,0], [-3,-3,-3]]
print s.calculateMinimumHPConcise(inp)
# print s.calculateMinimumHP(inp)

