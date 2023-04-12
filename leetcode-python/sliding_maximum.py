def maxSlidingWindow(nums, k):
    q = []

    for i in range(k):
        while len(q) and (q[-1] < nums[i]):
            q.pop()
        q.append(nums[i])
    
    ans = []
    for i in range(k, len(nums)):
        ans.append(q[0])
        new_val = nums[i]
        while len(q) and (q[-1] < new_val):
            q.pop()
        q.append(new_val)

        if nums[i-k] == q[0]:
            q = q[1:]
    ans.append(q[0])
    return ans

nums = [9,10,9,-7,-4,-8,2,-6]
k = 5
maxSlidingWindow(
    nums=nums,
    k=k
)

