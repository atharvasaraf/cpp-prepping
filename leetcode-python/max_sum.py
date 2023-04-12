def maxSubArray(nums) -> int:
    l = 0
    curr_sum = 0
    max_sum = 0
    while l < len(nums):
        if nums[l] > curr_sum:
            
            curr_sum = 0
        curr_sum += nums[l]
        max_sum = max(max_sum, curr_sum)
        l += 1
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)
