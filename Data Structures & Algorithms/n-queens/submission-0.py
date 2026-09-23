class Solution:
    def hasDiagonal(self, board, row, col, n):
        r, c = row, col
        while r < n - 1 and 0 < c:
            if board[r+1][c-1] == "Q":
                return True
            r += 1
            c -= 1
        r, c = row, col
        while 0 < r and 0 < c:
            if board[r-1][c-1] == "Q":
                return True
            r -= 1
            c -= 1
        return False
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        def dfs(board, c, n):
            if c == n:
                res.append(["".join(row) for row in board])
                return
            for r in range(n):
                if "Q" not in board[r] and not self.hasDiagonal(board, r, c, n):
                    board[r][c] = "Q"
                    dfs(board, c+1, n)
                    board[r][c] = "."
        dfs(board, 0, n)
        return res

        