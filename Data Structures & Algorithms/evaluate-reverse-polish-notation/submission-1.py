class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return ( int(tokens[0]))
        l = []
        for i in tokens:
            if i in "+-/*":
                a = int(l.pop())
                b = int(l.pop())
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = b - a
                elif i == "*":
                    result = a * b
                elif i == "/":
                    result = b / a
                l.append(result)

            else:
                l.append(i)
        return int(l[0])