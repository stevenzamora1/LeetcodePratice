class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {}
        outputlist = []
        for n in strs:
            result = sorted(n)
            sorted_letters = "".join(result)
            if sorted_letters in output:
                output[sorted_letters].append(n)
            else:
                output[sorted_letters] = [n]

        for key in output:
            outputlist.append(output[key])

        return outputlist


obj = Solution()
print(obj.groupAnagrams([""]))
