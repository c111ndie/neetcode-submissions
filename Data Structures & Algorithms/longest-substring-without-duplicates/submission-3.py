class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        substring = set()
        res = 0
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
                res = max(r - l, res)
            else:
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
                res = max(r - l, res)
        return res
                
