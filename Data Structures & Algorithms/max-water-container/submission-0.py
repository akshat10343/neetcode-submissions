class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            current = min(heights[left],heights[right])* (right - left)
            if current > most:
                most = current
            if heights[left] > heights[right]:
                right = right -1
            elif heights[left] <= heights[right]:
                left = left + 1
        return most