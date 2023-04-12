from sympy import per


def permute(nums):
    results = []

    def func(nums, curr_result):
        if len(nums) == 0:
            results.append(curr_result)
            return
        
        for i in range(len(nums)):
            val = nums[i]
            tmp_nums = nums[:i] + nums[i+1:]
            curr_result.append(val)
            func(tmp_nums, curr_result)
    
    func(nums, [])
    return results

permute([1,2 ,3])