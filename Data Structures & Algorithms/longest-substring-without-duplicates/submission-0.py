class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        current = ""
        for letter in s:
            if letter not in current:
                current = current + letter
                if len(current) > len(longest):
                    longest = current
            else:

                for j in range(len(current)):
                    if current[j] == letter:
                        current = current[j+1:] + letter
                        break
        return len(longest)