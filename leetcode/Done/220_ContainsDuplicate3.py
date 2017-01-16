#https://leetcode.com/problems/contains-duplicate-iii/
'''Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

    Inp: [3, 7, 18, 6, 12], t=2, k=3
    Out: True (7 and 6 are <= 2 apart and their indices differ by <= k)
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        '''Imagine if each element was a date of the year and we had to find two dates who were <= 30 days apart and had indices <= k.
        Now, we can shoehorn each number into an appropriate bucket(month).
        For a date1 to have another date2 within 30 days of it, date2 has to lie in the same month as date1 or the previous or next months.

        Note: At any point in the algorithm, if 2 dates enter the same bucket(month), then we return True. Hence we can be sure that each month contains at max only one date.

        Given a number, we first find the bucket that the number falls into. We then search in that bucket and the adjacent two buckets for candidate elements. Of these candidates, any candidate which is within 't' difference of the number, is a nearby duplicate.
        '''
        # abs(nums[i] - nums[j])>=0 for any i, j. Hence, t<0 can never result in duplicates
        if t<0:
            return False
        buckets = {}

        def findBucket(x):
            # If t==0, give each number its own bucket
            if t==0:
                return x
            # 0..5 goes to bucket 0. Hence you want -5...0 to go to the bucket -1
            if x < 0:
                return (x+1)/t - 1
            return x/t

        for i, num in enumerate(nums):
            bucket = findBucket(num)
            # Find all valid buckets that you could search from
            search_buckets = filter(lambda x: x in buckets, [bucket-1, bucket, bucket+1])
            for buck in search_buckets:
                # If there's an element in the neighbouring/same bucket within the last k-indices and the element is less than t distance apart, we have a duplicate.
                if abs(num-nums[buckets[buck]])<=t:
                    return True
            buckets[bucket] = i

            # Remove element that just fell out of the k-window
            if i>=k:
                buckets.pop(findBucket(nums[i-k]), None)
        return False

s = Solution()
print s.containsNearbyAlmostDuplicate([3, 7, 45, 6, 12], 2, 3)
print s.containsNearbyAlmostDuplicate([-1,-1], 1, -1)
print s.containsNearbyAlmostDuplicate([2, 1], 1, 1)
print s.containsNearbyAlmostDuplicate([0,10,22,15,0,5,22,12,1,5], 3, 3)
