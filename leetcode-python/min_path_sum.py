grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
] 
def func(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if (j == n-1) and (i == m-1):
                dp[i][j] = grid[i][j]
            elif i == m-1:
                dp[i][j] = grid[i][j] + dp[i][j+1]
            elif j == n-1:
                dp[i][j] = grid[i][j] + dp[i+1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
    
    return dp[0][0]

print(func(grid))