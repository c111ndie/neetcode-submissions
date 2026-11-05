class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        missing = len(t)
        l, r = 0, 0
        best_start = 0
        best_len = float("inf")
        while r < len(s):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    missing -= 1
                freq[s[r]] -= 1
            while missing == 0:
                if r - l + 1 < best_len:
                    best_start = l
                    best_len = r - l + 1
                if s[l] in freq and freq[s[l]] < 0:
                    freq[s[l]] += 1
                elif s[l] in freq and freq[s[l]] == 0:
                    missing += 1
                    freq[s[l]] += 1
                l += 1
            r += 1
        if best_len == float("inf"):
            return ""
        else:
            return s[best_start:best_start+best_len]