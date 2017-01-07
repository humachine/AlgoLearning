#https://leetcode.com/problems/permutations/
'''Given a set of distinct numbers, return all permutations of these numbers.

    Inp: [1, 2, 3]
    Out: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''
class Solution(object):
    def generatePermutations(self, nums, start, permutation, res):
        if start == len(nums): #If all the numbers of the sequence have been used up then we add this permutation to the result
            res.append(list(permutation))
        for i in xrange(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start] #Swap nums[i] with nums[start] and permute the rest
            permutation.append(nums[start]) #Adding nums[start] to the permutation list
            self.generatePermutations(nums, start+1, permutation, res)
            nums[start], nums[i] = nums[i], nums[start] # Restoring the nums array
            permutation.pop() #Popping the recently added number from the permutation.

    def permute(self, nums):
        res = []
        self.generatePermutations(nums, 0, [], res)
        return res

    def permuteIterative(self, nums):
        ''' In this iterative solution, we begin with an empty permutation. 
        As we process  a number, we insert it into each of the previous permutations at every possible position. 
        Then we update these newly gernated permutations as the permutations list
        '''
        perms = [[]] #perms contains the list of permutations using the first k numbers of nums
        for num in nums:
            newPerms = []
            for perm in perms:
                for i in xrange(len(perm)+1): #We want len(perm) + 1 spots where we can insert the new number. (len(perm)-1 spots between 2 existing elements) + 1 spot before all elements and 1 spot AFTER all elements.
                    newPerms.append(perm[:i] + [num] + perm[i:])
            perms = newPerms
        return perms

s = Solution()
print s.permute(range(1, 4))
print s.permute([])
print s.permute([1])
