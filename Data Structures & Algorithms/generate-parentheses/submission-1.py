class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cnt = [0] * 2
        res = []
        subset = []
        def dfs():
            if len(subset) == n*2:
                res.append("".join(subset.copy()))
            if cnt[0] < n:
                subset.append("(")
                cnt[0] += 1
                dfs()
                subset.pop()
                cnt[0] -= 1
            if cnt[1] < n and cnt[1] < cnt[0]:
                subset.append(")")
                cnt[1] += 1
                dfs()
                subset.pop()
                cnt[1] -= 1
        dfs()
        return res

