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


'''
Code explaination:


Create a hashmap 
The keys are each unique anagrams but sorted alphabatically using sorted() method.
The values are a list of each string that matches the letters of the keys



'''
