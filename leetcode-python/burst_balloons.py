def maxCoins(nums):
    n = len(nums)
    dp = {}

    def func(i, j):
        if i < 0:
            return 1
        if j > n-1:
            return 1
        
        if i == j:
            return nums[i]
        
        if (i, j) in dp:
            return dp[(i, j)]
        
        curr_max = 1
        for k in range(i+1, j+1):
            curr_max = max(
                curr_max,
                func(i, k-1)* nums[k]* func(k+1, j)
            )
        dp[(i, j)] = curr_max
        return dp[(i, j)]
    ans = func(0, n-1)

    return ans

nums = [1,5]
maxCoins(nums)

