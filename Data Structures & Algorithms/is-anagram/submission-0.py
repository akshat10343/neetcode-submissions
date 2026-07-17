class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check1 = {}
        check2 = {}
        for i in range(len(s)):
            if s[i] in check1:
                check1[s[i]] = check1[s[i]] + 1
            else:
                check1[s[i]] = 1
            if t[i] in check2:
                check2[t[i]] = check2[t[i]] + 1
            else:
                check2[t[i]] = 1
        return(check1 == check2)