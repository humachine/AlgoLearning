#https://leetcode.com/problems/split-array-largest-sum/
''' Given an input array, split it into m different sections so as to minimize the maximum of the sums of each section.

    Inp: [7, 2, 5, 10, 8], m=2
    Out: 18 (7,2,5 & 10,8 are the best splits of the array into 2 parts so that max Sum of the sections is the least)
'''
from bisect import bisect_left, bisect_right
class Solution(object):
    def validSplit(self, nums, m, maxSum):
        ''' We perform a greedy algorithm here to form different sections each with sum < maxLimit.'''
        currSum, count= 0, 1
        for num in nums:
            if currSum + num > maxSum:
                count+=1 #Each time the addition of a number to a section would cause it's sum to shoot over maxSum, we break off that section and increase section count by 1
                currSum = num #Creating a new section that starts with 'num'
                if count > m: # If we already have crossed more than m sections, then we stop
                    return False
            else:
                currSum += num # If it is safe to add 'num' to current section without its sum exceeding maxLimit, go for it.
        return True

    def validSplitBinary(self, nums, m, cumSums, maxSum):
        curr, count, low = maxSum, 0, 0
        while low<len(cumSums):
            low = bisect_right(cumSums, curr, low) # We try to see if we have curr is found in the cumSums list. Say maxSum = 20, we start by searching for 20
            curr = cumSums[low-1] + maxSum #We now add maxSum to cumSums[low-1]. Eg: cumSums[low-1]=18. We next search for 18+20=38 so as not to violate the maxSum criteria
            count+=1
            if count>m:
                return False
        return True

    def splitArray(self, nums, m):
        ''' The least answer we can have is the max of the array. (Since at least one section of the array HAS to contain the maximum and will have sum at least = maximum). 
        The worst answer we can have is the sum of the array (case when m=1)

        We now run a binary search between arrayMax & arraySum. For each candidate during this binary search we check if it can lead to valid split of the array into <= m pieces, each with maxSum < candidate.

        Next we observe that if an array can be split into x(x<=m) portions with each portion having its sum as <= maxSplit, then it's as good as building an m-split array. (some of the portions can be further broken down to give m splits. Since the portions are only getting smaller, the maxSplit limit is not going to breached by breaking any of the portions further smaller.
        '''
        arrayMax, n, cumSums, some = max(nums), len(nums), [], 0
        # Building cumulative sums list
        for i in xrange(n):
            some += nums[i]
            cumSums.append(some)
        arraySum = cumSums[-1]
        left, right = arrayMax, arraySum #We know that the answer lies between arrayMax & arraySum
        while left<right:
            mid = (left+right)/2
            # if self.validSplit(nums, m, mid):
            if self.validSplitBinary(nums, m, cumSums, mid): #If we have a valid split, move right to mid
                right = mid
            else:
                left = mid+1
        return right
s = Solution()
print s.splitArray([7, 2, 5, 10, 8], 2)
