#https://leetcode.com/problems/lonely-pixel-i/
'''Given a picture consisting of black and white pixels, find the number of black lonely pixels.
A lonely pixel is one which is the only pixel of its color on both its row and column.

Inp:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Out:
3 (All 'B's are lonely pixels in this case)
'''
class Solution(object):
    def findLonelyPixel(self, picture):
        # In this straightforward solution, we just maintain counts of the number
        # of black pixels in each row and column.
        # We run through the entire array once again to see if there are any
        # lonely pixels
        if not picture:
            return 0
        m, n = len(picture), len(picture[0])
        cols = [0]*n
        rows = [0]*m
        lonely_pixel_count = 0
        for i in xrange(m):
            for j in xrange(n):
                # rows[] & cols[] have the counts of 'B' in each row & column.
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        for i in xrange(m):
            # If there is more than 1 row on this row, it can't have any lonely pixels.
            if rows[i]!=1:
                continue
            for j in xrange(n):
                # If this column also has only 1 pixel and it's a picture, then
                # it is a lonely pixel.
                if cols[j]==1 and picture[i][j]=='B':
                    lonely_pixel_count+=1
        return lonely_pixel_count

    def findLonelyPixel(self, picture):
        # This is a space optimization of the above solution reducing space
        # reqmts from O(M+N) to O(M) [or O(N), if required]
        m, n = len(picture), len(picture[0])
        cols = [0]*n
        lonely_pixel_count = 0
        for i in xrange(m):
            for j in xrange(n):
                # Maintaining only counts of one dimension (cols, in this case)
                if picture[i][j] == 'B':
                    cols[j] += 1

        for i in xrange(m):
            count, pos = 0, None
            for j in xrange(n):
                if picture[i][j] == 'B':
                    count, pos = count+1, j
            # If there was exactly 1 B in this row and only 1 B in that column, 
            # then we have a lonely pixel
            if count==1 and cols[pos]==1:
                lonely_pixel_count+=1
        return lonely_pixel_count

    def findLonelyPixel(self, picture):
        m, n = len(picture), len(picture[0])
        lonely_pixel_count = 0
        invalid_rows, invalid_cols = [False]*m, [False]*n

        for row in xrange(m):
            # If this row has already been ininvalidated, we move on to the next row.
            if invalid_rows[row]:
                continue
            count, col = 0, None
            for j in xrange(n):
                if picture[row][j] == 'B':
                    count, col = count+1, j
                    # If we have more than one 'B' on this row, then every column that has a 'B' is ininvalid
                    if count>1:
                        invalid_cols[col] = True
                        invalid_cols[j] = True

            if count==1 and not invalid_cols[col]:
                lonely = True
                for i in xrange(row+1, m):
                    # If we see another 'B' on the rest of the column, every row with a 'B' is invalid.
                    if picture[i][col] == 'B':
                        invalid_rows[i] = True
                        lonely = False
                if lonely:
                    lonely_pixel_count+=1
                invalid_cols[col] = True
        return lonely_pixel_count

s = Solution()
inp = [['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
print s.findLonelyPixel(inp)
inp = ["BBB","BBB","BBB"]
print s.findLonelyPixel(inp)
print s.findLonelyPixel(["BBB"])
inp = ["BBWBWBBBBW","WBWBBWWWWB","WBBBWWBWWB","WWWWWWWBWW","WBBWWWBBWB","BBBBWBWBWB","WWBBBWBWWB","BWWBBWWWWW","BWBWWBWBBW","BBBBWWWBBW"]
print s.findLonelyPixel(inp)
