class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = ""
        o, c = 0, 0
        def dfs():
            nonlocal string, o, c
            if len(string) == 2 * n:
                res.append(string)
                return
            if o < n:
                string += "(" 
                o += 1
                dfs()
                string = string[:-1]
                o -= 1
            if o > c:
                string += ")"
                c += 1
                dfs()
                string = string[:-1]
                c -= 1
        dfs()
        return res
