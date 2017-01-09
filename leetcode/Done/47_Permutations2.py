#https://leetcode.com/problems/permutations-ii/
''' Given a set of numbers (may contain duplicates), return all valid unique permutations of the numbers.

    Inp: [1, 1, 2]
    Out: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
'''
class Solution(object):
    def findPermutations(self, arr, currPath, used, res):
        if len(currPath) == len(arr): #If we've reached end of the permutation, add it to the result
            res.append(list(currPath))
            return

        for i in xrange(len(arr)):
            if used[i]: #If this element has already been used, don't reuse it
                continue
            if i>0 and arr[i-1] == arr[i] and not used[i-1]: #If this element is same as its previous, use it only if the previous element was ALSO used. 
                continue
            currPath.append(arr[i])
            used[i] = True
            self.findPermutations(arr, currPath, used, res)
            used[i] = False
            currPath.pop()


    def permuteUnique(self, nums):
        ''' In a typical backtracking solution, we pick diffferent starting elements for the permutation, find sequences from that; backtrack, change the starting element; and recurse
        '''
        res, currPath, used = [], [], [False]*len(nums)
        self.findPermutations(sorted(nums), currPath, used, res)
        return res

    def permuteUniqueIterative(self, nums):
        perms = [[]] #perms contains the list of permutations using the first k numbers of nums
        for num in nums:
            newPerms = []
            for perm in perms:
                for i in xrange(len(perm)+1): #We want len(perm) + 1 spots where we can insert the new number. (len(perm)-1 spots between 2 existing elements) + 1 spot before all elements and 1 spot AFTER all elements.
                    # There's no use inserting an element in a position that's after the same element. (eg: inserting 3 after an existing 3 is no different from inserting the new 3 BEFORE the existing 3
                    if i>0 and num==perm[i-1]:
                        break
                    newPerms.append(perm[:i] + [num] + perm[i:])
            perms = newPerms
        return perms
s = Solution()
inp = [2, 2, 1, 1]
out = s.permuteUnique(inp)
print out
# assert len(out) == 6
inp = [1, 1, 2]
out = s.permuteUnique(inp)
print out
# assert len(out) == 3
inp = [0,1,0,0,9]
out = s.permuteUnique(inp)
assert len(out) == 20
inp = [-1,2,0,-1,1,0,1]
out = s.permuteUnique(inp)
print len(out), sorted(inp)
