class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        check = {}
        for i in nums:
            if i in check:
                check[i] = check[i] + 1
            else:
                check[i] = 1
        b = sorted(check.items(),key=lambda pair: pair[1], reverse=True)
        print(b)
        for i in range(k):
            l.append(b[i][0])
        return l