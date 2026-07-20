class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final = final+ str(len(i)) + "#" + i
        return final

    def decode(self, s: str) -> List[str]:
        check = s
        l = []
        while len(check) > 0:
            if check[1] == "#":
                num = int(check[0])
                check = check[2:]
            else:
                if check[2] == "#":
                    num = int(check[:2])
                    check = check[3:]
                else:
                    num = int(check[:3])
                    check = check[4:]
            l.append(check[:num])
            check = check[num:]
        return l