class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = set(s)
        for c in chars:
            replace = 0
            l, r = 0, 0
            while r < len(s):
                if s[r] != c:
                    if replace < k:
                        replace += 1
                    else:
                        while s[l] == c:
                            l += 1
                        l += 1
                r += 1
                res = max(res, r-l)
        return res