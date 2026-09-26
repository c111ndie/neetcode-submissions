class Solution:
    def stringDiff(self, str_a, str_b):
        cnt = 0
        for i in range(len(str_a)):
            if str_a[i] == str_b[i]:
                continue
            else:
                cnt += 1
        return cnt

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        visit = set()
        seq = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return seq
                for w in wordList:
                    if w not in visit and self.stringDiff(w, word) == 1:
                        q.append(w)
                        visit.add(word)
            seq += 1
        return 0