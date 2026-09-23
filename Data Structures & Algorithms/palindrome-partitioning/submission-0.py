class Solution:
    def is_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substrings = []
        strlen = len(s)
        def dfs(left, right):
            if left == strlen:
                res.append(substrings.copy())
                return
            if right == strlen:
                return
            if self.is_palindrome(s[left:right+1]):
                substrings.append(s[left:right+1])
                dfs(right+1, right+1)
                substrings.pop()
            dfs(left, right+1)
        dfs(0, 0)
        return res
                
            
            