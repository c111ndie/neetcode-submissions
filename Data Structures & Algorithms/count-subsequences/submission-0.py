class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
        prevRow = [0] * (n + 1)
        prevRow[n] = 1
        for i in range(m-1, -1, -1):
            curRow = [0] * (n + 1)
            for j in range(n, -1, -1):
                if j == n:
                    curRow[j] = 1
                    continue
                if s[i] == t[j]:
                    curRow[j] = prevRow[j+1] + prevRow[j]
                else:
                    curRow[j] = prevRow[j]
            prevRow = curRow
        return prevRow[0]