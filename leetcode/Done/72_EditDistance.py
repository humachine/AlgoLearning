#https://leetcode.com/problems/edit-distance/
''' Given 2 words w1 & w2, find the edit distance between the 2 words.
Edit distance is given by the minimumber number of insertions/replacements/deletions required to word1 to transform it into word2.

    Inp: abc, de
    Out: 3 (replace, replace, insert)

    Inp: abcde, bcde
    Out: 1 (insert 'a' at the front of w2)
'''
class Solution(object):
    def findChanges(self, word1, word2, dists):
        ''' Here we attempt to retrace our path and find the actual changes that we need to make to transform one word into another.
        '''
        i, j = len(word1), len(word2)
        res = []
        while i>0 and j>0:
            if dists[i][j] == dists[i-1][j-1]: #If there was no edits made, move top-left
                i, j = i-1, j-1
            else:
                byReplacement = dists[i-1][j-1]+1 #Number of edits you would need if your last edit was by replacement
                byDeletion = dists[i-1][j] + 1
                byInsertion = dists[i][j-1] + 1
                if byInsertion == dists[i][j]:  #If the edit distance was with the last edit as an insertion, record the insertion.
                    res.append(('insert', word2[j-1]))
                    j-=1
                elif byDeletion == dists[i][j]: #Record the deletion
                    res.append(('delete', word1[i-1]))
                    i = i-1
                elif byReplacement == dists[i][j]:
                    res.append(('replace', word1[i-1], 'with', word2[j-1]))
                    i, j = i-1, j-1
        while i: #If you still have to add insertions, make them
            res.append(('insert', word1[i-1]))
            i-=1
        while j:
            res.append(('insert', word2[j-1]))
            j-=1
        for opn in res[::-1]:
            print opn


    def minDistance(self, word1, word2):
        if not any([word1, word2]):
            return max(len(word1), len(word2))
        m, n = len(word1), len(word2)
        if m>n:
            word1, word2 = word2, word1
            m, n = n, m

        ''' Let dists[i][j] = minimum number of steps reqd to transform word1[:i] to word2[:j]. If we can compute this, dists[m][n] is the Edit distance between the 2 words

        dists[0][j] = j, for all j
        dists[i][0] = i, for all i

        If word1[i-1] == word2[j-1], then dists[i][j] = dists[i-1][j-1] (i.e no additional edits required).
        If word1[i-1] != word2[j-1] and we replace either of the characters so as to make them equal, dists[i][j] = 1 + dists[i-1][j-1]
        Or say we delete word1[i-1], then dists[i][j] = 1 + dists[i-1][j]
        Say, we insert a character into word1, then dists[i][j] = 1 + dists[i][j-1]
        '''
        dists = [[0]*(n+1) for i in xrange(m+1)]
        dists[0] = range(n+1) # dists[0][j] = j
        for i in xrange(1, m+1):
            dists[i][0] = i # dists[i][0] = i
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # If word1[i-1] and word2[j-1] match, then we haven't introduced any extra edits
                    dists[i][j] = dists[i-1][j-1]
                else:
                    # Corresponding to replacement, insertion, deletion
                    dists[i][j] = 1 + min(dists[i-1][j-1], dists[i][j-1], dists[i-1][j])
        self.findChanges(word1, word2, dists)
        return dists[m][n]

    def minDistanceLessSpace(self, word1, word2):
        # Here we have taken the above O(M*N) solution and brought it down to an O(n) solution using 2 lists of size n each
        if not any([word1, word2]):
            return max(len(word1), len(word2))
        if len(word1)  < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)

        prevRow = range(n+1)
        currRow = [0]*(n+1)

        for i in xrange(1, m+1):
            currRow[0] = i
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    currRow[j] = prevRow[j-1]
                else:
                    currRow[j] = 1 + min(currRow[j-1], prevRow[j], prevRow[j-1])
            prevRow, currRow = currRow, prevRow
        return prevRow[-1]

    def minDistanceLesserSpace(self, word1, word2):
        # Here we have taken the above O(N) solution and brought it further down to just 1 array of size N.
        if not any([word1, word2]):
            return max(len(word1), len(word2))
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)

        currRow = range(n+1)
        for i in xrange(1, m+1):
            prev = currRow[0] #Previous always stores prevRow[j-1] (= dists[i-1][j-1])
            currRow[0] = i
            for j in xrange(1, n+1):
                temp = currRow[j] #dists[i-1][j] is stored into temp to become the next prev
                if word1[i-1] == word2[j-1]:
                    currRow[j] = prev
                else:
                    # currRow[j] is actually prevRow[j], currRow[j-1] is dists[i][j-1] and prev is prevRow[j-1]
                    currRow[j] = 1 + min(currRow[j-1], currRow[j], prev)
                prev = temp # prev is now dists[i-1][j]
        return currRow[-1]
s = Solution()
print s.minDistance('abc', 'de')
print s.minDistance('abcde', 'bcde')
