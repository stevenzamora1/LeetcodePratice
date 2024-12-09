class Solution:
    def isPalindrome(self, oldString: str) -> bool:
        oldString = oldString.lower()

        s = ""
        for n in oldString:
            if ord(n) >= 97 and ord(n) <= 122:

                s = s + n
        low = 0
        high = len(s) - 1
        while (low <= high):
            if (s[low] != s[high]):
                return False
            low += 1
            high -= 1
        return True

    def betterIsPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


obj = Solution()
print(obj.isPalindrome("0P"))
print(obj.isPalindrome("race a car"))
