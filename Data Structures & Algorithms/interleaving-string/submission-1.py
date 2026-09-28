from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @cache
        def check(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i < len(s1) and j < len(s2):
                if s1[i] == s3[k] and s2[j] == s3[k]:
                    return check(i+1, j, k+1) or check(i, j+1, k+1)
                elif s1[i] == s3[k]:
                    return check(i+1, j, k+1)
                elif s2[j] == s3[k]:
                    return check(i, j+1, k+1)
                else:
                    return False
            elif j == len(s2):
                if s1[i] == s3[k]:
                    return check(i+1, j, k+1)
                else:
                    return False
            else:
                if s2[j] == s3[k]:
                    return check(i, j+1, k+1)
                else:
                    return False
        return check(0, 0, 0)