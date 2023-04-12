from typing import List


class Solution:
    def __init__(self):
        return
    
    def solve(self, matrix, dp, i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        
        value = 0
        for p in [-1, 0, 1]:
            for q in [-1, 0, 1]:
                if (p == 0) and (q == 0):
                    continue
                
                if self.is_valid(i+p, j+q, matrix):
                    if matrix[i][j] > matrix[i+p][j+q]:
                        value = max(
                            value,
                            1+self.solve(matrix, dp, i+p, j+q)
                        )
        dp[i][j] = value
        return value
    
    def is_valid(self, i, j, matrix):
        if (i<0) or (i >= len(matrix)):
            return False
        
        if (j<0) or (j >= len(matrix[0])):
            return False
        
        return True
    
    def longestIncreasingPath(
        self,
        matrix: List[List[int]]
    )-> int:

        dp = [[-1]* len(matrix[0])]* len(matrix)
        max_val = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = self.solve(matrix, dp, i, j) 
                max_val = max(val, max_val)

        return  max_val

def main():
    input_value = [[9,9,4],[6,6,8],[2,1,1]]
    input_value = [[3,4,5],[3,2,6],[2,2,1]]
    solution = Solution()
    ans = solution.longestIncreasingPath(input_value)
    print(ans)

if __name__ == "__main__":
    main()
