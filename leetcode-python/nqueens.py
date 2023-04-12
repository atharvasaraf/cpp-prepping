def solveNQueens(n):
    
    def is_valid(r, c, board):
        for i in range(len(board)):
            if (board[i][c] == "Q") or (board[r][i] == "Q"):
                return False
            
            if (r-i > 0) and (c-i > 0) and (board[r-i][c-i] == "Q"):
                return False
            
            if (r-i > 0) and (c+i < len(board)) and (board[r-i][c+i] == "Q"):
                return False
        return True


    def backtrack(row, col, queens, board, results):
        if queens == 0:
            ans_board = ["".join(row) for row in board]
            results.append(ans_board)
            return

        if row == n:
            return
        
        if col == n:
            backtrack(row+1,0,queens,board,results)
        
        for r in range(row, n):
            for c in range(col, n):
                if board[r][c] == "." and (is_valid(r, c, board)):
                    board[r][c] = "Q"
                    backtrack(row, col+1, queens-1, board, results)
                    board[r][c] = "."

        return

    board = [["." for _ in range(n)] for _ in range(n)]
    results = []
    backtrack(0, 0, n, board, results)
    print(results)
    return

if __name__ == "__main__":
    solveNQueens(3)