# 53 Maximum Subarray
'''
Given an integer array nums, 
find the subarray with the largest sum, and return its sum.
'''

def max_noncontinue_elements(nums):
    total_sum = sum(nums)
    result = nums
    for num in nums:
        if total_sum - num > total_sum:
            result.remove(num)

    return sum(result)

def maxSubArra(nums):
    max_sum = current_sum = nums[0]
    for i in nums[1:]:
        current_sum = max(i, current_sum + i)
        max_sum = max(current_sum, max_sum)
    return max_sum    

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubArra(nums)
print(result)  