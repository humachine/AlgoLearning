#https://leetcode.com/problems/minimum-size-subarray-sum/
def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0

    left, right, addedSum = 0, 0, 0
    ans = len(nums)
    while left < len(nums):
        if addedSum <s and right<len(nums)-1:
            addedSum += nums[right];
            right+=1
        else:
            ans = min(ans, right-left+1)
            left+=1
            if left<len(nums):
                addedSum -= nums[left]
    return ans

print(minSubArrayLen(4, [1, 4, 4]))
