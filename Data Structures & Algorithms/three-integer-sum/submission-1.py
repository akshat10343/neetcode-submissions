class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = set()  
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) -1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    answer.add((nums[left],nums[right], nums[i]))
                    left = left + 1
                    right = right -1
                elif nums[left] + nums[right] < -nums[i]:
                    left = left + 1
                else:
                    right = right - 1
        final = []
        for i in answer:
            check = list(i)
            final.append(check)
        return final
