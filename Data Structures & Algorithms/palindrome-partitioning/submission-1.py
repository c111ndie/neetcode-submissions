class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        subset = []
        res = []
        def dfs(l, r):
            if l == len(s):
                res.append(subset.copy())
                return
            if r == len(s):
                return
            string = s[l:r+1]
            if is_palindrome(string):
                subset.append(string)
                dfs(r+1, r+1)
                subset.pop()
            dfs(l, r+1)
        dfs(0, 0)
        return res
        