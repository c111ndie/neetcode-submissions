class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        visit = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O" or (r, c) in visit:
                    continue
                region = []
                q = deque()
                surrounded = True
                q.append((r, c))
                visit.add((r, c))
                while q:
                    qr, qc = q.popleft()
                    region.append((qr, qc))
                    if qr == 0 or qc == 0 or qr == rows - 1 or qc == cols - 1:
                        surrounded = False
                    for dr, dc in directions:
                        nr, nc = qr + dr, qc + dc
                        if  0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in visit:
                            q.append((nr, nc))
                            visit.add((nr, nc))
                if surrounded:
                    for rr, cc in region:
                        board[rr][cc] = "X"
                    

        