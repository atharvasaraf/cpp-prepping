def consecutiveNumbersSum( n):
    consecutive_sums = set()
    total = 1
    curr_sum = 0
    i = 0
    while i < n:
        consecutive_sums.add(curr_sum)
        i += 1
        curr_sum += i
        if (curr_sum - n) in consecutive_sums:
            total += 1
    return total


consecutiveNumbersSum(5)