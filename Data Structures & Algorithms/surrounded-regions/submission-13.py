class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        row, col = len(board), len(board[0])
        def dfs(r, c):
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O"):
                    continue
                dfs(nr, nc)
        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row-1][c] == "O":
                dfs(row-1, c)
        for r in range(1, row-1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col-1] == "O":
                dfs(r, col-1)
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
        