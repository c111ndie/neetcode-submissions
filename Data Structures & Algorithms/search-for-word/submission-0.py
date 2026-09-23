class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or board[row][col] != word[i] or (row, col) in visited:
                return False
            
            visited.add((row, col))
            found = (dfs(row + 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col - 1, i + 1))
            visited.remove((row, col))
            return found
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
            
        return False
            
                
            
                
        