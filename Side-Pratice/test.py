def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    div = 1
    while x >= 10 * div:
        div *= 10
    print(div)
    while x:

        r = x % 10
        l = x // div

        if l != r:
            return False
        x = x % div

        x = x // 10

        div = div / 100

    return True


print(isPalindrome(1000021))
print(isPalindrome(11))
# print(isPalindrome(10))
# print(isPalindrome(121))
