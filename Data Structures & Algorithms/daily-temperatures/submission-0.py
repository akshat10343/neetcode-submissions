class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        check = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    check[i] = count
                    break
                else:
                    count = count + 1
        return check