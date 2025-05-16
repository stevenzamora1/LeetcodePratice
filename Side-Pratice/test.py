def topKFrequent(nums: list[int], k: int) -> list[int]:
    hashTable = {}
    freq = [[] for i in range(len(nums))]

    for n in nums:
        if n in hashTable:
            hashTable[n] += 1
        else:
            hashTable[n] = 1

    for key in hashTable:
        freq[hashTable[key]].append(key)
    freq2 = [val for val in freq if val != []]
    res = []

    for i in range(len(freq2) - 1, -1, -1):

        res.extend(freq2[i])

        if len(res) == k:
            return res


def topKFrequent(nums: list[int], k: int) -> list[int]:
    hashMap = {}

    current = nums[0]
    count = 0
    for n in nums:
        print(current, n)
        if n == current:
            count += 1
        else:
            hashMap[count] = current
            current = n
            count = 0

    print(hashMap)
    print(sorted(hashMap))
    return [3]


def isValid(s: str) -> bool:
    stack = []
    hashMap = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    for n in s:

        if n == "{" or n == "[" or n == "(":
            stack.append(n)
        elif len(stack) > 0 and (stack[-1] == hashMap[n]):
            stack.pop()
        else:
            return False

    if len(stack) != 0:
        return False
    return True


def containsDuplicate(nums: list[int]) -> bool:
    dupSet = set()
    for n in nums:
        if n in dupSet:
            return True
        dupSet.add(n)

    return False


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    stringHash = {}
    stringArray = []
    for n in strs:
        sortedString = "".join(sorted(n))
        if sortedString in stringHash:
            stringHash[sortedString].append(n)
        else:
            stringHash[sortedString] = [n]
    for y in stringHash:
        stringArray.append(stringHash[y])

    return stringArray


print(groupAnagrams(["rat", "tar", "art", "car", "arc", "elbow", "below"]))
print(groupAnagrams(["a", "b", "c"]))
print(groupAnagrams(["a"]))
