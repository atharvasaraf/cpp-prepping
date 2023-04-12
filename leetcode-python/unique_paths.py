def uniquePathsIII(grid) -> int:
    m, n = len(grid), len(grid[0])

    start_index = [
        (x, y)
        for x in range(m)
        for y in range(n)
        if grid[x][y] == 1
    ][0]

    def dfs(row, col, path, results):
        if (
            (row < 0) or (row >= m) or 
            (col < 0) or (col >= n)
        ):
            return

        if grid[row][col] == 2:
            path.append((row, col))
            results.append(path)
            return

        if grid[row][col] == -1:
            return
        
        next_step = [
            [-1, 0], #up
            [1, 0], #down
            [0, -1], #left
            [0, 1], #right
        ]

        for i, j in next_step:
            tmp, grid[row][col] = grid[row][col], -1
            path.append((row, col))
            dfs(row+i, col+j, path, results)
            grid[row][col] = tmp
            path.pop()
        return
    results = []
    # grid[start_index[0]][start_index[1]] = -1

    dfs(
        start_index[0],
        start_index[1],
        [],
        results
    )
    print(results)
    return len(results)

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(
    uniquePathsIII(grid)
)
