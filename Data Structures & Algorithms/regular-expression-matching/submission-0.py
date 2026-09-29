class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prevRow = [False] * (n+1)
        prevRow[n] = True
        for i in range(m, -1, -1):
            curRow = [False] * (n+1)
            curRow[n] = (i == m)
            for j in range(n-1, -1, -1):
                first_match = (i < m and (s[i] == p[j] or p[j] == "."))
                if j + 1 < n and p[j+1] == "*":
                    curRow[j] = (first_match and prevRow[j]) or curRow[j+2]
                elif first_match:
                    curRow[j] = prevRow[j+1]
            prevRow = curRow
        return prevRow[0]
