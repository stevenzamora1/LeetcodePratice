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


obj = Solution()
print(obj.isPalindrome("0P"))
print(obj.isPalindrome("race a car"))
