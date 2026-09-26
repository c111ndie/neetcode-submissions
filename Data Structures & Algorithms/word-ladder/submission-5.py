class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        group = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                group[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        seq = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return seq
                for j in range(len(word)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for nei in group[pattern]:
                        if nei not in visit and nei != w:
                            q.append(nei)
                            visit.add(nei)
            seq += 1
        return 0