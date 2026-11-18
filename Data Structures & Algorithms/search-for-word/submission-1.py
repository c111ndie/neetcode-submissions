class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        row, col = len(board), len(board[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < row and 0 <= c < col and board[r][c] == word[i]) or (r, c) in visit:
                return False
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i+1) == True:
                    return True
            visit.remove((r, c))
            return False
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
            
            