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


# print(isValid("([])"))  # true
# print(isValid("([)"))  # false
print(isValid("("))  # false
print(isValid("]"))  # false
print(isValid("[(])"))
