from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @cache
        def check(i, j):
            k = i + j
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s1[i] == s3[k] and check(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and check(i, j+1):
                return True
            return False
        return check(0, 0)