class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_t = defaultdict(int)
        for i in t:
            freq_t[i] += 1
        l = 0
        while l < len(s) and s[l] not in freq_t:
            l += 1
        if (len(s) - l) < len(t):
            return ""
        freq_s = defaultdict(int)
        shortest = (0, 0)
        have, required = 0, len(freq_t)
        for r in range(l, len(s)):
            freq_s[s[r]] += 1
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                have += 1
            while have == required:
                if shortest[1] == 0 or (r - l + 1) < shortest[1]:
                    shortest = (l, (r - l + 1))
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        return s[shortest[0]:shortest[0]+shortest[1]]
                
            

        