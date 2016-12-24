#https://leetcode.com/problems/subsets/
'''
Given an array of distinct integers, return all possible subsets of the array
    
    Inp: [1, 2, 3]
    Out: [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]
'''
class Solution(object):
    '''
    In this class, we describe 3 varieties of approaching the same problem
    '''

    def subsetsRecursive(self, nums, start):
        # Say, we have all the subsets from numbers i+1->n, then subsets using numbers i->n is subsets(i+1->n) + [nums[i]] or subsets(i+1->n)
        # This is because, for each number we can have a set of subsets which do not contain that number and another set which contains the number
        if start == len(nums):
            return [[]]
        # Smaller subsets represents the subsets obtained by just using numbers nums[start+1..n]
        smallerSubsets = self.subsetsRecursive(nums, start+1)
        # currSubset is obtained by appending the current number to all previous subsets
        currSubset = [x + [nums[start]] for x in smallerSubsets] if smallerSubsets else [[nums[start]]]
        # we finally return the currSubsets (subsets that contain the current number) + smallerSubsets (past subsets which DO not contain the current number)
        return smallerSubsets + currSubset

    def subsets(self, nums):
        # Here, we recurse and try to compute all the subsets
        if not nums:
            return [[]]
        return self.subsetsRecursive(nums, 0)
    
    def subsetsIterative(self, nums):
        # We start out with an empty set. At each point, we add a new number to all elements of the current set and append them to the current set
        # [[]] 
        # [[], [1]]
        # [[], [1], [2], [1, 2]] and so on...
        sets = [[]]
        for i in xrange(len(nums)):
            numSets = len(sets)
            for j in xrange(numSets):
                sets.append(sets[j]+[nums[i]])
        return sets

    def subsetsBinary(self, nums):
        '''
        We can use binary numbers to represent a subset.
        A binary number of length N will represent a unique subset. (1s for number that are present in the subset and 0s for numbers NOT present in subset)
        0x0 will be the null set

        We iterate from 0..2^n and obtain a subset each time and append that to answer
        In a small modification, we obtain the subset for a string slightly differently
        '''
        if not nums:
            return [[]]
        n = len(nums)
        numSubSets = 2**n
        sets = [[] for x in xrange(numSubSets)]
        for i in xrange(len(nums)):
            # For all the subsets where the ith bit is 1, we append nums[i] to sets[j]
            for j in xrange(numSubSets):
                if j>>i & 1: #Checking if the ith bit of the jth subset is 1. If yes, we append nums[i] to sets[j]
                    sets[j].append(nums[i])
        return sets

s = Solution()
print s.subsetsIterative([1, 2, 3])
print s.subsets([1, 2, 3])
print s.subsetsBinary([1, 2, 3])
