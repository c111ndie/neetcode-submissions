class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        cur.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row, col = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        trie = Trie()
        for i in range(len(words)):
            trie.insert(words[i], i)
        res = []
        visit = set()
        def dfs(root, r, c):
            if not (0 <= r < row and 0 <= c < col and board[r][c] in root.children and (r, c) not in visit):
                return
            if root.children[board[r][c]].word:
                res.append(words[root.children[board[r][c]].idx])
                root.children[board[r][c]].word = False
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(root.children[board[r][c]], nr, nc)
            visit.remove((r, c))
        for r in range(row):
            for c in range(col):
                dfs(trie.root, r, c)
        return res

            
                
            
            
        
        