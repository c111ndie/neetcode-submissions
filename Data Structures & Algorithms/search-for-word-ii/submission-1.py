class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.endofWord = False
    
class Solution:
    def insert(self, root, word, i):
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.idx = i
        cur.endofWord = True

    
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i in range(len(words)):
            self.insert(root, words[i], i) 
        visit = set()
        def dfs(r, c, root, visit):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] not in root.children:
                return 
            if root.children[board[r][c]].endofWord:
                res.append(words[root.children[(board[r][c])].idx])
                root.children[board[r][c]].endofWord = False
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, root.children[board[r][c]], visit)
            visit.remove((r, c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, visit)
        return res
