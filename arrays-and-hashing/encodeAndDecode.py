class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ""
        for s in strs:
            num = len(s)
            output += str(num) + "%" + s
        return output

    # First try at decode that did not work

    # error was assuming each word had a single digit length,
    # it doesnt account for words 10>

    def decode(self, s: str) -> list[str]:
        output = []
        index = 0
        while index < len(s):

            specifc = int(s[index])
            output.append(s[index + 2: index + 2+specifc])
            index = index+specifc + 2

        return output

    # Correct answer that makes sure to find the delimiter
    # and handles strings greather than 9

    def decodeAnswer(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1 + length])
            i = j + 1 + length
        return res


obj = Solution()
print(obj.encode(["hello", "listen", "yay"]))
print(obj.decode(obj.encode(["hello", "listen", "yay"])))
print(obj.decodeAnswer(obj.encode(["hello", "listen", "yay"])))
