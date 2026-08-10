class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        for i in s:
            if i == '[':
                balance +=1
            else:
                if balance > 0:
                    balance -= 1
        return (balance + 1) // 2