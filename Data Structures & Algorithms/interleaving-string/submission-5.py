class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        prevRow = [False] * (len(s2) + 1)
        prevRow[len(s2)] = True
        for i in range(len(s1), -1, -1):
            curRow = [False] * (len(s2) + 1)
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    curRow[j] = True
                else:
                    k = i + j
                    if i < len(s1) and s1[i] == s3[k] and prevRow[j]:
                        curRow[j] = True
                    if j < len(s2) and s2[j] == s3[k] and curRow[j+1]:
                        curRow[j] = True
            prevRow = curRow
        return prevRow[0]
        
