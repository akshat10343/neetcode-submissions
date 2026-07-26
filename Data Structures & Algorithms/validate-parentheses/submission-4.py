class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                l.append(i)
            elif i == ")":
                if not l:
                    return False
                check = l.pop()
                if check != "(":
                    return False
            elif i == "]":
                if not l:
                    return False
                check = l.pop()
                if check != "[":
                    return False
            elif i == "}":
                if not l:
                    return False
                check = l.pop()
                if check != "{":
                    return False
        if len(l) == 0:
            return True
        else:
            return False
