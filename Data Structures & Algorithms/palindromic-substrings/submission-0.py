class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        for i in range(n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
                else:
                    break
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
                else:
                    break
        return cnt + n
        