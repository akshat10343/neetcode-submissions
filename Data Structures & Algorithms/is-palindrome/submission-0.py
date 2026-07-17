class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for i in s:
            if i.isalnum():
                check = check + i.lower()
        if check == check[::-1]:
            return True
        return False