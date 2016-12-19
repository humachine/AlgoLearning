#https://leetcode.com/problems/first-bad-version/
'''
From n versions [1,2...n], we wish to find the first bad version k. 
All versions>k are automatically assumed to be bad. 

Given an API bool isBadVersion(version), find the first bad version. Minimize number of calls to the API
'''
class Solution(object):
    def firstBadVersion(self, n):
        if n==1:    return n

        left, right = 1, n
        ''' Just a simple binary search approach.
        Beyond a particular k (k<n), all versions are bad. 

        Left moves up ahead until mid is squarely in 'bad' territory. 
        Once mid is in bad, left does not move at all. Instead, right moves closer and closer to left, until they become equal
        '''
        while left < right:
            mid = left + (right-left)/2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left
