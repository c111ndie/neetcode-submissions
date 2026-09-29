class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prevRow = [n - j for j in range(n + 1)]
        for i in range(m-1, -1, -1):
            curRow = [0] * (n + 1)
            curRow[n] = m - i
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    prevRow[j] = 1
                    curRow[j+1] = 1
                if word1[i] == word2[j]:
                    curRow[j] = prevRow[j+1]
                else:
                    curRow[j] = 1 + min(curRow[j+1], prevRow[j], prevRow[j+1])
            prevRow = curRow
        return prevRow[0]
        '''
        recursion:
            if word1[i] == word2[j]:
                ops[i][j] = ops[i+1][j+1]
            else:
                ops[i][j] = 1 + min(ops[i][j+1], ops[1+1][j], ops[i+1][j+1])
                apple_ napple_
        '''
        