class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        for n in tokens:
            if n not in {"+", "-", "*", "/"}:
                num.append(int(n))
            else:
                r = num.pop()
                l = num.pop()
                if n == '+':
                    num.append(l + r)
                elif n == '-':
                    num.append(l - r)        
                elif n == '*':
                    num.append(l * r)  
                else:
                    num.append(int(l / r)) 
        return num[0]