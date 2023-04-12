def fourSum(nums, target):

    def func(idx, n, t, curr_nums, results):
        if (n == 0) and (t == 0):
            results.append(curr_nums.copy())
            
