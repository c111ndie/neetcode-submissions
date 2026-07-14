class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                tmp.append(i)
            elif i == "]":
                if not tmp or tmp.pop() != "[":
                    return False
            elif i == ")":
                if not tmp or tmp.pop() != "(":
                    return False    
            elif i == "}":
                if not tmp or tmp.pop() != "{":
                    return False
        return not tmp


        