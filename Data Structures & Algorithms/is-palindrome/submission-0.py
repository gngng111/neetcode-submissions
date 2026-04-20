class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(s) // 2
        for i in range(0, n):
            if s[i] != s[-i-1]:
                return False
        return True