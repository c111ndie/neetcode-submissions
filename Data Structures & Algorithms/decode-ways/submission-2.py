class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0":
            return 0
        if n <= 1:
            return n
        
        dp = [1, 1]
        i = 1
        while i < n:
            res = 0
            if s[i] != "0":
                res += dp[1]
            if 10 <= int(s[i-1] + s[i]) <= 26:
                res += dp[0]
            tmp = dp[1]
            dp[1] = res
            dp[0] = tmp
            i += 1
        return dp[1]
        