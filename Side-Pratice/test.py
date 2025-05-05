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


def twoSumt(nums: list[int], target: int) -> list[int]:
    indexOne = 0

    for n in range(1, len(nums)):

        print([indexOne, n])
        if target - nums[indexOne] == nums[n]:
            return [indexOne, n]
        indexOne += 1


def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}
    for n in range(0, len(nums)):
        found = target - nums[n]
        if nums[n] in hashMap:
            return [n, hashMap.get(nums[n])]
        hashMap[found] = n
