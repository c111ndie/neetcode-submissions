class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        def diag(r, c):
            i, j = r, c
            while 0 <= r and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            return True
        def dfs(c):
            if c == n:
                res.append(["".join(row) for row in board])
                return
            for r in range(n):
                if "Q" not in board[r] and diag(r, c):
                    board[r][c] = "Q"
                    dfs(c+1)
                board[r][c] = "."
        dfs(0)
        return res
            