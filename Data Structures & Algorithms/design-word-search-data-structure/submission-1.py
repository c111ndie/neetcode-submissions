class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                if word[j] in cur.children:
                    cur = cur.children[word[j]]
                elif word[j] == ".":
                    for c in cur.children.values():
                        if dfs(j+1, c):
                            return True
                    return False
                else:
                    return False
            return cur.endofWord
        return dfs(0, self.root)
