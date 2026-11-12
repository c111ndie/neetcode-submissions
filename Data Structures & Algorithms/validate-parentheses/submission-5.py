class Solution:
    def isValid(self, s: str) -> bool:
        match = []
        for c in s:
            if c in [")", "}", "]"]:
                if not match:
                    return False
                m = match.pop()
                if (c == ")" and m == "(") or (c == "]" and m == "[") or (c == "}" and m == "{"):
                    continue
                else:
                    return False
            else:
                match.append(c)
        return len(match) == 0
                