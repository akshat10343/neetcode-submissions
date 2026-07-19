class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ""
        
        # Slide a window of size 3 across the string
        # We stop at len(num) - 2 because a 3-char window can't start past that
        for i in range(len(num) - 2):
            # Check if all elements inside the current window are identical
            if num[i] == num[i + 1] == num[i + 2]:
                # Update max_digit if this digit is larger than what we've seen
                max_digit = max(max_digit, num[i])

        return max_digit * 3