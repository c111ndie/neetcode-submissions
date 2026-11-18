class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        substring = []
        res = []
        if not digits:
            return []
        def dfs(i, j):
            if i == len(digits):
                res.append("".join(substring))
                return
            if j == len(digit_map[digits[i]]):
                return
            substring.append(digit_map[digits[i]][j])
            dfs(i+1, 0)
            substring.pop()
            dfs(i, j+1)
        dfs(0, 0)
        return res
