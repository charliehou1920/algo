# 53 Maximum Subarray
'''
Given an integer array nums, 
find the subarray with the largest sum, and return its sum.
'''

def maxSubArray(nums):
    total_sum = sum(nums)
    result = nums
    for num in nums:
        if total_sum - num > total_sum:
            result.remove(num)

    return sum(result)

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubArray(nums)
print(result)