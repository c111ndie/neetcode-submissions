class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        og_color = image[sr][sc]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visit = set()
        def dfs(r, c):
            image[r][c] = color
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == og_color and (nr, nc) not in visit:
                    dfs(nr, nc)
        dfs(sr, sc)
        return image
        