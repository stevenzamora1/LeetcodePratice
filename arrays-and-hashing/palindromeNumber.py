class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        # Initialize a divisor to find the most significant digit
        div = 1
        while x > 10 * div:
            div *= 10  # Increase div until it matches the leftmost digit's place

        # Compare digits from both ends
        while x:
            right = x % 10  # Extract the rightmost digit
            left = x // div  # Extract the leftmost digit

            # If they are not the same, it's not a palindrome
            if left != right:
                return False

            # Remove leftmost and rightmost digits
            x = (x % div) // 10
            div = div / 100  # Reduce divisor by two places since we removed two digits
        return True


obj = Solution()
print(obj.isPalindrome(121))
