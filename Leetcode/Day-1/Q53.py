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
    max_array = current_array = nums[0]
    for i in range(1, len(nums)):
        

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = max_noncontinue_elements(nums)
print(result)