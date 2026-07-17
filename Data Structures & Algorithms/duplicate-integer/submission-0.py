class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        if len(nums) == 0:
            return False
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False