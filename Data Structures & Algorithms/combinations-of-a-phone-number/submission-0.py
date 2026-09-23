class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        word = ""
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def dfs(i, word):
            if i == len(digits):
                if word:
                    res.append(word)
                return
            for letter in letterMap[digits[i]]:
                word += letter
                dfs(i+1, word)
                word = word[:-1]
        dfs(0, word)
        return res

        