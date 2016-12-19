#https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""
    For array of size n, all elements of array between 1 <= arrayElement <= n
    Inp: [4, 3, 2, 8, 7, 3, 5, 4]
    Out: [3, 4]
"""
class Solution(object):
    def findDuplicates(self, nums):
        duplicates = []
        """ If you find a number, set array[num-1] to be negative.
        If you come across a negative number, then you know it's a duplicate.

        Essentially we're using the sign of the number to be a flag for whether you've seen it or not
        """
        for i, el in enumerate(nums):
            if nums[abs(el)-1] < 0:
                duplicates.append(abs(el))
            else:
                nums[abs(el)-1] *= -1
        nums = [abs(x) for x in nums] #Restoring nums to original state
        return duplicates
    def findDuplicatesSwap(self, nums):
        i = 0
        ''' We try to bring each number to its rightful position in the array through a series of swaps. For instance, we try to bring number 3 to array[2], number 8 to array[7] and so on. 
        If a number nums[i] is already equal to the number at its rightful location, then we don't do anything. 
        Else, we swap nums[i] with nums[nums[i]-1]. This way, nums[i] has now reached its appropriate location (i.e, nums[i]-1). We now repeat the same procedure with the new number at nums[i].

        Finally, any number that is out of place and not in its rightful position is a duplicate.
        '''
        while i < len(nums):
            if nums[i] == nums[nums[i]-1]:
                i+=1
            else:
                ind = nums[i]-1
                nums[i], nums[ind] = nums[ind], nums[i]
        return [nums[i] for i in xrange(len(nums)) if nums[i]!=i+1]

s = Solution()
print s.findDuplicatesSwap([4, 3, 2, 8, 7, 3, 4, 5])
