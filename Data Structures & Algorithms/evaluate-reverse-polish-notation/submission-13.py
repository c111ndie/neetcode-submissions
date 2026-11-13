class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        to_be_calc = []
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                to_be_calc.append(int(c))
            else:
                c2 = to_be_calc.pop()
                c1 = to_be_calc.pop()
                if c == "+":
                    to_be_calc.append(c1 + c2)
                elif c == "-":
                    to_be_calc.append(c1 - c2)
                elif c == "*":
                    to_be_calc.append(c1 * c2)
                else:
                    to_be_calc.append(int(c1 / c2))
        return to_be_calc[0]
