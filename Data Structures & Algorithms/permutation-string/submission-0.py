class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = {}
        for i in s1:
            if i in l:
                l[i] = l[i] + 1
            else:
                l[i] = 1
        if len(s1) > len(s2):
            return False
        check = {}
        left = 0
        right = len(s1)

        for i in s2[:right]:
            if i in check:
                check[i] = check[i] + 1
            else:
                check[i] = 1

        for i in range(len(s2)-len(s1)):
            if check == l:
                return True
            else:
                if s2[right] in check:
                    check[s2[right]] = check[s2[right]] + 1
                else:
                    check[s2[right]] = 1
                if check[s2[left]] > 1:
                    check[s2[left]] = check[s2[left]] -1
                else:
                    check.pop(s2[left])
            left = left + 1
            right = right + 1
        if check == l:
            return True
        else:
            return False