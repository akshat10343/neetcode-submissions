class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        if len(nums)<= 1:
                return (len(nums))
        check = 1
        most = 0
        for i in range(len(nums)):
            if nums[i]+ 1 in nums:
                check = check+ 1
                if check > most:
                    most = check
            else:
                check = 1
        if (most == 0):
            return 1
        return most