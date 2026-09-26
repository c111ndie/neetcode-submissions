class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = 0, 1
        for i in range(len(s)):
            # odd-length
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s):
                length = r - l + 1
                if s[l] == s[r] and length > resLen:
                    res = l
                    resLen = length
                elif s[l] != s[r]:
                    break
                l -= 1
                r += 1
            # even-length
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                length = r - l + 1
                if s[l] == s[r] and length > resLen:
                    res = l
                    resLen = length
                elif s[l] != s[r]:
                    break
                l -= 1
                r += 1
        return s[res:res+resLen]
