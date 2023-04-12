from turtle import back


def exist(board, word):
    def backtrack(row_idx, col_idx, word, visited):
        if len(word) == 0:
            return True
        
        if board[row_idx][col_idx] != word[0]:
            return False
        
        moves = [
            [-1, 0], # up
            [1, 0], # down
            [0, -1], #left,
            [0, 1], #right
        ]
        for move in moves:
            row = row_idx+move[0]
            col = col_idx+move[1]

            if (row < 0) or (col < 0):
                continue
            
            if (row >= len(board)) or (col >= len(board[0])):
                continue
            
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            if backtrack(row, col, word[1:], visited):
                return True
            else:
                visited.remove((row, col))

        return False

    for row_idx, row in enumerate(board):
        for col_idx, start_letter in enumerate(row):
            if start_letter == word[0]:
                visited = set()
                if backtrack(row_idx, col_idx, word, visited):
                    return True

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "SEE"

result = exist(
    board=board,
    word=word
)
print(result)